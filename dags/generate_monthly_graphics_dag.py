from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators import (
    StageCsvToRedshiftOperator, PostgresOperator, StageJsonToRedshiftOperator,
    LoadDimensionOperator, LoadFactOperator, DataQualityOperator
)
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from helpers import SqlQueries
from nyc_taxi_trips_load_tasks.generate_monthly_price_frequency_graphics import (
    generate_monthly_graphics as generate_price_frequency_graphics
)
from nyc_taxi_trips_load_tasks.generate_daily_tip_amount_graphics import (
    generate_monthly_graphics as generate_monthly_tip_amount_graphics
)
from nyc_taxi_trips_load_tasks.generate_monthly_pickups_maps_html import (
    generate_monthly_htmls as generate_monthly_pickups_maps_htmls
)
from nyc_taxi_trips_load_tasks.generate_monthly_dropoffs_maps_html import (
    generate_monthly_htmls as generate_monthly_dropoffs_maps_htmls
)

default_args = {
    'owner': 'gabriel',
    'start_date': datetime(2009, 1, 1, 0, 0, 0),
    'end_date': datetime(2012, 12, 31, 23, 59, 59),
    # 'end_date': datetime(2009, 12, 31, 23, 59, 59),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
    'catchup': True
}

dag = DAG('generate_monthly_graphics_dag',
          default_args=default_args,
          description='Generate all the monthly based graphics',
          schedule_interval='@monthly'
        )


def nyc_taxi_trips_load_execution_date(dt):
    return dt.replace(month=1, day=1, hour=0, minute=0, second=0)


wait_nyc_taxi_trips_load_task = ExternalTaskSensor(
    task_id='wait_nyc_taxi_trips_load',
    external_dag_id='nyc_taxi_trips_load',
    external_task_id=None,
    execution_date_fn=nyc_taxi_trips_load_execution_date,
    dag=dag, mode='reschedule'
)

generate_monthly_price_frequency_graphics_task = PythonOperator(
    task_id='generate_monthly_price_frequency_graphics',
    dag=dag,
    python_callable=generate_price_frequency_graphics,
    provide_context=True
)

generate_monthly_tip_amount_graphics_task = PythonOperator(
    task_id='generate_monthly_tip_amount_graphics',
    dag=dag,
    python_callable=generate_monthly_tip_amount_graphics,
    provide_context=True
)

generate_monthly_pickups_maps_htmls_task = PythonOperator(
    task_id='generate_monthly_pickups_maps_htmls',
    dag=dag,
    python_callable=generate_monthly_pickups_maps_htmls,
    provide_context=True
)

generate_monthly_dropoffs_maps_htmls_task = PythonOperator(
    task_id='generate_monthly_dropoffs_maps_htmls',
    dag=dag,
    python_callable=generate_monthly_dropoffs_maps_htmls,
    provide_context=True
)



wait_nyc_taxi_trips_load_task >> generate_monthly_price_frequency_graphics_task
wait_nyc_taxi_trips_load_task >> generate_monthly_tip_amount_graphics_task
wait_nyc_taxi_trips_load_task >> generate_monthly_pickups_maps_htmls_task
wait_nyc_taxi_trips_load_task >> generate_monthly_dropoffs_maps_htmls_task

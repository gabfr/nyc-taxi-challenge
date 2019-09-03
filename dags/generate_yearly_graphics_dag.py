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
from airflow.operators.sensors import TimeDeltaSensor
from helpers import SqlQueries
from nyc_taxi_trips_load_tasks.generate_daily_avg_trip_distance_graphics import (
    generate_yearly_graphics as generate_yearly_avg_trip_distance_graphics
)
from nyc_taxi_trips_load_tasks.generate_bianual_revenue_per_vendor_graphics import (
    generate_bianual_graphics as generate_bianual_revenue_per_vendor_graphics
)
from nyc_taxi_trips_load_tasks.generate_monthly_avg_weekend_trips_duration_graphics import (
    generate_yearly_graphics as generate_yearly_avg_weekend_trips_duration_graphics
)



default_args = {
    'owner': 'gabriel',
    'start_date': datetime(2009, 1, 1, 0, 0, 0),
    'end_date': datetime(2012, 12, 31, 23, 59, 59),
    # 'end_date': datetime(2009, 12, 31, 23, 59, 59),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=300),
    'catchup': True
}

dag = DAG('generate_yearly_graphics_dag',
          default_args=default_args,
          description='Generate all the yearly graphics',
          schedule_interval='@yearly'
        )

generate_daily_avg_trip_distance_graphics_task = PythonOperator(
    task_id='generate_daily_avg_trip_distance_graphics',
    dag=dag,
    python_callable=generate_yearly_avg_trip_distance_graphics,
    provide_context=True
)

generate_bianual_revenue_per_vendor_graphics_task = PythonOperator(
    task_id='generate_bianual_revenue_per_vendor_graphics',
    dag=dag,
    python_callable=generate_bianual_revenue_per_vendor_graphics,
    provide_context=True
)

generate_yearly_avg_weekend_trips_duration_graphics_task = PythonOperator(
    task_id='generate_yearly_avg_weekend_trips_duration_graphics',
    dag=dag,
    python_callable=generate_yearly_avg_weekend_trips_duration_graphics,
    provide_context=True
)

generate_daily_avg_trip_distance_graphics_task
generate_bianual_revenue_per_vendor_graphics_task
generate_yearly_avg_weekend_trips_duration_graphics_task

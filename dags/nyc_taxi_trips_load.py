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

dag = DAG('nyc_taxi_trips_load',
          default_args=default_args,
          description='Load the trips datasets into Spark/EMR',
          schedule_interval='@yearly',
          max_active_runs=1
        )

recreate_trips_table = PostgresOperator(
    task_id="recreate_trips_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.recreate_trips_table
)

recreate_payment_lookups_table = PostgresOperator(
    task_id="recreate_payment_lookups_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.recreate_payment_lookups_table
)

recreate_vendor_lookups_table = PostgresOperator(
    task_id="recreate_vendor_lookups_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.recreate_vendor_lookups_table
)

load_trips_dataset = StageJsonToRedshiftOperator(
    task_id='load_trips_dataset',
    dag=dag,
    table="trips",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    # s3_bucket="data-sprints-eng-test",
    # s3_key="data-sample_data-nyctaxi-trips-{ds_year}-json_corrigido.json",
    s3_bucket="social-wiki-datalake",
    s3_key="data-sprints-eng-test/data-sample_data-nyctaxi-trips-{ds_year}-json_corrigido.json",
    extra_copy_parameters="TIMEFORMAT 'auto' REGION 'us-east-2'"
)

load_vendor_lookups_table = StageCsvToRedshiftOperator(
    task_id='load_vendor_lookups_table',
    dag=dag,
    table="vendor_lookups",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    # s3_bucket="data-sprints-eng-test",
    # s3_key="data-sprints-eng-test/data-vendor_lookup-csv.csv",
    s3_bucket="social-wiki-datalake",
    s3_key="data-sprints-eng-test/data-vendor_lookup-csv.csv",
    extra_copy_parameters="REGION 'us-east-2'"
)

load_payment_lookups_table = StageCsvToRedshiftOperator(
    task_id='load_payment_lookups_table',
    dag=dag,
    table="payment_lookups",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    # s3_bucket="data-sprints-eng-test",
    # s3_key="data-payment_lookup-csv.csv",
    s3_bucket="social-wiki-datalake",
    s3_key="data-sprints-eng-test/data-payment_lookup-csv.csv",
    extra_copy_parameters="REGION 'us-east-2'"
)

dummy_wait = TimeDeltaSensor(
    task_id='dummy_wait',
    dag=dag,
    delta=timedelta(seconds=1)
)

upsert_bi_daily_avg_trip_distance = PostgresOperator(
    task_id="upsert_bi_daily_avg_trip_distance",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.upsert_bi_daily_avg_trip_distance
)

upsert_bi_bianual_revenue_per_vendor = PostgresOperator(
    task_id="upsert_bi_bianual_revenue_per_vendor",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.upsert_bi_bianual_revenue_per_vendor
)

upsert_bi_monthly_price_frequency = PostgresOperator(
    task_id="upsert_bi_monthly_price_frequency",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.upsert_bi_monthly_price_frequency
)

upsert_bi_daily_tip_amount = PostgresOperator(
    task_id="upsert_bi_daily_tip_amount",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.upsert_bi_daily_tip_amount
)

upsert_bi_monthly_avg_weekend_trips_duration = PostgresOperator(
    task_id="upsert_bi_monthly_avg_weekend_trips_duration",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.upsert_bi_monthly_avg_weekend_trips_duration
)

upsert_bi_pickups = PostgresOperator(
    task_id="upsert_bi_pickups",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.upsert_bi_pickups
)

upsert_bi_dropoffs = PostgresOperator(
    task_id="upsert_bi_dropoffs",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.upsert_bi_dropoffs
)

recreate_trips_table >> load_trips_dataset
recreate_payment_lookups_table >> load_vendor_lookups_table
recreate_vendor_lookups_table >> load_payment_lookups_table
load_trips_dataset >> dummy_wait
load_vendor_lookups_table >> dummy_wait
load_payment_lookups_table >> dummy_wait
dummy_wait >> upsert_bi_daily_avg_trip_distance
dummy_wait >> upsert_bi_bianual_revenue_per_vendor
dummy_wait >> upsert_bi_monthly_price_frequency
dummy_wait >> upsert_bi_daily_tip_amount
dummy_wait >> upsert_bi_monthly_avg_weekend_trips_duration
dummy_wait >> upsert_bi_pickups
dummy_wait >> upsert_bi_dropoffs

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import PostgresOperator
from airflow.operators.sensors import TimeDeltaSensor
from helpers import SqlQueries


default_args = {
    'owner': 'gabriel',
    'start_date': datetime(2009, 12, 31, 23, 59, 59),
    'end_date': datetime(2012, 12, 31, 23, 59, 59),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=300),
    'catchup': True
}

dag = DAG('recreate_bi_tables',
          default_args=default_args,
          description='Recreate the business intelligence tables',
          schedule_interval=None,
          max_active_runs=1
        )

dummy_wait = TimeDeltaSensor(
    task_id='dummy_wait',
    dag=dag,
    delta=timedelta(seconds=1)
)

recreate_bi_tables = PostgresOperator(
    task_id="recreate_bi_tables_task",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.recreate_bi_tables
)

dummy_wait >> recreate_bi_tables

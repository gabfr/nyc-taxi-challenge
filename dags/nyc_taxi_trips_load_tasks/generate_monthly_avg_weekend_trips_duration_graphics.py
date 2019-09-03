import datetime
import matplotlib.pyplot as plt
import pandas.io.sql as sqlio
from nyc_taxi_trips_load_tasks.common.aws import upload_file_to_s3
import pandas as pd
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
import os


def build_query_for(year):
    return """
        SELECT 
            pickup_month,
            trip_duration_avg_in_seconds
        FROM 
            bi_monthly_avg_weekend_trips_duration
        WHERE
            pickup_month LIKE '{}-%'
    """.format(year)


def build_graphic_for(execution_date, conn, credentials):
    df = sqlio.read_sql_query(build_query_for(execution_date.year), conn)

    if df.empty:
        return

    df.plot()
    img_name = "{}_monthly_avg_weekend_trips_duration.png".format(execution_date.year)
    plt.savefig(img_name)

    upload_file_to_s3(img_name, "data-sprints-eng-test/outputs/{}".format(img_name), credentials)

    os.remove(img_name)


def generate_yearly_graphics(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    conn = redshift_hook.get_conn()

    # # #
    execution_date = datetime.datetime.strptime(kwargs["ds"], '%Y-%m-%d')
    # # #

    build_graphic_for(execution_date, conn, credentials)


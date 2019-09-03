import datetime
import matplotlib.pyplot as plt
import pandas.io.sql as sqlio
import os
from nyc_taxi_trips_load_tasks.common.aws import upload_file_to_s3
import pandas as pd
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook


def generate_yearly_graphics(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    conn = redshift_hook.get_conn()

    # # #
    execution_date = datetime.datetime.strptime(kwargs["ds"], '%Y-%m-%d')
    # # #

    df = sqlio.read_sql_query("""
        SELECT 
            pickup_date,
            avg_trip_distance
        FROM 
            bi_daily_avg_trip_distance
        WHERE
            EXTRACT(yr FROM pickup_date) = {}
    """.format(execution_date.year), conn)

    if df.empty:
        return

    df.plot()
    img_name = "{}_daily_avg_trip_distance.png".format(execution_date.year)
    plt.savefig(img_name)

    upload_file_to_s3(img_name, "data-sprints-eng-test/outputs/{}".format(img_name), credentials)

    os.remove(img_name)
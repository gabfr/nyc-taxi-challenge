import datetime
import matplotlib.pyplot as plt
import pandas.io.sql as sqlio
from nyc_taxi_trips_load_tasks.common.aws import upload_file_to_s3
import pandas as pd
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
import os

def build_query_for(year, semester):
    return """
        SELECT 
            vendor_lookups.name AS vendor_name
            total_amount_sum
        FROM 
            bi_bianual_revenue_per_vendor
            JOIN vendor_lookups ON (vendor_lookups.vendor_id = bi_bianual_revenue_per_vendor.vendor_id)
        WHERE
            pickup_semester = '{}-{}'
    """.format(year, semester)


def build_graphic_for(execution_date, semester, conn, credentials):
    df = sqlio.read_sql_query(build_query_for(execution_date.year, semester), conn)

    if df.empty:
        return

    df.plot(kind='pie')
    img_name = "{}-{}_bianual_revenue_per_vendor.png".format(execution_date.year, semester)
    plt.savefig(img_name)

    upload_file_to_s3(img_name, "data-sprints-eng-test/outputs/{}".format(img_name), credentials)

    os.remove(img_name)


def generate_bianual_graphics(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    conn = redshift_hook.get_conn()

    # # #
    execution_date = datetime.datetime.strptime(kwargs["ds"], '%Y-%m-%d')
    # # #

    build_graphic_for(execution_date, 1, conn, credentials)
    build_graphic_for(execution_date, 2, conn, credentials)


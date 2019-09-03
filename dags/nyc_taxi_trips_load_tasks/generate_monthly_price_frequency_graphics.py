import datetime
import matplotlib.pyplot as plt
import pandas.io.sql as sqlio
from nyc_taxi_trips_load_tasks.common.aws import upload_file_to_s3
import pandas as pd
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
import os
import logging


def build_query_for(year, month):
    return """
        SELECT 
            amount_group,
            frequency
        FROM 
            bi_monthly_price_frequency
        WHERE
            pickup_month = '{}-{}'
    """.format(year, '0' + str(month) if month < 10 else month)


def build_graphic_for(execution_date, conn, credentials):
    sql_query = build_query_for(execution_date.year, execution_date.month)
    logging.info(sql_query)
    df = sqlio.read_sql_query(sql_query, conn).sort_values(by='amount_group')

    if df.empty:
        logging.info('Query returned empty results set')
        return

    df.plot(kind='bar', x='amount_group', y='frequency')
    img_name = "{}-{}_monthly_price_frequency.png".format(execution_date.year, execution_date.month)
    plt.savefig(img_name)

    upload_file_to_s3(img_name, "data-sprints-eng-test/outputs/{}".format(img_name), credentials)

    os.remove(img_name)


def generate_monthly_graphics(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    conn = redshift_hook.get_conn()

    # # #
    execution_date = datetime.datetime.strptime(kwargs["ds"], '%Y-%m-%d')
    # # #

    build_graphic_for(execution_date, conn, credentials)


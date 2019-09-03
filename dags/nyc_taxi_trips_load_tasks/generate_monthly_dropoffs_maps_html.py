import datetime
import folium
from folium import (Map, CircleMarker)
from folium.plugins import MarkerCluster
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
            dropoff_latitude,
            dropoff_longitude
        FROM 
            bi_dropoffs
        WHERE
            dropoff_month = '{}-{}'
    """.format(year, '0' + str(month) if month < 10 else month)


def build_html_for(execution_date, conn, credentials):
    sql_query = build_query_for(execution_date.year, execution_date.month)
    logging.info(sql_query)
    df = sqlio.read_sql_query(sql_query, conn)

    if df.empty:
        logging.info('Query returned empty results set')
        return

    dropoff_map = Map(
        location=[
            df['dropoff_latitude'].mean(),
            df['dropoff_longitude'].mean()
        ],
        tiles='OpenStreetMap',
        zoom_start=12
    )

    mc = MarkerCluster()

    for row in df.itertuples():
        mc.add_child(folium.Marker(location=[row.dropoff_latitude, row.dropoff_longitude],
                                   popup=str(row.dropoff_latitude) + ',' + str(row.dropoff_longitude)))

    dropoff_map.add_child(mc)
    html_file_name = "{}-{}_dropoffs_map.html".format(execution_date.year, execution_date.month)
    dropoff_map.save(outfile=html_file_name)

    upload_file_to_s3(
        html_file_name,
        "data-sprints-eng-test/outputs/{}".format(html_file_name),
        credentials,
        "text/html"
    )

    os.remove(html_file_name)


def generate_monthly_htmls(*args, **kwargs):
    aws_hook = AwsHook("aws_credentials")
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    conn = redshift_hook.get_conn()

    # # #
    execution_date = datetime.datetime.strptime(kwargs["ds"], '%Y-%m-%d')
    # # #

    build_html_for(execution_date, conn, credentials)


import datetime
import folium
from folium import (Map, CircleMarker)
from folium.features import (GeoJson)
from folium.plugins import MarkerCluster
import pandas.io.sql as sqlio
from nyc_taxi_trips_load_tasks.common.aws import upload_file_to_s3
import pandas as pd
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
import os


def build_query_for(year, month):
    return """
        SELECT 
            pickup_latitude,
            pickup_longitude
        FROM 
            trips
        WHERE
            TO_CHAR(pickup_datetime, 'YYYY-MM') = '{}-{}'
    """.format(year, '0' + str(month) if month < 10 else month)


def build_html_for(execution_date, conn, credentials):
    df = sqlio.read_sql_query(build_query_for(execution_date.year, execution_date.month), conn)

    if df.empty:
        return

    pickup_map = Map(
        location=[
            df['pickup_latitude'].mean(),
            df['pickup_longitude'].mean()
        ],
        tiles='OpenStreetMap',
        zoom_start=12
    )

    mc = MarkerCluster()

    for row in df.itertuples():
        mc.add_child(folium.Marker(location=[row.pickup_latitude, row.pickup_longitude],
                                   popup=str(row.pickup_latitude) + ',' + str(row.pickup_longitude)))

    pickup_map.add_child(mc)
    html_file_name = "{}-{}_pickups_map.html".format(execution_date.year, execution_date.month)
    pickup_map.save(outfile=html_file_name)

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


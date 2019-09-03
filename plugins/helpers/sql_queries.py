class SqlQueries:

    recreate_bi_tables = ("""
        DROP TABLE IF EXISTS bi_daily_avg_trip_distance;
        CREATE TABLE bi_daily_avg_trip_distance (
            pickup_date DATE SORTKEY,
            avg_trip_distance NUMERIC(15,2)
        );
        
        DROP TABLE IF EXISTS bi_bianual_revenue_per_vendor;
        CREATE TABLE bi_bianual_revenue_per_vendor (
            pickup_semester CHAR(6) SORTKEY,
            vendor_id VARCHAR(5) DISTKEY,
            total_amount_sum NUMERIC(15,2)
        );
        
        DROP TABLE IF EXISTS bi_monthly_price_frequency;
        CREATE TABLE bi_monthly_price_frequency (
            pickup_month CHAR(7) SORTKEY,
            amount_group VARCHAR(7) DISTKEY,
            frequency NUMERIC(15,0)
        );
        
        DROP TABLE IF EXISTS bi_daily_tip_amount;
        CREATE TABLE bi_daily_tip_amount (
            pickup_date DATE SORTKEY,
            tip_amount_sum NUMERIC(15,2)
        );
        
        DROP TABLE IF EXISTS bi_monthly_avg_weekend_trips_duration;
        CREATE TABLE bi_monthly_avg_weekend_trips_duration (
            pickup_month CHAR(7) SORTKEY,
            trip_duration_avg_in_seconds NUMERIC(15,0)
        );
        
        DROP TABLE IF EXISTS bi_pickups;
        CREATE TABLE bi_pickups (
            pickup_month CHAR(7) SORTKEY,
            pickup_latitude NUMERIC(15, 6),
            pickup_longitude NUMERIC(15, 6)
        ) DISTSTYLE EVEN;
        
        DROP TABLE IF EXISTS bi_dropoffs;
        CREATE TABLE bi_dropoffs (
            dropoff_month CHAR(7) SORTKEY,
            dropoff_latitude NUMERIC(15, 6),
            dropoff_longitude NUMERIC(15, 6)
        ) DISTSTYLE EVEN;
    """)

    recreate_trips_table = ("""
        DROP TABLE IF EXISTS trips;
        CREATE TABLE trips (
            dropoff_datetime TIMESTAMP,
            dropoff_latitude NUMERIC(15, 6),
            dropoff_longitude NUMERIC(15, 6),
            fare_amount NUMERIC(15,2),
            passenger_count NUMERIC(15,0),
            payment_type VARCHAR(100),
            pickup_datetime TIMESTAMP SORTKEY,
            pickup_latitude NUMERIC(15, 6),
            pickup_longitude NUMERIC(15, 6),
            rate_code VARCHAR(100),
            store_and_fwd_flag VARCHAR(100),
            surcharge NUMERIC(15,1),
            tip_amount NUMERIC(15,2),
            tolls_amount NUMERIC(15,2),
            total_amount NUMERIC(15,2),
            trip_distance NUMERIC(15,2),
            vendor_id VARCHAR(5) DISTKEY
        );
    """)

    recreate_payment_lookups_table = ("""
        DROP TABLE IF EXISTS payment_lookups;
        CREATE TABLE payment_lookups (
            payment_type VARCHAR(255),
            payment_lookup VARCHAR(255)
        ) DISTSTYLE ALL;
    """)

    recreate_vendor_lookups_table = ("""
        DROP TABLE IF EXISTS vendor_lookups;
        CREATE TABLE vendor_lookups (
            vendor_id VARCHAR(5),
            name VARCHAR(255),
            address VARCHAR(255),
            city VARCHAR(255),
            state VARCHAR(2),
            zip VARCHAR(5),
            country VARCHAR(3),
            contact VARCHAR(255),
            current VARCHAR(3)
        ) DISTSTYLE ALL;
    """)

    upsert_bi_daily_avg_trip_distance = ("""
        INSERT INTO bi_daily_avg_trip_distance 
        SELECT 
            TRUNC(pickup_datetime) AS pickup_date,
            AVG(trip_distance) AS avg_trip_distance
        FROM
            trips
        WHERE
            passenger_count <= 2 AND 
            pickup_date NOT IN (SELECT pickup_date FROM bi_daily_avg_trip_distance)
        GROUP BY pickup_date;
    """)

    upsert_bi_bianual_revenue_per_vendor = ("""
        INSERT INTO bi_bianual_revenue_per_vendor 
        SELECT 
            (
                CAST(EXTRACT(yr FROM pickup_datetime) AS CHAR(4)) || '-' || 
                (CASE WHEN EXTRACT(mon FROM pickup_datetime) <= 6 THEN '1' ELSE '2' END)
            ) AS pickup_semester,
            vendor_id,
            SUM(total_amount) AS total_amount_sum
        FROM
            trips
        WHERE
            pickup_semester NOT IN (SELECT bi.pickup_semester FROM bi_bianual_revenue_per_vendor bi WHERE bi.vendor_id = trips.vendor_id)
        GROUP BY
            pickup_semester, vendor_id;
    """)

    upsert_bi_monthly_price_frequency = ("""
        INSERT INTO bi_monthly_price_frequency
        SELECT 
            TO_CHAR(pickup_datetime, 'YYYY-MM') AS pickup_month,
            (
                CASE WHEN total_amount BETWEEN 0 AND 4.99 THEN '$0-$4'
                     WHEN total_amount BETWEEN 5 AND 9.99 THEN '$5-$9'
                     WHEN total_amount BETWEEN 10 AND 14.99 THEN '$10-$14'
                     WHEN total_amount BETWEEN 15 AND 19.99 THEN '$15-$19'
                     WHEN total_amount BETWEEN 20 AND 24.99 THEN '$20-$24'
                     WHEN total_amount BETWEEN 25 AND 29.99 THEN '$25-$29'
                     WHEN total_amount BETWEEN 30 AND 34.99 THEN '$30-$34'
                     WHEN total_amount BETWEEN 35 AND 39.99 THEN '$35-$39'
                     WHEN total_amount BETWEEN 40 AND 44.99 THEN '$40-$44'
                     WHEN total_amount BETWEEN 45 AND 49.99 THEN '$45-$49'
                     WHEN total_amount BETWEEN 50 AND 54.99 THEN '$50-$54'
                     WHEN total_amount BETWEEN 55 AND 59.99 THEN '$55-$59'
                     WHEN total_amount >= 60 THEN '$60+'
                     ELSE '?'
                 END
            ) AS amount_group,
            COUNT(1) AS frequency
        FROM
            trips
        WHERE
            LOWER(payment_type) = 'cash' AND 
            pickup_month NOT IN (SELECT bi.pickup_month FROM bi_monthly_price_frequency bi WHERE bi.amount_group = amount_group)
        GROUP BY
            1, 2;
    """)

    upsert_bi_daily_tip_amount = ("""
        INSERT INTO bi_daily_tip_amount
        SELECT 
            TRUNC(pickup_datetime) AS pickup_date,
            SUM(tip_amount) AS tip_amount_sum
        FROM
            trips
        WHERE
            pickup_date NOT IN (SELECT pickup_date FROM bi_daily_tip_amount)
        GROUP BY
            1;
    """)

    upsert_bi_monthly_avg_weekend_trips_duration = ("""
        INSERT INTO bi_monthly_avg_weekend_trips_duration
        SELECT 
            TO_CHAR(pickup_datetime, 'YYYY-MM') AS pickup_month,
            AVG(DATEDIFF(secs, pickup_datetime, dropoff_datetime)) AS trip_duration_avg_in_seconds
        FROM
            trips
        WHERE
            EXTRACT(weekday FROM pickup_datetime) IN (0,1) AND 
            pickup_month NOT IN (SELECT pickup_month FROM bi_monthly_avg_weekend_trips_duration)
        GROUP BY 
            1;
    """)

    upsert_bi_pickups = ("""
        INSERT INTO bi_pickups
        SELECT 
            TO_CHAR(t.pickup_datetime, 'YYYY-MM') AS pickup_month,
            t.pickup_latitude AS pickup_latitude,
            t.pickup_longitude AS pickup_longitude
        FROM 
            trips t
        WHERE
            pickup_latitude NOT IN (
                SELECT bi.pickup_latitude 
                FROM bi_pickups bi
                WHERE 
                    bi.pickup_month = TO_CHAR(t.pickup_datetime, 'YYYY-MM') AND
                    bi.pickup_longitude = t.pickup_longitude
            );
    """)

    upsert_bi_dropoffs = ("""
        INSERT INTO bi_dropoffs
        SELECT 
            TO_CHAR(t.dropoff_datetime, 'YYYY-MM') AS dropoff_month,
            t.dropoff_latitude AS dropoff_latitude,
            t.dropoff_longitude AS dropoff_longitude
        FROM 
            trips t
        WHERE
            dropoff_latitude NOT IN (
                SELECT bi.dropoff_latitude 
                FROM bi_dropoffs bi
                WHERE 
                    bi.dropoff_month = TO_CHAR(t.dropoff_datetime, 'YYYY-MM') AND
                    bi.dropoff_longitude = t.dropoff_longitude
            );
    """)



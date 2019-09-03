# NYC Taxi Challenge Analysis

This analysis will focus on logistic improvement of our taxi fleets. It was made from data from 2009 to 2012.

All the questions below are answered with graphics. Besides my initiative of plotting graphics through the Airflow DAG.
My strength is not in `matplotlib`, so there's some graphics that are buggy with legend being cut by the image canvas.
Because of my short time to do this challenge I decided to focus more on the ETL structure than on the graphic 
appeareance. Moreover, on the roadmap of this project I will beauty up those graphics as soon as I get a chance.

## Daily average distance for trips with 2 passengers max

The daily **average distance is in miles**, it was grouped in graphics for each year:

 - [2009](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2009_daily_avg_trip_distance.png)
 - [2010](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2010_daily_avg_trip_distance.png)
 - [2011](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2011_daily_avg_trip_distance.png)
 - [2012](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2012_daily_avg_trip_distance.png)

Analyzing the graphics we can see a pattern that occurs with a frequency of every month, which means that we have a 
period of each month we can lower our fleet size to avoid unecessary costs.

## The largest vendors (in terms of trips revenue) of the semester

Identifying the largest vendors is important to verify wether we have a fair distribution between all vendors or
there's a monopoly and why's that. Moreover, I grouped in biannual graphics to check if there's a season for the 
vendors:

 - [2009-1](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2009-1_bianual_revenue_per_vendor.png)
 - [2009-2](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2009-2_bianual_revenue_per_vendor.png)
 - [2010-1](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2010-1_bianual_revenue_per_vendor.png)
 - [2010-2](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2010-2_bianual_revenue_per_vendor.png)
 - [2011-1](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2011-1_bianual_revenue_per_vendor.png)
 - [2011-2](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2011-2_bianual_revenue_per_vendor.png)
 - [2012-1](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2012-1_bianual_revenue_per_vendor.png)
 - [2012-2](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2012-2_bianual_revenue_per_vendor.png)

And, it is confirmed that there is not a season.

## The monthly price frequency (also known as histogram) of the trips paid in cash

The monthly price frequency of trips paid in cash reflects how many people still uses cash and which kind of trips 
(larger ones or smaller ones) they do. So, to analyze it I splitted in monthly graphics with the price frequency
histogram:

 - **Years:**
 - 2009
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-1_monthly_price_frequency.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-2_monthly_price_frequency.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-3_monthly_price_frequency.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-4_monthly_price_frequency.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-5_monthly_price_frequency.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-6_monthly_price_frequency.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-7_monthly_price_frequency.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-8_monthly_price_frequency.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-9_monthly_price_frequency.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-10_monthly_price_frequency.png)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-11_monthly_price_frequency.png)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-12_monthly_price_frequency.png)
 - 2010
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-1_monthly_price_frequency.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-2_monthly_price_frequency.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-3_monthly_price_frequency.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-4_monthly_price_frequency.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-5_monthly_price_frequency.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-6_monthly_price_frequency.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-7_monthly_price_frequency.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-8_monthly_price_frequency.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-9_monthly_price_frequency.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-10_monthly_price_frequency.png)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-11_monthly_price_frequency.png)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-12_monthly_price_frequency.png)
 - 2011
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-1_monthly_price_frequency.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-2_monthly_price_frequency.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-3_monthly_price_frequency.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-4_monthly_price_frequency.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-5_monthly_price_frequency.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-6_monthly_price_frequency.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-7_monthly_price_frequency.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-8_monthly_price_frequency.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-9_monthly_price_frequency.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-10_monthly_price_frequency.png)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-11_monthly_price_frequency.png)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-12_monthly_price_frequency.png)
 - 2012
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-1_monthly_price_frequency.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-2_monthly_price_frequency.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-3_monthly_price_frequency.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-4_monthly_price_frequency.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-5_monthly_price_frequency.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-6_monthly_price_frequency.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-7_monthly_price_frequency.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-8_monthly_price_frequency.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-9_monthly_price_frequency.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-10_monthly_price_frequency.png)

## Daily tips revenue amount in the last 3 months of 2012

The tips are important for the satisfaction of the taxi drivers, consequently their amusement reflects on their service
levels. So, to discover when they're doing great in terms of tips I splitted this graphics monthly, grouping each
graphic point into a daily revenue amount sum:

 - **Years:**
 - 2009
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-1_daily_tip_amount.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-2_daily_tip_amount.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-3_daily_tip_amount.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-4_daily_tip_amount.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-5_daily_tip_amount.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-6_daily_tip_amount.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-7_daily_tip_amount.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-8_daily_tip_amount.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-9_daily_tip_amount.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-10_daily_tip_amount.png)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-11_daily_tip_amount.png)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-12_daily_tip_amount.png)
 - 2010
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-1_daily_tip_amount.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-2_daily_tip_amount.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-3_daily_tip_amount.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-4_daily_tip_amount.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-5_daily_tip_amount.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-6_daily_tip_amount.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-7_daily_tip_amount.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-8_daily_tip_amount.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-9_daily_tip_amount.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-10_daily_tip_amount.png)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-11_daily_tip_amount.png)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-12_daily_tip_amount.png)
 - 2011
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-1_daily_tip_amount.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-2_daily_tip_amount.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-3_daily_tip_amount.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-4_daily_tip_amount.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-5_daily_tip_amount.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-6_daily_tip_amount.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-7_daily_tip_amount.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-8_daily_tip_amount.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-9_daily_tip_amount.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-10_daily_tip_amount.png)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-11_daily_tip_amount.png)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-12_daily_tip_amount.png)
 - 2012
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-1_daily_tip_amount.png)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-2_daily_tip_amount.png)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-3_daily_tip_amount.png)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-4_daily_tip_amount.png)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-5_daily_tip_amount.png)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-6_daily_tip_amount.png)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-7_daily_tip_amount.png)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-8_daily_tip_amount.png)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-9_daily_tip_amount.png)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-10_daily_tip_amount.png)

## Monthly average trip duration on weekends

One of the most busy days are the ones on the weekend, because of that we will break the weekends into monthly averages
to analyze which month is having the most long trips. As we have 12 months, these visualizations are grouped into
into one graphic per year:

 - [2009](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2009_monthly_avg_weekend_trips_duration.png)
 - [2010](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2010_monthly_avg_weekend_trips_duration.png)
 - [2011](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2011_monthly_avg_weekend_trips_duration.png)
 - [2012](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/2012_monthly_avg_weekend_trips_duration.png)
 
And yet nothing changed. The peaks are on december/january and on the summer too. With a exception for 2010 that december
weekends had one of the shorter average trip duration of those years.

## Visualization map per month of pickups 

To optimize our urban logistics grouping the pickups locations is essential to analyze the best fleet distribution
across the city. So, for this analysis we grouped into maps for each month. **_Please, keep in mind that there
is around 100.000 locations per month, so this map can load up your browser._ Be patient while the map loads!**

**Important observation: there was an error with the zoom map property, so when you open it, you will only see
the blue ocean near new york offshore. Just zoom out and you will see NYC. Thanks for your patience, again.**
 - **Years:**
 - 2009
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-1_pickups_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-2_pickups_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-3_pickups_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-4_pickups_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-5_pickups_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-6_pickups_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-7_pickups_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-8_pickups_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-9_pickups_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-10_pickups_map.html)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-11_pickups_map.html)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-12_pickups_map.html)
 - 2010
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-1_pickups_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-2_pickups_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-3_pickups_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-4_pickups_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-5_pickups_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-6_pickups_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-7_pickups_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-8_pickups_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-9_pickups_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-10_pickups_map.html)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-11_pickups_map.html)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-12_pickups_map.html)
 - 2011
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-1_pickups_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-2_pickups_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-3_pickups_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-4_pickups_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-5_pickups_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-6_pickups_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-7_pickups_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-8_pickups_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-9_pickups_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-10_pickups_map.html)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-11_pickups_map.html)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-12_pickups_map.html)
 - 2012
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-1_pickups_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-2_pickups_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-3_pickups_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-4_pickups_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-5_pickups_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-6_pickups_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-7_pickups_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-8_pickups_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-9_pickups_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-10_pickups_map.html)

## Visualization map per month of dropoffs

To optimize our urban logistics grouping the dropoffs locations is a must too, to analyze the best traffic flow
across the city. So, for this analysis we grouped into maps for each month. **_Please, keep in mind that there
is around 100.000 locations per month, so this map can load up your browser._ Be patient while the map loads!**

**Important observation: there was an error with the zoom map property, so when you open it, you will only see
the blue ocean near new york offshore. Just zoom out and you will see NYC. Thanks for your patience, again.**
 - **Years:**
 - 2009
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-1_dropoffs_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-2_dropoffs_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-3_dropoffs_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-4_dropoffs_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-5_dropoffs_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-6_dropoffs_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-7_dropoffs_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-8_dropoffs_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-9_dropoffs_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-10_dropoffs_map.html)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-11_dropoffs_map.html)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2009-12_dropoffs_map.html)
 - 2010
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-1_dropoffs_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-2_dropoffs_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-3_dropoffs_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-4_dropoffs_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-5_dropoffs_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-6_dropoffs_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-7_dropoffs_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-8_dropoffs_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-9_dropoffs_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-10_dropoffs_map.html)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-11_dropoffs_map.html)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2010-12_dropoffs_map.html)
 - 2011
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-1_dropoffs_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-2_dropoffs_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-3_dropoffs_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-4_dropoffs_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-5_dropoffs_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-6_dropoffs_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-7_dropoffs_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-8_dropoffs_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-9_dropoffs_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-10_dropoffs_map.html)
    / [November](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-11_dropoffs_map.html)
    / [December](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2011-12_dropoffs_map.html)
 - 2012
    - **Months:**
      [January](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-1_dropoffs_map.html)
    / [February](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-2_dropoffs_map.html)
    / [March](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-3_dropoffs_map.html)
    / [April](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-4_dropoffs_map.html)
    / [May](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-5_dropoffs_map.html)
    / [June](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-6_dropoffs_map.html)
    / [July](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-7_dropoffs_map.html)
    / [August](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-8_dropoffs_map.html)
    / [September](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-9_dropoffs_map.html)
    / [October](https://social-wiki-datalake.s3.amazonaws.com/data-sprints-eng-test/outputs/monthly/2012-10_dropoffs_map.html)

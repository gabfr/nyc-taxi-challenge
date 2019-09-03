# NYC Taxi Challenge

This project aims to answer a few specific questions regarding the NYC Taxi Trips Dataset with the objective
of analysing the taxi's performances and improve it through logistic reorganization and service improvement.

 - **[Click here to check the final analysis of this challenge](ANALYSIS.md)**
 - [If you are interested, you can checkout the data exploration steps in this notebook located
in another repository.](https://github.com/gabfr/data-engineering-nanodegree/blob/master/explorations/nyc-taxi-challenge.ipynb)

## Getting started

This project is based on several DAGs (Directed Acyclic Graphs) that are executed on Apache Airflow, moreover I used
Airflow to orchestrate all ETL processes and maintain their correct frequency along with a AWS Redshift database cluster.

### Provisioning the Redshift Cluster

Create (if not already created) your Redshift cluster. I provided a few scripts to help spining up a Redshift
cluster using the AWS API, directly from the command line. Before diving into them, make a copy of the `dwh.cfg.example`
as `dwh.cfg` and fill all the keys (except the `HOST` under `CLUSTER` section). Then you just need to:

 1. Start the cluster provisioning by running: 
     - `python aws/create_cluster.py`
 2. Wait a few minutes and check if the cluster status is available by running: 
     - `python aws/check_cluster_available.py`
     - You should run this script until the cluster is available. Because this script is responsible of updating our 
     `dwh.cfg` with the `HOST` address
 3. When the cluster is already available, your dwh.cfg would be rewrited with its `HOST` address. Then you just need to
 copy that configuration over to the Airflow Connections. There's a script to do that:
      - `python aws/register_airflow_connections.py`
 4. (_optional, after work_) And for the sake of our AWS bills (keep'em low), there´s also a script to destroy the cluster: 
 `python aws/destroy_cluster.py` (**but this one is for later**)
 
 After doing that, before activating the DAGs you have to configure the following Airflow connections. But before we 
 need to get Airflow itself running:
 
### Running Airflow locally

We will use Docker to provision our local environment and to ease the production deployment process too (if required).
The Docker image we will use is the puckel/docker-airflow (`docker pull puckel/docker-airflow`)

**Inside the root folder of this project run the following command:**

```bash
docker run -d -p 8080:8080  \
    -v $(pwd)/dags:/usr/local/airflow/dags \
    -v $(pwd)/plugins:/usr/local/airflow/plugins \
    -v $(pwd)/requirements.txt:/requirements.txt \
    puckel/docker-airflow webserver
```

### Airflow Connections

If you hit on the wall with the `python aws/register_airflow_connections.py` below we have a table with a dictionary
of connections:

| Service | Conn ID | Conn Type | Other fields |
| ------- | ------- | --------- | ------------------ |
| Redshift | `redshift` | `Postgres` | This one you should figure out by yourself. (It's your database credentials!) |
| Amazon Web Services Credentials | `aws_credentials` | `Amazon Web Services` | On the **login** field you fill with your API Key. And in the password field you fill with your API Secret. |


FROM apache/airflow:slim-latest-python3.11
USER root
RUN apt-get update && \\
    apt-get -y install git && \\
    apt-get clean
USER airflow
FROM jupyter/all-spark-notebook
COPY ./jupyter_notebook_config.py /config/location/jupyter_notebook_config.py
RUN mkdir jupyter
RUN pip install psycopg2-binary\
    minio
WORKDIR /jupyter
COPY . .
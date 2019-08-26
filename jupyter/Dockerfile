FROM jupyter/all-spark-notebook
COPY ./jupyter_notebook_config.py /config/location/jupyter_notebook_config.py
RUN mkdir jupyter
WORKDIR /jupyter
RUN pip install psycopg2-binary\
    minio
RUN RUN Rscript -e "install.packages('stringr')"

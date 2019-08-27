FROM jupyter/all-spark-notebook
COPY ./jupyter_notebook_config.py /config/location/jupyter_notebook_config.py
RUN mkdir jupyter
COPY ./requirements.txt /jupyter/requirements.txt
COPY ./requirements.r /jupyter/requirements.r
WORKDIR /jupyter
RUN pip install -r requirements.txt
RUN Rscript requirements.r

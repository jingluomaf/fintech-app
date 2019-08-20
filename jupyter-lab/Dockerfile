FROM jupyter/all-spark-notebook
COPY ./jupyter_notebook_config.py /config/location/jupyter_notebook_config.py
RUN mkdir jupyter-lab
WORKDIR /jupyter-lab
COPY . .
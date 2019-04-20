FROM continuumio/anaconda3:2018.12

RUN apt-get update
RUN apt-get install build-essential --yes
RUN apt-get install libarchive-dev --yes
RUN conda build purge
RUN conda config --add channels conda-forge

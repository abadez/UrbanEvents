FROM python:3.6

RUN apt-get -y update && apt-get -y install gdal-bin

RUN mkdir /UrbanEvents
ADD UrbanEvents/ /UrbanEvents/

WORKDIR /UrbanEvents

RUN pip install -r requirements.txt



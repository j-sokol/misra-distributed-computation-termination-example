FROM python:3.8
MAINTAINER Jan Sokol "sokolja2@fit.cvut.cz"


RUN apt-get -y update
RUN apt-get install -y build-essential cmake python3 libgeos-dev


# Copy reqs first because of docker layers
COPY requirements.txt /app/


# Set working directory
WORKDIR /app


# RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install -r requirements.txt
# Copy app to remote container
COPY . /app

EXPOSE 5049

ENV PYTHONPATH=/app

ENTRYPOINT ["sh", "docker-entrypoint.sh"]

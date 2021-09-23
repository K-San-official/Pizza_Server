# Filename: Dockerfile

# Base Image
FROM ubuntu:latest

# Update
RUN apt-get -y update

# Add all python dependencies
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
RUN pip3 install flask-restful
RUN pip3 install mysql-connector-python

# Install mySQL
RUN apt-get install -y mysql-server

# Copy the application files
ADD . /server
WORKDIR /server

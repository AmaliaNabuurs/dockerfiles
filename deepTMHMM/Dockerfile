FROM ubuntu:20.04

#update apt
RUN apt-get update -y

#install python and packages
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install pybiolib -U

WORKDIR /app

COPY deeptmhmm.py .

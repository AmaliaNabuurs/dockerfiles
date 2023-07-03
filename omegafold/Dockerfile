FROM ubuntu:latest

RUN apt update

RUN apt install python3 python3-pip -y
RUN pip install --upgrade pip

RUN apt install -y git

RUN git clone https://github.com/HeliXonProtein/OmegaFold
WORKDIR OmegaFold/
RUN python3 setup.py install


FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY blastout_to_list.py .

CMD [ "executable" ] [ "python3", "./blastout_to_list.py"]
FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY results_parser.py .

CMD [ "executable" ] [ "python3", "./results_parser.py"]

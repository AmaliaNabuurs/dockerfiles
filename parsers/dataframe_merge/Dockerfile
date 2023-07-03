FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY dataframe_merge.py .

CMD [ "executable" ] [ "python3", "./dataframe_merge.py"]
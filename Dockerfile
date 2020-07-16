FROM python:3.7-slim-buster

WORKDIR /opt/test_app/

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ ./

RUN pytest -v datahandler_test.py && rm database.csv
CMD [ "python3", "app.py"]
FROM python:3
FROM postgres:11

WORKDIR /home/tyrell/app
COPY . /home/tyrell/app

COPY csv /home/tyrell/app
# RUN pip install --no-cache-dir -r requirements.txt


CMD [ "./main/importer.py", "python"]
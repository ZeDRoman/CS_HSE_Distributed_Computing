FROM ubuntu:latest
FROM python:latest
MAINTAINER Roman Ilgovskit 'ilgovskiy@mail.ru'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python create_db.py
ENTRYPOINT ["python"]
CMD ["__init__.py"]

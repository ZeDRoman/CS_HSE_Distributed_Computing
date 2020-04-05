FROM python:latest
MAINTAINER Roman Ilgovskiy 'ilgovskiy@mail.ru'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.5/bin/ pip install psycopg2
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ADD run.sh /
RUN chmod +x /run.sh
CMD ["/run.sh"]

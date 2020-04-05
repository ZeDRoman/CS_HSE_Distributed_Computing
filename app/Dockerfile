FROM python:latest
MAINTAINER Roman Ilgovskiy 'ilgovskiy@mail.ru'
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ADD run.sh /
RUN chmod +x /run.sh
CMD ["/run.sh"]
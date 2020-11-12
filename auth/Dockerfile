FROM python:latest
MAINTAINER Roman Ilgovskiy 'ilgovskiy@mail.ru'
COPY . /auth
WORKDIR /auth
RUN pip install -r requirements.txt
ADD run.sh /
RUN chmod +x /run.sh
CMD ["/run.sh"]

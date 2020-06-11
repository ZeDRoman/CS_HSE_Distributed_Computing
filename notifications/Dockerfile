FROM python:latest
MAINTAINER Roman Ilgovskiy 'ilgovskiy@mail.ru'
COPY . /notifications
WORKDIR /notifications
RUN pip install -r requirements.txt
CMD ["python", "./run.py"]

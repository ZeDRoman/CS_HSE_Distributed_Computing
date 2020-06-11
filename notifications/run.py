import smtplib
import time
import logging
import pika
import json
import socket

from pika.exceptions import AMQPConnectionError

from config import FROM_EMAIL, MSG_QUEUE, SMTP_URL, SMTP_PORT

def wait_connection():
    rounds = 10
    round = 0
    sleep = 1

    connection = None
    while round < rounds:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=MSG_QUEUE))
            break
        except (AMQPConnectionError, socket.gaierror) as ex:
            time.sleep(sleep)
        round += 1
        connection = None
    return connection

def send_email(email_adress, message, header="Email confirmation"):
    email = "\r\n".join((
        "From: %s" % FROM_EMAIL,
        "To: %s" % email_adress,
        "Subject: %s" % header,
        "",
        message
    ))

    server = smtplib.SMTP(SMTP_URL, SMTP_PORT)
    try:
        server.sendmail(FROM_EMAIL, [email_adress], email)
        logging.warning("sent msg to " + email_adress)
    except smtplib.SMTPException as e:
        print(e.strerror)
    finally:
        server.quit()


def callback(ch, method, _, body):
    logging.warning("got msg")
    data = json.loads(body)
    try:
        send_email(email_adress=data["email"], message=data["confirmation_url"])
    except socket.gaierror:
        return
    ch.basic_ack(delivery_tag=method.delivery_tag)


logging.warning("started")
connection = wait_connection()
channel = connection.channel()
channel.queue_declare(queue="notifications", durable=True)
channel.basic_consume(on_message_callback=callback, queue="notifications")
channel.start_consuming()
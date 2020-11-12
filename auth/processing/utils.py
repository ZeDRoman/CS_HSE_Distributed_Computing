import string
import random
import socket
import time
import pika
import jwt
import json
from pika.exceptions import AMQPConnectionError

from config import MSG_QUEUE, CONFIRM_SECRET, CONFIRM_URL


def createToken(size=255, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


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


def send_message(queue, message):
    connection = wait_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=2))
    connection.close()


def send_confirmation_email(email, password):
        confirmation_token = jwt.encode({"email":email, "password":password}, CONFIRM_SECRET).decode()
        confirmtaion_url = CONFIRM_URL + '?confirm_token=' + confirmation_token
        send_message("notifications", json.dumps({"email": email, "confirmation_url": confirmtaion_url}))
        import logging
        logging.warning(confirmtaion_url)
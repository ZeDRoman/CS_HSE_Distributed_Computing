import json

import socket
import pika
from flask import current_app
from pika.exceptions import AMQPConnectionError
from processing.debug_messages import log_form_validation_error, production_form_data
from config import MSG_QUEUE

def checkIsNumber(elem, elem_type):
    if isinstance(elem, int):
        return True

    if elem is None or not isinstance(elem, str) or not elem.isdigit():
        current_app.logger.info(elem_type + ' not a number, value: ' + str(elem))
        return False
    return True


def formIsValid(form):
    if not form.validate():
        app.logger.info(log_form_validation_error(production_form_data(), form))
        return False
    return True



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


def send_confirmation_csv_file(file_name):
        send_message("csv", json.dumps({"file": file_name}))
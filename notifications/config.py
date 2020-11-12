import os

SMTP_URL = os.environ.get('SMTP_URL', '127.0.0.1')
SMTP_PORT = os.environ.get('SMTP_PORT', "25")
SMTP_URI = SMTP_URL + ":" + SMTP_PORT
FROM_EMAIL = os.environ.get("FROM_EMAIL", "my_app@local")
MSG_QUEUE = os.environ.get('MSG_QUEUE')
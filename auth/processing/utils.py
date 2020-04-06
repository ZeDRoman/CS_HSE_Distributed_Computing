import string
import random


def createToken(size=255, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
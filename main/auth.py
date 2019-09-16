import random
import secrets
import string

_alphabet = string.ascii_letters + string.digits


AUTH = ''.join(secrets.choice(_alphabet) for i in range(20)) # for a 20-character password
USER = 'User'
PASS = '12345'
'''Security primitves that provide helpful, must-have features like
secure password hashing and our preferred encoding schemes.
'''

import hashlib
import os


def hash_password(password: str) -> str:
    '''Apply a secure (in 2019) configuration of the
    [Scrypt](https://en.wikipedia.org/wiki/Scrypt) hashing algorithm
    to produce a hash that can be stored in the database without exposing
    the user's password when it's checked at login or in case of compromise.
    '''

    salt = os.urandom(16)
    pwd = bytes(password, 'utf-8')

    return hashlib.scrypt(pwd, salt=salt, n=16, r=10, p=2)

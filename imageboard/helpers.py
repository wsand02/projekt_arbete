import os
import hashlib
import binascii
import random
import shortuuid


def get_random():
    a = random.randint(1, 1000000000000000)
    return a


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


def hash_filename(f_name):
    ext = f_name.split('.')[-1]
    notsalt = (f"{str(f_name)}")
    notsalt = str.encode(notsalt)
    salt = get_random()
    salt = f'{salt}'
    salt = str.encode(salt)
    dk = hashlib.pbkdf2_hmac('sha256', notsalt, salt, 10000)
    m = binascii.hexlify(dk)
    m = m.decode("utf-8")
    p = m
    p = f"{p}.{ext}"
    return p


def shortuuid_filename(f_name):
    ext = f_name.split('.')[-1]
    sid = shortuuid.uuid()
    p = f'{sid}.{ext}'
    return p


def random_file_name(instance, filename):
    result_filename = shortuuid_filename(filename)
    return f'uploads/{result_filename}'

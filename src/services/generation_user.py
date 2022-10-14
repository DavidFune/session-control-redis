from faker import Faker
import time
import random
import redis
import json

def genaration_users(key):

    fake = Faker()

    user = {
      "id": key,
      "nome": fake.name(),
      "email": fake.ascii_safe_email(),
      "password": fake.password(length=8)
    }

    return user

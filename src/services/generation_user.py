from faker import Faker
import time
import random
import redis
import json

keys = ['id-4558', 'id-8272', 'id-5069', 'id-7369']

fake = Faker()

for key in keys:
  users = {
    "id": key,
    "nome": fake.name(),
    "email": fake.ascii_safe_email(),
    "password": fake.password(length=8)
  }
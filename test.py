import hashlib
import redis
import json

r = redis.Redis(host="localhost", port=6379, db=0, password="")


keys = [
    '8e443b99-ffd0-49d7-98bb-db835eded4c1',
    'f8fff694-1379-44be-9827-f005da066395'
    '86f9bf4c-ccb4-4791-aee4-5c9faafb3a1c',
    '71355566-9548-48fe-bf4f-a38afbaef523'
    ]

passwd = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiMmNkYWFkNjEtYTc4YS00ZWMxLWFmODAtMjI3MjU0NGQxYWJmIiwibmFtZSI6IkRhdmlkIEZ1bmUiLCJlbWFpbCI6ImRhdmlkLmZ1bmVAZXNtYXJ0ZW5nLmNvbSIsImNyZWF0ZWRfYXQiOiIyMDIxLTEwLTExVDAyOjAyOjEwLjU5MTA2MiIsInVwZGF0ZWRfYXQiOiIyMDIyLTA5LTMwVDE5OjQzOjE0Ljk0NTEwMiJ9LCJleHAiOjE2NjYwMTMzOTB9.GLsf0yfJtUcb3OgsWs0pXdR4fkafggs2JGDuLgvT8rKPhMRAGLgUp-EnYrI5pNl3DJ6usBLU5p6t2-QHYwXoBG5P7lVF6i3T9lRTmIUMQQwg1sLLbvoZKPyZp9Ny5cnK8vS2956Wuvcb2m-lgwMpcegtxMxmOl2NUe7eJ8Ij2juv4Cn_KHwijg9iK46K-WJKtECazd7GwO4eubPCwh_AQ_2CYkj8_be47o50eYrHPR8PIkG3z5eroM0LP3Tlx9CfvAdWPi6jESnc6JsK5_Fjg3HH6ulYegJqz7JFh90koDWk3pkp-lcBq8xEhcvkbkZ7Z8z4Xb1MXxpXtbdj4XI2u9IOGDQnFvAUBOolugNjHHeCmaVcn_CymCJndomdwClKCnP-_FSUeEY8XCeWb7CKM74nf1Ug_V0aAOULgAezgaky6aAcJt4ZFRLQg9nJ7CMYzexCpZH2x8Tz9_a5tNRHsiTxnruHUpEhKwyZCHpndAABQ2-gJVp3Q24no9xYaOvepVaGf5g9oby_SuWLEyESx3xp_F_Yg-umQh5-4MRIVD_i0qMcmxvGJaWILppUeDYG3DApyEp-4CQcHO0jDRRqITQX0ZnikBnJ08BtTD6xAKl8g-vAjcSyhvk1UFZL6PrDBqJPcYEkztvSJOyNJHo-ghNGC5bf2tdv0Ay7mOu1toM'
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def test_redis_user():
    u = r.get(f'user:{keys[0]}')
    if u == None:
        return {}
    return json.loads(u)

def test_redis_token():
    u = r.get(keys[0])
    if u == None:
        return {}
    return u.decode()

def get_private_key():
    return open("src/certificates/jwtRS256.key", "rb").read()

print(test_redis_user())
print(test_redis_token())
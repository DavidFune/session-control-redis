import redis
import json
from services import token


r = redis.Redis(host="localhost", port=6379, db=0, password="")

def login(user):

    if r.get(user.id) == None:
        
        _token = token.create(user)
        sha_token = token.sha_token(_token)
        r.set(user.id, sha_token, ex=30)
        return _token

    elif r.get(user.id) != None:
        r.delete(user.id)
        _token = token.create(user)
        sha_token = token.sha_token(_token)
        r.set(user.id, sha_token, ex=30)
        return _token

def logout(user):
    if r.get(user.id) == None:
        return 'User not found'
    elif r.get(user.id) != None:
        r.delete(user.id)
        return 'logout success'




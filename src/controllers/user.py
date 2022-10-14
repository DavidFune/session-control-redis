import redis
import json
from services import token


r = redis.Redis(host="localhost", port=6379, db=0, password="")

def login(user):
    user_id = user['id']
    if r.get(user_id) == None:

        _token = token.create(user)
        sha_token = token.sha_token(_token)

        r.set(user_id, sha_token, ex=30)
        r.set(f'user:{user_id}', json.dumps(user), ex=30)

        return _token

    elif r.get(user_id) != None:

        r.delete(user_id)
        r.delete(f'user:{user_id}')
        
        _token = token.create(user)
        sha_token = token.sha_token(_token)

        r.set(user_id, sha_token, ex=30)
        r.set(f'user:{user_id}', json.dumps(user), ex=30)

        return _token

def logout(user):

    if r.get(user['id']) == None:
        return 'User not found'
        
    elif r.get(user['id']) != None:
        
        r.delete(user['id'])
        return 'logout success'

def get_user(user_id, _token):
   
    sha_token = token.sha_token(_token)

    _user_token = r.get(user_id).decode()
    user_token = _user_token or None

    if user_token == sha_token:
        return json.loads(r.get(f'user:{user_id}'))
    else:
        return 'unauthorized'







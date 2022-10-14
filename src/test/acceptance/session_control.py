from services.generation_user import genaration_users
from controllers import user


keys = [
    '8e443b99-ffd0-49d7-98bb-db835eded4c1',
    'f8fff694-1379-44be-9827-f005da066395'
    '86f9bf4c-ccb4-4791-aee4-5c9faafb3a1c',
    '71355566-9548-48fe-bf4f-a38afbaef523'
    ]

def login_and_get_user():
    _user = genaration_users(keys[0])
    _token = user.login(_user)
    this_user = user.get_user(_user['id'], _token)
    return this_user

def simultaneous_logins():
    user_seesion1 = genaration_users(keys[0])
    user_seesion2 = genaration_users(keys[0])
    _token1 = user.login(user_seesion1)
    user.login(user_seesion2)
    this_user = user.get_user(user_seesion1['id'], _token1)
    return this_user
from test.acceptance import session_control


print('Login and Get User')
session_control.login_and_get_user()

print('Simultaneous logins: unauthorized')
print(session_control.simultaneous_logins())
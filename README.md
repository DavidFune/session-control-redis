# session control

This is a simple python application for sessionless access control for api' rest, using redis as a system to store the keys of logged in users

# Up the redis

at the root of the directory from the command

```
docker-compose up -d

```

# Preparing environment

at the root of the directory from the command

```
python -m venv venv

```

if you have doubts about how to use venv, follow the tutorial

https://www.youtube.com/watch?v=ZQ60SJDACuc&list=PLxUgxeBGSBjshdS-XRP2gNLs1ji_EbPI4&index=1&ab_channel=Ot%C3%A1vioMiranda

with the venv terminal activated give the command

```
pip install -r src/requirements.txt
```

right after to see the tests run

```
python src/main.py

```





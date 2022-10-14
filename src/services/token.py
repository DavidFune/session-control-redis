import jwt
import hashlib


def get_private_key():
    return open("src/certificates/jwtRS256.key", "rb").read()

def get_public_key():
    return open("src/certificates/jwtRS256.key.pub", "rb").read()


def create(user, exp=30):
    private_key = get_private_key()

    user.pop('password')
    payload = {"user": user, "exp": exp}

    encoded = jwt.encode(payload, private_key, algorithm="RS256")

    return encoded

def decode(token):
    public_key = get_public_key()
    decoded = jwt.decode(token, public_key, algorithms=["RS256"])

    return decoded

def sha_token(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
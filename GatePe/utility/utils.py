# common/utils.py

import jwt
from django.conf import settings
from datetime import datetime, timedelta

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA,
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    return token

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

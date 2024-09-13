import jwt
from datetime import datetime, timedelta
import datetime as dt

now = datetime.now(dt.UTC)

payload = {
    'iss': 'https://auth.coffeemesh.io/',
    'sub': 'fasdf-fasd-fasdf-fasd-fasf',
    'aud': 'http://localhost:8000/orders',
    'iat': now.timestamp(),
    'exp': (now + timedelta(hours=24)).timestamp(),
    'scope': 'openid'
}

token = jwt.encode(payload=payload, key='secret', algorithm='HS256')
print(token)
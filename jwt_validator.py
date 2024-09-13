import jwt
from datetime import datetime, timedelta
import datetime as dt
import logging
from pathlib import Path
import json
from cryptography.hazmat.primitives import serialization

import pem

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def add_time_to_payload(payload:dict, **timedelta_params) -> dict:
    ''' adds current iat and exp fields to payload'''

    now = datetime.now(dt.UTC)
    logger.info (f'setting {now = }')

    payload['iat'] = now.timestamp()
    payload['exp'] = (now + timedelta(**timedelta_params)).timestamp()

    logger.info(f'setting payload = {json.dumps(payload, indent=2)}')
    return payload

def create_pems(private_pem:str, publc_pem:str):
    ''' creates pem files deleting any existing ones'''

    for pemfile in private_pem, public_pem:
        pemfile = Path(pemfile)
        if pemfile.exists():
            logger.info(f'deleting existing {pemfile}')
            pemfile.unlink()

    pem.create_pem_keys(cn='jwt-tutorial')

def generate_jwt(payload:dict, private_pem:str):
    ''' creates jwt token from payload and private pem file'''

    logger.info('getting private pem text')
    private_key_text = pem.load_pem_key(private_pem)

    logger.info('getting private key')
    private_key = serialization.load_pem_private_key(
        private_key_text.encode(),
        password=None
    )
    
    logger.info('generating jwt token')
    return jwt.encode(payload, private_key, 'RS256')


payload = {
    'iss': 'https://auth.coffeemesh.io/',
    'sub': 'fasdf-fasd-fasdf-fasd-fasf',
    'aud': 'http://localhost:8000/orders',
    # 'iat': None,
    # 'exp': None,
    'scope': 'openid'
}
private_pem = 'private_key.pem'
public_pem = 'public_key.pem'

create_pems(private_pem, public_pem)
payload = add_time_to_payload(payload, minutes=1)
token = generate_jwt(payload, private_pem)
print(f'{token = }')



import jwt
from datetime import datetime, timedelta
import datetime as dt
import logging
from pathlib import Path
import json

import pem

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

now = datetime.now(dt.UTC)
logger.info (f'setting {now = }')

payload = {
    'iss': 'https://auth.coffeemesh.io/',
    'sub': 'fasdf-fasd-fasdf-fasd-fasf',
    'aud': 'http://localhost:8000/orders',
    'iat': now.timestamp(),
    'exp': (now + timedelta(hours=24)).timestamp(),
    'scope': 'openid'
}
logger.info(f'setting payload = {json.dumps(payload, indent=2)}')

private_pem = 'private_key.pem'
public_pem = 'public_key.pem'

for pemfile in private_pem, public_pem:
    if Path(pemfile).exists():
        logger.info(f'deleting existing {pemfile}')

pem.create_pem_keys(cn='jwt-tutorial')

private_key_text = pem.load_pem_key(private_pem)
public_key_text = pem.load_pem_key(public_pem)


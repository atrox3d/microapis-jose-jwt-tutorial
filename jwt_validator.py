from pathlib import Path
from turtle import pu
import jwt
import logging
from cryptography.x509 import load_pem_x509_certificate

import jwt_generator, payload_manager

logger = logging.getLogger(__name__)

def decode_and_validate_token(access_token:str, public_pem:str, audience:str):
    unverified_headers = jwt.get_unverified_header(access_token)
    logger.debug(f'{unverified_headers = }')

    public_key = Path(public_pem).read_text()
    logger.debug(f'{public_key = }')

    x509_certificate = load_pem_x509_certificate(
        public_key.encode()
    ).public_key()
    logger.debug(f'{x509_certificate = }')

    return jwt.decode(
        access_token,
        x509_certificate,
        algorithms=unverified_headers['alg'],
        audience=audience
    )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    payload = payload_manager.load_payload_from_json('payload.json')

    private_pem = 'private_key.pem'
    public_pem = 'public_key.pem'
    jwt_generator.create_pems(private_pem, public_pem)
    
    token = jwt_generator.generate_jwt(payload, private_pem)
    decoded = decode_and_validate_token(token, public_pem, payload['aud'])
    print(f'{decoded = }')
    
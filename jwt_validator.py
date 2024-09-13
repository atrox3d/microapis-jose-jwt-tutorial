import jwt
import logging

import jwt_generator, payload_manager

logger = logging.getLogger(__name__)

def decode_and_validate_token(access_token:str):
    unverified_headers = jwt.get_unverified_header(access_token)
    logger.info(f'{unverified_headers = }')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    payload = payload_manager.load_payload_from_json('payload.json')

    private_pem = 'private_key.pem'
    public_pem = 'public_key.pem'
    jwt_generator.create_pems(private_pem, public_pem)
    
    token = jwt_generator.generate_jwt(payload, private_pem)
    decode_and_validate_token(token)
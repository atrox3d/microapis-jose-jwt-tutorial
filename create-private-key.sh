#!/bin/bash

openssl req -x509 -nodes -newkey rsa:2048 -keyout private_key.pem -out public_key.pem -subj '/CN=jwt-tutorial'

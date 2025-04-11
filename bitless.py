import os
import hashlib

def keypair():
    private_key = hashlib.sha256(os.urandom(32)).digest()
    public_key = hashlib.sha256(private_key).digest()
    return private_key, public_key

def sign(message, private_key):
    if message == '':
        signedbit = private_key
        return signedbit
    raise NotImplementedError

def verify(signedbit, public_key):
    if hashlib.sha256(signedbit).digest().hex() == public_key.hex():
        message = ''
        return message
    raise NotImplementedError

# private_key, public_key = keypair()
# print(f"Private Key: {private_key.hex()}")
# print(f"Public Key:  {public_key.hex()}")
# print(f"Signature:   {sign('', private_key).hex()}")
# print(f"Verified:    {verify(sign('', private_key), public_key)}")

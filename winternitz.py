# import fourbit

# def keypair(message):
#     return [fourbit.keypair() for _ in message]

# def sign(message, keypairs):
#     signatures = []
#     for i in range(len(message)):
#         sk = keypairs[i][1]
#         print(i)
#         for _ in range(message[i]):
#             sk = fourbit.sign(message[i], sk)
#             print(sk)
#         signatures.append(sk)
#     return signatures
# # def verify
# message =  [1,2,3,4]
# keypairs = keypair(message)
# signatures = sign(message, keypairs)

# print(signatures)

import hashlib
import os

def keypair():
    secret = hashlib.sha256(os.urandom(32)).digest()
    public = secret
    for _ in range(16):
        public = hashlib.sha256(public).digest()
    return secret, public

def calculate_checksum(message):
    return (16 - 1 - message).to_bytes(2, byteorder='big')

def sign(message, secret):
    if not (0 <= message <= 15):
        raise ValueError("Message must be a 4-bit integer (0–15).")
    
    checksum = calculate_checksum(message)
    
    sig = secret
    for _ in range(message):
        sig = hashlib.sha256(sig).digest()

    signature = sig + checksum
    return signature

def verify(signature, public, message):
    
    sig = signature[:-2]
    checksum = signature[-2:]

    calculated_checksum = calculate_checksum(message)
    if checksum != calculated_checksum:
        return False  
    check = sig
    for _ in range(16 - message):
        check = hashlib.sha256(check).digest()

    return check == public

# message = 12
# secret, public = keypair()
# signature = sign(message, secret)
# print("Signature:", signature.hex())
# print("Verification result:", verify(signature, public, message))

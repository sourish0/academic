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

def sha256(x):
    return hashlib.sha256(x).digest()

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def generate_mask(seed, i):
    return sha256(seed + i.to_bytes(1, 'big'))

def keypair():
    secret = sha256(os.urandom(32))
    seed = os.urandom(16)
    public = secret
    for i in range(16):
        mask = generate_mask(seed, i)
        public = sha256(xor_bytes(public, mask))
    return (secret, seed), public

def calculate_checksum(message):
    return (15 - message).to_bytes(2, byteorder='big') 

def sign(message, keypair):
    secret, seed = keypair
    checksum = calculate_checksum(message)
    sig = secret
    for i in range(message):
        mask = generate_mask(seed, i)
        sig = sha256(xor_bytes(sig, mask))
    return sig + checksum + seed

def verify(signature, public, message):
    sig = signature[:32]
    checksum = signature[32:34]
    seed = signature[34:]

    if checksum != calculate_checksum(message):
        return False

    val = sig
    for i in range(message, 16):
        mask = generate_mask(seed, i)
        val = sha256(xor_bytes(val, mask))

    return val == public


# if __name__ == "__main__":
#     message = 12
#     key, pub = keypair()
#     sig = sign(message, key)
#     print("Signature:", sig.hex())
#     print("Valid? ->", verify(sig, pub, message))

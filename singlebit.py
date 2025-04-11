import bitless

def keypair():
    p0,s0 = bitless.keypair()
    p1,s1 = bitless.keypair()
    return p0+p1, s0+s1

def sign(message,private_key):
    if message == 0:
        return ('0',bitless.sign('',private_key[0:32]))
    elif message == 1:
        return ('1',bitless.sign('',private_key[32:64]))
    raise NotImplementedError
def verify(signedbit, public_key):
    if signedbit[0] == '0':
        bitless.verify(signedbit[1],public_key[0:32])
        return 0
    elif signedbit[0] == '1':
        bitless.verify(signedbit[1],public_key[32:64])
        return 1
    raise NotImplementedError

# private_key, public_key = keypair()
# signedbit = sign(1,private_key)
# print(f"Private Key: {private_key.hex()}")
# print(f"Public Key:  {public_key.hex()}")
# print(f"Signature:   {signedbit[1].hex()}")
# verified_bit = verify(signedbit,public_key)
# print(f"Verified:    {verified_bit}")
import singlebit

def keypair():
    p0,s0 = singlebit.keypair()
    p1,s1 = singlebit.keypair()
    p2,s2 = singlebit.keypair()
    p3,s3 = singlebit.keypair()
    return p0+p1+p2+p3, s0+s1+s2+s3

def sign(message, private_key):
    if message < 0 or message > 15:
        raise ValueError
    m0 = singlebit.sign(1 & (message >> 0), private_key[0:64])
    m1 = singlebit.sign(1 & (message >> 1), private_key[64:128])
    m2 = singlebit.sign(1 & (message >> 2), private_key[128:192])
    m3 = singlebit.sign(1 & (message >> 3), private_key[192:256])
    return (m0, m1, m2, m3)



def verify(signedbit, public_key):
    m0 = singlebit.verify(signedbit[0], public_key[0:64])
    m1 = singlebit.verify(signedbit[1], public_key[64:128])
    m2 = singlebit.verify(signedbit[2], public_key[128:192])
    m3 = singlebit.verify(signedbit[3], public_key[192:256])
    return (m0 + 2*m1 + 4*m2 + 8*m3)


private_key, public_key = keypair()
signedbit = sign(11, private_key)

print(f"Private Key: {private_key.hex()}")
print(f"Public Key:  {public_key.hex()}")
print(f"Signature:   {signedbit}")

# This should be True
print(signedbit[2][1])
print(singlebit.sign(int(signedbit[2][0]), private_key[128:192])[1])


verified_bit = verify(signedbit, public_key)
print(f"Verified bit: {verified_bit}")


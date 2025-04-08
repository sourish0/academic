import numpy as np
import hashlib

def signing_key(message):
    message = str(message)
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    print(f"\n[1] Binary representation of message: {binary_message}")
    
    message_bits = [int(i) for i in binary_message]  
    k = len(message_bits)  # Security Parameter
    
    key = np.random.randint(0, 2**16, size=(2*k, k)).tolist()
    print(f"\n[2] Private Signing Key (2k x k):")
    for i, row in enumerate(key):
        print(f"  Row {i}: {row}")
    
    return key, binary_message, message_bits

def verifying_key(key):
    print(f"\n[3] Verifying Key (Hash of each row in signing key):")
    verification_key = []
    for i, row in enumerate(key):
        hashed_row = [hashlib.sha256(str(r).encode()).hexdigest() for r in row]
        print(f"  Row {i} hash: {hashed_row}")
        verification_key.append(hashed_row)
    return verification_key

def signature(message_bits, key):
    sig = []
    print(f"\n[4] Signature:")
    for idx, bit in enumerate(message_bits):
        row_index = 2 * idx + bit
        sig_row = key[row_index]
        print(f"  Bit {bit} at index {idx}: Picking row {row_index} → {sig_row}")
        sig.append(sig_row)
    return sig

def verification(binary_message, message_bits, verification_key, signature):
    print(f"\n[5] Verifying Signature:")
    hashed_signature = []
    for i, row in enumerate(signature):
        hashed_row = [hashlib.sha256(str(r).encode()).hexdigest() for r in row]
        print(f"  Signature row {i} hashed: {hashed_row}")
        hashed_signature.append(hashed_row)

    for idx, bit in enumerate(message_bits):
        expected = verification_key[2*idx + bit]
        actual = hashed_signature[idx]
        if expected != actual:
            print(f"  ❌ Mismatch at bit index {idx}: Expected hash doesn't match actual hash.")
            return False
        else:
            print(f"  ✅ Match at bit index {idx}")
    return True

# 🔍 Full Demo

message = "H"
print(f"\n=== DIGITAL SIGNATURE DEMO FOR MESSAGE: '{message}' ===")

# 1. Key Generation
private_key, binary_msg, message_bits = signing_key(message)

# 2. Generate Verifying Key (Public Key)
public_key = verifying_key(private_key)

# 3. Sign the message
sig = signature(message_bits, private_key)

# 4. Verify the signature
is_valid = verification(binary_msg, message_bits, public_key, sig)

print(f"\n[6] Final Verification Result: {'✅ Signature is valid' if is_valid else '❌ Signature is invalid'}")

import fourbit

dictionary = {
    'h': 0,
    'e': 1,
    'l': 2,
    'o': 3,
    'w': 4,
    'r': 5,
    'd': 6,
    ' ': 7
}
rev_dict = {v: k for k, v in dictionary.items()}
BASE = 16

def encode_message(text):
    return [dictionary[c] for c in text]

def compute_checksum(msg, base):
    checksum = sum((base - 1 - m) for m in msg)
    chunks = []
    while checksum > 0:
        chunks.append(checksum & 0b1111) 
        checksum >>= 4
    return chunks

def sign_full_message(full_msg):
    keypairs = [fourbit.keypair() for _ in range(len(full_msg))]
    signatures = [fourbit.sign(full_msg[i], keypairs[i][0]) for i in range(len(full_msg))]
    return keypairs, signatures

def verify_full_message(signatures, keypairs):
    return [fourbit.verify(signatures[i], keypairs[i][1]) for i in range(len(signatures))]

def decode_message(bits):
    return ''.join([rev_dict[b] for b in bits])

def verify_checksum(message_bits, checksum_bits):
    recalculated = compute_checksum(message_bits, BASE)
    return recalculated == checksum_bits

# text = "hello world"
# message = encode_message(text)
# checksum = compute_checksum(message, BASE)
# full_message = message + checksum

# keypairs, signatures = sign_full_message(full_message)
# verified_bits = verify_full_message(signatures, keypairs)

# original_len = len(message)
# verified_message = verified_bits[:original_len]
# verified_checksum = verified_bits[original_len:]

# decoded = decode_message(verified_message)
# checksum_valid = verify_checksum(verified_message, verified_checksum)

# print(f"Original Text:      {text}")
# print(f"Encoded Message:    {message}")
# print(f"Checksum (chunks):  {checksum}")
# print(f"Verified Bits:      {verified_bits}")
# print(f"Decoded Message:    {decoded}")
# print(f"Checksum Valid:     {checksum_valid}")

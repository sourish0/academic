import fourbit

# h->0
# e->1
# l->2
# o->3
# w->4
# r->5
# d->6
# " " -> 7
dictionary ={
    'h': 0,
    'e': 1,
    'l': 2,
    'o': 3,
    'w': 4,
    'r': 5,
    'd': 6,
    ' ': 7
}
message = [0, 1, 2, 2, 3, 7, 4, 3, 5, 2, 6]  # hello world

keypair = [fourbit.keypair() for _ in range(len(message))]
signature=[None for _ in range(len(message))]
for i in range(len(message)):
    print(f"Private Key {i}: {keypair[i][0].hex()}")
    print(f"Public Key {i}:  {keypair[i][1].hex()}")
for i in range(len(message)):
    signature[i] = fourbit.sign(message[i], keypair[i][0])

print(f"Signature: {signature}")
verified_bit = [fourbit.verify(signature[i], keypair[i][1]) for i in range(len(message))]
print(f"Verified: {verified_bit}")

rev_dict = {v: k for k, v in dictionary.items()}
decoded_message = ''.join([rev_dict[b] for b in verified_bit])
print(f"Decoded message: {decoded_message}")

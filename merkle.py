import winternitz
import hashlib
def sha256(x):
    return hashlib.sha256(x).digest()


def build_merkle_tree(leaves):
    tree = [leaves]
    while len(tree[-1]) > 1:
        current_level = tree[-1]
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else current_level[i]
            next_level.append(sha256(left + right))
        tree.append(next_level)
    return tree

def merkle_root(tree):
    return tree[-1][0]

def auth_path(tree, index):
    path = []
    for level in tree[:-1]:
        sibling_index = index ^ 1
        if sibling_index < len(level):
            path.append(level[sibling_index])
        else:
            path.append(level[index])
        index //= 2
    return path

def verify_merkle_path(leaf, path, index, root):
    current = leaf
    for sibling in path:
        print(sibling.hex())
        if index % 2 == 0:
            current = sha256(current + sibling)
        else:
            current = sha256(sibling + current)
        index //= 2
    return current == root



num_keys = 4
messages = [3, 7, 2, 5]


keypairs = [winternitz.keypair() for _ in range(num_keys)]
public_keys = [kp[1] for kp in keypairs]

tree = build_merkle_tree(public_keys)
root = merkle_root(tree)
print("Merkle Root:", root.hex())

index = 2
message = messages[index]
sig = winternitz.sign(message, keypairs[index][0])
pubkey = public_keys[index]
path = auth_path(tree, index)

print("Verifying...")
valid_wots = winternitz.verify(sig, pubkey, message)
valid_merkle = verify_merkle_path(pubkey, path, index, root)
print("WOTS Valid?", valid_wots)
print("Merkle Path Valid?", valid_merkle)

if valid_wots and valid_merkle:
    print("✅ Full Signature is Valid!")
else:
    print("❌ Invalid Signature.")
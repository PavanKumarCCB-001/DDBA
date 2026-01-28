from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Step 1: Take message from user
msg = input("Enter your message: ").encode()

# Step 2: Generate Private Key
private_key = ec.generate_private_key(ec.SECP256R1())

# Step 3: Generate Public Key
public_key = private_key.public_key()

# Step 4: Hash the message using SHA256
hash_obj = hashes.Hash(hashes.SHA256())
hash_obj.update(msg)
hash_value = hash_obj.finalize()

print("\nSHA-256 Hash:", hash_value.hex())

# Step 5: Create Digital Signature
signature = private_key.sign(msg, ec.ECDSA(hashes.SHA256()))
print("\nDigital Signature:", signature.hex())

# Step 6: Verify Signature
try:
    public_key.verify(signature, msg, ec.ECDSA(hashes.SHA256()))
    print("\nSignature Verified ✔ Message is Authentic")
except InvalidSignature:
    print("\nSignature Verification Failed ❌") 
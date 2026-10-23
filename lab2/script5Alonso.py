from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(key)
nonce = os.urandom(12)
msg = b"Transfer 100 euros"
aad = b"cabecera"
ct = aesgcm.encrypt(nonce, msg, aad)
pt = aesgcm.decrypt(nonce, ct, aad)

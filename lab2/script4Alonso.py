from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

msg = b"Transfer 100 euros"
ct1 = f.encrypt(msg)
ct2 = f.encrypt(msg)
print(" ".join(ct1.hex()[i:i + 32] for i in range(0, len(ct1.hex()), 32)))
print(" ".join(ct2.hex()[i:i + 32] for i in range(0, len(ct2.hex()), 32)))
pt = f.decrypt(ct1, ttl=60)
print("-----------------Desencriptado------------------------")
print(pt.hex())
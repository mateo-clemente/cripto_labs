from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = b'1234567890123456'
iv = b'0000000000000000'
def encrypt(msg):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padded = msg + b' ' * (16 - len(msg) % 16)
    
    return encryptor.update(padded) + encryptor.finalize()

def decrypt(ct):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    
    return decryptor.update(ct) + decryptor.finalize()


msg1 = b"Transfer 100 euros from Ana to Juan"
msg2 = b"Transfer 100 euros from Ana to Luis"
msg3 = b"Transfer 100 euros from Ana to Juis"

c1 = encrypt(msg1)
c2 = encrypt(msg2)
c3 = encrypt(msg3)

print(c1.hex()[:32]," ",c1.hex()[32:64]," ",c1.hex()[64:])
print(c2.hex()[:32]," ",c2.hex()[32:64]," ",c2.hex()[64:])
print(c3.hex()[:32]," ",c3.hex()[32:64]," ",c3.hex()[64:])
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = b'1234567890123456'
iv = b'0000000000000000'
def encryptconpadding(msg):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()

    #esto de abajo es lo mismo, es para hacer el padded
    padded = msg + b' ' * (16 - len(msg) % 16)
    #if len(msg) % 16 != 0: 
        #raise ValueError("El mensaje debe ocupar bloques completos")

    return encryptor.update(padded) + encryptor.finalize()

def encryptsinpadding(msg):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()

    #esto de abajo es lo mismo, es para hacer el padded
    #padded = msg + b' ' * (16 - len(msg) % 16)
    if len(msg) % 16 != 0: 
        raise ValueError("El mensaje debe ocupar bloques completos")

    return encryptor.update(msg) + encryptor.finalize()

def encryptCBC(msg):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    
    padded = msg + b' ' * (16 - len(msg) % 16)
    
    return encryptor.update(padded) + encryptor.finalize()

msg1 = b"Transfer 100 euros from Ana to Juan"
msg2 = b"Transfer 100 euros from Ana to Luis"
msg3 = b"Transfer 100 euros from Ana to Juis"
msg4 = b"Transfer 100 euros from Ana to J. Thank you!"
msg5 = b"Transfer 100 euros from Ana to L. Thank you!"

c1 = encryptconpadding(msg1)
c2 = encryptconpadding(msg2)
c3 = encryptconpadding(msg3)
c4 = encryptCBC(msg4)
c5 = encryptCBC(msg5)

print(c1.hex()[:32]," ",c1.hex()[32:64]," ",c1.hex()[64:])
print(c2.hex()[:32]," ",c2.hex()[32:64]," ",c2.hex()[64:])
print(c3.hex()[:32]," ",c3.hex()[32:64]," ",c3.hex()[64:])
print(c4.hex()[:32]," ",c4.hex()[32:64]," ",c4.hex()[64:])
print(c5.hex()[:32]," ",c5.hex()[32:64]," ",c5.hex()[64:])
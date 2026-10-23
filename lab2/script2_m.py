from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
 
iv = b'0000000000000000' 
key = b'1234567890123456' 
def encryptECB_sinpadding(msg): 
    cipher = Cipher(algorithms.AES(key), modes.ECB()) 
    encryptor = cipher.encryptor() 
    if len(msg) % 16 != 0: 
            raise ValueError("El mensaje debe ocupar bloques completos") 
    return encryptor.update(msg) + encryptor.finalize()

def encryptECB_conpadding(msg):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    padded = msg + b' ' * (16 - len(msg) % 16)
    return encryptor.update(padded) + encryptor.finalize()

def encryptCBC(msg): 
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) 
	encryptor = cipher.encryptor() 
	padded = msg + b' ' * (16 - len(msg) % 16) 
	
	return encryptor.update(padded) + encryptor.finalize() 

def decrypt(ct): 
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) 
	decryptor = cipher.decryptor() 
	
	return decryptor.update(ct) + decryptor.finalize() 


msg1 = b"Transfer 100 euros from Ana to J. Thank you!"
msg2 = b"Transfer 100 euros from Ana to L. Thank you!" 
c1_ecb = encryptECB_conpadding(msg1) 
c1_cbc = encryptCBC(msg1)
c2 = encryptECB_conpadding(msg2)
c2_cbc = encryptCBC(msg2) 
print("\n MENSAJE CIFRADO con ECB C1") 
print(c1_ecb.hex()[:32], "", c1_ecb.hex()[32:64], "", c1_ecb.hex()[64:])

print("\n MENSAJE CIFRADO con ECB C2") 
print(c2.hex()[:32], "", c2.hex()[32:64], "", c2.hex()[64:])

print("--------------------------------")

print("\n MENSAJE CIFRADO con CBC C1")
print(c1_cbc.hex()[:32], "", c1_cbc.hex()[32:64], "", c1_cbc.hex()[64:])

print("\n MENSAJE CIFRADO con CBC C2")
print(c2_cbc.hex()[:32], "", c2_cbc.hex()[32:64], "", c2_cbc.hex()[64:])



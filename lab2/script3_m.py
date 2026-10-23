from cryptography.fernet import Fernet 

key = Fernet.generate_key() 
f = Fernet(key) 
msg = b"Transfer 100 euros" 
ct1 = f.encrypt(msg) 
ct2 = f.encrypt(msg) 
print(ct1.hex()) 
print(ct2.hex()) 
pt = f.decrypt(ct1) 
print(pt)


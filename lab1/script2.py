from cryptography.hazmat.primitives import hashes 
def hash_password(pw): 
    digest = hashes.Hash(hashes.SHA256()) 
    digest.update(pw.encode()) 
    return digest.finalize() 
pw1 = "password123" 
pw2 = "password123" 
print(hash_password(pw1)) 
print(hash_password(pw2))
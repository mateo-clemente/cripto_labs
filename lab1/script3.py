from cryptography.hazmat.primitives import hashes 
def hash_password(pw): 
    digest = hashes.Hash(hashes.SHA256()) 
    digest.update(pw.encode()) 
    return digest.finalize() 

found = False
fd = open("diccionario.txt", "r")
common = [l.strip() for l in fd.readlines()]
fd.close()
target = hash_password("chamba") 
for pw in common: 
    if hash_password(pw) == target: 
        found = True

if found: 
    print("Password encontrada")
else:
    print("Password no encontrada")


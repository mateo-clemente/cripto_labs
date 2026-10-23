from cryptography.hazmat.primitives import hashes 
def hash_password(pw): 
    digest = hashes.Hash(hashes.SHA256()) 
    digest.update(pw.encode()) 
    return digest.finalize() 

def check_passwords(common, target):
    for pw in common: 
        for i in range(0, 365):
            passw = pw + str(i)
            if hash_password(passw) == target: 
                found = True
                print("Password encontrada: " + passw)
                return True
    return False

fd = open("diccionario.txt", "r")
common = [l.strip() for l in fd.readlines()]
fd.close()
target = hash_password("chamba1") 


found = check_passwords(common, target)
if not found:
    print("Password no encontrada")


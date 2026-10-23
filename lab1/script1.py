from cryptography.hazmat.primitives import hashes

def sha256_hash(password):
	digest = hashes.Hash(hashes.SHA256())
	digest.update(password.encode())
	return digest.finalize().hex()
	
	
def almacenar_password(password):
	return sha256_hash(password)
	
def verificar_password(password, hash_almacenado):
	return sha256_hash(password) == hash_almacenado
	
hash_usuario = almacenar_password("123456")

if verificar_password("123456", hash_usuario):
	print("Acceso concedido")
else:
	print("Acceso denegado")
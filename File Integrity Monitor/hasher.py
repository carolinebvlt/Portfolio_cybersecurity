import hashlib

def hasher(file_to_hash) :
    
    with open(file_to_hash, "rb") as file :
        content = file.read()
        file_hash = hashlib.sha256(content).hexdigest()
    return file_hash 
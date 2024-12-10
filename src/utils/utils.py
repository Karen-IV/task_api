import bcrypt

def hash_password(hashed_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(hashed_password.encode('utf-8'), salt)
    print (hashed)
    return hashed.decode('utf-8')

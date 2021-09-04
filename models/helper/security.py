import bcrypt


def generate_password_hash(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())


def check_password_hash(hashed_password, password):
    if bcrypt.checkpw(password, hashed_password):
        return True
    else:
        return False

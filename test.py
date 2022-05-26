import bcrypt

password = bcrypt.hashpw('password'.encode("utf-8"), bcrypt.gensalt())
print(bcrypt.checkpw("password".encode("utf-8"), password))
print(password.decode("UTF-8"))
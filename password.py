import random
import string

def generate_password(length: int = 12) -> str:
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

print(" GENERATED PASSWORD IS : ",generate_password(int(input("ENTER THE SIZE OF PASSWORD : "))))
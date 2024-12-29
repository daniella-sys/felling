import random
import string
def generate_password(lengh=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)
                       for _ in range(lengh))
    return password
print(generate_password(12))
import random
import string

KEY_LENGTH = 16
KEY_FILE = "key.txt"

def generate_key(length):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

new_key = generate_key(KEY_LENGTH)

with open(KEY_FILE, "w") as f:
    f.write(new_key)

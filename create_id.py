import random
import string

# UUIDs are long and complicated, so creating my own six character random
# IDs for this assignment instead
def create_id():
    uid = []
    for n in range(0,6):
        if random.randint(0,1):
            uid.append(random.choice(string.digits))
        else:
            uid.append(random.choice(string.ascii_lowercase))

    return ''.join(uid)



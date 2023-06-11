import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def coin():
    coi = random.randint(0, 1)
    if coi == 0:
        return "1 first"
    else:
        return "2 second" 
def randemoj():
    emoj = ["☺", "☻", "♥", "♦", "♣"]
    return random.choice(emoj)
def gamerps():
    a = random.randint(1,3)
    b = random.randint(1,3)
    if b == a and b == 2 or b == a and b == 1 or b == a and b == 3:
        return "ничья"
    elif b == 1 and a == 2 or b == 2 and a == 3 or b == 3 and a == 1:
        return "Бот победил"
    else:
        return "Второй бот победил"
        
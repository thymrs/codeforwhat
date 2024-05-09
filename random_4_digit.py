import random

def verify_digits(x):
    x_str = str(x)
    
    seen = set()
    
    for digit in x_str:
        if digit in seen:
            return False
        seen.add(digit)
    return True

def randanswer():
    ran_four = random.randint(1000,9999)
    if verify_digits(ran_four):
        return ran_four
        
randanswer()
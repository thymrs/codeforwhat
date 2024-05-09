def verify_digits(x):
    x_str = str(x)
    
    seen = set()
    
    for digit in x_str:
        if digit in seen:
            return False
        seen.add(digit)
    return True

print(verify_digits(12324))
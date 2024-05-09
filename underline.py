def func(x):
   y = x**2*(2-2**(-x/100))
   return y

def under(x, y):
    if func(x) > y:
        return True
    return False

x = float(input("Enter X: "))
y = float(input("Enter Y: "))

if under(x,y):
    print("It is.")
else:
    print("It is not.")
def plus(inp1, inp2):
    print(f"result is {inp1+inp2}")

def mult(inp1, inp2):
    print(f"result is {inp1*inp2}")

user_input = (input("1 or 2: "))
inp1 = int(input("Enter number 1: "))
inp2 = int(input("Enter number 2: "))

if user_input == "1":
    plus(inp1, inp2)
elif user_input == "2":
    mult(inp1, inp2)
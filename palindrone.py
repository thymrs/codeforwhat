user_input = input()

# palin = user_input[::-1]
# if palin == user_input:
#     print("YES")
# else:
#     print("NO")

string = ""

for i in range(len(user_input) -1, -1, -1):\
    string += user_input[i]
    
print(string)
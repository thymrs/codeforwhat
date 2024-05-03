# num = int(input())

# if num == 2:
#     print("this is a prime number")
# elif num == 3:
#     print("this is a prime number")
# elif num == 9:
#     print("this is a prime number")
# elif num % 2 == 0:
#     print("this is not a prime number")
# elif num % 3 == 0:
#     print("this is not a prime number")
# else:
#     print("this is a prime number")

# num = int(input("กรุณาใส่เลข: "))
# is_prime = True

# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{num} เป็นเลขจำนวนเฉพาะ")
# else:
#     print(f"{num} ไม่เป็นเลขจำนวนเฉพาะ")

num = int(input("ใส่เลขมา: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("เลขนี้เท่ากับ", num, "คือเลขจำนวนเฉพาะ!")
else:
    print("เลขนี้เท่ากับ", num, "ไม่ใช่เลขจำนวนเฉพาะ!")
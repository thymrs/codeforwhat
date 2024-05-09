H = int(input('H: '))
U = int(input('U: '))
D = int(input('D: '))

days = 1
a = 0

while True:
    a = a + U
    if a >= H:
        print(f"{days} day(s)")
        break
    a = a - D
    days += 1
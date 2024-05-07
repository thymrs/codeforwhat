import math

x = int(input())
y = int(input())

area = math.ceil((x * y) / 1600)

print(area)
if area < 10:
    print(area*1000)
elif area > 10:
    print('10000')
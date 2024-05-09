count = [0] * 10


while True:
    num = int(input("ป้อนเลข 0-9: "))
    
    if 0 <= num <= 9:
        count[num] += 1
    else:
        break

for i in range(10):
    print(f"{i}= {count[i]}")
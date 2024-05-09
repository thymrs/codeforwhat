data = []
while True:
    num = int(input("ป้อนจำนวนเต็มระหว่าง 0 ถึง 99 (ป้อนค่าลบเพื่อสิ้นสุด): "))
    if num < 0:
        break
    data.append(num)

groups = [[] for _ in range(10)]
for num in data:
    group_index = num // 10
    groups[group_index].append(num)

print("ฮิสโตแกรม:")
print(groups)
for group in groups:
    frequency = len(group)
    print(": "+"*" * frequency)
import random

# สร้างลิสต์ของชื่อลิฟท์
lift_names = ["1", "2", "3", "4", "5"]

# สุ่มเลขชั้นที่ลิฟท์ตัวแต่ละตัว
lifts = [random.randint(1, 25) for _ in range(5)]

# รับค่าชั้นที่ผู้ใช้กด
user_floor = int(input("ระบุชั้นที่กดลิฟท์ (1-25): "))

# หาลิฟท์ที่ใกล้ที่สุด
closest_lift = None
min_difference = float('inf')

for lift_name, lift_floor in zip(lift_names, lifts):
    difference = abs(user_floor - lift_floor)
    if difference < min_difference:
        min_difference = difference
        closest_lift = lift_name
    elif difference == min_difference:
        closest_lift = min(closest_lift, lift_name)

# แสดงผลลัพธ์
print("ลิฟท์ที่จะมารับ:", closest_lift)
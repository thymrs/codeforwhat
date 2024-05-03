students = []

# วนลูปเพื่อรับชื่อและคะแนนของนักเรียน
while True:
    name = input("ป้อนชื่อนักเรียน (หรือป้อนว่างเพื่อหยุด): ")
    if not name:
        break
    score = float(input(f"ป้อนคะแนนของ {name}: "))
    students.append({"name": name, "score": score})

# แสดงผลรายงานการเรียน
print("รายงานการเรียน")
for student in students:
    if student["score"] >= 80:
        grade = "A"
    elif student["score"] >= 70:
        grade = "B"
    elif student["score"] >= 60:
        grade = "C"
    elif student["score"] >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"{student['name']} ได้เกรด {grade}")
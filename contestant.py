people = []

# while True:
#     name = input("ป้อนชื่อนักเรียน (หรือป้อนว่างเพื่อหยุด): ")
#     if not name:
#         break
#     score = float(input(f"ป้อนคะแนนของ {name}: "))
#     people.append({"name": name, "score": score})

num_of_cons = int(input("Enter a total of consistant: "))
print("Enter a name and score:")
for i in range(num_of_cons):
    name_point = input()
    name, score = name_point.split(",")
    people.append({"name": name.strip(), "score": int(score.strip())})
    sorted_people = sorted(people, key=lambda ele: ele["score"], reverse=True)

print("Result:")
for i, people in enumerate(sorted_people):
    print(f"{i+1}. {people['name']}: {people['score']}")

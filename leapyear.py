while True:
    year = int(input("ป้อนปี (ป้อน 0 เพื่อหยุด): "))
    if year == 0 or year < 0:
        break
    elif year % 400 == 0:
        print("leap year")
    elif year % 100 == 0:
        print("not leap year")
    elif year % 4 == 0:
        print("leap year")
    else:
        print("not leap year")
christian_year = int(input("ปี ค.ศ.: "))


buddhist_year = christian_year + 543
print("ปี พ.ศ.:", buddhist_year)


christian_sum = sum(int(digit) for digit in str(christian_year))
print("ผลรวมของตัวเลขแต่ละหลักของปี ค.ศ.:", christian_sum)


buddhist_sum = sum(int(digit) for digit in str(buddhist_year))
print("ผลรวมของตัวเลขแต่ละหลักของปี พ.ศ.:", buddhist_sum)
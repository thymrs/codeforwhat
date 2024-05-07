student = 0

def calc_bmi(weight, heights):
    bmi = weight / (heights ** 2)
    return bmi

while True:
    weight = int(input())
    height = float(input())
    heights = height / 100
    if weight <= 0 or height <= 0:
        break
    result_bmi = calc_bmi(weight, heights)
    if result_bmi < 18.5:
        student += 1
    else:
        student += 0
        
print(student)
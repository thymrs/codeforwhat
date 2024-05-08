fares = {1: 27, 2: 35, 3: 42}

coins = [10, 5, 2, 1]

destination = int(input("กรุณาเลือกสถานีปลายทาง (1, 2, 3): "))
amount = int(input("กรุณาใส่จำนวนเงินที่ให้เข้าระบบ: "))

while amount == fares[destination]:
    print("ห้ามใช้เงินที่เท่ากับราคาโดยสาร กรุณาใส่จำนวนเงินใหม่")
    amount = int(input("กรุณาใส่จำนวนเงินที่ให้เข้าระบบ: "))

change = amount - fares[destination]

while change < 0:
    print("จำนวนเงินไม่เพียงพอ กรุณาใส่จำนวนเงินใหม่")
    amount = int(input("กรุณาใส่จำนวนเงินที่ให้เข้าระบบ: "))
    while amount == fares[destination]:
        print("ห้ามใช้เงินที่เท่ากับราคาโดยสาร กรุณาใส่จำนวนเงินใหม่")
        amount = int(input("กรุณาใส่จำนวนเงินที่ให้เข้าระบบ: "))
    change = amount - fares[destination]

change_coins = {coin: 0 for coin in coins}

for coin in coins:
    while change >= coin:
        change_coins[coin] += 1
        change -= coin

print("จำนวนเหรียญที่ต้องทอน:")
for coin, count in change_coins.items():
    print(f"{coin} บาท: {count} เหรียญ")
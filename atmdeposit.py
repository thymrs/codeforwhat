notes = [1000, 500, 100]
change_coins = {note: 0 for note in notes}

for i in range(0,2):
    usr = int(input())
    deposit = usr
    if usr > 20000 or usr < 100:
        print('Input Error')
    else:

        for note in notes:
            while deposit >= note:
                change_coins[note] += 1
                deposit -= note
                
print("จำนวนธนบัตรที่ได้รับ:")
for note, count in change_coins.items():
    print(f"{note} บาท: {count} ใบ")
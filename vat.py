vat = 0

for i in range(4):
    usr = int(input())
    if usr < 100000:
        vat += 0
    elif 100000 <= usr <= 500000:
        vat += usr * 0.05
    elif 500001 <= usr <= 1000000:
        vat += usr * 0.1
    else:
        vat += usr * 0.2
        
vat = "%2.2f" % vat
print(vat)
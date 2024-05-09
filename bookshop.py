books = int(input('How many books: '))
price = int(input('How much: '))

if books > 3 and price > 500:
    print(f"You have to pay {price - (price * 0.1)} bath.")
else:
    print(f"You have to pay {price} bath.")
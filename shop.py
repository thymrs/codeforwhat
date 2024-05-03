print("โปรดเลือกทำรายการ:\n1. เพิ่มสินค้าใหม่\n2. แสดงรายการสินค้าทั้งหมด\n3. ค้นหาสินค้า\n4. ออกจากระบบ")

stocks = []

while True:
    user_input = input("โปรดเลือกหมายเลข: ")
    if user_input == "1":
        print("โปรดป้อนข้อมูลสำหรับสินค้าใหม่:")
        name = input("ชื่อสินค้า: ")
        price = input("ราคา: ")
        amount = input("จำนวน: ")
        stocks.append({"name": name, "price": price, "amount": amount})
        print(f"สินค้า {name} ถูกเพิ่มเข้าเรียบร้อยแล้ว")
    elif user_input == "2":
        print("รายการสินค้าทั้งหมด:")
        for stock in stocks:
            print(f"ชื่อ: {stock['name']} | ราคา: {stock['price']} | จำนวน: {stock['amount']}")
    elif user_input == "3":
        search_product = input("โปรดป้อนชื่อสินค้าที่ต้องการ: ")
        if search_product == stock["name"]:
            print(f"พบสินค้า {search_product} ในระบบ:")
        for stock in stocks:
            if search_product == stock["name"]:
                print(f"ชื่อ: {stock['name']} | ราคา: {stock['price']} | จำนวน: {stock['amount']}")
        else:
            print("ไม่พบสินค้าในระบบ")
    elif user_input == "4":
        print("ขอบคุณที่ใช้บริการ และบายบาย!")
        
            
        

        
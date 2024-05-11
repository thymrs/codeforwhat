# 🚀 Hero Sum Game

# หากคุณเปิดดูยูทูปบ่อยๆ คุณคงเคยเห็นโฆษณาเกมมือถือ (ปลอมๆ) ที่จะมีมอนสเตอร์พร้อมตัวเลขคะแนน ยืนกันเรียงราย แล้วผู้เล่นจะต้องสั่งให้ฮีโร่ โจมตีมอนสเตอร์ที่มีพลัง "น้อยกว่า" ตัวเอง เพื่อดูดพลังของมอนสเตอร์มารวมกับพลังของฮีโร่ แต่จะไม่สามารถเลือกโจมตีมอนสเตอร์ที่มีพลังมากกว่าหรือเท่ากับเราได้

# ตัวอย่างเช่น ถ้าฮีโร่มีพลังอยู่ 5 หน่วย จะยังไม่สามารถโจมตีมอนสเตอร์ที่มีพลัง 5 หน่วยขึ้นไปได้ แต่จะสามารถโจมตีมอนสเตอร์ที่มีพลังน้อยกว่า 5 หน่วยได้ เช่น ถ้าโจมตีมอนสเตอร์ที่มีพลัง 3 หน่วย จะทำให้พลังของเราเปลี่ยนเป็น 5 + 3 = 8 หน่วย เป็นต้น

# ให้หาว่า ในเกมที่กำหนดให้ ฮีโร่จะสามารถจัดการบอส (มอนสเตอร์ที่มีพลังสูงสุด) ได้หรือไม่ ถ้าทำได้ จะต้องทำการโจมตี "อย่างน้อยที่สุด" กี่ครั้ง

# 📥 รูปแบบข้อมูล Input

# ข้อมูล Input จะระบุมาผ่านตัวแปรตั้งต้นใน Init Code โดยตัวแปรต่างๆ มีคุณสมบัติต่อไปนี้:

# * ตัวแปร hero เป็นพลังเริ่มต้นของฮีโร่ เป็นจำนวนเต็ม มีค่าระหว่าง 0 - 1,000,000

# * ตัวแปร mons ระบุพลังของมอนสเตอร์แต่ละตัว เป็นลิสต์ของจำนวนเต็ม ซึ่งมีสมาชิกไม่เกิน 50 ตัว แต่ละตัวมีค่าระหว่าง 0 - 1,000,000

# hero = 100
# mons = [90, 180, 360, 720, 1440]

# boss = max(mons)

# mons.sort()

# attack_count = 0

# can_attack_boss = False

# for mon in mons:
#     if mon < hero:
#         hero += mon
#         attack_count += 1
#         mons.pop(mons)
#     if hero >= boss:
#         can_attack_boss = True
#         attack_count += 1
#         break

# if can_attack_boss:
#     print(attack_count)
# else:
#     print("no")

# boss = max(mons)
# i = count = 0
# mons.sort(reverse=True)

# while hero <= boss:
#     if hero > mons[i]:
#         hero += mons[i]
#         count += 1
#         mons.pop(i)
#         i = 0
#         continue
#     i += 1
#     if i == len(mons):
#         print('no')
#         break

# if hero > boss:
#     print(count+1)

hero = 6
mons = [1, 1, 1, 1, 5, 10]

def test_attack(mons, hero):
    count = 0
    boss = max(mons)
    mons.sort(reverse=True)
    i = 0

    while(i < len(mons)):
        if hero > boss:
            print(count + 1)
            return
        if hero > mons[i]:  
            hero += mons[i]
            count += 1
            mons.pop(i)
            i = 0
        else:
            i += 1
        
    print("no") 
    
test_attack(mons, hero)
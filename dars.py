print("Hello, World!")
ism=input("Ismingizni kiriting: ")
yosh=int(input("Yoshingizni kiriting: "))   
if yosh<18:
    print(f"Salom {ism}, siz hali yosh ekansiz!")
elif yosh==18:
    print(f"Salom {ism}, siz endi kattalar qatoriga qo'shildingiz!")
else:
    print(f"Salom {ism}, siz kattasiz!")
    print("Kattalar uchun maxsus takliflarimiz bor!")
    ism=input("Ismingizni kiriting: ")
yosh=int(input("Yoshingizni kiriting: "))

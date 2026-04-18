
Python mosligi
Bu matchbayonot turli shartlarga asoslangan holda turli xil amallarni bajarish uchun ishlatiladi.

Python moslik bayonoti
Ko'p bayonotlar yozish o'rniga if..else, siz bayonotdan foydalanishingiz mumkin match.

Bayonot matchbajarilishi kerak bo'lgan ko'plab kod bloklaridan birini tanlaydi.

SintaksisO'zingizning Python serveringizni oling
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
Bu quyidagicha ishlaydi:

Ifoda matchbir marta baholanadi.
Ifodaning qiymati har birining qiymatlari bilan taqqoslanadi case.
Agar moslik bo'lsa, tegishli kod bloki bajariladi.
Quyidagi misolda hafta kuni nomini chop etish uchun hafta kuni raqamidan foydalaniladi:

Misol
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

REKLAMALARNI OLIB TASHLASH

Standart qiymat
Agar boshqa mosliklar bo'lmaganda kod bloki bajarilishini xohlasangiz, pastki chiziqli belgi _ ni oxirgi holat qiymati sifatida ishlating:

Misol
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
_ qiymati har doim mos keladi, shuning uchun uni standart holat sifatida ishlashi uchun uni oxirgi holat sifatida joylashtirish muhimdir .

Qiymatlarni birlashtirish
Bitta holatda bir nechta qiymat mos kelishini tekshirish uchun holatni baholashda yoki operatori sifatida | quvur belgisidan foydalaning :

Misol
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
Agar soqchilar sifatida bayonotlar bo'lsa
ifSiz qo'shimcha shart-tekshirish sifatida ishni baholashda bayonotlarni qo'shishingiz mumkin :

Misol
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
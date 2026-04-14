"Python Yo'q
NonePythonda qiymatning yo'qligini ifodalovchi maxsus konstantadir.

Uning ma'lumotlar turi NoneType, va Noneobyektning yagona namunasidir NoneType.

Hech qanday tur
NoneO'zgaruvchilar "qiymat yo'q" yoki "o'rnatilmagan" ni ko'rsatish uchun tayinlanishi mumkin .

MisolO'zingizning Python serveringizni oling
Qiymatni tayinlang va ko'rsating None:
"
x = None
print(x)
type()Qiymat turini ko'rish uchun foydalaning None.

Misol
Qiymatning ma'lumot turini tayinlang va chop eting None:

x = None
print(type(x))
"Hech biri bilan taqqoslash
Qiymatni bilan taqqoslash uchun Noneidentifikatsiya operatoridan foydalaning isyokiis not

Misol
isQuyidagi bilan taqqoslash uchun identifikatsiya operatoridan foydalaning None:
"
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")
"Misol
Shunga o'xshash misol, lekin buning is noto'rniga:

"result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")



"To'g'ri yoki noto'g'ri
NoneFalsemantiqiy kontekstda ni baholaydi .

Misol
Haqiqatni tekshiring:

"print(bool(None))
Hech qaysi funksiya qaytarilmaydi
Aniq qiymat qaytarmaydigan funksiyalar Nonesukut bo'yicha qaytaradi.

Misol
Qaytish operatori bo'lmagan funksiya quyidagini qaytaradi None:

def myfunc():
  x = 5

x = myfunc()
print(x)

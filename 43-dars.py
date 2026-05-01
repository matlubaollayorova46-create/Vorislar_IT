Bul qiymatlari ikkita qiymatdan birini ifodalaydi: Trueyoki False.

Boolean qiymatlari
Dasturlashda siz ko'pincha ifoda Trueyoki ekanligini bilishingiz kerak bo'ladi False.

Pythonda istalgan ifodani baholashingiz va ikkita javobdan birini olishingiz mumkin, Trueyoki False.

Ikki qiymatni taqqoslaganda, ifoda baholanadi va Python Boolean javobini qaytaradi:

MisolO'zingizning Python serveringizni oling
print(10 > 9)
print(10 == 9)
print(10 < 9)
Agar if operatorida shart bajarilsa, Python Trueyoki funksiyasini qaytaradi False:

Misol
Shart Trueyoki shartga qarab xabarni chop eting False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
Qiymatlar va o'zgaruvchilarni baholash
Funksiya bool()sizga har qanday qiymatni baholash va sizga Trueyoki False evaziga berish imkonini beradi,

Misol
Satr va raqamni baholang:

print(bool("Hello"))
print(bool(15))
Misol
Ikkita o'zgaruvchini baholang:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

REKLAMALARNI OLIB TASHLASH

Ko'pgina qiymatlar haqiqatdir
TrueDeyarli har qanday qiymat , agar u biron bir tarkibga ega bo'lsa, baholanadi .

Bo'sh satrlardan tashqari istalgan satr bo'ladi True.

Har qanday son True, dan tashqari, bo'ladi 0.

Bo'sh bo'lganlardan tashqari har qanday ro'yxat, tuple, to'plam va lug'at ga teng True.

Misol
Quyidagilar True qiymatini qaytaradi:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
Ba'zi qiymatlar noto'g'ri
Aslida, ga teng qiymatlar ko'p emas , faqat , , , , soni va qiymati Falsekabi bo'sh qiymatlardan tashqari . Va, albatta, qiymat ga teng qiymat oladi .()[]{}""0NoneFalseFalse

Misol
Quyidagilar False qiymatini qaytaradi:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
Bu holda yana bir qiymat yoki obyekt ga teng bo'ladi va bu sizda yoki ni qaytaradigan funksiyaga Falseega klassdan yaratilgan obyekt bo'lsa, shunday bo'ladi :__len__0False

Misol
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

REKLAMALARNI OLIB TASHLASH

Funksiyalar Boolean qiymatini qaytarishi mumkin
Siz Boolean qiymatini qaytaradigan funksiyalarni yaratishingiz mumkin:

Misol
Funksiyaning javobini chop eting:

def myFunction() :
  return True

print(myFunction())
Siz funktsiyaning Boolean javobiga asoslanib kodni bajarishingiz mumkin:

Misol
Agar funksiya True qaytarsa, "YES!" deb yozing, aks holda "NO!" deb yozing:

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
Python shuningdek, funksiya kabi mantiqiy qiymatni qaytaradigan ko'plab o'rnatilgan funktsiyalarga ega isinstance() , ular obyektning ma'lum bir ma'lumot turiga tegishli ekanligini aniqlash uchun ishlatilishi mumkin:

Misol
Ob'ekt butun son yoki yo'qligini tekshiring:

x = 200
print(isinstance(x, int))
Python iteratorlari
Iterator - bu sanab bo'ladigan miqdordagi qiymatlarni o'z ichiga olgan obyekt.

Iterator - bu iteratsiya qilinishi mumkin bo'lgan obyekt, ya'ni siz barcha qiymatlarni ko'rib chiqishingiz mumkin.

__iter__() Texnik jihatdan, Pythonda iterator - bu iterator protokolini amalga oshiradigan ob'ekt bo'lib, u va usullaridan iborat __next__().

Iterator va Iterable
Ro'yxatlar, katakchalar, lug'atlar va to'plamlar - bularning barchasi iteratsiya qilinadigan obyektlar. Ular iteratorni olishingiz mumkin bo'lgan iteratsiya qilinadigan konteynerlardir .

Bu obyektlarning barchasi iter()iteratorni olish uchun ishlatiladigan usulga ega:

MisolO'zingizning Python serveringizni oling
Tuple'dan iteratorni qaytaring va har bir qiymatni chop eting:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
Hatto satrlar ham iteratsiya qilinadigan obyektlar bo'lib, iteratorni qaytarishi mumkin:

Misol
Satrlar ham takrorlanadigan obyektlar bo'lib, ularda belgilar ketma-ketligi mavjud:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
Iterator orqali sikl o'tkazish
forShuningdek, takrorlanuvchi obyekt orqali takrorlanish uchun sikldan foydalanishimiz mumkin :

Misol
Bir juftlikning qiymatlarini takrorlang:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
Misol
Satr belgilarini takrorlang:

mystr = "banana"

for x in mystr:
  print(x)
Aslida, sikl foriterator obyektini yaratadi va next() har bir sikl uchun metodni bajaradi.


REKLAMALARNI OLIB TASHLASH

Iterator yarating
Iterator sifatida obyekt/klass yaratish uchun siz usullarni __iter__()va __next__()obyektingizga qo'llashingiz kerak.

Python Classes/Objects bobida bilib olganingizdek , barcha klasslarda deb nomlangan funksiya mavjud bo'lib __init__(), u sizga obyekt yaratilayotganda ba'zi initsializatsiyalarni amalga oshirish imkonini beradi.

Usul __iter__()shunga o'xshash ishlaydi, siz operatsiyalarni bajarishingiz mumkin (boshlang'ichlashtirish va boshqalar), lekin har doim iterator obyektining o'zini qaytarishi kerak.

Usul __next__()shuningdek, operatsiyalarni bajarishga imkon beradi va ketma-ketlikdagi keyingi elementni qaytarishi kerak.

Misol
1 dan boshlanadigan raqamlarni qaytaradigan iterator yarating va har bir ketma-ketlik bittaga ko'payadi (1, 2, 3, 4, 5 va hokazolarni qaytaradi):

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

REKLAMALARNI OLIB TASHLASH

StopIteration
Yuqoridagi misol, agar sizda yetarli next() operatorlari bo'lsa yoki u siklda ishlatilgan bo'lsa, abadiy davom etadi for.

Iteratsiyaning abadiy davom etishiga yo'l qo'ymaslik uchun biz StopIterationoperatordan foydalanishimiz mumkin.

Usulda __next__(), agar iteratsiya belgilangan miqdordagi marta bajarilsa, xatolik yuzaga kelishi uchun tugatish shartini qo'shishimiz mumkin:

Misol
20 ta iteratsiyadan keyin to'xtating:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

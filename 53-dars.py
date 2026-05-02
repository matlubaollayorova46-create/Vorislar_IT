Generatorlar
Generatorlar - bu ularning bajarilishini to'xtatib turishi va davom ettirishi mumkin bo'lgan funksiyalar.

Generator funksiyasi chaqirilganda, u iterator bo'lgan generator obyektini qaytaradi.

Funksiya ichidagi kod hali bajarilmagan, u faqat kompilyatsiya qilingan. Funksiya faqat generator ustida iteratsiya qilinganda bajariladi.

MisolO'zingizning Python serveringizni oling
Oddiy generator funksiyasi:

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
Generatorlar sizga butun ma'lumotlar to'plamini xotirada saqlamasdan ma'lumotlar ustida iteratsiya qilish imkonini beradi.

returnGeneratorlar dan foydalanish o'rniga yieldkalit so'zdan foydalanadilar.

Hosildorlik kalit so'zi
Kalit yieldso'z funksiyani generatorga aylantiradigan narsadir.

ga yieldduch kelganda, funksiyaning holati saqlanadi va qiymat qaytariladi. Keyingi safar generator chaqirilganda, u to'xtagan joyidan davom etadi.

Misol
Raqamlarni chiqaradigan generator:

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)
dan farqli o'laroq return, funksiyani tugatadi, yielduni to'xtatib turadi va bir necha marta chaqirilishi mumkin.


REKLAMALARNI OLIB TASHLASH

Generatorlar xotirani tejaydi
Generatorlar xotiradan samarali foydalanadi, chunki ular hamma narsani xotirada saqlash o'rniga, qiymatlarni tezkor ravishda yaratadilar.

Katta ma'lumotlar to'plamlari uchun generatorlar xotirani tejaydi:

Misol
Katta ketma-ketliklar uchun generator:

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
next() ni generatorlar bilan ishlatish
Siz funktsiyadan foydalanib, generator orqali qo'lda iteratsiya qilishingiz mumkin next():

Misol
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
Beriladigan boshqa qiymatlar qolmaganda, generator StopIterationistisno keltirib chiqaradi:

Misol
def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) # This will raise StopIteration

REKLAMALARNI OLIB TASHLASH

Generator ifodalari
Ro'yxat tushunchalariga o'xshab, siz kvadrat qavslar o'rniga qavslar bilan generator ifodalari yordamida generatorlar yaratishingiz mumkin:

Misol
Ro'yxatni tushunish va generator ifodasi:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
Misol
Summa bilan generator ifodasini ishlatish:

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)
Fibonachchi ketma-ketlik generatori
Fibonachchi ketma-ketligini yaratish uchun generatorlardan foydalanish mumkin.

U xotira tugab qolmasdan, cheksiz qiymatlarni yaratishda davom etishi mumkin:

Misol
100 Fibonachchi sonini yarating:

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))
Jeneratör usullari
Jeneratörlar ilg'or boshqaruv uchun maxsus usullarga ega:

send() usuli
Usul send()sizga generatorga qiymat yuborish imkonini beradi:

Misol
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")
close() usuli
Usul close()generatorni to'xtatadi:

Misol
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

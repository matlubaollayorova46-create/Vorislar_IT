Xususiyatlar - bu sinfga tegishli bo'lgan o'zgaruvchilar. Ular sinfdan yaratilgan har bir obyekt uchun ma'lumotlarni saqlaydi.

MisolO'zingizning Python serveringizni oling
Xususiyatlarga ega sinf yarating:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
Kirish xususiyatlari
Nuqta belgisi yordamida obyekt xususiyatlariga kirishingiz mumkin:

Misol
Ob'ekt xususiyatlariga kirish:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

REKLAMALARNI OLIB TASHLASH

Xususiyatlarni o'zgartirish
Ob'ektlardagi xususiyatlar qiymatini o'zgartirishingiz mumkin:

Misol
Yosh xususiyatini o'zgartirish:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)
Xususiyatlarni o'chirish
Kalit so'z yordamida obyektlardan xususiyatlarni o'chirishingiz mumkin del:

Misol
Yosh xususiyatini o'chirish:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error

REKLAMALARNI OLIB TASHLASH

Sinf xususiyatlari va obyekt xususiyatlari
Ichkarida aniqlangan xususiyatlar __init__()har bir obyektga tegishli (nusxa xususiyatlari).

Metodlardan tashqarida aniqlangan xususiyatlar sinfning o'ziga tegishli (klass xususiyatlari) va barcha obyektlar tomonidan birgalikda qo'llaniladi:

Misol
Sinf xususiyati va instance xususiyati:

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
Sinf xususiyatlarini o'zgartirish
Sinf xususiyatini o'zgartirganingizda, u barcha obyektlarga ta'sir qiladi:

Misol
Sinf xususiyatini o'zgartirish:

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)
Yangi mulklar qo'shish
Mavjud obyektlarga yangi xususiyatlar qo'shishingiz mumkin:

Misol
Ob'ektga yangi xususiyat qo'shish:

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)
Eslatma: Xususiyatlarni shu tarzda qo'shish ularni faqat o'sha aniq obyektga qo'shadi, sinfning barcha obyektlariga emas.


Metodlar - bu sinfga tegishli funksiyalar. Ular sinfdan yaratilgan obyektlarning xatti-harakatlarini belgilaydi.

MisolO'zingizning Python serveringizni oling
Sinfda usul yarating:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()
Izoh:self Barcha usullar birinchi parametr sifatida bo'lishi kerak .

Parametrli usullar
Metodlar oddiy funksiyalar kabi parametrlarni qabul qilishi mumkin:

Misol
Parametrlarga ega usul yarating:

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

REKLAMALARNI OLIB TASHLASH

Xususiyatlarga kirish usullari
Metodlar quyidagilar yordamida obyekt xususiyatlariga kirishi va o'zgartirishi mumkin self:

Misol
Obyekt xususiyatlariga kirish usuli:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())
Xususiyatlarni o'zgartirish usullari
Metodlar obyektning xususiyatlarini o'zgartirishi mumkin:

Misol
Xususiyat qiymatini o'zgartiradigan usul:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
REKLAMALARNI OLIB TASHLASH

__str__() usuli
Usul __str__()- bu obyekt chop etilganda nima qaytarilishini boshqaradigan maxsus usul:

Misol
Usulsiz __str__():

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)
Misol
Usul bilan __str__():

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)
Bir nechta usullar
Sinf birgalikda ishlaydigan bir nechta usullarga ega bo'lishi mumkin:

Misol
Bitta sinfda bir nechta usullarni yarating:

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
O'chirish usullari
Kalit so'z yordamida metodlarni sinfdan o'chirishingiz mumkin del:

Misol
Sinfdan metodni o'chirish:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # This will cause an error
Izoh: O'chirilgan metodga murojaat qilish xatoga olib keladi, chunki u endi mavjud emas.                            
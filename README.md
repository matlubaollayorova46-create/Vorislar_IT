Python massivlari
Eslatma: Pythonda massivlar uchun o'rnatilgan qo'llab-quvvatlash mavjud emas, lekin buning o'rniga Python Lists dan foydalanish mumkin.

Massivlar
Eslatma: Ushbu sahifada LISTS dan ARRAYS sifatida qanday foydalanish ko'rsatilgan, ammo Pythonda massivlar bilan ishlash uchun siz NumPy kutubxonasi kabi kutubxonani import qilishingiz kerak bo'ladi .

Massivlar bitta o'zgaruvchida bir nechta qiymatlarni saqlash uchun ishlatiladi:

MisolO'zingizning Python serveringizni oling
Avtomobil nomlarini o'z ichiga olgan massiv yarating:

cars = ["Ford", "Volvo", "BMW"]
Massiv nima?
Massiv - bu bir vaqtning o'zida bir nechta qiymatni saqlashi mumkin bo'lgan maxsus o'zgaruvchi.

Agar sizda elementlar ro'yxati (masalan, avtomobil nomlari ro'yxati) bo'lsa, avtomobillarni bitta o'zgaruvchida saqlash quyidagicha ko'rinishi mumkin:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
Biroq, agar siz mashinalarni ko'rib chiqib, aniq bir mashinani topmoqchi bo'lsangiz-chi? Va agar sizda 3 ta emas, balki 300 ta mashina bo'lsa-chi?

Yechim massivdir!

Massiv bitta nom ostida ko'plab qiymatlarni saqlashi mumkin va siz ularga indeks raqamiga murojaat qilish orqali kirishingiz mumkin.

Massiv elementlariga kirish
Siz massiv elementiga indeks raqamiga murojaat qilish orqali murojaat qilasiz .

Misol
Birinchi massiv elementining qiymatini oling:

x = cars[0]
Misol
Birinchi massiv elementining qiymatini o'zgartiring:

cars[0] = "Toyota"
Massiv uzunligi
len()Massiv uzunligini (massivdagi elementlar soni) qaytarish uchun usuldan foydalaning .

Misol
Massivdagi elementlar sonini qaytaring cars :

x = len(cars)
Izoh: Massiv uzunligi har doim eng yuqori massiv indeksidan bittaga ko'p.

REKLAMALARNI OLIB TASHLASH

Massiv elementlarini sikllashtirish
Siz for insikldan foydalanib, massivning barcha elementlarini sikl bilan ko'rib chiqishingiz mumkin.

Misol
Massivdagi har bir elementni chop eting cars:

for x in cars:
  print(x)
Massiv elementlarini qo'shish
Siz append()usuldan foydalanib, massivga element qo'shishingiz mumkin.

Misol
Massivga yana bitta element qo'shing cars:

cars.append("Honda")
Massiv elementlarini olib tashlash
pop()Massivdan elementni olib tashlash uchun usuldan foydalanishingiz mumkin .

Misol
Massivning ikkinchi elementini o'chirish cars:

cars.pop(1)
remove()Shuningdek , usuldan massivdan elementni olib tashlash uchun ham foydalanishingiz mumkin .

Misol
"Volvo" qiymatiga ega elementni o'chiring:

cars.remove("Volvo")
Izoh: Ro'yxat remove()usuli faqat ko'rsatilgan qiymatning birinchi marta paydo bo'lishini olib tashlaydi.

Massiv usullari
Python ro'yxatlar/massivlarda foydalanishingiz mumkin bo'lgan bir qator o'rnatilgan usullarga ega.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the listPython massivlari
Eslatma: Pythonda massivlar uchun o'rnatilgan qo'llab-quvvatlash mavjud emas, lekin buning o'rniga Python Lists dan foydalanish mumkin.

Massivlar
Eslatma: Ushbu sahifada LISTS dan ARRAYS sifatida qanday foydalanish ko'rsatilgan, ammo Pythonda massivlar bilan ishlash uchun siz NumPy kutubxonasi kabi kutubxonani import qilishingiz kerak bo'ladi .

Massivlar bitta o'zgaruvchida bir nechta qiymatlarni saqlash uchun ishlatiladi:

MisolO'zingizning Python serveringizni oling
Avtomobil nomlarini o'z ichiga olgan massiv yarating:

cars = ["Ford", "Volvo", "BMW"]
Massiv nima?
Massiv - bu bir vaqtning o'zida bir nechta qiymatni saqlashi mumkin bo'lgan maxsus o'zgaruvchi.

Agar sizda elementlar ro'yxati (masalan, avtomobil nomlari ro'yxati) bo'lsa, avtomobillarni bitta o'zgaruvchida saqlash quyidagicha ko'rinishi mumkin:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
Biroq, agar siz mashinalarni ko'rib chiqib, aniq bir mashinani topmoqchi bo'lsangiz-chi? Va agar sizda 3 ta emas, balki 300 ta mashina bo'lsa-chi?

Yechim massivdir!

Massiv bitta nom ostida ko'plab qiymatlarni saqlashi mumkin va siz ularga indeks raqamiga murojaat qilish orqali kirishingiz mumkin.

Massiv elementlariga kirish
Siz massiv elementiga indeks raqamiga murojaat qilish orqali murojaat qilasiz .

Misol
Birinchi massiv elementining qiymatini oling:

x = cars[0]
Misol
Birinchi massiv elementining qiymatini o'zgartiring:

cars[0] = "Toyota"
Massiv uzunligi
len()Massiv uzunligini (massivdagi elementlar soni) qaytarish uchun usuldan foydalaning .

Misol
Massivdagi elementlar sonini qaytaring cars :

x = len(cars)
Izoh: Massiv uzunligi har doim eng yuqori massiv indeksidan bittaga ko'p.

REKLAMALARNI OLIB TASHLASH

Massiv elementlarini sikllashtirish
Siz for insikldan foydalanib, massivning barcha elementlarini sikl bilan ko'rib chiqishingiz mumkin.

Misol
Massivdagi har bir elementni chop eting cars:

for x in cars:
  print(x)
Massiv elementlarini qo'shish
Siz append()usuldan foydalanib, massivga element qo'shishingiz mumkin.

Misol
Massivga yana bitta element qo'shing cars:

cars.append("Honda")
Massiv elementlarini olib tashlash
pop()Massivdan elementni olib tashlash uchun usuldan foydalanishingiz mumkin .

Misol
Massivning ikkinchi elementini o'chirish cars:

cars.pop(1)
remove()Shuningdek , usuldan massivdan elementni olib tashlash uchun ham foydalanishingiz mumkin .

Misol
"Volvo" qiymatiga ega elementni o'chiring:

cars.remove("Volvo")
Izoh: Ro'yxat remove()usuli faqat ko'rsatilgan qiymatning birinchi marta paydo bo'lishini olib tashlaydi.

Massiv usullari
Python ro'yxatlar/massivlarda foydalanishingiz mumkin bo'lgan bir qator o'rnatilgan usullarga ega.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the listPython massivlari
Eslatma: Pythonda massivlar uchun o'rnatilgan qo'llab-quvvatlash mavjud emas, lekin buning o'rniga Python Lists dan foydalanish mumkin.

Massivlar
Eslatma: Ushbu sahifada LISTS dan ARRAYS sifatida qanday foydalanish ko'rsatilgan, ammo Pythonda massivlar bilan ishlash uchun siz NumPy kutubxonasi kabi kutubxonani import qilishingiz kerak bo'ladi .

Massivlar bitta o'zgaruvchida bir nechta qiymatlarni saqlash uchun ishlatiladi:

MisolO'zingizning Python serveringizni oling
Avtomobil nomlarini o'z ichiga olgan massiv yarating:

cars = ["Ford", "Volvo", "BMW"]
Massiv nima?
Massiv - bu bir vaqtning o'zida bir nechta qiymatni saqlashi mumkin bo'lgan maxsus o'zgaruvchi.

Agar sizda elementlar ro'yxati (masalan, avtomobil nomlari ro'yxati) bo'lsa, avtomobillarni bitta o'zgaruvchida saqlash quyidagicha ko'rinishi mumkin:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
Biroq, agar siz mashinalarni ko'rib chiqib, aniq bir mashinani topmoqchi bo'lsangiz-chi? Va agar sizda 3 ta emas, balki 300 ta mashina bo'lsa-chi?

Yechim massivdir!

Massiv bitta nom ostida ko'plab qiymatlarni saqlashi mumkin va siz ularga indeks raqamiga murojaat qilish orqali kirishingiz mumkin.

Massiv elementlariga kirish
Siz massiv elementiga indeks raqamiga murojaat qilish orqali murojaat qilasiz .

Misol
Birinchi massiv elementining qiymatini oling:

x = cars[0]
Misol
Birinchi massiv elementining qiymatini o'zgartiring:

cars[0] = "Toyota"
Massiv uzunligi
len()Massiv uzunligini (massivdagi elementlar soni) qaytarish uchun usuldan foydalaning .

Misol
Massivdagi elementlar sonini qaytaring cars :

x = len(cars)
Izoh: Massiv uzunligi har doim eng yuqori massiv indeksidan bittaga ko'p.

REKLAMALARNI OLIB TASHLASH

Massiv elementlarini sikllashtirish
Siz for insikldan foydalanib, massivning barcha elementlarini sikl bilan ko'rib chiqishingiz mumkin.

Misol
Massivdagi har bir elementni chop eting cars:

for x in cars:
  print(x)
Massiv elementlarini qo'shish
Siz append()usuldan foydalanib, massivga element qo'shishingiz mumkin.

Misol
Massivga yana bitta element qo'shing cars:

cars.append("Honda")
Massiv elementlarini olib tashlash
pop()Massivdan elementni olib tashlash uchun usuldan foydalanishingiz mumkin .

Misol
Massivning ikkinchi elementini o'chirish cars:

cars.pop(1)
remove()Shuningdek , usuldan massivdan elementni olib tashlash uchun ham foydalanishingiz mumkin .

Misol
"Volvo" qiymatiga ega elementni o'chiring:

cars.remove("Volvo")
Izoh: Ro'yxat remove()usuli faqat ko'rsatilgan qiymatning birinchi marta paydo bo'lishini olib tashlaydi.

Massiv usullari
Python ro'yxatlar/massivlarda foydalanishingiz mumkin bo'lgan bir qator o'rnatilgan usullarga ega.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

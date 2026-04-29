Faylni o'chirish
Faylni o'chirish uchun siz OS modulini import qilishingiz va uning os.remove()funksiyasini bajarishingiz kerak:

MisolO'zingizning Python serveringizni oling
"demofile.txt" faylini olib tashlang:

import os
os.remove("demofile.txt")
Fayl mavjudligini tekshiring:
Xatolikka yo'l qo'ymaslik uchun faylni o'chirishdan oldin uning mavjudligini tekshirishingiz mumkin:

Misol
Fayl mavjudligini tekshiring, keyin uni o'chiring:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
Jildni o'chirish
Butun papkani o'chirish uchun quyidagi os.rmdir()usuldan foydalaning:

Misol
"myfolder" papkasini olib tashlang:

import os
os.rmdir("myfolder")
Eslatma: Siz faqat bo'sh papkalarni olib tashlashingiz mumkin.
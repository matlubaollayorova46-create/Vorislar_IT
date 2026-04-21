O'rtacha, mediana va rejim
Raqamlar guruhiga qarab nimani o'rganishimiz mumkin?

Mashinada o'qitishda (va matematikada) bizni qiziqtiradigan uchta qiymat ko'pincha mavjud:

O'rtacha - o'rtacha qiymat
Median - O'rtacha qiymat
Rejim - Eng keng tarqalgan qiymat
Misol: Biz 13 ta mashinaning tezligini ro'yxatdan o'tkazdik:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

O'rtacha, o'rtacha yoki eng keng tarqalgan tezlik qiymati nima?

O'rtacha
O'rtacha qiymat o'rtacha qiymatdir.

O'rtacha qiymatni hisoblash uchun barcha qiymatlar yig'indisini toping va yig'indini qiymatlar soniga bo'ling:

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

NumPy modulida buning uchun usul mavjud. NumPy moduli haqida bizning NumPy qo'llanmamizda bilib oling .

MisolO'zingizning Python serveringizni oling
mean()O'rtacha tezlikni topish uchun NumPy usulidan foydalaning :

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

REKLAMALARNI OLIB TASHLASH

Mediana
Mediana qiymati barcha qiymatlarni saralab bo'lgandan keyin o'rtadagi qiymatdir:

77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111

Medianani topishdan oldin raqamlarni saralash muhimdir.

NumPy modulida buning uchun usul mavjud:

Misol
median()O'rtacha qiymatni topish uchun NumPy usulidan foydalaning :

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)
Agar o'rtada ikkita raqam bo'lsa, bu sonlarning yig'indisini ikkiga bo'ling.

77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103

(86 + 87) / 2 = 86.5

Misol
NumPy modulidan foydalanish:

import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)
Rejim
Rejim qiymati eng ko'p marta paydo bo'ladigan qiymatdir:

99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

SciPy modulida buning uchun usul mavjud. SciPy moduli haqida bizning SciPy qo'llanmamizda bilib oling .

Misol
mode()Eng ko'p ko'rinadigan raqamni topish uchun SciPy usulidan foydalaning :

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
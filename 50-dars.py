Massiv elementlariga kirish
Massiv indekslash massiv elementiga kirish bilan bir xil.

Massiv elementiga uning indeks raqamiga murojaat qilish orqali kirishingiz mumkin.

NumPy massivlaridagi indekslar 0 dan boshlanadi, ya'ni birinchi element 0 indeksga, ikkinchisi esa 1 indeksga va hokazolarga ega.

MisolO'zingizning Python serveringizni oling
Quyidagi massivdan birinchi elementni oling:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
Misol
Quyidagi massivdan ikkinchi elementni oling.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])
Misol
Quyidagi massivdan uchinchi va to'rtinchi elementlarni oling va ularni qo'shing.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

REKLAMALARNI OLIB TASHLASH

2 o'lchamli massivlarga kirish
2 o'lchamli massivlardan elementlarga kirish uchun biz elementning o'lchami va indeksini ifodalovchi vergul bilan ajratilgan butun sonlardan foydalanishimiz mumkin.

2 o'lchamli massivlarni qator va ustunlardan iborat jadval kabi tasavvur qiling, bu yerda o'lcham satrni, indeks esa ustunni ifodalaydi.

Misol
Birinchi qator, ikkinchi ustundagi elementga kirish:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
Misol
2-qator, 5-ustundagi elementga kirish:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])
3 o'lchamli massivlarga kirish
3 o'lchamli massivlardan elementlarga kirish uchun biz elementning o'lchamlari va indeksini ifodalovchi vergul bilan ajratilgan butun sonlardan foydalanishimiz mumkin.

Misol
Birinchi massivning ikkinchi massivining uchinchi elementiga kirish:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
Misol tushuntirildi
arr[0, 1, 2]qiymatini chop etadi 6.

Va shuning uchun:

Birinchi raqam ikkita massivni o'z ichiga olgan birinchi o'lchamni ifodalaydi:
[[1, 2, 3], [4, 5, 6]]
va:
[[7, 8, 9], [10, 11, 12]]
Biz ni tanlaganimiz uchun 0birinchi massiv qoladi:
[[1, 2, 3], [4, 5, 6]]

Ikkinchi raqam ikkinchi o'lchamni ifodalaydi, u ikkita massivni ham o'z ichiga oladi:
[1, 2, 3]
va:
[4, 5, 6]
Biz ni tanlaganimiz uchun 1ikkinchi massiv qoladi:
[4, 5, 6]

Uchinchi raqam uchinchi o'lchovni ifodalaydi, u uchta qiymatni o'z ichiga oladi:
4
5
6
Biz ni tanlaganimiz sababli 2, uchinchi qiymatga ega bo'lamiz:
6

Salbiy indekslash
Massivga oxiridan kirish uchun salbiy indekslashdan foydalaning.

Misol
Ikkinchi dimdan oxirgi elementni chop eting:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

Python diapazoni
O'rnatilgan range()funksiya o'zgarmas sonlar ketma-ketligini qaytaradi, bu odatda ma'lum bir marta sikl qilish uchun ishlatiladi.

Bu raqamlar to'plami o'zining ma'lumot turiga ega, deb ataladi range.

Izoh: O'zgarmas degani, u yaratilgandan keyin o'zgartirib bo'lmasligini anglatadi.
Diapazonlarni yaratish
Funksiya range()quyidagi sintaksis yordamida 1, 2 yoki 3 argument bilan chaqirilishi mumkin:

range(start, stop, step)

Bitta argument bilan range() ni chaqirish
Agar diapazon funksiyasi faqat bitta argument bilan chaqirilsa, argument qiymatni ifodalaydi stop.


Argument startixtiyoriy va agar ko'rsatilmagan bo'lsa, u standart holatda 0 ga teng bo'ladi.

range(10)0 dan 9 gacha bo'lgan har bir sonning ketma-ketligini qaytaradi. (Start argumenti, 0, inklyuziv va stop argumenti, 10, inklyuziv).

MisolO'zingizning Python serveringizni oling
0 dan 9 gacha bo'lgan raqamlar diapazonini yarating:

x = range(10)
Ikki argumentli range() ni chaqirish
Agar diapazon funksiyasi ikkita argument bilan chaqirilsa, birinchi argument qiymatni start, ikkinchi argument esa stopqiymatni ifodalaydi.

range(3, 10)3 dan 9 gacha bo'lgan har bir sonning ketma-ketligini qaytaradi:

Misol
3 dan 9 gacha bo'lgan raqamlar diapazonini yarating:

x = range(3, 10)
Uchta argument bilan range() ni chaqirish
Agar diapazon funksiyasi uchta argument bilan chaqirilsa, uchinchi argument qiymatni ifodalaydi step.

Bosqich qiymati ketma-ketlikdagi har bir raqam orasidagi farqni anglatadi. Bu ixtiyoriy va agar ko'rsatilmagan bo'lsa, standart qiymati 1 ga teng bo'ladi.

range(3, 10, 2)3 dan 9 gacha bo'lgan har bir sonning ketma-ketligini, 2 qadam bilan qaytaradi:

Misol
3 dan 9 gacha bo'lgan raqamlar diapazonini yarating:

x = range(3, 10, 2)

REKLAMALARNI OLIB TASHLASH

Diapazonlardan foydalanish
forDiapazonlar ko'pincha sonlar ketma-ketligi bo'yicha iteratsiya qilish uchun sikllarda ishlatiladi .

Misol
Bir diapazondagi har bir qiymat ustida takrorlang:

for i in range(10):
  print(i)
Diapazonlarni ko'rsatish uchun ro'yxatni ishlatish
Range obyekti o'zgarmas sonlar ketma-ketligini ifodalovchi ma'lumotlar turi bo'lib, uni to'g'ridan-to'g'ri ko'rsatib bo'lmaydi.

Shuning uchun, diapazonlar ko'pincha namoyish qilish uchun ro'yxatlarga aylantiriladi.

Misol
Turli diapazonlarni ro'yxatlarga aylantirish:

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
Dilimlash diapazonlari
Boshqa ketma-ketliklar singari, keyingi ketma-ketlikni ajratib olish uchun diapazonlarni tilimlash mumkin.

Misol
Quyidagi diapazondan ketma-ketlikni ajratib oling:

r = range(10)
print(r[2])
print(r[:3])
Izoh: Birinchi print operatori 2-indeksdagi qiymatni qaytaradi, ikkinchi print operatori esa 0 dan 3 gacha bo'lgan indeksdan yangi diapazon obyektini qaytaradi.
A'zolik testi
Range operator bilan a'zolik sinovini qo'llab-quvvatlaydi in.

Misol
6 va 7 raqamlari diapazonda mavjudligini tekshiring:

r = range(0, 10, 2)
print(6 in r)
print(7 in r)
Qaytish qiymati Trueraqam diapazonda mavjud bo'lganda va Falseu mavjud bo'lmaganda bo'ladi.

Uzunlik
Diapazonlar len()diapazondagi elementlar sonini olish funksiyasini qo'llab-quvvatlaydi.

Misol
Diapazon uzunligini oling:

r = range(0, 10, 2)
print(len(r))

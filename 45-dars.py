Blok trysizga kod blokini xatolar uchun sinab ko'rish imkonini beradi.

Blok exceptsizga xatoni hal qilish imkonini beradi.

Blok elsesizga xato bo'lmaganda kodni bajarishga imkon beradi.

Blok finallysizga try- va except bloklarining natijasidan qat'i nazar, kodni bajarishga imkon beradi.

Istisnolarni qayta ishlash
Xatolik yoki biz uni istisno deb ataganimizda, Python odatda to'xtaydi va xato xabarini yaratadi.

Ushbu istisnolar quyidagi bayonot yordamida hal qilinishi mumkin try:

MisolO'zingizning Python serveringizni oling
Blok tryistisno yaratadi, chunki xu aniqlanmagan:

try:
  print(x)
except:
  print("An exception occurred")
try bloki xatolik yuzaga keltirgani uchun, except bloki bajariladi.

Usha bloki bo'lmasa, dastur ishdan chiqadi va xatolik yuzaga keladi:

Misol
Bu bayonot xatoga olib keladi, chunki xaniqlanmagan:

print(x)
Ko'pgina istisnolar
Siz xohlagancha istisno bloklarini belgilashingiz mumkin, masalan, agar siz maxsus turdagi xato uchun maxsus kod blokini bajarmoqchi bo'lsangiz:

Misol
Agar try bloki a ni ko'tarsa, bitta xabarni NameErrorva boshqa xatolar uchun boshqa xabarni chop eting:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
Python o'rnatilgan istisnolar ma'lumotnomasida ko'proq xato turlarini ko'ring .

REKLAMALARNI OLIB TASHLASH

Boshqa
elseAgar xatolik yuzaga kelmasa, bajariladigan kod blokini aniqlash uchun kalit so'zdan foydalanishingiz mumkin :

Misol
Ushbu misolda, tryblok hech qanday xatolik keltirib chiqarmaydi:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
Nihoyat
Agar blok finallybelgilangan bo'lsa, urinish bloki xatolik tug'diradimi yoki yo'qmi, qat'i nazar, bajariladi.

Misol
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
Bu obyektlarni yopish va resurslarni tozalash uchun foydali bo'lishi mumkin:

Misol
Yozib bo'lmaydigan faylni ochib, unga yozishga harakat qiling:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
Dastur fayl obyektini ochiq qoldirmasdan davom etishi mumkin.

REKLAMALARNI OLIB TASHLASH

Istisno qo'yish
Python dasturchisi sifatida siz biron bir shart yuzaga kelganda istisno qo'yishni tanlashingiz mumkin.

Istisno qo'yish (yoki oshirish) uchun raisekalit so'zdan foydalaning.

Misol
Agar x 0 dan past bo'lsa, xatolik haqida xabar bering va dasturni to'xtating:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
Kalit raiseso'z istisno qo'zg'atish uchun ishlatiladi.

Siz qanday xatolik yuz berishini va foydalanuvchiga chop etiladigan matnni belgilashingiz mumkin.

Misol
Agar x butun son bo'lmasa, TypeError xatosini ko'taring:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

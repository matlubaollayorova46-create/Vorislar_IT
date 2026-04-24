with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
  
  with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())
  
  f = open("myfile.txt", "x")

import os
os.remove("demofile.txt")


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
  import os
os.rmdir("myfolder")

"- Matn - Standart qiymat. Matn rejimi"

"b"-" Ikkilik - Ikkilik rejim (masalan, rasmlar)"
"r"-" O'qish - Standart qiymat. Faylni o'qish uchun ochadi, agar fayl mavjud bo'lmasa, xatolik yuz beradi"

"a"- "Qo'shish - Faylni qo'shish uchun ochadi, agar u mavjud bo'lmasa, faylni yaratadi"

"w"- "Yozish - Faylni yozish uchun ochadi, agar u mavjud bo'lmasa, faylni yaratadi"

"x"-" Yaratish - Belgilangan faylni yaratadi, agar fayl mavjud bo'lsa, xato qaytaradi"
Django ko'rinishlari - bu HTML hujjatlari kabi http so'rovlarini qabul qiladigan va http javobini qaytaradigan Python funksiyalari.

Django'dan foydalanadigan veb-sahifa turli vazifalar va missiyalarga ega ko'rinishlarga to'la.

views.pyKo'rishlar odatda ilovangiz papkasida joylashgan faylga joylashtiriladi .

views.pySizning memberspapkangizda quyidagicha ko'rinadigan fayl mavjud :

my_tennis_club/members/views.py:

from django.shortcuts import render

# Create your views here.
Uni toping, oching va tarkibni quyidagi bilan almashtiring:

my_tennis_club/members/views.py:

from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
"Eslatma: Ko'rinish nomi ilova nomi bilan bir xil bo'lishi shart emas.

membersMen buni shu kontekstga mos kelishini o'ylaganim uchun shunday deb atayman .

Bu brauzerga javobni qanday qaytarishning oddiy misoli.

Lekin ko'rinishni qanday bajarishimiz mumkin? Xo'sh, biz ko'rinishni URL orqali chaqirishimiz kerak.

Keyingi bobda URL manzillari haqida bilib olasiz ."
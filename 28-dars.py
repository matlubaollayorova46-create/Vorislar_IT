a="ism"
print(a)
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"Ko'pgina qiymatlar haqiqatdir
TrueDeyarli har qanday qiymat , agar u biron bir tarkibga ega bo'lsa, baholanadi .

Bo'sh satrlardan tashqari istalgan satr bo'ladi True.

Har qanday son True, dan tashqari, bo'ladi 0.

Bo'sh bo'lganlardan tashqari har qanday ro'yxat, tuple, to'plam va lug'at ga teng True.

Misol
Quyidagilar True qiymatini qaytaradi:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def myFunction() :
  return True

print(myFunction())
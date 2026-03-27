x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


x = y = z = "Orange"
print(x)
print(y)
print(z)


  #O'rnatilgan ma'lumotlar turlari
Dasturlashda ma'lumotlar turi muhim tushunchadir.

O'zgaruvchilar turli xil ma'lumotlarni saqlashi mumkin va turli xil o'zgaruvchilar turli xil ishlarni bajarishi mumkin.

Python ushbu toifalarda sukut bo'yicha quyidagi ma'lumotlar turlariga ega:

Matn turi:	str
Raqamli turlari:	int, float, complex
Ketma-ketlik turlari:	list, tuple, range
Xaritalash turi:	dict
To'plam turlari:	set,frozenset
Boolean turi:	bool
Ikkilik turlari:	bytes, bytearray, memoryview
Turi yo'q:	NoneType 

#Example	Data Type	Try it
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	


#Muayyan ma'lumot turini sozlash
#Agar siz ma'lumotlar turini ko'rsatmoqchi bo'lsangiz, quyidagi konstruktor funksiyalaridan foydalanishingiz mumkin:

#Example	Data Type	
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	

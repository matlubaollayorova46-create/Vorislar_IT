x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


x = str("s1") # x will be 's1'

y = str(2)    # y will be '2'

z = str(3.0)  # z will be '3.0'



a = "Hello, World!"
print(a.upper())
a = "Hello, World!"


print(a.lower())
a = " Hello, World! "

print(a.strip()) # returns "Hello, World!"


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print(10 > 9)



print(10 == 9)


print(10 < 9)


try:
  print(x)
except:
  print("An exception occurred")

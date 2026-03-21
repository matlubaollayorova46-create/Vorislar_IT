f = open("demofile.txt")
print(f.read())

f = open("D:\\myfiles\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
  print(f.read())
  
  f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt") as f:
  print(f.read(5))
  
with open("demofile.txt") as f:
print(f.readline())
  
  with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

with open("demofile.txt") as f:
  for x in f:
    print(x)

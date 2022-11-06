a = "hello"
b = " " #space works as string
c = "world"

print(a+b+c)



a = "hello"
b = 5

c = b + len(a)

print(c)

print("-------")

a = "world"
for i in range (len(a)):
  c = a[i]
  print(c)

print("-------")

f = "d"

for i in range (len(a)):
  c = a[i]
  if c == f: #must match a string
    print("found", c)

x = ""
print(x)
x = "above line is skipped"
print(x)

y = "6"

z = int(y) #converts string into numerical value

print(z)

def func(j, k):
  return len(j+k)

a = "hello"
b = "world"
c = func(a,b)

print(c)

def func(j, k):
  return j*len(k)

a = 7
b = "hello"
c = func(a,b)

print(c)


#ASCII representation of my name: 083 117 110 103 109 105 110 075 105 109
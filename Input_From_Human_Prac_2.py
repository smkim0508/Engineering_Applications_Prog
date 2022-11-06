# program 1
print('Enter F degrees:') 
F = int(input())
C = (F-32)*5/9
print("C =", C)

# program 2
print('Enter cubits:') 
Cubits = int(input())
m = 0.4572*Cubits
attoparsec = m/0.0308568
print("Attoparsec =", attoparsec)

# program 3 
print('Enter loops:') 
loops = int(input())
loops += 1
for i in range (0,loops):
  print(i)
 
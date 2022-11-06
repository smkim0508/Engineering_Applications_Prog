# program 1
print('Enter loops:') 
loops = int(input())
sum0 = 0
loops += 1
for i in range (0,loops):
  print(i)
  sum0 = sum0 + i

print("sum=", sum0 )

# program 2
print('Enter loops:') 
loops = int(input())
product = 1
loops += 1
for i in range (1,loops):
  product = product * i

print("Factorial =", product)
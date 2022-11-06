ASCII = "083,117,110,103,109,105,110,075,105,109"
deliminator = ","

def sumfunc(a,b):
  sum0 = 0
  comb = ""
  for i in range (len(a)):
    char = a[i]
    if char == b:
      sum0 += int(comb)
      comb = ""
    else:
      comb = comb + char
  sum0 += int((a[len(a)-3]+a[len(a)-2]+a[len(a)-1]))
  return sum0

sum1 = sumfunc(ASCII, deliminator)

print(sum1)


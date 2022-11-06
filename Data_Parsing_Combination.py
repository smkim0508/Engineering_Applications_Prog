ASCII = "083,117,110,103,109,105,110,075,105,109"
sum0 = 0
comb = ""
for i in range (len(ASCII)):
  char = ASCII[i]
  if char == ",":
    sum0 += int(comb)
    comb = ""
  else:
    comb = comb + char
sum0 += int((ASCII[len(ASCII)-3]+ASCII[len(ASCII)-2]+ASCII[len(ASCII)-1]))

print(sum0)


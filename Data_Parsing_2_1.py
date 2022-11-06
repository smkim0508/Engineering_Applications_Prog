datalist = []
ASCII = "083,117,110,103,109,105,110,075,105,109,"
deliminator = ","

def updatelist(a,b):
  locallist = []
  comb = ""
  for i in range (len(a)):
    char = a[i]
    if char == b:
      locallist.append(comb)
      comb = ""
    else:
      comb = comb + char
  
  return locallist

datalist = updatelist(ASCII, deliminator)

print(datalist)


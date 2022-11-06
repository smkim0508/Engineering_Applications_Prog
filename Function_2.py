LowTemp = [27, 26, 8, 14, 24, 22, 23, 19]
HighTemp = [48, 42, 37, 25, 40, 42, 43, 40]

def min_max(a, b):
   minLo = a[0]
   maxLo = a[0]
   minHi = b[0]
   maxHi = b[0]
   for i in range (0, len(a)):
    if minLo > a[i]:
      minLo = a[i]
    if minHi > b[i]:
      minHi = b[i]
    if maxLo < a[i]:
      maxLo = a[i]
    if maxHi < b[i]:
      maxHi = b[i]
  
   return minLo, minHi, maxLo, maxHi

print

min_low, min_high, max_low, max_high = min_max(LowTemp, HighTemp)
print("Low Temp: min = %2.1f"%min_low, "high = %2.1f"%max_low)
print("High Temp: min = %2.1f"%min_high, "max = %2.1f"%max_high)

  


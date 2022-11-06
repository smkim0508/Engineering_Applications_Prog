LowTemp = [27, 26, 8, 14, 24, 22, 23, 19]
HighTemp = [48, 42, 37, 25, 40, 42, 43, 40]

def avgTemp(LowTemp, HighTemp):
  sum_temp_low = 0
  sum_temp_high = 0
  smaller_set = len(LowTemp)
  if smaller_set > len(HighTemp):
    smaller_set = HighTemp
  for i in range (0, smaller_set):
    sum_temp_low += LowTemp[i]
    sum_temp_high += HighTemp[i]
  average_temp_low = (sum_temp_low/smaller_set)
  average_temp_high = (sum_temp_high/smaller_set)
  
  return average_temp_high, average_temp_low

avg_high, avg_low = avgTemp(LowTemp, HighTemp)

print("High Temp = %2.1f"%avg_high, "Low Temp = %2.1f"%avg_low)

# with two separate functions:

# LowTemp = [27, 26, 8, 14, 24, 22, 23, 19]
# HighTemp = [48, 42, 37, 25, 40, 42, 43, 40]

# sum_temp_low = 0
# sum_temp_high = 0

# def avgTempLo(LowTemp):
#   sum_temp_low = 0
#   for i in range (0, len(LowTemp)):
#     sum_temp_low += LowTemp[i]
#   average_temp_low = (sum_temp_low/len(LowTemp))
#   return(average_temp_low)


# def avgTempHi(HighTemp):
#   sum_temp_high = 0
#   for i in range (0, len(HighTemp)):
#     sum_temp_high += HighTemp[i]
#   average_temp_high = (sum_temp_high/len(HighTemp))
#   return(average_temp_high)

# average_Temp_High = avgTempHi(HighTemp)
# average_Temp_Low = avgTempLo(LowTemp)

# print("High Temp = %2.1f"%average_Temp_High)
# print("Low Temp = %2.1f"%average_Temp_Low)

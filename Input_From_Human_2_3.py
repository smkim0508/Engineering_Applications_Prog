sum0=0
count = 0
while(1): 
  print('Enter value:') # prompt user
  value = input() # wait for input entered by user
  if (value == "done"):
    break
  else:
    sum0 += int(value)
    count += 1
average = (sum0/count)
print("Average = %2.2f"%average)

x = 1
y = 4
z = x+y
print ("z without function = ", z)

def addValues(a, b):
  sum_of_arguments = x+y
  print(sum_of_arguments)
  return(sum_of_arguments)
  
sum0 = addValues(a, b)
print("z with function = ", sum0)

x = 2
y = 3
sum = addValues(x, y)
print("z with function = ", sum)

heights = [5.1, 5.2, 5.3, 5.4, 5.5]

def firstLast(listValues):
  first = listValues [0]
  last = listValues [len(listValues) - 1]
  return first, last

firstHeight, lastHeight = firstLast(heights)
print("First height = %2.1f"% firstHeight, "Last height = %2.1f"% lastHeight)

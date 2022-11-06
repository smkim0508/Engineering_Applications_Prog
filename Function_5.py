HighTemp = [48, 42, 37, 25, 40, 42, 43, 40]
x = [1, 2, 3, 4, 5, 6, 7, 8]
#x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#y = np.array(HighTemp)


def mxb(x, y):
    m = 0
    sumXY=0
    sumX=0
    sumX2=0
    sumY=0
  
    for i in range (0, len(y)):
      sumXY += x[i]*y[i]
      sumX += x[i]
      sumY += y[i]
      sumX2 += x[i]*x[i]
    sumXY = sumXY/len(x)
    sumX = sumX/len(x)
    sumY = sumY/len(y)
    sumX2 = sumX2/len(x)
    m = (sumXY-sumX*sumY)/(sumX2-sumX*sumX)
    b = (sumX2*sumY-sumXY*sumX)/(sumX2-sumX*sumX)
    return m, b

slope, y_intercept = mxb(x, HighTemp)

print("Slope = %2.3f"%slope, "Y-intercept = %2.3f"%y_intercept)


from maxprofitlinear import ArrayMaxLinear

def getArrayMin(prices, start, end):
  min = prices[start]
  for i in range(start+1 , end+1):
    if(min > prices[i]):
      min = prices[i]

  return min   

def getArrayMax(prices, start, end):
  max = prices[start]
  for i in range(start+1 , end+1):
    if(max < prices[i]):
      max = prices[i]

  return max   

def maxProfitDnC(prices, start, end):
  if(start >= end):
    return -1

  mid = int((start + end )/2)
  
  leftProfit = maxProfitDnC(prices, start, mid)
  rightProfit = maxProfitDnC(prices, mid+1, end)
  
  minLeft = getArrayMin(prices, start,mid)
  maxRight = getArrayMax(prices, mid, end)

  profit = maxRight - minLeft


  return max(leftProfit, rightProfit, profit)

  


  
    
def readInputFile():
  prices = []
  inputFile = open("inputPS8.txt", "r")
  for line in inputFile:
    data = line.split("/")
    price = int(data[1].strip())
    prices.append(price)

  inputFile.close()

  return prices

prices = readInputFile()
linearProfit = ArrayMaxLinear()
linearProfit.maxProfitLinear(prices)

print(prices)
print(maxProfitDnC(prices,0, len(prices)-1))
from maxdifferencelinear import ArrayMaxDifferenceLinear
from maxdifferencerecursive import ArrayMaxDifferenceRecursive
    
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

linearProfit = ArrayMaxDifferenceLinear()
linearProfit.maxDifference(prices)

recursiveProfit= ArrayMaxDifferenceRecursive()
recursiveProfit.maxDifference(prices)

print(prices)

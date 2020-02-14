from maxdifferencelinear import ArrayMaxDifferenceLinear
from maxdifferencerecursive import ArrayMaxDifferenceRecursive

#function to read and parse input file    
def readInputFile():
  prices = []
  inputFile = open("inputPS8.txt", "r")
  #read the file and add price data to a list
  for line in inputFile:
    data = line.split("/")
    price = int(data[1].strip())
    prices.append(price)

  inputFile.close()

  return prices

prices = readInputFile()

#Recursive approach
recursiveProfit= ArrayMaxDifferenceRecursive()
recursiveProfit.maxDifference(prices)

#Linear approach
linearProfit = ArrayMaxDifferenceLinear()
linearProfit.maxDifference(prices)




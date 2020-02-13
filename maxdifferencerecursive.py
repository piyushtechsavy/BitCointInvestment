class ArrayMaxDifferenceRecursive:

  def getArrayMin(self,prices, start, end):
    min = prices[start]
    minIndex = start
    for i in range(start+1 , end+1):
      if(min > prices[i]):
        min = prices[i]
        minIndex = i

    return (min, minIndex)   

  def getArrayMax(self,prices, start, end):
    max = prices[start]
    maxIndex = start
    for i in range(start+1 , end+1):
      if(max < prices[i]):
        max = prices[i]
        maxIndex = i

    return (max, maxIndex)   

  def maxProfitDnC(self,prices, start, end):
    if(start >= end):
      return (-1,start,start)

    mid = int((start + end )/2)
    
    leftProfit,leftMin,leftMax = self.maxProfitDnC(prices, start, mid)
    rightProfit,rightMin,rightMax = self.maxProfitDnC(prices, mid+1, end)
    
    minLeft,minIndex = self.getArrayMin(prices, start,mid)
    maxRight,maxIndex = self.getArrayMax(prices, mid, end)

    profit = maxRight - minLeft

    maxProfit = max(leftProfit, rightProfit, profit)

    if(maxProfit == leftProfit):
      return (leftProfit,leftMin,leftMax)

    if(maxProfit == rightProfit):
      return (rightProfit,rightMin,rightMax)
      
    return (profit, minIndex, maxIndex)

  def maxDifference(self,prices):
    maxProf,dayIndxToBuy,dayIndxToSell = self.maxProfitDnC(prices,0, len(prices)-1)

    outputFile = open("outputPS8.txt", "a")
    outputFile.write("Maximum Profit (Recursive solution): %d \n" %(maxProf))
    outputFile.write("Day to buy: %d \n" %(dayIndxToBuy + 1))
    outputFile.write("Day to sell: %d \n" %(dayIndxToSell + 1))

    outputFile.close() 
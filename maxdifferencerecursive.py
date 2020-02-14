#Class that return max profit using Divide and Conquer approach
class ArrayMaxDifferenceRecursive:

  #Returns min element and its postiton in an array between start and end
  def getArrayMin(self,prices, start, end):
    min = prices[start]
    minIndex = start
    for i in range(start+1 , end+1):
      if(min > prices[i]):
        min = prices[i]
        minIndex = i

    return (min, minIndex)   

  #Returns max element and its postiton in an array between start and end
  def getArrayMax(self,prices, start, end):
    max = prices[start]
    maxIndex = start
    for i in range(start+1 , end+1):
      if(max < prices[i]):
        max = prices[i]
        maxIndex = i

    return (max, maxIndex)   

  #Recursive fucntion to calculate maximum profit with days to buy and sell
  def maxProfitDnC(self,prices, start, end):
    if(start >= end):
      return (-1,start,start)

    #break the array in to two parts
    mid = int((start + end )/2)
    
    #get max profit of left part
    leftProfit,leftMin,leftMax = self.maxProfitDnC(prices, start, mid)

    #get max profit of right part
    rightProfit,rightMin,rightMax = self.maxProfitDnC(prices, mid+1, end)
    
    #get min element from left and max from right
    minLeft,minIndex = self.getArrayMin(prices, start,mid)
    maxRight,maxIndex = self.getArrayMax(prices, mid, end)

    #calculate current profit
    profit = maxRight - minLeft

    #max profit is max of all three profits
    maxProfit = max(leftProfit, rightProfit, profit)

    #return max profit with day to buy and sell
    if(maxProfit == leftProfit):
      return (leftProfit,leftMin,leftMax)

    if(maxProfit == rightProfit):
      return (rightProfit,rightMin,rightMax)
      
    return (profit, minIndex, maxIndex)

  #This function calls respective methods to calculate max profit
  def maxDifference(self,prices):
    
    maxProf,dayIndxToBuy,dayIndxToSell = self.maxProfitDnC(prices,0, len(prices)-1)

    #print to output file
    outputFile = open("outputPS8.txt", "w")
    outputFile.write("Maximum Profit (Divide & Conquer solution): %d \n" %(maxProf))
    outputFile.write("Day to buy: %d \n" %(dayIndxToBuy + 1))
    outputFile.write("Day to sell: %d \n\n" %(dayIndxToSell + 1))

    outputFile.close() 
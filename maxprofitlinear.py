class ArrayMaxLinear:
  def maxProfitLinear(self,prices):
    size = len(prices)
    dayIndxToBuy = 0
    minIndex = 0
    dayIndxToSell = 0
    maxProf = prices[dayIndxToSell] - prices[dayIndxToBuy] 
    minElement = prices[dayIndxToBuy] 
        
    for i in range( 1, size ): 
      if (prices[i] - minElement > maxProf): 
        maxProf = prices[i] - minElement 
        dayIndxToSell = i
        dayIndxToBuy = minIndex
    
      if (prices[i] < minElement): 
        minElement = prices[i] 
        minIndex = i
    
    
    outputFile = open("outputPS8.txt", "w")
    outputFile.write("Maximum Profit (Iterative solution): %d \n" %(maxProf))
    outputFile.write("Day to buy: %d \n" %(dayIndxToBuy + 1))
    outputFile.write("Day to sell: %d \n" %(dayIndxToSell + 1))

    outputFile.close() 
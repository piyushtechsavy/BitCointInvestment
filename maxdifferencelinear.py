#Class that return max profit using a linear Dynamic programming approach
class ArrayMaxDifferenceLinear:
  def maxDifference(self,prices):
    size = len(prices)
    #this is a dynamic programming approach
    #assume day to buy and sell as 0
    dayIndxToBuy = 0
    minIndex = 0
    dayIndxToSell = 0

    #max profit as per day to buy and sell
    maxProf = prices[dayIndxToSell] - prices[dayIndxToBuy] 
    minElement = prices[dayIndxToBuy] 

    #iterate the price list    
    for i in range( 1, size ): 
      #maxProfit so far is max difference from minimum element so far and current element
      if (prices[i] - minElement > maxProf): 
        maxProf = prices[i] - minElement #max profit
        dayIndxToSell = i #index of day to sell
        dayIndxToBuy = minIndex #index of day to buy
      
      #set minimum element so fat by comparing with current element
      if (prices[i] < minElement): 
        minElement = prices[i] #min element
        minIndex = i #index of min element, would be day to buy
    
    #add output to output file
    outputFile = open("outputPS8.txt", "a")
    outputFile.write("Maximum Profit (Iterative solution): %d \n" %(maxProf))
    outputFile.write("Day to buy: %d \n" %(dayIndxToBuy + 1))
    outputFile.write("Day to sell: %d \n" %(dayIndxToSell + 1))

    outputFile.close() 
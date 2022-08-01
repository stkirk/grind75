# Given an array of prices, prices[i] is the price of the stock on the ith day
# find the optimal day to buy where profit could be taken in a future day
# return the max profit from buying and selling on the optimal day
# if no profit can be achieved return 0

def max_profit(prices):
    # init a buy price to prices[0]
    buy_price = prices[0]
    # init a max profit to 0
    max_profit = 0

    # loop through price in prices
    for price in prices:
        # init cur_profit
        cur_profit = price - buy_price
        # slide the buy index if this price is less
        if price < buy_price:
            buy_price = price
        if cur_profit > max_profit:
            max_profit = cur_profit
            
    return max_profit
    

print(max_profit([7,1,5,3,6,4])) # 5, buy on day 2, sell on day 5
print(max_profit([7,6,4,3,1])) # 0, no profit can be achieved

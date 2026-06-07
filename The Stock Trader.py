
def max_profit(prices):
    if not prices:
        return 0
        
    min_price = prices[0]  # Start by assuming the first day is the cheapest
    max_profit = 0         # Start with 0 profit
    
    for price in prices[1:]:
        # If we found a lower buying price, lock it in
        if price < min_price:
            min_price = price
        # Otherwise, check what our profit would be if we sold today
        else:
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
            
    return max_profit
a = [1, 3, 6, 9, 11]
print(max_profit(a))

def max_profit(prices):
    if not prices:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Test cases
prices1 = [9, 1, 3, 6, 4, 8, 3, 5, 5]
prices2 = [6, 4, 3, 3, 2]

print("Max profit for prices1:", max_profit(prices1))  # Output: 7
print("Max profit for prices2:", max_profit(prices2))  # Output: 0

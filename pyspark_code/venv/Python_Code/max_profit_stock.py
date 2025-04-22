"""
Problem: Determine the maximum profit that can be made by buying and selling a stock once.
"""

def Profit(sp):
    min_price = sp[0]
    max_profit = 0

    for price in sp:
        if min_price > price:
            min_price = price
        if max_profit < price - min_price:
            max_profit = price - min_price

    return max_profit

SP1 = [7, 1, 5, 3, 6, 4]
SP2 = [7, 5, 3, 6, 4, 1]

print("Max Profit SP1:", Profit(SP1))  #5
print("Max Profit SP2:", Profit(SP2)) #5

#!/usr/bin/python
# finds the maximum profit given an array of numbers representing
# stock price changes througout the day.
#
#
# Goal: O(n) time and O(1) space

def get_max_profit(price_array):
    if len(price_array) > 2:
        # set a starting profit by selling @1 and buying @0
        max_profit = price_array[1] - price_array[0]
        # set a min for the day at the first price
        min_price = price_array[0]

        for index, current_price in enumerate(price_array):
            # can't buy/sell at same time
            if index == 0:
                continue

            # what's the max we COULD get
            potential_profit = current_price - min_price
            # is the potential bigger than what we already have?
            max_profit = max(max_profit, potential_profit)
            # set a new min if the current is less than what we know
            min_price = min(current_price, min_price)

        return max_profit



# simple starting array
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(stock_prices_yesterday)

# what happens if the price goes down all day (best profit is negative)
stock_prices_yesterday = [10, 8, 6, 4, 2]
print get_max_profit(stock_prices_yesterday)

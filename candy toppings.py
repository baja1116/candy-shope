old_toppings_and_prices = [["choclate chips", 0.80], ["candy cane", 0.96], ["gummy bears", 0.97], ["gun powder", 0.65]]


toppings = [["choclate chips"], ["candy cane"], ['gummy bears'], ['gun powder']]

grades = [[0.70], [0.90], [0.50], ["free"]]

new_toppings_and_prices = [["choclate chips", 0.70], ["candy cane", 0.90], ["gummy bears", 0.50], ["gun powder", "free"]]

compare_word = ("these are our old and new prices please take a look")
new_toppings_and_prices[3].remove("gun powder")
new_toppings_and_prices[3].remove("free")

comparison_chart = old_toppings_and_prices + new_toppings_and_prices
print(compare_word)
print(comparison_chart)

# Repetitive code (BEFORE refactoring)

price1 = 100
discounted1 = price1 - (price1 * 0.10)

price2 = 250
discounted2 = price2 - (price2 * 0.10)

price3 = 500
discounted3 = price3 - (price3 * 0.10)

print(discounted1, discounted2, discounted3)

# Refactored code (AFTER refactoring)
def apply_discount(price, discount_rate=0.10):
    return price - (price * discount_rate)
prices = [100, 250, 500]
discounted_prices = [apply_discount(price) for price in prices]
print(*discounted_prices)
# Repetitive code (BEFORE refactoring)
price1 = 100
discounted1 = price1 - (price1 * 0.10)
price2 = 250
discounted2 = price2 - (price2 * 0.10)
price3 = 500
discounted3 = price3 - (price3 * 0.10)
print(discounted1, discounted2, discounted3)



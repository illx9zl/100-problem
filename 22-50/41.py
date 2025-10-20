from typing import List

def calculate_discounted_prices(prices: List[float], discount_percentage: float) -> List[float]:
    factor = 1 - (discount_percentage / 100)
    discounted = [round(price * factor, 2) for price in prices]
    return discounted


# ตัวอย่างการใช้งาน
prices = [100.0, 250.0, 75.0]
discount_percentage = 20.0

print(calculate_discounted_prices(prices, discount_percentage))

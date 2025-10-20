from typing import Tuple

def calculate_profit(
    sales: Tuple[float, float, float, float, float],
    costs: Tuple[float, float, float, float, float]
) -> Tuple[Tuple[float, float, float, float, float], float]:
    
    # คำนวณกำไรประจำปี
    annual_profits = tuple(s - c for s, c in zip(sales, costs))
    
    # คำนวณกำไรรวม
    total_profit = sum(annual_profits)
    
    return annual_profits, total_profit


# ตัวอย่างการใช้งาน
sales = (10000.0, 15000.0, 20000.0, 25000.0, 30000.0)
costs = (7000.0, 8000.0, 9000.0, 11000.0, 12000.0)

print(calculate_profit(sales, costs))

from typing import List

def calculate_investment_growth(principal: float, annual_rate: float, years: int = 5) -> List[float]:
    results = []
    for n in range(1, years + 1):
        amount = principal * ((1 + annual_rate / 100) ** n)
        results.append(amount)
    return results


# ตัวอย่างการใช้งาน
print(calculate_investment_growth(1000, 5, 5))

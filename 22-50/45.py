def calculate_annual_return(initial_investment: float, final_investment: float, years: int) -> float:
    # ใช้สูตร CAGR
    rate = (final_investment / initial_investment) ** (1 / years) - 1
    return round(rate * 100, 2)


# ตัวอย่างการใช้งาน
print(calculate_annual_return(1000, 1500, 5))  # 8.45

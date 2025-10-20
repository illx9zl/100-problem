from typing import Tuple

def highest_sales_country(sales: dict[str, int]) -> Tuple[str, int]:
    # ใช้ max() โดยกำหนด key เป็นยอดขาย
    country = max(sales, key=sales.get)
    return country, sales[country]


# ตัวอย่างการใช้งาน
sales_data = {
    "Thailand": 1500,
    "Laos": 1200,
    "Vietnam": 1800,
    "Japan": 1700,
    "China": 2000
}

print(highest_sales_country(sales_data))

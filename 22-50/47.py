def calculate_rectangle_area(width: float, length: float) -> float:
    if width <= 0 or length <= 0:
        raise ValueError("Width and length must be positive numbers greater than 0.")
    return float(width * length)


# ตัวอย่างการใช้งาน
print(calculate_rectangle_area(5, 10))   # 50.0


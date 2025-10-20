def calculate_perimeter(a: float, b: float, c: float) -> float:
    # ตรวจสอบว่าเป็นสามเหลี่ยมที่ถูกต้อง
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    
    return a + b + c


# ตัวอย่างการใช้งาน
print(calculate_perimeter(3, 4, 5))  # 12

def calculate_jumps(d: int, s: int) -> int:
    # ใช้การหารปัดขึ้น (ceiling division)
    jumps = (d + s - 1) // s
    return jumps


# ตัวอย่างการใช้งาน
print(calculate_jumps(20, 7))  # 3


def print_diamond_pattern(n: int) -> None:
    # ส่วนบน (เพิ่มจำนวนดอกจัน)
    for i in range(1, n + 1):
        print("*" * i)
    # ส่วนล่าง (ลดจำนวนดอกจัน)
    for i in range(n - 1, 0, -1):
        print("*" * i)
print_diamond_pattern(3)

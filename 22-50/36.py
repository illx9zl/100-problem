def print_diamond_pattern(n: int) -> None:
    half = n // 2
    # ส่วนบน (รวมแถวกลาง)
    for i in range(half):
        stars = "*" * (half - i)
        hyphens = "-" * (2 * i)
        print(stars + hyphens + stars)
    # ส่วนล่าง (สะท้อนกลับ)
    for i in range(half - 2, -1, -1):
        stars = "*" * (half - i)
        hyphens = "-" * (2 * i)
        print(stars + hyphens + stars)
print_diamond_pattern(10)

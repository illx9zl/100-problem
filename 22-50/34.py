def print_rectangle_pattern(rows: int, columns: int) -> None:
    for _ in range(rows):              # วนตามจำนวนแถว
        print("*" * columns)           # พิมพ์ดอกจันตามจำนวนคอลัมน์
print_rectangle_pattern(5, 5)

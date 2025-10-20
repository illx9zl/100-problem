def print_number_pattern(rows: int) -> None:
    for i in range(1, rows + 1):
        # พิมพ์ขีดกลาง (rows - i ตัว)
        dashes = "-" * (rows - i)
        # พิมพ์ตัวเลขจาก i ลงไปถึง 1
        numbers = "".join(str(j) for j in range(i, 0, -1))
        print(dashes + numbers)
print_number_pattern(5)

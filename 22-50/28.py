from typing import Set

def check_membership(s: Set, value: str) -> bool:
    # ถ้า value เป็นตัวเลขในรูป string เช่น "2" → แปลงเป็น int ก่อน
    if value.isdigit():
        value = int(value)
    return value in s


# ตัวอย่างการใช้งาน
s = {1, 2, 3, 'a', 'e', 'i', 'o', 'u', "red", "green", "blue"}

print(check_membership(s, "2"))       # True (เพราะ "2" ถูกแปลงเป็น int 2)
print(check_membership(s, "a"))       # True
print(check_membership(s, "yellow"))  # False

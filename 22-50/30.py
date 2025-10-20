from typing import Set, Tuple

def calculate_set_differences(set1: Set[str], set2: Set[str]) -> Tuple[Set[str], Set[str]]:
    diff1 = set1 - set2   # สมาชิกที่อยู่ใน set1 แต่ไม่อยู่ใน set2
    diff2 = set2 - set1   # สมาชิกที่อยู่ใน set2 แต่ไม่อยู่ใน set1
    return diff1, diff2


# ตัวอย่างการใช้งาน
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}

print(calculate_set_differences(set1, set2))

from typing import List, Dict

def create_dictionary(list1: List[int], list2: List[str]) -> Dict[int, str]:
    # ใช้ zip() จับคู่ค่าใน list1 และ list2
    return dict(zip(list1, list2))

# ตัวอย่างการใช้งาน
list1 = [1, 2, 3, 4]
list2 = ["blue", "green", "pink", "yellow"]
print(create_dictionary(list1, list2))

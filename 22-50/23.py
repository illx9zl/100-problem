from typing import Tuple, Dict

def create_dictionary(tuple1: Tuple[int, ...], tuple2: Tuple[str, ...]) -> Dict[int, str]:
    # ใช้ zip() จับคู่ค่าใน tuple1 และ tuple2
    return dict(zip(tuple1, tuple2))

# ตัวอย่างการใช้งาน
tuple1 = (1, 2, 3, 4)
tuple2 = ("ant", "cat", "dog", "cow")
print(create_dictionary(tuple1, tuple2))

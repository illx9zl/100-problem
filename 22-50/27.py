from typing import Set, List

def build_set_from_list(inputs: List[int]) -> Set[int]:
    numbers: Set[int] = set()
    for value in inputs:
        if len(numbers) == 5:
            break
        numbers.add(value)
    return numbers

# ตัวอย่างการทดสอบ
test_inputs = [10, 20, 30, 40, 50]  # จำลองว่าผู้ใช้ป้อนค่าเหล่านี้
print(build_set_from_list(test_inputs))


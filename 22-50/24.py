from typing import List, Tuple, Dict

def store_student_info(student_data: List[Tuple[str, str]]) -> Dict[str, str]:
    # ใช้ dict() แปลง list ของ tuple ให้เป็น dictionary
    return dict(student_data)

# ตัวอย่างการใช้งาน
students = [("123456", "Alice"), ("654321", "Bob"), ("112233", "Charlie")]
print(store_student_info(students))

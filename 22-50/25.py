from typing import List, Tuple, Dict

def store_student_scores(student_data: List[Tuple[str, str, float]]) -> Dict[str, Dict[str, float]]:
    result = {}
    for student_id, name, score in student_data:
        result[student_id] = {"name": name, "score": score}
    return result

# ตัวอย่างการใช้งาน
students = [
    ("123456", "Alice", 85.5),
    ("654321", "Bob", 92.0),
    ("112233", "Charlie", 78.0)
]

print(store_student_scores(students))

from typing import Set, Tuple

def set_operations(set1: Set[str], set2: Set[str]) -> Tuple[Set[str], Set[str]]:
    union_set = set1.union(set2)          # หรือ set1 | set2
    intersection_set = set1.intersection(set2)  # หรือ set1 & set2
    return union_set, intersection_set


# ตัวอย่างการใช้งาน
set1 = {'a', 'e', 'i', 'o', 'u'}
set2 = {'h', 'e', 'l', 'l', 'o'}

print(set_operations(set1, set2))


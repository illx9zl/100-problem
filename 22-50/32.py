from typing import List

def calculate_median(lst: List[int]) -> float:
    lst_sorted = sorted(lst)  # เรียงลิสต์
    n = len(lst_sorted)
    mid = n // 2
    
    if n % 2 == 1:  # ถ้าจำนวนสมาชิกเป็นคี่
        return float(lst_sorted[mid])
    else:  # ถ้าจำนวนสมาชิกเป็นคู่
        return (lst_sorted[mid - 1] + lst_sorted[mid]) / 2
        

# ตัวอย่างการใช้งาน
data = [8, 4, 7, 4, 6, 2, 10, 9, 3, 7, 1]
print("Median:", calculate_median(data))
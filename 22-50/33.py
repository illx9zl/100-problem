from typing import Dict, List, Tuple

def calculate_median(provinces: Dict[str, int]) -> List[Tuple[str, int]]:
    values = sorted(provinces.values())
    n = len(values)
    mid = n // 2
    
    # คำนวณมัธยฐาน
    if n % 2 == 1:  # จำนวนประเทศเป็นคี่
        median = values[mid]
    else:  # จำนวนประเทศเป็นคู่
        median = (values[mid - 1] + values[mid]) / 2
    
    # คืนประเทศที่จำนวนจังหวัดตรงกับ median
    return [(country, count) for country, count in provinces.items() if count == median]


# ตัวอย่างการใช้งาน
data = {'Thailand':76, 'Laos':17, 'Vietnam':58, 'Japan':47, 'China':23}
print(calculate_median(data))

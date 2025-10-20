from typing import Dict, List

def search_countries_by_letter(country_data: Dict[str, str], letter: str) -> List[str]:
    # แปลง letter ให้เป็นตัวพิมพ์เล็กเพื่อเปรียบเทียบแบบ case-insensitive
    letter = letter.lower()
    
    # เลือกชื่อประเทศที่ขึ้นต้นด้วย letter
    result = [name for name in country_data.values() if name.lower().startswith(letter)]
    
    # เรียงลำดับตามตัวอักษร
    return sorted(result)


# ตัวอย่างการใช้งาน
country_data = {
    "+1": "United States",
    "+44": "United Kingdom",
    "+91": "India",
    "+81": "Japan",
    "+49": "Germany",
    "+86": "China"
}
letter = "U"

print(search_countries_by_letter(country_data, letter))

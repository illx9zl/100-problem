def toggle_case(s: str) -> str:
    result = []
    for char in s:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)  # ไม่ใช่ตัวอักษร → คงเดิม
    return "".join(result)


# ตัวอย่างการใช้งาน
print(toggle_case("Hello World!"))   # hELLO wORLD!
    

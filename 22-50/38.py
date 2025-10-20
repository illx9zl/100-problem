def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        # จัดการกรณีหารด้วยศูนย์
        return None
    return a / b


# ตัวอย่างการใช้งาน
print("add(5, 3) =", add(5, 3))           # 8
print("subtract(5, 3) =", subtract(5, 3)) # 2
print("multiply(5, 3) =", multiply(5, 3)) # 15
print("divide(6, 3) =", divide(6, 3))     # 2.0
print("divide(6, 0) =", divide(6, 0))     # None

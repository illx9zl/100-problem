from typing import Tuple

def calculate_coins(amount: int) -> Tuple[int, int, int, int]:
    coins_10 = amount // 10
    amount %= 10
    
    coins_5 = amount // 5
    amount %= 5
    
    coins_2 = amount // 2
    amount %= 2
    
    coins_1 = amount  # ที่เหลือคือเหรียญ 1
    
    return coins_10, coins_5, coins_2, coins_1


# ตัวอย่างการใช้งาน
print(calculate_coins(28))  # (2, 1, 1, 1)


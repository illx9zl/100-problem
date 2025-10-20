from typing import List

def find_words_of_length(words: List[str], length: int) -> List[str]:
    return [word for word in words if len(word) == length]


# ตัวอย่างการใช้งาน
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
print(find_words_of_length(words, 5))  # ["apple", "grape"]


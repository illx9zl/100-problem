def remove_word(sentence: str, word_to_remove: str) -> str:
    words = sentence.split()  # แยกเป็นคำ
    filtered_words = [word for word in words if word != word_to_remove]
    return " ".join(filtered_words)
print(remove_word("Python is a popular programming language.", "popular"))


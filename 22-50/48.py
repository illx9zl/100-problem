def cumulative_sum(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer greater than 0")
    return n * (n + 1) // 2   # ใช้สูตรคณิตศาสตร์
print(cumulative_sum(5))   # 15


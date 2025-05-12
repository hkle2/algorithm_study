def solution(hp):
    a, hp = divmod(hp, 5)
    b, c = divmod(hp, 3)
    return a + b + c
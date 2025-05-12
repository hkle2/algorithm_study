# def solution(hp):
#     a, hp = divmod(hp, 5)
#     b, c = divmod(hp, 3)
#     return a + b + c

def solution(hp):
    return hp // 5 + (hp % 5) // 3 + (hp % 5) % 3
# def solution(a, b):
#     if (a + b) % 2 == 1:
#         return 2 * (a + b)
#     elif a % 2 == 1:
#         return a**2 + b**2
#     else:
#         return abs(a - b)

def solution(a, b):
    return 2 * (a + b) if (a + b) % 2 == 1 else (a**2 + b**2 if a % 2 == 1 else abs(a - b))
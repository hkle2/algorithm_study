# def solution(n):
#     i = 1
#     while True:
#         if 6 * i % n == 0:
#             return i
#         else:
#             i += 1

def solution(n):
    return next(i for i in range(1, n+1) if 6 * i % n == 0)
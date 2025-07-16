# def solution(n):
#     arr = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 arr[i][j] = 1
#     return arr

def solution(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
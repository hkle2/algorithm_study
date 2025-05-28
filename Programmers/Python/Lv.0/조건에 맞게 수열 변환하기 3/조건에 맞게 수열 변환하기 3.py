# def solution(arr, k):
#     if k % 2 != 0:
#         return [a * k for a in arr]
#     else:
#         return [a + k for a in arr]

def solution(arr, k):
    return [a * k for a in arr] if k % 2 != 0 else [a + k for a in arr]
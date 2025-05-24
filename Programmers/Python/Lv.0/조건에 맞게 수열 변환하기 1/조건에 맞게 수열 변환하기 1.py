# def solution(arr):
#     for i in range(len(arr)):
#         if arr[i] >= 50 and arr[i] % 2 == 0:
#             arr[i] /= 2
#         elif arr[i] < 50 and arr[i] % 2 != 0:
#             arr[i] *= 2
#     return arr

def solution(arr):
    for i, num in enumerate(arr):
        if num >= 50 and num % 2 == 0:
            arr[i] = num / 2
        elif num < 50 and num % 2 != 0:
            arr[i] = num * 2
    return arr
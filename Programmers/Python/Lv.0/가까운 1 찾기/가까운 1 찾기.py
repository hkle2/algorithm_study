# def solution(arr, idx):
#     return next((i for i in range(idx, len(arr)) if arr[i] == 1), -1)

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1
# def solution(num_list):
#     for i, num in enumerate(num_list):
#         if num < 0:
#             return i
#     return -1

def solution(num_list):
    return next((i for i, num in enumerate(num_list) if num < 0), -1)
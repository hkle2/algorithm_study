# def solution(num_list):
#     diff_num = num_list[-1] - num_list[-2]
#     if diff_num > 0:
#         num_list.append(diff_num)
#     else:
#         num_list.append(num_list[-1] * 2)
#     return num_list

def solution(num_list):
    diff_num = num_list[-1] - num_list[-2]
    num_list.append(diff_num if diff_num > 0 else num_list[-1] * 2)
    return num_list
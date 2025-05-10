# def solution(s1, s2):
#     return sum(1 for s in s1 if s in s2)

def solution(s1, s2):
    return len(set(s1).intersection(set(s2)))
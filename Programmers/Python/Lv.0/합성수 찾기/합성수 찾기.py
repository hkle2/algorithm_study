def solution(n):
    return sum(1 for i in range(2, n+1) if sum(1 for j in range(1, i+1) if i % j == 0) >= 3)
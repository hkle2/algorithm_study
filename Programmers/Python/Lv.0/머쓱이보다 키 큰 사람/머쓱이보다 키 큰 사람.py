def solution(array, height):
    return sum(num > height for num in array)
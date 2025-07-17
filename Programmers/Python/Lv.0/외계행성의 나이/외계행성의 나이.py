def solution(age):
    return "".join(chr(ord(num) + 49) for num in str(age))
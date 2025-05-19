def solution(strArr):
    for i, str in enumerate(strArr):
        if i % 2 != 0:
            strArr[i] = str.upper()
        else:
            strArr[i] = str.lower()
    return strArr
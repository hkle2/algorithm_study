# def solution(myString):
#     for c in myString:
#         if c < "l":
#             myString = myString.replace(c, "l")
#     return myString

def solution(myString):
    return "".join("l" if c < "l" else c for c in myString)
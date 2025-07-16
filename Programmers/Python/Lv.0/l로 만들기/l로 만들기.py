# def solution(myString):
#     for chr in myString:
#         if chr < "l":
#             myString = myString.replace(chr, "l")
#     return myString

def solution(myString):
    return "".join("l" if chr < "l" else chr for chr in myString)
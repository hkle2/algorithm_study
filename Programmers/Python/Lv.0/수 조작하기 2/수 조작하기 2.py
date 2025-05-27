def solution(numLog):
    num_dict = {1: "w", -1: "s", 10: "d", -10: "a"}
    return "".join(num_dict[numLog[i+1] - numLog[i]] for i in range(len(numLog)-1))
        
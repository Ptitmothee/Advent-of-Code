def getlines(path):
    doc = open(path, "r")
    return doc.read().strip().split("\n")

def list_StrToInt(L):
    n = len(L)
    Result = []
    for i in range(n):
        if type(L[i]) == list:
            Result.append(list_StrToInt(L[i]))
        else:
            Result.append(int(L[i]))
    return Result
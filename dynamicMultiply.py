def multiply(x, y):
    if x > y:
        ans = recursiveMultiply(x, y)
    else:
        ans = recursiveMultiply(y, x)

    print(ans)

def recursiveMultiply(x, y):
    divOrMinus = 0

    if(y == 1):
        ans = x
        return ans

    if(y % 2):
        ans = recursiveMultiply(x, y - 1)
    else:
        divOrMinus = 1
        ans = recursiveMultiply(x, y >> 1)

    if(divOrMinus):
        return ans << 1
    else:
        return ans + x

multiply(4, 5)
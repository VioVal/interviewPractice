def multiply(x, y):
    if x > y:
        ans = recursiveMultiply(x, x, y)
    else:
        ans = recursiveMultiply(y, y, x)

    print(ans)

def recursiveMultiply(base, x, y):
    if y == 1: 
        return x
    x += base
    y -= 1

    ans = recursiveMultiply(base, x, y)

    return ans

multiply(4, 5)
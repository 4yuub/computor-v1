def abs(n: int):
    return n if n >= 0 else -n

def pow(n: int, p: int):
    if p == 0:
        return 1
    res = pow(n, p // 2)
    res *= res
    if p % 2 == 1:
        res *= n
    return res

def round(n: float, precision: int):
    return int(n * pow(10, precision)) / pow(10, precision)

def sqrt(n: int):
    res = -1
    min = 0
    max = n / 2
    SMALL = 0.0000001
    while abs(min - max) > SMALL:        
        mid = (min + max) / 2

        if abs(mid * mid - n) < SMALL:
            res = mid
            break

        if mid * mid > n:
            max = mid - 1
        else:
            min = mid + 1
        res = max

    return round(res, 6)

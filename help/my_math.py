def abs(n: int):
    return n if n >= 0 else -n

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

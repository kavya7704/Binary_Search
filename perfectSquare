#perfectSquare gfg

def perfectSquarebinary(n):
    low = 1
    high = n 
    ans = 0
    while low <= high :

        mid = (low + high) // 2
        root = mid * mid
        if root <= n:
            ans = mid
            low = mid + 1
        elif root > n:
            high = mid - 1
    return ans

print(perfectSquarebinary(5))

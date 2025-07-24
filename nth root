#nth root gfg

def nth_root(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2
        power = mid ** n
        if power == m:
            return mid
        elif power > m:
            high = mid - 1
        else:
            low = mid + 1

    return -1 
print(nth_root(2,49))

def koko(arr,k):
    low = 1
    high = max(arr)

    while low <= high:
        div = (low + high)//2
        Time = 0
        for num in arr:
            Time += ceil(num/div)
        if Time <= k:
            high = div - 1
        else:
            low = div + 1
    return low
print(koko([3, 6, 7, 11] , k = 8))

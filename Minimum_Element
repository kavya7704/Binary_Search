#Find the minimum element in rototed sorted array

def Minimum(arr):
    low = 0
    high = len(arr) - 1
    Min = float("inf")
    while low <= high:
        mid = (high + low) // 2
        if arr[low] <= arr[mid]:
            if arr[low] < Min:
                Min = arr[low]
            high = mid - 1
        if arr[mid] <= arr[high]:
            if arr[mid] < Min:
                Min = arr[mid]
            low = mid + 1
    return Min
print(Minimum([9,8,7,1,2,3,4]))

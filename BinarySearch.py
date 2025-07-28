def binary_search(arr,k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
    return -1
print(binary_search([1,2,3,4,5,6],4))

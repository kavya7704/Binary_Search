#search an element in rotated sorted array with duplicates

def Rotated_Array_duplicate(arr,key):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        if arr[low] == arr[high] == arr[mid]:
            low += 1
            high -= 1
        elif arr[low] <= arr[mid]:
            if arr[low] <= key <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] <= arr[high]:
            if arr[mid] <= key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

print(Rotated_Array_duplicate([3,2,1,2,3,3,4],3))

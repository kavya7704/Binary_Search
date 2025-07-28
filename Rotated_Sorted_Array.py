#search an element in rotated sorted array
def Rotated_Array(arr,key):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
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

print(Rotated_Array([7,8,9,1,2,3,4,5,6],4))

#finding a unique element in sorted array where other elements repeats exactly twice
def unique(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    
    low = 1
    high = n - 2
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        #left half
        elif mid % 2 == 0 and nums[mid] == nums[mid + 1] or mid % 2 == 1 and nums[mid] == nums[mid - 1]:
            low = mid + 1
        #right half
        elif mid % 2 == 0 and nums[mid] == nums[mid - 1] or mid % 2 == 1 and nums[mid] == nums[mid + 1]:
            high = mid - 1
            
    return -1

print(unique([1,1,2,2,3,3,4,5,5]))

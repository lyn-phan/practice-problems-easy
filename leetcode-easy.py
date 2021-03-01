
### Remove Duplicates from Sorted Array ###

### Test Cases ###
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]


def removeDuplicates(nums):
    #remove duplicates in place
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    
    count = 0
    for i, num in enumerate(nums):
        if num not in nums[i-1:1]:
            return nums[i-1:1]

    #return length, sorted list

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

""" Remove Duplicates from Sorted Array """

### Test Cases ###
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]

# def removeDuplicates(nums):
#     #remove duplicates in place
#     if len(nums) == 0 or len(nums) == 1:
#         return len(nums)
    
#     count = 0
#     for i, num in enumerate(nums):
#         if num not in nums[i-1:1]:
#             return nums[i-1:1]

#     #return length, sorted list

# nums = [0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicates(nums))


"""given a two digit integer, add them together """
# def addTwoDigits(n):
#     digits = [int(digit) for digit in str(n)]
#     return digits[0] + digits[1]

# print(addTwoDigits(n = 29))


""" Given an integer n, return the largest number that contains exactly n digits."""
# For n = 2, the output should be
# largestNumber(n) = 99.

# def largestNumber(n):
#     return (10**n) - 1
# ###initialize num to capture answer
# # initialize counter

# print(largestNumber(n=3))

"""n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split."""

# def candies(n, m):
#     ###if n = 3 (children)
#     ### m = 10 candies
#     ## each child gets 3, answer is 9
    
#     candies_per_child = m % n
#     return m - candies_per_child


# print(candies(n = 3, m = 10))
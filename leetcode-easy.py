
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

""" given a theatre with nCols, and nRows. And given your seat at col, row - find the area
behind your seat, assuming all seats are taken """
# For nCols = 16, nRows = 11, col = 5, and row = 3, the output should be
# seatsInTheater(nCols, nRows, col, row) = 96.

#by hand:
# nCols - (col -1) * nRows - row
# def seatsInTheater(nCols, nRows, col, row):
#     area = (nCols - (col-1)) * (nRows - row)

#     return area

# print(seatsInTheater(nCols = 16, nRows = 11, col = 5, row = 3))

"""Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0."""

# def maxMultiple(divisor, bound):
#     return bound - (bound % divisor)

# print(maxMultiple(divisor = 3, bound = 10))

# def fizzBuzz(n):
#     for i in range(n + 1):
#         if (i % 3 == 0) and (i % 5 == 0):
#             print("FizzBuzz")
#         elif (i % 3 == 0) and (i % 5 != 0):
#             print("Fizz")
#         elif (i % 3 != 0) and (i % 5 == 0):
#             print("Buzz")
#         else:
#            if i % 3 != 0 or i % 5 != 0:
#                print(i)

# print(fizzBuzz(n = 15))

""" design a game of black jack """

# Is this for one player vs the computer? 
# Will I need to design for multiple games or just one game?
# can I use random module?

# score = 0 # track score

# create functions to:
# - greet a player
# - deal a card
# - hit or stop
# - play game

""" Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber. """

# def circleOfNumbers(n, firstNumber):

# #     # take n - 1 and assign list from 0 to n - 1
# #     # lst = [x for x in range(0, n)]
     
# #     # length = len(lst)
# #     # diff = length // 2

# #     # result = firstNumber + diff
# #     # return result
#     return (firstNumber + n/2)%n
# #     7 + 10/2 = 12 % 10
# #     2 + 10/2 = 7 % 10
# #     5 + 18/2 = 14 % 10

# # print(circleOfNumbers(10, 7))
# print(circleOfNumbers(10, 2))
# print(circleOfNumbers(18, 5))
# # print(12%10)
# # print(7%10)
# # print(14%10)

# def lateRide(n):
#     hours = n//60 
#     minutes = n % 60

#     time_format = list(f"{hours}{minutes}")
    
#     total = 0
#     for i in range(0, len(time_format)):
#         total += int(time_format[i])
    
#     return total


# print(lateRide(808))


# def phoneCall(min1, min2_10, min11, s):
#     if s < min1:
#         return 0
#     # for i in range(2, 11):
#     #     if s < min1 + min2_10 * (i - 1):
#     #         return i - 1
#     return (s - min1 - min2_10 * 9.0) // min11 + 10

# print(phoneCall(min1 = 2, min2_10 = 2, min11 = 1, s = 24))


    # minutes = 0

    # first = s - min1 #22
    # minutes += first #22

    # second_ten = min2_10 * 9 # 18
    # minutes = minutes - second_ten #4

    # eleven_onward = minutes//min11 #4

    # return 1 + second_ten + eleven_onward


# def firstNotRepeatingCharacter(s):
#     tuple_counter = ()

#     for char in s:
#         if char not in tuple_counter:
#             tuple_counter[0] = char
#             tuple_counter[0, 1] = 1
#     return tuple_counter


# print(firstNotRepeatingCharacter("ababac"))


# def firstUniqChar(s):
#     char_count = {}

#     for i in s:
#         char_count[i] = char_count.get(i, 0) + 1
    
#     return next((i for i in s if char_count[i] == 1), '__')


# print(firstUniqChar("leetcode"))

""" return first duplicate number for which the 2nd occurence has the minimal index""" 
# def firstDuplicate(a):
#     seen = set()

#     for i in a:
#         if i in seen:
#             return i
#         seen.add(i)
#     return -1

# print(firstDuplicate(a = [2, 1, 3, 5, 3, 2]))
# 3

# def rotateImage(a):
#     # return list(zip(*a[::-1]))

#     # return list(zip(*a[::-1]))
#     a.reverse()
#     for r in range(len(a)):
#         for c in range(r):
#             a[r][c], a[c][r] = a[c][r], a[r][c]
#     return a

# print(rotateImage(a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]))

# expected = rotateImage(a) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]

def reverseStr(a):
    return a.sort()

print(reverseStr(a = [12, 32, 43, 24, 15])
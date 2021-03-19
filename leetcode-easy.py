
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

"""truncate char in a string"""
#create a var for current and for result
# iterate through a
# if i != current,
# add to result, update current
# resturn result

# def truncateChar(a):
#     current = ''
#     result = ''

#     for i in a:
#         if i != current:
#             result += i
#             current = i
    
#     return result


# print(truncateChar(a="aaabaaabbbe"))

""" reverse digits """

# def reverse_digits(n):
#     # rev = reversed(str(n))
#     # return ''.join(rev)

#     convert_to_str = str(n)
#     rev = convert_to_str[::-1]
#     return rev

# print(reverse_digits(n = 182))

""" group anagrams """
# Group anagrams. Write a function that takes in a list of words and prints each word, 
# with anagrams grouped together. Order doesn’t matter. 

#initialize a dictionary
# iterate through words
# sort the words by characters
# if sorted word in anagrams dict, add word as value
# if not, add it as a key

#iterate through the values
#iterate through each word and print that word

# def group_anagrams(words):
#     anagrams = {}

#     for word in words:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagrams:
#             anagrams[sorted_word].append(word)
#         else:
#             anagrams[sorted_word] = [word]
    
#     for words in anagrams.values():
#         for word in words:
#             print(word)

# print(group_anagrams(words=["cat", "bat", "act", "moon"]))

""" reverse a list in place without using built in functions """

# def rev_list_in_place(lst):
#     for i in range(len(lst) // 2): #splits the list in half
#         lst[i], lst[-i -1] = lst[-i -1], lst[i]  #tuple unpacking, swaps the first with the last, second with second to last
#         print(lst[i])
#         print(lst[-i])
#         print(lst[-i -1])
    
#     return lst

# print(rev_list_in_place(lst = [12, 15, 21, 18, 2]))

"""Max depth binary tree"""

# def maxDepth(root):
#     return maxDepthHelper(root, 1)

# def maxDepthHelper(node, depth):
#     if node.children == 0:
#         return depth
    
#     if node == None:
#         return 0
    
#     leftDepth = maxDepthHelper(node.left, depth+1)
#     rightDepth = maxDepthHelper(node.right, depth+1)

#     return max(leftDepth, rightDepth)

# print(maxDepth(root = [3,9,20,None,None,15,7]))


""" version number comparison """

# The goal of this question is to write a function, in a language of
# your choice, that will compare two version number strings. Version
# number strings are strings like "1.2.3" or "2.12.4". They are strings
# of digits separated by periods. You may assume that the strings do
# not contain any other characters.
#
# The comparison function will take 2 such strings as inputs, and
# return an integer as the result. If the input strings are "a" and
# "b", the function should return:
#
# 1, if a > b
# 0, if a == b
# -1, if a < b
#
# The comparison needs to be based on the version numbers. This
# comparison is defined by considering each component integer of the
# strings pairwise. Here are some examples:
#
# 2.12 > 2.2 (because 12 > 2)
# 1.2.3 == 1.2.3
# 1.2.0 == 1.2
# 1.2.0.0 == 1.2
# 1.2.0.0.0.0 == 1.2.0.0
# 1.2.0.1 > 1.2.0.0
# 1.2.10 < 1.2.12
# 1.3.2 > 1.2.3
# 1.2 < 1.2.0.1

#split strings by "."
# loop through the longer string
# convert to int
# convert to list to iterate
# compare each set of numbers one at a time
# if a > b, return 1
# if a == b, return 0
# else, if a < b return -1

#edge cases:
#if a is too long for b, set remaining of b to zero
# if b is too long for a, set remaining of a to zero

# def versionNum(a, b):
#     split_a = a.split(".")
#     split_b = b.split(".")

#     lst_a = list(split_a)
#     lst_b = list(split_b)

#     for i in range(max(len(lst_a), len(lst_b))):
#         if i >= len(lst_b): #if i is too big for lst_b
#             int_b = 0
#         else:
#             int_b = int(lst_b[i])

#         if i >= len(lst_a): #if i is too big for lst_a
#             int_a = 0
#         else:
#             int_a = int(lst_a[i])
        
#         if int_a > int_b:
#             return 1
#         elif int_a == int_b:
#             continue
#         elif int_a < int_b:
#             return -1
    
#     return 0


# print(versionNum(a = "1.2", b = "1.2"))


"""print out the word version of a number
input = 123
output = one hundred and twenty three """

# depending on the length of the number
# if len = 4, 1204
# " one thousand + two hundred + and four"
#if len = 5, 12456, 20345,
#twelve thousand + four hundred + fifty + six
# if len = 3, 345
# "three hundred forty five"
#if len = 2, 36
#thirty + six

#start with a dictionary

# convert to str and split the number
#if len(num) is 5,
# take first two numbers and look up in teens and tens and single_nums, return value + 3rd number is from single_nums + "hundred" , look up 
# tens + single_nums



    # ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
    # 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 
    # 18: "eighteen", 19: "nineteen"}
    # # tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    #                     tens = 0 / tens = 1 / tens = 2
onetoOneHundred = {0: ('Zero', 'Ten', 'Hundred'),
                    1: ('One', 'Eleven'),
                    2: ('Two', 'Twelve', 'Twenty'),
                    3: ('Three', 'thirteen', 'Thirty'),
                    4: ('Four', 'Fourteen', 'Forty'),
                    5: ('Five', 'Fifteen', 'Fifty'),
                    6: ('Six', 'Sixteen', 'Sixty'),
                    7: ('Seven', 'Seventeen', 'Seventy'),
                    8: ('Eight', 'Eighteen', 'Eighty'),
                    9: ('Nine', 'Nineteen', 'Ninety')}
    
def two_digit(str_num):
    if len(str_num) == 1:
        ones = int(str_num[0])
        tens = 0
    else:
        tens = int(str_num[0]) #[tens] = loop up by 0, return value
        ones = int(str_num[1]) # look at 2nd #, then loop up corresponding value by index
    
    if tens == 0 or tens == 1:   # if in the teens, <20
        return onetoOneHundred[ones][1]
    else: # 20 or greater
        word = onetoOneHundred[tens][2]
        word += ' ' + onetoOneHundred[ones][0]
        return word

def three_digit(str_num):
    hundreds = int(str_num[0]) #854, 8 = hundreds

    if hundreds == 0:
        return two_digit(str_num[-2:])
    
    tens_ones = str_num[1:]
    
    word = onetoOneHundred[hundreds][0] + ' ' + "hundred"
    if tens_ones != '00':
        word += ' ' + two_digit(tens_ones)
    
    return word


print(three_digit(str_num = '100'))


# def three_digit(str_num): 
#     hundreds = int(str_num[0])
#     if hundreds == 0:
#         return two_digit((str_num[-2:]))
#     tens_ones = str_num[1:]
#     word = onetoOneHundred[hundreds][0] + ' ' + 'Hundred'
#     if tens_ones != '00':
#         word += ' ' + two_digit(tens_ones)
#     return word
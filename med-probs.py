""" take in two arrays, where you take in several numbers from array B and add them to array A. Find
    the maximum length of the resulting arithmetic progression for array A """


# def max_arithmetic_seq(a, b):

#     differences = set()

# # First, find the difference between each element in list A and store it in a set, assign it to a variable
#     for i in range(len(a) - 1):
#         differences.add(a[i + 1] - a[i])
#     # Grab the smallest difference by finding min(set) and set to variable pattern (pattern is 4 rn)
#     arith_prog_num = min(differences)

#     # go back to A and check if number + pattern is in A or if in B
#     # if in a A continue
#     # if number + pattern is not in A AND is in B, insert (a + 1, num + pattern)
#     for j, num in enumerate(a):

#         print(len(a)-1)
#         if (num + arith_prog_num) in a:
#             continue
#         elif (num + arith_prog_num) not in a and (num + arith_prog_num) in b:
#             a.insert(j+1, (num + arith_prog_num))
#         else:
#                 # else, if we get to the end of the list and there aren't any matches in arith_exp_num, return -1
#             if j != len(a) - 1:
#                 return -1

#     # return len (a)
#     return len(a)
 
# print(max_arithmetic_seq(a = [0, 4, 8, 16], b = [0, 2, 6, 12, 14, 20]))
# print(max_arithmetic_seq(a = [5, 7, 13, 14], b = [9, 11, 15]))


##############################################################
"""Given a square matrix of positive integers, sort the number in each of its diagonals parallel to the secondary diagonal.
Each diagonal should contain the same set of numbers as before but sorted in ascending order from the bottom-left to top-right"""

#     def secondary_diagonal(matrix):

#     #R   0  1  2  3  --> C 
#     #0  [1, 3, 9, 4]
#     #1  [9, 5, 7, 7]
#     #2  [3, 6, 9, 7]
#     #3  [1, 2, 2, 2]


#     #R   0  1  2  3  --> C 
#     #0  [1, 9, 9, 7]
#     #1  [3, 5, 6, 9]
#     #2  [3, 4, 7, 7]
#     #3  [1, 2, 2, 2]


#     # keeping of yur diagonal starung point
#     # get digaonal numbers 
#     # sort the numbers -- [1]
#     # put back in the diagonal 



#     def get_next_diag_point(coordinates, max_row, max_column):
#         # if i can go down do that
#         if coordinates[0] < max_row:
#             return (coordinates[0] + 1, coordinates[1])
#         # elif if can go right do that
#         if coordinates[1] < max_column:
#             return(coordinates[0], coordinates[1] + 1)
#         # else return none
#         else:
#             return (None, None)

#     def sort_diag(matrix, diag_coordinates, max_row, max_column):

#         current_row = diag_coordinates[0]
#         current_column = diag_coordinates[1]

#         diag_values = []

#         while 0 <= current_row <= max_row and 0 <= current_column <= max_row:
#             diag_values.append(matrix[current_row][current_column])
#             current_row -= 1
#             current_column += 1

#         current_row = diag_coordinates[0]
#         current_column = diag_coordinates[1]

#         while 0 <= current_row <= max_row and 0 <= current_column <= max_row:
#             diag_values = sorted(diag_values)
#             matrix[current_row][current_column] = diag_values.pop(0)
#             current_row -= 1
#             current_column += 1

#         diag_coordinates = get_next_diag_point(
#             diag_coordinates, max_row, max_column)

#         if diag_coordinates[0] != None:
#             return sort_diag(matrix, diag_coordinates, max_row, max_column)

#     sort_diag(matrix, (0, 0), len(matrix) - 1, len(matrix[0]) - 1)

#     return matrix

##############################################################

""" Task: group arrays by their means in ascending order """

# For
# a = [[3, 3, 4, 2], #mean = 3
#      [4, 4], # mean = 4
#      [4, 0, 3, 3], #mean = 2.5
#      [2, 3], #mean = 2.5
#      [3, 3, 3]] #mean = 3

# output = [[0, 4],
#           [1],
#           [2, 3]]

# constraints: return array of arrays, grouped together where indices are grouped in ascending order and
#  groups are in ascending order

# By hand
# initialize an empty dictionary called, averages 
# loop through enumerate array A, take average of each mini-array and assign averages by key, and 
# index by value

#loop through dictionary:
#(k,v) for k, v in dict.items()

#initialize output list:
#append values
# sort list by values in ascending order

# def meanGroups(a):
#     averages = {}

#     for index, value in enumerate(a):
#         avg = sum(value) / len(value)
#         averages.setdefault(avg, []).append(index)

#     return sorted(list(averages.values()))

# print(meanGroups(a = [[3, 3, 4, 2], [4, 4], [4, 0, 3, 3], [2, 3], [3, 3, 3]] ))

""" arrange the words hacker rank"""

# def arrange(sentence):
#     word_counts = {}
#     len_of_word = 0
#     sentence_list = []

#     for i in sentence.split():
#         count = len(i)
#         len_of_word += count
#         word_counts[i] = count
#         sorted_dict = sorted(word_counts.items(), key=lambda x:x[1])
    
#     for i in sorted_dict:
#         sentence_list.append(i[0])
#         return ''.join(str(sentence_list))

# print(arrange("I love to code"))


# def braces(values):
#     open_list = ("(", "[", "{")
#     closed_list = (")", "]", "}")
    
#     balanced = {open_list[0]:closed_list[0],
#     open_list[1]:closed_list[1],
#     open_list[2]:closed_list[2]}
    
#     stack = []
    
#     for i in values:
#         if stack:
#             if i in open_list:
#                 stack.append(i)
#             elif i in closed_list:
#                 index = closed_list.index[i]
#                 if len(stack) > 0 and stack[-1] == open_list[index]:
#                     stack.pop()
#         elif not stack:
#             return "No"
#         return "Yes" 


# print(braces(['[{}]', '[]']))

# def brackets(expression):
#    all_br = ['()', '{}', '[]']
#    while any(x in expression for x in all_br):
#       for br in all_br:
#          expression = expression.replace(br, '')
#    return not expression

# # calling the function
# input_string = "([]{}()"
# if brackets(input_string):
#    print(input_string,"balanced")
# else:
#    print(input_string,"Not balanced")

# brackets = {
#   '(': ')',
#   '{': '}',
#   '[': ']'
# }

# On each input string, process it using the balance checker
# def balancedBrackets(string):
#   stack = []
#   # Process every character on input
#   for char in string:
#     # Assign an initial value in case the stack is empty
#     last = 0
#     # Assign the value of the last element if stack is not empty
#     if stack:
#       last = stack[len(stack) - 1]
#     if stack and last in brackets and brackets[last] == char:
#       stack.pop()
#     else:
#       stack.append(char)

#   return not stack

# print(balancedBrackets(('[{}]', '[]')))

# """return a spiral matrix """ 
# def spiralOrder(matrix):
#     r = len(matrix) #length is rows
#     col = len(matrix[0]) #length in columns
#     output = []

#     # Boundaries:
#     top_row = 0
#     right_column =  col - 1   
#     bottom_row = r - 1    
#     left_column = 0

#     seen = set()

#     while top_row <= bottom_row and left_column <= right_column:
        
#         #traverse right
#         i = top_row
#         for j in range(col):
#             if (i, j) not in seen:
#                 seen.add((i, j))
#                 output.append(matrix[i][j])
        
#         #traverse down
#         j = right_column
#         for i in range(r):
#             if (i, j) not in seen:
#                 seen.add((i, j))
#                 output.append(matrix[i][j])
        
#         #traverse left
#         i = bottom_row
#         for j in range(col-1, -1, -1):
#             if (i, j) not in seen:
#                 seen.add((i, j))
#                 output.append(matrix[i][j])

#         #traverse up
#         j = left_column
#         for i in range(r-1, -1, -1):
#             if (i, j) not in seen:
#                 seen.add((i, j))
#                 output.append(matrix[i][j])

#         top_row += 1
#         bottom_row -= 1
#         left_column += 1
#         right_column -= 1

#     return output      
        
# print(spiralOrder(matrix = ([1,2,3], [4,5,6], [7,8,9]))) 

# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]

# matrix[0][1]

    # ** update boundaries
    # ** update current operation
    # ** when working with the row, range is column and vice versa
        # if current_operation == left_to_right:

            # printLeftToRight(matrix, top_row, right_column, left_column)
            # top_row += 1
            # current_operation = top_to_bottom
        # elif current_operation == top_to_bottom:
        #     printTopToBottom(matrix, right_column, top_row, bottom_row)
        #     right_column = right_column - 1
        #     current_operation = right_to_left
        # elif current_operation == right_to_left:
        #     printRightToLeft(matrix, bottom_row, right_column, left_column)
        #     bottom_row = bottom_row - 1
        #     current_operation = bottom_to_top
        # elif current_operation == bottom_to_top:
        #     printBottomTop(matrix, left_column, bottom_row, top_row)
        #     left_column += 1
        #     current_operation = left_to_right

    # return

# def printLeftToRight(matrix, top_unprinted_row, right_most_unprinted_column, left_most_unprinted_column):
#     """print the top row of matrix"""

#     for i in range(len(matrix)):
#         """return the first index of left_most and first index of right_most and everything in between top"""
#         return i



# print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))


# Input: matrix = 
# [[1,2,3]
# [4,5,6],
# [7,8,9]]
# Matrix[0] -> [1,2,3]
# Matrix[0][0] -> 1
# Matrix[0][1] -> 2
# Ideas:
# 4 types of operations: left->right, top->bottom, right->left, bottom->top
# Do those operations in sequence, and start over if we still have more things to print
# Need to keep track of “boundaries”: top unprinted row, right-most unprinted column, bottom unprinted row, left-most unprinted column
# Once we finish an operation (eg. left->right), need to update the boundary
# Output: [1,2,3,6,9,8,7,4,5]

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
# onetoOneHundred = {0: ('Zero', 'Ten', 'Hundred'),
#                     1: ('One', 'Eleven'),
#                     2: ('Two', 'Twelve', 'Twenty'),
#                     3: ('Three', 'thirteen', 'Thirty'),
#                     4: ('Four', 'Fourteen', 'Forty'),
#                     5: ('Five', 'Fifteen', 'Fifty'),
#                     6: ('Six', 'Sixteen', 'Sixty'),
#                     7: ('Seven', 'Seventeen', 'Seventy'),
#                     8: ('Eight', 'Eighteen', 'Eighty'),
#                     9: ('Nine', 'Nineteen', 'Ninety')}
    
# def two_digit(str_num):
#     if len(str_num) == 1:
#         ones = int(str_num[0])
#         tens = 0
#     else:
#         tens = int(str_num[0]) #[tens] = loop up by 0, return value
#         ones = int(str_num[1]) # look at 2nd #, then loop up corresponding value by index
    
#     if tens == 0 or tens == 1:   # if in the teens, <20
#         return onetoOneHundred[ones][1]
#     else: # 20 or greater
#         word = onetoOneHundred[tens][2]
#         word += ' ' + onetoOneHundred[ones][0]
#         return word

# def three_digit(str_num):
#     hundreds = int(str_num[0]) #854, 8 = hundreds

#     if hundreds == 0:
#         return two_digit(str_num[-2:])
    
#     tens_ones = str_num[1:]
    
#     word = onetoOneHundred[hundreds][0] + ' ' + "hundred"
#     if tens_ones != '00':
#         word += ' ' + two_digit(tens_ones)
    
#     return word


# print(three_digit(str_num = '100'))

# '''' house robber'''

# def houseRobber(nums):
#     n = len(nums)
#     if n==0:
#         return 0;
#     if n == 1:
#         return nums[0]
#     s = [0]*(n+1)
#     s[1] = nums[0]
#     s[2] = nums[1]
        
#     for i in range(3,n+1):
#         s[i] = (max(s[i-2],s[i-3]) + nums[i-1])
#     return max(s[n],s[n-1])

# print(houseRobber(nums=[2,5,7,3]))

#go through each house and decide a) steal from this house and skipping the next or b) skipping the next house

# def houseRobber(nums):
#     length = len(nums)
#     if length == 0:
#         return 0
#     if length == 1:
#         return nums[0]
    
#     return max(nums)

"""product of array except self""" 
"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]."""

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

#create a list to track output
#output [0] = nums[1]*[2]*[3]
# output [1] = nums[0]*[2]*[3]
#output[2] = nums[0]*[1]*[3]
# initialize product to 1
# iterate right
# iterate left
# take in left and right and multiply them, add to results


# def productExceptSelf(nums):
#     results = []
#     length = len(nums)
#     right = []
#     left = []

#     multiplier = 1
#     for i in range(0, length): # going right
#         right.append(multiplier)
#         multiplier = multiplier * nums[i]
#     # return right [1,3,12,60,360]
    
#     multiplier = 1
#     for i in range(len(nums)-1, -1, -1): # going left
#         left.append(multiplier)
#         multiplier = multiplier * nums[i]  
#     left.reverse() ## [840, 210, 42, 7, 1]

#     results = [left * right for left, right in zip(left, right)]
#     return results


# print(productExceptSelf(nums=[3,4,5,6,7]))
# print(productExceptSelf(nums=[1,2,3,4]))

""" 3sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""

#initialize length
# track min_diff
# set target to 0
# loop through each list, assign i, j, k and add them, assign to current_sum
# if current_sum < min_diff, current_sum = min_dff
def threeSums(nums):
    length = len(nums)
    target = 0
    # min_diff = abs(nums[0]+nums[1]+nums[2])

    for i in range(0, length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                diff = (nums[i] + nums[j] + nums[k])
                if diff == target:
                    
                    return nums[i], nums[j], nums[k]



print(threeSums(nums= [-1,0,1,2,-1,-4]))
#output = [[-1,-1,2],[-1,0,1]]
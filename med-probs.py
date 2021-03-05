
# def max_arithmetic_seq(a, b):
#     """ take in two arrays, where you take in several numbers from array B and add them to array A. Find
#     the maximum length of the resulting arithmetic progression for array A """

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

#     def secondary_diagonal(matrix):
#     """Given a square matrix of positive integers, sort thr number in each of its diagonals parallel to the secondary diagonal.
#     Each diagonal should contain the same set of numbers as before but sorted in ascending order from the bottom-left to top-right"""

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

# Task: group arrays by their means in ascending order 

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
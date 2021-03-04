# # You are given two arrays of integers a and b, which are both sorted in an ascending order and contain unique elements (i.e. no duplicates).
# # You can take several (possibly zero) numbers from the array b and add them to a at any positions in any order. You want the array ato be an arithmetic progression after this.
# # Your task is to find the maximal length of the resulting arithmetic progression represented by array a that can be achieved. If it is impossible to obtain an array forming an arithmetic progression, return -1.
# # Example
# # For a = [0, 4, 8, 16] and b = [0, 2, 6, 12, 14, 20], the output should be maxArithmeticLength(a, b) = 6.
# # You can add b[3] = 12 and b[5] = 20 to a and obtain array [0, 4, 8, 12, 16, 20], which is an arithmetic progression of length 6 (the sequence increases by 4 from each element to the next). It is impossible to obtain a longer arithmetic progression, so the answer is 6.
# # For a = [5, 7, 13, 14] and b = [9, 11, 15], the output should be maxArithmeticLength(a, b) = -1.
# # It is impossible to obtain an arithmetic progression with these elements, so the answer is -1.
# # a = [2, 4, 8], b = [1, 6, 10, 12] -> a = [2, 4, 6, 8, 10, 12] -> return 6

def max_arithmetic_seq(a, b):
    """ take in two arrays, where you take in several numbers from array B and add them to array A. Find
    the maximum length of the resulting arithmetic progression for array A """

    differences = set()
    
# First, find the difference between each element in list A and store it in a set, assign it to a variable
    for i in range(len(a) - 1):
        differences.add(a[i + 1] - a[i])
    # Grab the smallest difference by finding min(set) and set to variable pattern (pattern is 4 rn)
    arith_exp_num = min(differences)

    # go back to A and check if number + pattern is in A or if in B
    # if in a A continue
    # if number + pattern is not in A AND is in B, insert (a + 1, num + pattern)
    for j, num in enumerate(a):

        print(len(a)-1)
        if (num + arith_exp_num) in a:
            continue
        elif (num + arith_exp_num) not in a and (num + arith_exp_num) in b:
            a.insert(j+1, (num + arith_exp_num))
        else:
                # else, if we get to the end of the list and there aren't any matches in arith_exp_num, return -1
            if j != len(a) - 1:
                return -1

    # return len (a)
    return len(a)
 
print(max_arithmetic_seq(a = [0, 4, 8, 16], b = [0, 2, 6, 12, 14, 20]))
print(max_arithmetic_seq(a = [5, 7, 13, 14], b = [9, 11, 15]))







# def max_arithmetic_seq(a, b):
#     """
# max_arithmetic_seq([2,4,8], [1,6,10,12])
#     6
#     [2,4,6,8,10,12]
#     >>> max_arithmetic_seq([5,7,13,14], [9,11,15])
#     -1
#     >>> max_arithmetic_seq([0, 4, 8, 16], [2, 6, 12, 14, 20])
#     6
#     [0, 4, 8, 12, 16, 20]
#     """

#     # a = [2, 4, 6, 8, 10, 12]  ---> 6
#     # b = [1,6,10,12]

#     # difference = 2
#     #
#     #   a = [5,7,13,14]
#     #   b = [9,11,15]  -- done it impossoble return -1
#     # difference = 1

#     #  a = [0, 4, 8, 12, 16, 20]
#     # b = [2, 6, 12, 14, 20]
#     # difference = 4, 4, 8

#     # go through and put into a set the difference between number and following num
#     # find the smallest difference and set it to the pattern
#     # start from front of a and check if number + patter is next in a or if in b
#     # keep going

#     b = set(b)
#     differences = set()

#     for i in range(len(a) - 1):
#         differences.add(a[i+1] - a[i])

#     pattern = min(differences)
#     for i, num in enumerate(a):
#         if num + pattern in a:
#             continue
#         elif (num + pattern not in a) and (num + pattern in b):
#             a.insert(i+1, num + pattern)
#         else:
#             if i != len(a) - 1:
#                 return - 1

#     return len(a)

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
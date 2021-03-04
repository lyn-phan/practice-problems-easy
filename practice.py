# def boundedRatio(a, l, r):
#     # initialize empty boolean list
#     # iterate through list, a
#     # apply a[i] = (i + 1)
#     # does a[0] / (i+ 1) = x # solve for x
#     # is l <= x, and is x <= r
#     #  if yes, append "True"
#     #  else, append False
    
#     output = []
    
#     for i in range(len(a)):
#         # a[i] = (i + 1) 
#         x = a[i] / (i + 1)
#         if l <= x <= r:
#             output.append(True)
#         else:
#             output.append(False)
#     return output


# print(boundedRatio(a = [8,5,6,16,5], l=1, r=3))


# def countTinyPairs(a, b, k):
#     tiny_list_count = 0
#     concat_list = []

#     for i, j in zip(a, b):
#         str_i = str(i)
#         str_j = str(j)
#         concat = str_i + str_j
#         convert_to_int = int(concat)
#         concat_list.append(convert_to_int)

#     for x in concat_list:
#         if x < k:
#             tiny_list_count += 1
#     return tiny_list_count

# print(countTinyPairs(a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], k = 743))
  


def average_arrays(a):
    #initialize output list (will contain list of lists)
    #initialize list of means
    #iterate through each mini list, take the average of each mini list and add it to list of averages
    #if mean of list is the same, group those indices together
    #sort through list in ascending order
    #add indices with lowest element to output list
    #return output list

    output_list = []
    list_of_averages = []

    
    for i, j in enumerate(a):
        avg = sum(a[i])/len(a[i])
        list_of_averages.append(avg)
        for x in list_of_averages:
            print(x)
            
print(average_arrays(a = [[3, 3, 4, 2], [4, 4], [4, 0, 3, 3], [2, 3], [3, 3, 3]]))

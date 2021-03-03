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


def countTinyPairs(a, b, k):
    tiny_list_count = 0
    concat_list = []

    for i, j in zip(a, b):
        str_i = str(i)
        str_j = str(j)
        concat = str_i + str_j
        convert_to_int = int(concat)
        concat_list.append(convert_to_int)

    for x in concat_list:
        if x < k:
            tiny_list_count += 1
    return tiny_list_count

print(countTinyPairs(a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], k = 743))
  




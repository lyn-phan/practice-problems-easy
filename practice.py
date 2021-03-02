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
    # initialize tiny_list_count = 0
    tiny_list_count = 0
    list_of_concat = []

    # iterate through a normally
    for i in a:
        for j in b[::-1]:
            # result = str(a[i] + b[j])
            # print(result)
            # print(type(result))
            str_i = str(i)
            str_j = str(j)
            concat = str_i + str_j
            convert_to_int = int(concat)
            list_of_concat.append(convert_to_int)
            print(list_of_concat)

    # for x in list_of_concat:
    #     if x < k:
    #         tiny_list_count += 1
    # return tiny_list_count

print(countTinyPairs(a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], k = 743))
    
    # iterate through b by -1
    #concatenate each pair
    #check if pair is < k
    # if less than k, increment count
    # return list count


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
  


# def average_arrays(a):
#     #initialize output list (will contain list of lists)
#     #initialize list of means
#     #iterate through each mini list, take the average of each mini list and add it to list of averages
#     # add new loop, initialized lst_item = []
#     # loop through list, and add index of i and values to lst_item list
#     # sort through list item again that is sorted
#     # return just the index

#     output = []
#     lst_item = []
#     list_of_averages = []
    
#     for i, j in enumerate(a):
#         avg = sum(a[i]) / len(a[i])
#         list_of_averages.append(avg)
    
#     for i in range(len(list_of_averages)):
#         lst_item.append([list_of_averages[i], i])
#         lst_item.sort()
    
#     for x in lst_item:
#         output.append(x[1])
    
#     return output  
            
            
# print(average_arrays(a = [[3, 3, 4, 2], [4, 4], [4, 0, 3, 3], [2, 3], [3, 3, 3]]))
#list_of_averages = 3, 4, 2.5, 2.5, 3
# what we want in output = [2, 3, 0, 4, 1]





    # for i, j in enumerate(a):
    #     avg = sum(a[i])/len(a[i])
    #     list_of_averages.append(avg)
    #     # list_of_averages.sort()
        
    # for i in range(len(list_of_averages)):
    #     lst_item.append([list_of_averages[i], i])
    #     lst_item.sort()
    
    # for x in lst_item:
    #     output.append(x[1])
    #     print(x)
    #     print(lst_item) 


#sort both arr and pieces
# iterate through pieces.
#is pieces[0] == arr == 0? if yes cont
# if no return false
# def shuffleThePieces(arr, pieces):

#     arr.sort()
#     pieces.sort()
#     test_list = []

#     for i in range(0, len(pieces)-1):
#         if pieces[i] == arr[i]:
#             test_list.append(pieces[i])
    
#     if test_list == arr:
#         return True
#     return False



# print(shuffleThePieces(arr = [1, 2, 3, 5, 6], pieces = [[5], [1,2], [6,3]]))


    # arr.sort()
    # pieces.sort()
    # test_list = []

    # for i in range(0, len(pieces)-1):
    #     if pieces[i] == arr[i]:
    #         test_list.append(pieces[i])
    
    # if test_list == arr:
    #     return True
    # return False

    #plan:

### initiate an empty dictionary to track services
## when a service is opened, add to dictionary
# a dictionary of dictionaries, work_type as the sub dictionary

# False = 
# if True does not have a False within same car_id + work_type

# if there is a duplicate in work_type

# if the time_stamp of close is before time_stamp of open
### 


#if state is True and has a closing False AND work_type is the same,
    # check to make sure car_id matches, and the close is after the open
    # return True

# class MaintenanceEvent(object):
#     def __init__(self, state, car_id, work_type, timestamp):
#         self.state = state # open = True, closed = False
#         self.car_id = car_id # unique, like license plate
#         self.work_type = work_type # “oil”, “fuel”, “wash”, etc.
#         self.timestamp = timestamp # timestamp, like 1030 for 10:30 AM

# def processed_correctly(events):
#     current_services = {}
#     # current_services = {809: {"oil": 1000}}
#     for i in events:
#         if i.state == True: # when service is open, add to current_services
#             if i.car_id not in current_services:
#                 current_services[i.car_id] = {} #creating a sub dictionary,adds the subdict to the current_services
#             if i.work_type in current_services[i.car_id]: #if worktype exists already
#                 return False  
#             elif i.work_type not in current_services:
#                 current_services[i.car_id][i.work_type] = i.timestamp # open a regular service, if its not in current_ services


#         if i.state == False:
#             if i.car_id not in current_services: #if the service hasn't been opened yet
#                 return False
                
#             elif i.car_id in current_services: 
#                 if i.work_type in current_services[i.car_id]:
#                     if i.timestamp < current_services[i.car_id][i.work_type]: # if the service is closed before opening
#                         return False
#                     else: # if timestamp is okay, work time is open before the close, we remove from current services
#                         del current_services[i.car_id][i.work_type]
#                 else: # if i.work_type is NOT in current_services[i.car_id]. We have a close w/o an open
#                     return False

#     for j in current_services: #checking for any opened services that are not closed, return False
#         if len(current_services[j]) != 0:
#             return False  
                        
#     return True

# assert processed_correctly(
#     [MaintenanceEvent(True, 809, "oil", 1000),
#      MaintenanceEvent(True, 600, "tires",1000),
#      MaintenanceEvent(False, 809, "oil", 1030),
#      MaintenanceEvent(False, 600, "tires",1200)])
# assert not processed_correctly(
#     [MaintenanceEvent(True, 81, "brakes",1000), # not closed
#      MaintenanceEvent(True, 82, "fuel", 1000),
#      MaintenanceEvent(False, 82, "fuel", 1030),
#      MaintenanceEvent(False, 82, "oil", 1200)]) # not opened
# assert not processed_correctly(
#     [MaintenanceEvent(True, 11, "wash", 1000),
#      MaintenanceEvent(True, 12, "filter",1000),
#      MaintenanceEvent(False, 12, "filter",1030),
#      MaintenanceEvent(True, 12, "oil", 1200), # not closed
#      MaintenanceEvent(False, 11, "wash", 1200),
#      MaintenanceEvent(True, 13, "tires", 1200)]) # not closed
# assert not processed_correctly(
#     [MaintenanceEvent(True, 8099, "wash", 800),
#      MaintenanceEvent(True, 6780, "fuel", 830),
#      MaintenanceEvent(True, 8099, "wash", 840), # duplicate
#      MaintenanceEvent(False, 6780, "fuel", 845),
#      MaintenanceEvent(False, 8099, "wash", 1100)])

# Interview question: implement integer division
# 
# The goal of this function is to write a function, in a language of
# your choice, that will take two integer number as inputs, and perform
# an integer division of these numbers _without_ using the language's
# built-in division (/) or modulus (%) operators.
#
# The function should return both a quotient and a remainder.
#
# Examples:
# divide(3, 2)   -> (1, 1)  # quotient = 1, remainder = 1
# divide(4, 2)   -> (2, 0)  # quotient = 2, remainder = 0
# divide(33, 8)  -> (4, 1)  # quotient = 4, remainder = 1
# divide(-10, 2) -> (-5, 0) # quotient = -5, remainder = 0

# input (33, 8) x, y
# output (4, 1)
# y * num = x 
# num = x/y
# remainder = x - (num * y)

# minimum is 0
# maximum is numerator

# loop through range(min, max)
# i > 0
# remainder should be < denominator 

# if both positive => positive
# if both negative => positive
# if one is negative => negative answer

#how to make it faster? Binary search

def divide(numerator, denominator):
    
    answer_should_be_positive = True
    if (numerator < 0) ^ (denominator < 0):
        answer_should_be_positive = False

    numerator = abs(numerator)
    denominator = abs(denominator)
    
    minimum, maximum = 0, numerator
    guess = (minimum + maximum) // 2 ## this is our guess

    while True:
        # check if our guess is too big or too small
        #if mid = guess, figure out what the remainder would be
        # if guess is too big, the numerator < denominator * mid
        if numerator < denominator * guess: # if guess is too big
        # pick a new guess that's smaller. max = current guess
            maximum = guess
            guess = (minimum + maximum) // 2
        #new guess = middle of minimum & new max

        if (numerator - guess * denominator) >= denominator:
            minimum = guess
            guess = ((minimum + maximum) // 2) + 1
        # if guess is too small, if (numerator - guess * denominator) >= denominator
        # pick a bigger guess. set min = midpoint of min and max
        # new guess is between new min and new max

        if (numerator - guess * denominator) < denominator and (numerator - guess * denominator) >= 0:
            if answer_should_be_positive is False:
                return (-guess, (numerator - guess * denominator))
            return (guess, (numerator - guess * denominator))


# print(divide(numerator = -10, denominator = 2)) 
# 33/8 - guess was 2, 2*8 = 16, 33-16 = 17, 17 > 8
print(divide(numerator = 1000000000, denominator = 2))

# range = 0, 500
# i = 1 r = 995
# i = 2 r = 990
# i = 3 r = 985
# i = 4 r = 980

# print(divide(numerator = 100000000, denominator = 1))





# def divide(numerator, denominator):
    
#     answer_should_be_positive = True
#     if (numerator < 0) ^ (denominator < 0):
#         answer_should_be_positive = False
#     numerator = abs(numerator)
#     denominator = abs(denominator)
    
#     minimum = 0
#     maximum = numerator    
    
#     for i in range(minimum, maximum):

#         remainder = numerator - (i * denominator)
#         if remainder < denominator:
#             if answer_should_be_positive is False:
#                 return (-i, remainder)
#             return (i, remainder)
   

# # print(divide(numerator = 10, denominator = 2))
# print(divide(numerator = 1000000000, denominator = 1))
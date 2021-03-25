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

class MaintenanceEvent(object):
    def __init__(self, state, car_id, work_type, timestamp):
        self.state = state # open = True, closed = False
        self.car_id = car_id # unique, like license plate
        self.work_type = work_type # “oil”, “fuel”, “wash”, etc.
        self.timestamp = timestamp # timestamp, like 1030 for 10:30 AM

def processed_correctly(events):
    current_services = {}
    # current_services = {809: {"oil": 1000}}
    for i in events:
        if i.state == True: # when service is open, add to current_services
            current_services[i.car_id] = {} #creating a sub dictionary,adds the subdict to the current_services
            if i.work_type in current_services[i.car_id]: #if worktype exists already
                current_services[i.car_id][i.work_type] = i.timestamp # we added work_type and timestamp into sub dict
        if i.state == False:
            for j in events: # loop over events a second time, and check if its the same car id and work type
                if j.state == True and i.car_id == j.car_id and i.work_type == j.work_type: # if so, it has been properly opened / closed, return True
                    return True
                elif j.state == True not in current_services: # if there isn't a True for a False
                    return False
                elif  j.state == True and i.timestamp > j.timestamp:
                    return False
        if i.car_id in current_services:
            if i.car_id == current_services[i.car_id] and i.work_type == current_services[i.car_id][i.work_type]:
                return False #check for duplicates           
    return False

assert processed_correctly(
    [MaintenanceEvent(True, 809, "oil", 1000),
     MaintenanceEvent(True, 600, "tires",1000),
     MaintenanceEvent(False, 809, "oil", 1030),
     MaintenanceEvent(False, 600, "tires",1200)])
assert not processed_correctly(
    [MaintenanceEvent(True, 81, "brakes",1000), # not closed
     MaintenanceEvent(True, 82, "fuel", 1000),
     MaintenanceEvent(False, 82, "fuel", 1030),
     MaintenanceEvent(False, 82, "oil", 1200)]) # not opened
assert not processed_correctly(
    [MaintenanceEvent(True, 11, "wash", 1000),
     MaintenanceEvent(True, 12, "filter",1000),
     MaintenanceEvent(False, 12, "filter",1030),
     MaintenanceEvent(True, 12, "oil", 1200), # not closed
     MaintenanceEvent(False, 11, "wash", 1200),
     MaintenanceEvent(True, 13, "tires", 1200)]) # not closed
assert not processed_correctly(
    [MaintenanceEvent(True, 8099, "wash", 800),
     MaintenanceEvent(True, 6780, "fuel", 830),
     MaintenanceEvent(True, 8099, "wash", 840), # duplicate
     MaintenanceEvent(False, 6780, "fuel", 845),
     MaintenanceEvent(False, 8099, "wash", 1100)])

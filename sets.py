#################################################################################################
#   ****SETS****                                                                                #
#   These functions are used to manipulate sets. It produces sets from lists, as well as         #
#   determines the union, intersection, and symmetric difference of two sets.                   #
#                                                                                               #
#   Kehlsey Lewis                                                                               #
#   MTH 225(03)                                                                                 #
#                                                                                               #
#################################################################################################

################################################################################################
# make_set: This takes in a list and makes it into a set by removing duplicates.
# It will return the new set when finished. 
################################################################################################

def make_set(lists):
    
    #creating an empty set to add the new elements to
    set = []
    
    #goes through the given list and removes duplicates and adds them to the new set
    for x in lists:
        if x not in set:
            set.append(x)
    return set

################################################################################################
# is_inter: This takes in two lists and finds the elements that they share.
# It will return the set when finished. 
################################################################################################

def inter(list1, list2):
    
    #creating an empty set to add the new elements to
    set = []
    
    #goes through list1 and figures out if the element is in list2 
    #are not already listed in the new set
    for x in list1:
        if x in list2 and x not in set:
            set.append(x)
    return set

################################################################################################
# union: This takes in two lists and creates a new list containing the elements from both list,
# but removes duplicates. It will return the new set.
################################################################################################

def union(list1, list2):
    
    #creating an empty set to add the new elements to
    set = []
    
    #adds elements from list1 to the set list
    for x in list1:
        set.append(x)
        
    #adds elements from list2 to the set list
    for y in list2:
        set.append(y)
        
    #makes the set list into a set without duplicates
    answer = make_set(set)
    return answer

################################################################################################
# sym_diff: This takes in two lists and creates a new list containing their symmetric differences.
# The new set will contain elements from list1 (but not in list 2) and it will also contain the 
# elements in list2(but not list1). It will return the new set containing the differences.
################################################################################################

def sym_dif(list1, list2):
    
    #takes the lists and makes them a set
    list10 = make_set(list1)
    list20 = make_set(list2)
    
    #creating a list to hold the differences
    set = []
    
    #going through list 1.0 and adding them if they are not in the new set
    for x in list10:
        if x not in set:
            set.append(x)
    
    #going through list 2.0 and removing them from the set list if they are repeated        
    for y in list20:
        if y in set:
            set.remove(y)
        #if they aren't in list 1.0 then they are added to the set list
        else:
            set.append(y)
    return set  

################################################################################################
# power: This takes in a list called given and it will return all of the powersets of that list.
################################################################################################

def power(given): 
    
    #creates a set containing the empty set because it is always in the powerset
    #to every set
    answer = [[]]
    
    #going through the set and creating mixes of the elements
    for y in given:
     for z in answer:
             #creating an empty list, adding the mix into that list, and adding it to the answer list
             answer = answer + [list(z)+[y]]
              
    #removing duplicate sets from the answer list and putting them into a new list
    temp = []
    for item in answer:
     if sorted(item) not in temp:
        temp.append(sorted(item))
    
    #making the lists inside the temp list into sets    
    temp2 = []    
    for a in temp:
        if make_set(a) not in temp2:
            temp2.append(make_set(a))
    
    #returning temp2 because it contains the full list of powersets without duplicates
    return temp2
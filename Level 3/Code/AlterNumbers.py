'''
* Write a method called interleave that accepts two lists of integers a1 and a2 
* as parameters and inserts the elements of a2 into a1 at alternating indexes. If the 
* lists are of unequal length, the remaining elements of the longer list are left at 
* the end of a1. 

'''

def interleave(list_1, list_2):
    times = min(len(list_1), len(list_2));
    i = 0;
    
    for i in range(0, times):
        num = list_2[i];
        list_1.insert(2 * i + 1, num);

    if (i < len(list_2)):
        for j in range(i + 1, len(list_2)):
            list_1.append(list_2[j])

    return list_1, list_2;

print (interleave([1,2,4],[5,6,7,4,6]))
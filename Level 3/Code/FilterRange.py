'''
Write a method filterRange that accepts an ArrayList of integers and
two integer values min and max as parameters and removes all elements 
whose values are in the range min through max (inclusive) from the 
list. If no elements in range min-max are found in the list, the list's 
contents are unchanged. If an empty list is passed, the list remains empty. 
You may assume that the list is not null. 

'''

def filterRange(list_of_Elements, min, max):
	
	
	for i in range(min, max + 1):
		x = min;
		if (min <= len(list_of_Elements) - 1):
			list_of_Elements.pop(x);

	return list_of_Elements;

print (filterRange([1,4,6,3,6,7,9,8],5,56))
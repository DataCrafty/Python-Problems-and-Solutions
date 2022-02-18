'''

Write a method leasToFront that takes an list of integers as a 
 parameter and that moves the minimum value in the list to the front, 
 otherwise preserving the order of the elements. You may assume that the 
 list stores at least one value.

'''
def minToFront(listOfElements):
	minIndex = 0;
	order_list = listOfElements;

	for i in range(0, len(order_list)):
		if (order_list[minIndex] > order_list[i]):
			minIndex = i;

	minValue = order_list.pop(minIndex);
	order_list.insert(0,minValue)

	return order_list;

print (minToFront ([5451,44,59566,247]))
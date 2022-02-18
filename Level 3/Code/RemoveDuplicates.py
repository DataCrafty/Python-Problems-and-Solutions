'''
* Write a method removeDuplicates that takes as a parameter a sorted 
* ArrayList of Strings and that eliminates any duplicates from the list. 
'''

def removeDuplicates(string_list):
	for i in range(0, len(string_list)):
		if (i != len(string_list)):
			if ((string_list[i] == string_list[i+1])):
				string_list.pop(i+1);
				i = i - 1;

	return string_list;

print (removeDuplicates(['hi','hi','hi', 'hid']))
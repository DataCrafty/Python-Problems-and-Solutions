'''
* Write a method AsteriskLength that takes an list of Strings as 
* a parameter and that places a string of four asterisks "****" in
* previous index of every string of length 4.
'''

def AsteriskLength(list_string):
	temp = [] * len(list_string);
	for i in range(0, len(list_string)):
		if (len(list_string[i]) == 4):
			temp.insert(i*i+1, "****");
		temp.append(list_string[i])
			

	return temp;

print (AsteriskLength(['hirr', 'hell', 'jkd', 'kdjdkjd', 'pyth']))
'''
* Write a method doubleList that takes an ArrayList of Strings as a 
* parameter and that replaces every string with two of that string. 
'''

def doubleList(listOfElementsasString):
	#oldSize = listOfElementsasString.size();
    word = '';
    doubled = listOfElementsasString;
    for i in range(0, len(listOfElementsasString)):
    	word = listOfElementsasString[2*i];
    	doubled.insert(2*i+1, word);

    return doubled;

print (doubleList(["hi", "Hello"]))
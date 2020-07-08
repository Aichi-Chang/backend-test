Write a method which accepts an array (or list in Python) of integers and returns an element of that array.

The method should determine the frequency of each element (how many times the element appears in the array) and whenever possible should return the element with the second-lowest frequency. Otherwise it should return the integer with the lowest frequency.

If there is more than one element satisfying the requirements then the second smallest one (according to value) should be returned.

Example outputs:

secondLowest( [4, 3, 1, 1, 2] ) == 1
secondLowest( [4, 3, 1, 1, 2, 2] ) == 2
secondLowest( [4, 3, 1, 2] ) == 2
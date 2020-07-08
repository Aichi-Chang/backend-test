Implement the following function which takes a string of letters and finds the longest sequence where the same letter occurs continuously.

longestSequence(sequence)

The function must return a tuple (c, n) where c is the lowercase character and n is the length of this sub-sequence.

If there are multiple characters with a continuous sequence of the same length, return the information for the letter which occurs first alphabetically.

Example outputs:

longest_sequence( "dghhhmhmx" ) == ("h", 3)
longest_sequence( "dhkkhhKKKt" ) == ("k", 3)
longest_sequence( "aBbBadddadd" ) == ("b", 3)
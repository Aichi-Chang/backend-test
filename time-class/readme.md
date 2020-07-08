Implement a class called Time. The following class variables should be initialised as integers in the class constructor (or __init__ method in Python):

hours
minutes
seconds

Include a method which normalises the time and invoke it appropriately so that the time is automatically adjusted when large integers are passed in. The following rules should remain true:

0 <= hours <= 23
0 <= minutes <= 59
0 <= seconds <= 59

Include a method called scale which will accept an integer of seconds and add it to the time held in the current instance.

Include a method called timeString which returns a string in the format “hh:mm:ss”.

Example outputs:

Time t = new Time( 1, 30, 20 );
t.timeString() == “01:30:20”
t.scale( 400 );
t.timeString() == “01:37:00”

Time t = new Time( 1, 100, 0 );
t.timeString() == “02:40:00”
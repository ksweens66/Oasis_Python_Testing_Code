# This program demos the threaded timer functionality in python

import threading 
def delayed_function(): 
	print("I was delayed!\n") 

print("Let's try the timer function")
timer = threading.Timer(10, delayed_function) 
timer.start() 


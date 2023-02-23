import time 
x = 0

#This loop says while the variable x is storing a value less than five, do the loop

while x < 5:
    time.sleep(0.5)
    print("hello world")
    #adds 1 to x value so not to cause an infinite loop
    x += 1 
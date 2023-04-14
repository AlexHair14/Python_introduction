import time 
x = 0

#This loop says while the variable x is storing a value less than five, do the loop

while x < 5:
    time.sleep(0.5)
    print("hello world")
    #adds 1 to x value so not to cause an infinite loop
    x += 1 

print("\n")

for i in range(5):
    time.sleep(0.5)
    print("hello world")
    #this prints hello world exactly 5 times and doesn't need a condition to be broken to stop 
    #it will only go for the specified number of times
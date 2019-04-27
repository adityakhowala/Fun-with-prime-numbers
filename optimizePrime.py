#!/usr/bin/python3

from time import time
from time import sleep

start=time()
sleep(1)
flag=0
number = 9981897  				# The number to check if it is prime or not.
if(number%2==0):          
        end=time()
        print("Total time taken is :	{}".format(end-start))
        print("Not Prime")
        exit()

n=int(number/2)
for i in range(3,n+1,2):
        if(number%i==0):
                flag=1
                break
end=time()
print("Total time taken is : {}".format(end-start))

if(flag==1):
        print("Not Prime")
else:
        print("Prime ... ")

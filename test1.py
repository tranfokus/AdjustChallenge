# python program to print the number from 1 to 10 in random number
# test at https://repl.it/languages/python3
import random

in_list = [x for x in range(1,11)] # create a list with number from 1 to 10
out_list = [] # define a list to store the result

# move element at random position from in_list (until the list is empty) to the out_list
while len(in_list) > 0:
    random_postion = random.randint(0,len(in_list)-1)  
    out_list.append(in_list[random_postion])            
    del in_list[random_postion]

# print the result from out_list in one line  
print(' '.join(map(str, out_list))) 


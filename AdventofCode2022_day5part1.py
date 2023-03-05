import re

with open("input_day5.txt") as file:
    list = []
    stacks = []
    for line in file:
        
        while line[0] == ' ' or line[0] == '[':
            line = line.strip('\n').strip(',').split(' ')
            stacks.append(line)
            #print(stacks)
            list(map(list, zip(stacks)))
            print(list)
        #stack = list(map(list, (zip(line) for line in file)))
        #print(stack)

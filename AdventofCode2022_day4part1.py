import re

with open("input_day4.txt") as file:
    counter = 0
    for line in file:
        bounds = [int(s) for s in re.findall('\d+', line)]
        if bounds[0] <= bounds[2] and bounds[3] <= bounds[1]:
            counter += 1
        elif bounds[2] <= bounds[0] and bounds[1] <= bounds[3]:
            counter += 1
            print(bounds)

    print(counter)
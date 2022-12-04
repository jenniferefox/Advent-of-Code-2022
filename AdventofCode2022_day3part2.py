with open("input_day3.txt") as file:
    potentialDuplicates = []
    total = 0
    for x, line in enumerate(file):
        if x % 3 == 0:
            lineOne = line
        elif x % 3 == 1:
            for char in line:
                if char in lineOne:
                    potentialDuplicates.append(char)
        else:
            for charac in line:
                if charac in potentialDuplicates:
                    if charac.islower():
                        total += (ord(charac)-96)
                    else: 
                        total += (ord(charac)-38)
                    print(charac)
                    potentialDuplicates = []
                    break
    print(total)

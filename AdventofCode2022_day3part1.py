with open("input_day3.txt") as file:
    total = 0
    for line in file:
        lineLength = int(len(line)/2)
        bagOne = line[:lineLength]
        bagTwo = line[lineLength:]
        for i in bagOne:
            if i in bagTwo:
                print(i)
                if i.islower():
                    total += (ord(i)-96)
                else: 
                    total += (ord(i)-38)
                break
                
    print(total)
        

with open('input_day2.txt') as file:
    
    totalScore = 0

    for line in file:
        
        if line[2] == "X":
            totalScore += 1
            if line [0] == "A":
                totalScore += 3
            if line [0] == "C":
                totalScore += 6
        elif line[2] == "Y":
            totalScore += 2
            if line [0] == "B":
                totalScore += 3
            if line [0] == "A":
                totalScore += 6
        else:
            totalScore += 3
            if line [0] == "C":
                totalScore += 3
            if line [0] == "B":
                totalScore += 6
    print(totalScore)
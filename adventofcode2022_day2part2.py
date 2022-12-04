with open('input_day2.txt') as file:
    totalScore = 0
    for line in file:
        if line[2] == "X":
            if line[0] == "A":
                totalScore += 3
            elif line[0] == "B":
                totalScore += 1
            else:
                totalScore += 2
        elif line[2] == "Y":
            totalScore += 3
            if line[0] == "A":
                totalScore += 1
            elif line[0] == "B":
                totalScore += 2
            else:
                totalScore += 3
        else:
            totalScore += 6
            if line[0] == "A":
                totalScore += 2
            elif line[0] == "B":
                totalScore += 3
            else:
                totalScore += 1
    print(totalScore)
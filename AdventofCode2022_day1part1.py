with open('input_day1.txt') as file:

    currentCalorieTotal = 0
    mostCalories = 0

    for line in file:
        if line == "\n":
            if currentCalorieTotal > mostCalories:
                mostCalories = currentCalorieTotal
            currentCalorieTotal = 0
        else:
            currentCalorieTotal += int(line)
            #print(line)
    print(mostCalories)

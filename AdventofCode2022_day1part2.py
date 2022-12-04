import bisect 

with open('input_day1.txt') as file:

    currentCalorieTotal = 0
    mostCalories = [0, 0, 0]
    topThreeTotal = 0

    for line in file:
        if line == "\n":
            bisect.insort_left(mostCalories, currentCalorieTotal)
            currentCalorieTotal = 0
            print(mostCalories)
            mostCalories = mostCalories[1:]
        else:
            currentCalorieTotal += int(line)

    for total in mostCalories:
        topThreeTotal += total
    print(topThreeTotal)

def tripleStep(numberOfSteps):
    counter = 0
    stepsTaken = 0

    counter = recursiveComboChecker(numberOfSteps, stepsTaken, 3, counter)
    counter = recursiveComboChecker(numberOfSteps, stepsTaken, 2, counter)
    counter = recursiveComboChecker(numberOfSteps, stepsTaken, 1, counter)

    print(counter)

def recursiveComboChecker(numberOfSteps, stepsTaken, step, counter):
    stepsTaken += step

    if(stepsTaken == numberOfSteps):
        counter += 1
        return counter
    if(stepsTaken >= numberOfSteps):
        return counter
    
    counter = recursiveComboChecker(numberOfSteps, stepsTaken, 3, counter)
    counter = recursiveComboChecker(numberOfSteps, stepsTaken, 2, counter)
    counter = recursiveComboChecker(numberOfSteps, stepsTaken, 1, counter)

    return counter

tripleStep(3)
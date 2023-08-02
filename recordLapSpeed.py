# Accept user input for lap speeds. Store speeds in a list. Sort list, find average speed. Return to user


# Program entry
def Main():
    # list containing user entered speeds
    lapSpeed = []
    # Will store user input
    userInput = 0.0
    # Will store largest float in lapSpeed
    fastestLap = ''
    # Will store smallest float in lapSpeed
    slowestLap = ''
    # Will contain the average of all the items in lapSpeed
    averageLapSpeed = ''

    while userInput != -1:
        userInput = round(float(input("Enter a Lap time. Enter -1 to find total: ")), 2)
        if userInput == -1:
            break  
        lapSpeed.append(float(userInput))

    # Sort lapSpeed list into descending order
    SortList(lapSpeed)

    fastestLap = lapSpeed[0]
    slowestLap = lapSpeed[len(lapSpeed) - 1]
    averageLapSpeed = AverageSpeed(lapSpeed)

    print("Fastest Lap: " + str(fastestLap))
    print("Slowest Lap: " + str(slowestLap))
    print("Average Speed: " + str(averageLapSpeed))

    return Main()

    
def SortList(lapList):
    # Will contain LapSpeed list
    listToSort = lapList

    return listToSort.sort(reverse=True)


def AverageSpeed(speedList):
    # Will contain LapSpeed list
    lapSpeed = speedList
    # Add up all items in lapSpeed list.
    avgSpeed = 0.0
    
    for speed in lapSpeed:
        avgSpeed = avgSpeed + speed

    avgSpeed = round((avgSpeed / len(lapSpeed)), 2)

    return avgSpeed

    
Main()






















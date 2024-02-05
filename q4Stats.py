def printStats(t):
    file = open(t, "r")
    toInt = []

    # read from file
    for line in file.readlines():
        toInt.append(int((line.strip('\n'))))
    
    decorator(toInt)

def decorator(arr):

    print("Numbers read: ", arr)
    print("The count of the numbers: ", len(arr))
    print("The average of the numbers: ", (sum(arr) / len(arr)))
    print("The maximum of the numbers: ", max(arr))

printStats("./text.txt")
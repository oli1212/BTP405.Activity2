import matplotlib.pyplot as plt

def getCount(t):
    tenCM = 0
    twentyCM = 0
    thirtyCM = 0
    fortyCM = 0 
    fiftyCM = 0

    file = open(t, "r")

    for i in file.read().splitlines():
        num = int(i)
        if num >= 0 and num <= 10:
            tenCM += 1
        elif num >= 11 and num <= 20:
            twentyCM += 1
        elif num >= 21 and num <= 30:
            thirtyCM += 1
        elif num >= 31 and num <= 40:
            fortyCM += 1
        elif num >= 41 and num <= 50:
            fiftyCM += 1

    counts = [tenCM, twentyCM, thirtyCM, fortyCM, fiftyCM]

    file.close()

    return counts

def graphSnowfall(t):

    fig, ax = plt.subplots()
    count = getCount(t)
    measurements = ['0-10cm', '11-20cm', '21-30cm', '31-40cm', '41-50cm']

    ax.bar(measurements, count)

    ax.set_ylabel('Accumulated Snow Falls')
    ax.set_title('Snow Falls Measurement')
    ax.set_ylim(0,10)
    plt.show()



graphSnowfall("./text.txt")


def parseInput():
    input = open("input", "r")
    frequenciesList = input.read().splitlines()

    return frequenciesList

def formatFrequencies(frequenciesList):
    for position in range(len(frequenciesList)):
        frequenciesList[position] = int(frequenciesList[position])

    return frequenciesList

def calculateAdjustedFrequency(frequenciesList):
    frequency = 0

    for offset in frequenciesList:
        frequency += offset

    return frequency


def main():
    formattedInput = formatFrequencies(parseInput())
    adjustedFrequency = calculateAdjustedFrequency(formattedInput)

    print adjustedFrequency

main()

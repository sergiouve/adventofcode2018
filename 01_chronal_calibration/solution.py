import sys
import collections


from functools import reduce

def parse_input():
    input = open("input", "r")
    frequencies_list = input.read().splitlines()

    return frequencies_list


def format_frequencies(frequencies_list):
    for position in range(len(frequencies_list)):
        frequencies_list[position] = int(frequencies_list[position])

    return frequencies_list


def calculateAdjustedFrequency(frequenciesList):
    return reduce((lambda x, y: x + y), frequenciesList)


def get_first_repeated_frequency(frequencies_list):
    frequency = 0
    repeated = 0
    seen_frequencies = []

    for offset in frequencies_list:
        frequency += int(offset)
        print(frequency)

        if frequency in seen_frequencies:
            repeated = frequency
            break
        else:
            seen_frequencies.append(frequency)

    return repeated


def main():
    formattedInput = format_frequencies(parse_input())
    adjustedFrequency = calculateAdjustedFrequency(formattedInput)
    firstRepeatedFrequency = get_first_repeated_frequency(formattedInput)

    print(f'resulting_frequency: {adjustedFrequency}')
    print(f'first_repeated_frequency: {firstRepeatedFrequency}')
    sys.exit()

main()

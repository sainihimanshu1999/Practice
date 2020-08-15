# importing counter
from collections import Counter


def firstRepeat(input):
    # splitting the string into words, seperated by spaces
    words = input.split(' ')

    # converting list of words into dict
    dict = Counter(words)

    # traversing through the list and checking which first word is repeating in it
    for key in words:
        if dict[key] > 1:
            print(key)
            return


print(firstRepeat('Ravi had been saying that he had been there'))

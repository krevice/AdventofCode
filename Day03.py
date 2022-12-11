import string

rucksackContents = [x.strip() for x in open("list.txt").readlines()]

duplicateLetters = []
numericalValues = []
commonGroupLetters = []
groupValues = []

lowercaseLetters = dict()  # assign numerical values 1-26 to letters a-z
for index, letter in enumerate(string.ascii_lowercase):
    lowercaseLetters[letter] = index + 1
uppercaseLetters = dict()  # assign numerical values 27-52 to letters A-Z
for index, letter in enumerate(string.ascii_uppercase):
    uppercaseLetters[letter] = index + 27
lowercaseList = list(lowercaseLetters.items())  # convert dictionaries to lists
uppercaseList = list(uppercaseLetters.items())
lettersToNumbers = (
    lowercaseList + uppercaseList
)  # combine lists of lowercase and uppercase letters with their assigned numbers

for i in range(len(rucksackContents)):
    s1 = slice(
        0, len(rucksackContents[i]) // 2
    )  # split input string in half starting from 0
    s2 = slice(
        len(rucksackContents[i]) // 2, len(rucksackContents[i])
    )  # split input string in half starting in the middle
    for j in rucksackContents[i][
        s1
    ]:  # find duplicate characters in the two string halves
        if j in rucksackContents[i][s2]:
            duplicateLetters.append(j)
            break  # stop searching for duplicates as soon as one has been found for each string
for i in range(
    len(duplicateLetters)
):  # convert the duplicate letters to their respective numerical values and create a list of these values
    for j in range(len(lettersToNumbers)):
        if duplicateLetters[i] == lettersToNumbers[j][0]:
            numericalValues.append(lettersToNumbers[j][1])
groupedList = [
    rucksackContents[i : i + 3] for i in range(0, len(rucksackContents), 3)
]  # divide rucksackContents into groups of 3

for i in range(
    len(groupedList)
):  # find the common letter among the groups of 3 and place them into a list
    for j in groupedList[i][0]:
        if j in groupedList[i][1]:
            if j in groupedList[i][2]:
                commonGroupLetters.append(j)
                break
for i in range(
    len(commonGroupLetters)
):  # convert the common group letters to their respective numerical values and create a list of these values
    for j in range(len(lettersToNumbers)):
        if commonGroupLetters[i] == lettersToNumbers[j][0]:
            groupValues.append(lettersToNumbers[j][1])
print(
    "The sum of the priorities is", sum(numericalValues)
)  # show the summation of the numerical values in the list
print("The sum of the priorities of the groups is", sum(groupValues))

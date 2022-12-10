file = open("list.txt", "r")  # open file with calorie values
List = file.readlines()  # move file contents to python list

calories = []
calorieSums = []
sums = 0  # initializing the sums variable

for i in range(len(List)):
    calories.append(List[i].strip("\n"))  # remove the '\n' from all items in List
for i in range(len(calories)):
    if calories[i] != "":  # sum all items until there is a line break
        sums += int(calories[i])
    else:
        calorieSums.append(sums)  # place summations into calorieSums list
        sums = 0  # reset the sums variable to 0
        continue  # continue adding values until the next line break
print(
    "The highest calorie count is", max(calorieSums)
)  # print highest value in calorieSums

calorieSums = sorted(
    calorieSums, reverse=True
)  # sort list in descending numerical order

topThreeTotal = (
    calorieSums[0] + calorieSums[1] + calorieSums[2]
)  # sum the highest three values in the list
print("The sum of the top three calorie counts is", topThreeTotal)

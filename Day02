file = open("list.txt", "r")  # open file with calorie values
List = file.readlines()  # move file contents to python list

gameLegend = []
gameLegendSplit = []
myPoints = 0  # initialize the number of points
finalResults = 0  # initialize points for step 2

for i in range(len(List)):
    gameLegend.append(List[i].strip("\n"))  # remove the '\n' from all items in List
for i in range(len(gameLegend)):  # create a nested list, i.e. [[A,B], [C,D]]
    x = gameLegend[i].split()
    gameLegendSplit.append(x)
for i in range(
    len(gameLegendSplit)
):  # establish the point rules for the game and add up all points earned
    if gameLegendSplit[i][0] == "A" and gameLegendSplit[i][1] == "X":
        myPoints = myPoints + 4
        finalResults = finalResults + 3
    elif gameLegendSplit[i][0] == "A" and gameLegendSplit[i][1] == "Y":
        myPoints = myPoints + 8
        finalResults = finalResults + 4
    elif gameLegendSplit[i][0] == "A" and gameLegendSplit[i][1] == "Z":
        myPoints = myPoints + 3
        finalResults = finalResults + 8
    elif gameLegendSplit[i][0] == "B" and gameLegendSplit[i][1] == "X":
        myPoints = myPoints + 1
        finalResults = finalResults + 1
    elif gameLegendSplit[i][0] == "B" and gameLegendSplit[i][1] == "Y":
        myPoints = myPoints + 5
        finalResults = finalResults + 5
    elif gameLegendSplit[i][0] == "B" and gameLegendSplit[i][1] == "Z":
        myPoints = myPoints + 9
        finalResults = finalResults + 9
    elif gameLegendSplit[i][0] == "C" and gameLegendSplit[i][1] == "X":
        myPoints = myPoints + 7
        finalResults = finalResults + 2
    elif gameLegendSplit[i][0] == "C" and gameLegendSplit[i][1] == "Y":
        myPoints = myPoints + 2
        finalResults = finalResults + 6
    elif gameLegendSplit[i][0] == "C" and gameLegendSplit[i][1] == "Z":
        myPoints = myPoints + 6
        finalResults = finalResults + 7
    else:
        print("There is an invalid combination")
        continue
print("Following the legend, the total number of points is", myPoints)
print("Using the decoded legend results in the total number of points being", finalResults)

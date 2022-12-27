"""
Author: Linda Dominguez Saavedra
Purpose: Advent of Code '22 Solutions
Day: 1 Part 1 and Part 1
"""


with open("Elves.txt") as ElvesTxt:
    elvesFile = ElvesTxt.read().split("\n\n")
###import the elves.txt file which contains the weights and splits them
# print(elvesFile)


def largest():
    weightsList = []
    for elf in elvesFile:
        elfList = [int(weight) for weight in elf.split("\n")] ###list comprehension way
        # for weight in elf.split("\n"):
        #     elfList.append(int(weight))
        weightsList.append(elfList)
        weightsSum = []
        for elf in weightsList:
            elfSum = sum(elf)
            weightsSum.append(elfSum)
    # print (totalList)
    print(max(weightsSum))
largest()

###answer: 
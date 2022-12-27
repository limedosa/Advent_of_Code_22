"""
Author: Linda Dominguez Saavedra
Purpose: Advent of Code '22 Solutions
Day: 1 Part 1 and Part 2
"""
import heapq
# elvesFile = open("Elves.txt", "r").split("\n\n")
# readElves = elvesFile.read()
# ElvesList = readElves.split("\n")
# print(ElvesList)


with open("Elves.txt") as ElvesTxt:
    elvesFile = ElvesTxt.read().split("\n\n")
###import the elves.txt file which contains the weights and splits them
# print(elvesFile)


def largest3Sum():
    weightsList = []
    for elf in elvesFile:
        elfList = [int(weight) for weight in elf.split("\n")] ###list comprehension way
        # for weight in elf.split("\n"):
        #     elfList.append(int(weight))
        weightsList.append(elfList)
        
        # print(newList)
        # newList = [int(elf) for elf in newList]
        # print(newList)
        
    weightSum = []
    for elf in weightsList:
        elfWeightSum = sum(elf)
        weightSum.append(elfWeightSum)
    print(sum(heapq.nlargest(3,weightSum))) ###prints the sums of larest 3 nums
largest3Sum()

###answer: 205381

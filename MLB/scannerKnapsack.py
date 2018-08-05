import csv
from collections import namedtuple
##Reads the CSV File##

def sortResult(result, attributeSelection):
    print()
    print("Position    |    Name    |    Price    |    Average Score    |    Price per Point")
    result.sort(key=lambda x: getattr(x,str(attributeSelection)))

def attributePrompt():
    choice = input("Sort the following data by average score or price per point?\n"+
                "Enter 1 for average score\n"+
                "Enter 2 for price per point\n")
    return choice
    
def positionPrompt():
    choice = input("Will display data ranked on price per point from lowest to highest\n"+
            "Enter 1 for SP\n"+
            "Enter 2 for 1B\n"+
            "Enter 3 for 2B\n"+
            "Enter 4 for SS\n"+
            "Enter 5 for 3B\n"+
            "Enter 6 for C\n"+
            "Enter 7 for OF\n"+
            "Enter 8 for every position\n"+
            "Enter 9 to send data to knapsack\n"+
            "Enter 0 to quit:"+
            "\n")
    return choice

def greedyKnapsack(result):
    print("\nData sent to knapsack to begin computing...")


def safe_div(x,y):
    if float(y) == 0:
        return 0
    return float(x)/float(y)

Player = namedtuple('Player', 'position name price avg_score efficiency')
result = []

print("Begin reading in csv file..")

with open('DKSalaries.csv','r') as csvFile:
    csvReader = csv.reader(csvFile, dialect='excel')
    next(csvReader)
    for row in csvReader:
        result.append(Player(
            position = row[0],
            name = row[2],
            price = row[5],
            avg_score = row[8],
            efficiency = safe_div(row[5],row[8])
            ))
csvFile.close()    

print("Data has been loaded..")

print("Displaying data:\n")

attributeChoice = attributePrompt()
while int(attributeChoice) < 0 or int(attributeChoice) > 2:
    print("\nEntered wrong selection\nPlease select again:\n")
    attributeChoice = attributePrompt()
if attributeChoice == "1":
    attribute = "avg_score"
else:
    attribute = "efficiency"

print("Selection will be based on "+attribute+"\n")

positionChoice = positionPrompt()

while positionChoice != "0":

    if positionChoice == "1":
        sortResult(result, attribute)
        for person in result:
            if "SP" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()

    if positionChoice == "2":
        sortResult(result)
        for person in result:
            if "1B" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()
    
    if positionChoice == "3":
        sortResult(result)
        for person in result:
            if "2B" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()
    
    if positionChoice == "4":
        sortResult(result)
        for person in result:
            if "SS" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()

    if positionChoice == "5":
        sortResult(result)
        for person in result:
            if "3B" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()
    
    if choice == "6":
        sortResult(result)
        for person in result:
            if "C" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()

    if positionChoice == "7":
        sortResult(result)
        for person in result:
            if "OF" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="      ")
                print()

    if positionChoice == "8":
        sortResult(result)
        for person in result:
            if int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()

    if positionChoice == "9":
        greedyKnapsack(result)

    
    print()
    positionChoice = prompt()

print("Thank you for using my program!  ~ David")

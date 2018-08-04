import csv
from collections import namedtuple
##Reads the CSV File##

def sortResult(result):
    print()
    print("Position    |    Name    |    Price    |    Average Score    |    Price per Point")
    result.sort(key=lambda x: getattr(x,"efficiency"))

def prompt():
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

print("Displaying data:")

choice = prompt()

while choice != "0":

    if choice == "1":
        sortResult(result)
        for person in result:
            if "SP" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()

    if choice == "2":
        sortResult(result)
        for person in result:
            if "1B" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()
    
    if choice == "3":
        sortResult(result)
        for person in result:
            if "2B" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()
    
    if choice == "4":
        sortResult(result)
        for person in result:
            if "SS" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()

    if choice == "5":
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

    if choice == "7":
        sortResult(result)
        for person in result:
            if "OF" in person.position and int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="      ")
                print()

    if choice == "8":
        sortResult(result)
        for person in result:
            if int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end ="          ")
                print()

    if choice == "9":
        greedyKnapsack(result)

    
    print()
    choice = prompt()

print("Thank you for using my program!  ~ David")
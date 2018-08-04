import csv
from collections import namedtuple
##Reads the CSV File##

def sortResult(result, attribute, ):
    result.sort(key=lambda x: getattr(x,attribute))

def prompt():
    choice = input("Enter 1 for SP\n"+
            "Enter 2 for 1B\n"+
            "Enter 3 for 2B\n"+
            "Enter 4 for SS\n"+
            "Enter 5 for 3B\n"+
            "Enter 6 for C\n"+
            "Enter 7 for OF\n"+
            "Enter 8 for every position\n"+
            "Enter 9 for every position but NOT sorted\n"+
            "Enter 0 to quit:"+
            "\n")
    return choice

def safe_div(x,y):
    if float(y) == 0:
        return 0
    return float(x)/float(y)

Player = namedtuple('Player', 'position name avg_score efficiency')
result = []

print("Begin reading in csv file..")
with open('DKSalaries.csv','r') as csvFile:
    csvReader = csv.reader(csvFile, dialect='excel')
    next(csvReader)
    for row in csvReader:
        result.append(Player(
            position = row[0],
            name = row[2],
            avg_score = row[8],
            efficiency = safe_div(row[5],row[8])
            ))

csvFile.close()    

print("Data has been loaded..")
print("Displaying data:")

choice = prompt()

while choice != "0":

    if choice == "8":
        print()
        sortResult(result, "efficiency")
        print("Position    |    Name    |    Average Score    |    Price per Point")
        for person in result:
            if int(person.efficiency) > 0:
                for stat in person:
                    print(stat, end =" ")
                print()

    if choice == "9":
        for person in result:
            for stat in person:
                print(stat, end =" ")
            print()
    
    print()
    choice = prompt()

print("Thank you for using my program!  ~ David")
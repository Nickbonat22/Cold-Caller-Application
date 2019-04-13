#   4/11/19 15:40
#   Author: Zach Domke
#   Purpose of this code is as a prototype for reading/writing from/to a file.

import csv
import sys
currentSys = sys.path
sys.path.append('../Models/')
from student import Student
sys.path = currentSys

# code for reading file titled Roster.tsv
def readFile(studentQ):
    # sys.path.append('../Resources/')
    roster = open("../Resources/Roster.tsv", 'r')
    # sys.path = currentSys
    reader = csv.reader(roster, delimiter='\t')
    for row in reader:
        if row[-1] == 'X':
            reveal = True
        else:
            reveal = False

        studentQ.append(Student(row[0], row[1], row[2], row[3], row[4], reveal))
    roster.close()
    del studentQ[0]

# code for creating an output file that will not replace/override a file
def createFile():
    try:
        output = open("Test-Output.tsv", 'x')
    except FileExistsError:
        x = 1
        while True:
            try:
                output = open("Test-Output(" + str(x) + ").tsv", 'x')
                break;
            except FileExistsError:
                x += 1

    return output

# code to write studentQ to the output file
def writeToFile(studentQ, output):
    for x in studentQ:
        output.write(x.getFName() + '\t')
        output.write(x.getLName() + '\t')
        output.write(x.getEmail() + '\t')
        output.write(str(x.getReveal()) + '\n')

def main():
    studentQ = []
    readFile(studentQ)
    output = createFile()
    writeToFile(studentQ, output)
    output.close()

if __name__ == "__main__": main()

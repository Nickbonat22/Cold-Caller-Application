#   4/11/19 15:40
#   Author: Zach Domke
#   Purpose of this code is as a prototype for reading/writing from/to a file.

import os
import csv
from student_queue import Student_queue
from student import Student

def importRoster():
    try:
        newRoster = open("ImportFolder/New Roster.tsv", 'r')
    except FileNotFoundError:
        return

    reader = csv.reader(newRoster, delimiter='\t')
    newStudentQ = []
    for row in reader:
        if row[-1] == "True" or row[-1] == 'X':
            reveal = True
        else:
            reveal = False
        newStudentQ.append(Student(row[0], row[1], row[2], row[3], row[4], reveal))
    del newStudentQ[0]
    newRoster.close()

    existingRoster = open("Resources/Internal Roster.tsv", 'r')
    reader = csv.reader(existingRoster, delimiter='\t')
    oldStudentQ = []
    for row in reader:
        if row[-1] == "True" or row[-1] == 'X':
            reveal = True
        else:
            reveal = False
        oldStudentQ.append(Student(row[0], row[1], row[2], row[3], row[4], reveal))
    del oldStudentQ[0]
    existingRoster.close()

    if not warning(newStudentQ, oldStudentQ):
        return

    existingRoster = open("Resources/Internal Roster.tsv", 'w')
    existingRoster.write("<first name>\t<last name>\t<UO ID>\t<email address>\t<phonetic spelling>\t<reveal code>\n")
    for x in newStudentQ:
        existingRoster.write(x.getFName() + '\t')
        existingRoster.write(x.getLName() + '\t')
        existingRoster.write(x.getID() + '\t')
        existingRoster.write(x.getEmail() + '\t')
        existingRoster.write(x.getPSpell() + '\t')
        existingRoster.write(str(x.getReveal()) + '\n')
    existingRoster.close()
    if os.path.exists("ImportFolder/New Roster.tsv"):
        os.remove("ImportFolder/New Roster.tsv")
    return

def warning(newStudentQ, oldStudentQ):
    diffStudentQ = []
    for x in newStudentQ:
        isIn = False
        for y in oldStudentQ:
            if x == y:
                isIn = True
        if not isIn:
            diffStudentQ.append((x, "added"))
    for x in oldStudentQ:
        isIn = False
        for y in newStudentQ:
            if x == y:
                isIn = True
        if not isIn:
            diffStudentQ.append((x, "removed"))

    if not diffStudentQ:
        return True

    print("WARNING: There are differences between Internal Roster and New Roster:")
    for (x, code) in diffStudentQ:
        print(x.getFName() + ' ' + x.getLName() + ' ' + code)

    # Open window showing differences
    # ask if we continue

    continueImport = True #response
    return continueImport





def main():
    importRoster()

if __name__ == "__main__":
    main()
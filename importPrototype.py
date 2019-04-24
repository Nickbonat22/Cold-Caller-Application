#   4/23/19 15:40
#   Author: Zach Domke
#   Purpose of this code is to import a new roster and replace the internal roster

import os
import csv
from student import Student


# Main import function. Takes in a new roster and replaces the old roster.
# Checks for a new roster in the path "ImportFolder/New Roster.tsv" and replaces "Resources/Internal Roster.tsv".
class importer:
    def importRoster():
        # Locates the new roster or stops running if there is no new roster.
        try:
            newRoster = open("ImportFolder/New Roster.tsv", 'r')
        except FileNotFoundError:
            return

        # Populates the newStudentQ with the list of students from the new roster.
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

        # Populates the oldStudentQ with the students from the current/existing roster.
        existingRoster = open("Resources/Internal Roster.tsv", 'r')
        reader = csv.reader(existingRoster, delimiter='\t')
        oldStudentQ = []
        for row in reader:
            if row[-1] == "True" or row[-1] == 'X':
                reveal = True
            else:
                reveal = False
            tempStudent = Student(row[2], row[3], row[4], row[5], row[6], reveal)
            tempStudent.setCalledOnCount(row[0])
            tempStudent.setConcernCount(row[1])
            oldStudentQ.append(tempStudent)
        del oldStudentQ[0]
        existingRoster.close()

        # Checks if the queues are different. If they are different, we confirm with the user. If they are the same, we stop.
        if not warning(newStudentQ, oldStudentQ):
            return

        # Overwrites the existing internal roster with the new information.
        existingRoster = open("Resources/Internal Roster.tsv", 'w')
        existingRoster.write("<total times called>\t<times of concern>\t<first name>\t<last name>\t<UO ID>\t<email address>\t<phonetic spelling>\t<reveal code>\n")
        for x in newStudentQ:
            existingRoster.write(str(x.getCalledOnCount()) + '\t')
            existingRoster.write(str(x.getConcernCount()) + '\t')
            existingRoster.write(x.getFName() + '\t')
            existingRoster.write(x.getLName() + '\t')
            existingRoster.write(x.getID() + '\t')
            existingRoster.write(x.getEmail() + '\t')
            existingRoster.write(x.getPSpell() + '\t')
            existingRoster.write(str(x.getReveal()) + '\n')
        existingRoster.close()
        # if os.path.exists("ImportFolder/New Roster.tsv"):
        #     os.remove("ImportFolder/New Roster.tsv")
        return

    # Compares 2 lists of students and confirms changes with the user.
    def warning(newStudentQ, oldStudentQ):
        # Populates the list of differences and tells whether the student will be added or removed.
        diffStudentQ = []
        for x in newStudentQ:
            isIn = False
            for y in oldStudentQ:
                if x == y:
                    isIn = True
                    x.setCalledOnCount(y.getCalledOnCount())
                    x.setConcernCount(y.getConcernCount())
            if not isIn:
                diffStudentQ.append((x, "added"))
        for x in oldStudentQ:
            isIn = False
            for y in newStudentQ:
                if x == y:
                    isIn = True
            if not isIn:
                diffStudentQ.append((x, "removed"))

        # Stops running if there are no differences. Nothing will change.
        if not diffStudentQ:
            return False

        # Prints out a warning that changes will be made and lists the changes. Will ask the user to cancel or continue.
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
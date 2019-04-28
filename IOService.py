#!/usr/bin/env python3
'''
CIS 422 Project 1
Author: Zach Domke
Created on: Apr 14, 2019
Last modified by: Zach Domke @ Apr 27, 2019
Topic: IO Contoller Class
Effect: Imports a new roster to the system. Exports the current roster to the user. Manages the cache in the system.
'''

import os
import csv
from singleton import Singleton
from student import Student
from student_queue import Student_queue
DELIM = '\t'

# Main import function. Takes in a new roster and replaces the old roster.
# Checks for a new roster in the path "ImportFolder/New Roster.tsv" and replaces "Resources/Internal Roster.tsv".
@Singleton
class IO:
    curr_queue = None
    def __init__(self):
        self.curr_queue = Student_queue()
        with open("Resources/Internal Roster.tsv", 'r') as existingRoster:
            self.readFile(self.curr_queue.studentQ, existingRoster, True)
    
    def get_curr_queue(self): 
        return self.curr_queue
    
    def set_curr_queue(self, to_queue):
        self.curr_queue = to_queue
        self.cache(self.curr_queue)

    def importRoster(self, filePath):
        # Locates the new roster or stops running if there is no new roster.
        try:
            newRoster = open(filePath, 'r')
        except FileNotFoundError:
            return

        # Populates the newStudentQ with the list of students from the new roster.
        newStudentQ = []
        self.readFile(newStudentQ, newRoster, False)

        # Populates the oldStudentQ with the students from the current/existing roster.
        existingRoster = open("Resources/Internal Roster.tsv", 'r')
        oldStudentQ = []
        self.readFile(oldStudentQ, existingRoster, True)

        # Checks if the queues are different. If they are different, we confirm with the user. If they are the same, we stop.
        if not self.importWarning(newStudentQ, oldStudentQ):
            return

        # Overwrites the existing internal roster with the new information.
        existingRoster = open("Resources/Internal Roster.tsv", 'w')
        existingRoster.write("<total times called>" + DELIM +
        	"<times of concern>" + DELIM +
        	"<first name>" + DELIM +
        	"<last name>" + DELIM +
        	"<UO ID>" + DELIM +
        	"<email address>" + DELIM +
        	"<phonetic spelling>" + DELIM +
        	"<reveal code>\n")
        self.writeToFile(newStudentQ, existingRoster, True)
        existingRoster.close()
        # if os.path.exists("ImportFolder/New Roster.tsv"):
        #     os.remove("ImportFolder/New Roster.tsv")
        return

    # Compares 2 lists of students and confirms changes with the user.
    def importWarning(self, newStudentQ, oldStudentQ):
        # Populates the list of differences and tells whether the student will be added or removed.
        diffStudentQ = []
        for newStudent in newStudentQ:
            isIn = False
            for oldStudent in oldStudentQ:
                if newStudent == oldStudent:
                    isIn = True
                    newStudent.setCalledOnCount(oldStudent.getCalledOnCount())
                    newStudent.setConcernCount(oldStudent.getConcernCount())
            if not isIn:
                diffStudentQ.append((newStudent, "added"))
        for oldStudent in oldStudentQ:
            isIn = False
            for newStudent in newStudentQ:
                if oldStudent == newStudent:
                    isIn = True
            if not isIn:
                diffStudentQ.append((oldStudent, "removed"))

        # Stops running if there are no differences. Nothing will change.
        if not diffStudentQ:
            return False

        # Prints out a warning that changes will be made and lists the changes. Will ask the user to cancel or continue.
        print("WARNING: There are differences between Internal Roster and New Roster:")
        for (student, code) in diffStudentQ:
            print(student.getFName() + ' ' + student.getLName() + ' ' + code)

        # Open window showing differences
        # ask if we continue

        continueImport = True #response
        return continueImport

    def exportRoster(self, filePath):
        studentQ = []
        existingRoster = open("Resources/Internal Roster.tsv", 'r')
        self.readFile(studentQ, existingRoster, True)

        output = open(filePath, 'w')
        output.write("<first name>" + DELIM +
        	"<last name>" + DELIM +
        	"<UO ID>" + DELIM +
        	"<email address>" + DELIM +
        	"<phonetic spelling>" + DELIM +
        	"<reveal code>\n")
        self.writeToFile(studentQ, output, False)

    def cache(self, studentQueue):
        existingRoster = open("Resources/Internal Roster.tsv", 'w')
        existingRoster.write("<total times called>" + DELIM +
        	"<times of concern>" + DELIM +
        	"<first name>" + DELIM +
        	"<last name>" + DELIM +
        	"<UO ID>" + DELIM +
        	"<email address>" + DELIM +
        	"<phonetic spelling>" + DELIM +
       		"<reveal code>\n")
        self.writeToFile(studentQueue.getQueue(), existingRoster, True)
        existingRoster.close()

    # code for creating an output file that will not replace/override a file
    def createFile(self, fileName):
        try:
            output = open(fileName + ".tsv", 'x')
        except FileExistsError:
            counter = 1
            while True:
                try:
                    output = open(fileName + "(" + str(counter) + ").tsv", 'x')
                    break;
                except FileExistsError:
                    counter += 1

        return output

    def readFile(self, studentQ, input, importCodes):
        # sys.path = currentSys
        reader = csv.reader(input, delimiter='\t')
        for row in reader:
            if row[-1] == 'X' or row[-1] == "False":
                reveal = False
            else:
                reveal = True
            if importCodes:
                tempStudent = Student(row[2], row[3], row[4], row[5], row[6], reveal)
                tempStudent.setCalledOnCount(row[0])
                tempStudent.setConcernCount(row[1])
            else:
                tempStudent = Student(row[0], row[1], row[2], row[3], row[4], reveal)

            studentQ.append(tempStudent)
        input.close()
        del studentQ[0]
        return studentQ

    def writeToFile(self, studentQ, output, printCodes):
        if printCodes:
            for student in studentQ:
                output.write(str(student.getCalledOnCount()) + DELIM)
                output.write(str(student.getConcernCount()) + DELIM)
                output.write(student.getFName() + DELIM)
                output.write(student.getLName() + DELIM)
                output.write(student.getID() + DELIM)
                output.write(student.getEmail() + DELIM)
                output.write(student.getPSpell() + DELIM)
                output.write(str(student.getReveal()) + '\n')
        else:
            for student in studentQ:
                output.write(student.getFName() + DELIM)
                output.write(student.getLName() + DELIM)
                output.write(student.getID() + DELIM)
                output.write(student.getEmail() + DELIM)
                output.write(student.getPSpell() + DELIM)
                output.write(str(student.getReveal()) + '\n')



def main():
    # tester = IO.instance()

    # # Test import roster
    # tester.importRoster()

    # # Test export roster
    # tester.exportRoster()

    # # Test caching
    # studentQ = []
    # existingRoster = open("Resources/Internal Roster.tsv", 'r')
    # tester.readFile(studentQ, existingRoster, True)
    # workingQueue = Student_queue()
    # workingQueue.setQueue(studentQ)
    # workingQueue.pushRandom(workingQueue.popfrom(0))
    # workingQueue.pushRandom(workingQueue.popfrom(1))
    # workingQueue.pushRandom(workingQueue.popfrom(0))
    # workingQueue.pushRandom(workingQueue.popfrom(2))
    # workingQueue.pushRandom(workingQueue.popfrom(0))
    # tester.cache(workingQueue)

if __name__ == "__main__":
    main()
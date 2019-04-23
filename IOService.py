#   4/11/19 15:40
#   Author: Zach Domke
#   Purpose of this code is as a prototype for reading/writing from/to a file.

import csv
import os, errno
from student import Student
from singleton import Singleton
DELIMITER = '\t'
def main():
    studentQ = []
    readFile(studentQ)
    output = createFile()
    writeToFile(studentQ, output)
    output.close()

@Singleton
class IOService:
    def __init__(self):
        print("IOService started")
        self.APPDATA_PATH = os.path.join(os.getenv('HOME'), "CC_422P1")
        try:
            os.makedirs(self.APPDATA_PATH)
        except OSError as e:
            if e.errno != errno.EEXIST:
                self.APPDATA_PATH = os.getenv('HOME')

    # code for reading file titled Roster.tsv
    def readFile(self, roster_file, studentQ):
        if not os.path.exists(roster_file):
            roster_file = "Resoures/Roster.tsv"
            print("Assigned roster file is not existed")
            print("Using default roster file instead")
        global DELIMITER
        roster = open(roster_file, 'r')
        reader = csv.reader(roster, delimiter=DELIMITER)
        for row in reader:
            if row[-1] == 'X':
                reveal = True
            else:
                reveal = False
            studentQ.append(Student(row[0], row[1], row[2], row[3], row[4], reveal))
        roster.close()
        del studentQ[0]
        return studentQ
    
    def create_and_write_queue_to(self, studentQ, to_path, file_name):
        try:
            output = self.createFile(to_path, file_name)
            self.writeToFile(studentQ, )

    # code for creating an output file that will not replace/override a file
    def createFile(self, to_path, filename):
        try:
            output = open(os.path.join(to_path, filename), 'x')
        except FileExistsError:
            x = 1
            while True:
                try:
                    output = open(os.path.join(to_path, filename + "(" + str(x) + ").tsv"), 'x')
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
    def update_a_queue_with_file(self, queue, file_path):
        pass
    def save_a_queue_to_file(self, queue, file_path):
        pass


if __name__ == "__main__":
    main()
    # f = IOService() # Error, this isn't how you get the instance of a singleton

    f = IOService.instance() # Good. Being explicit is in line with the Python Zen
    g = IOService.instance() # Returns already created instance

    print(f is g) # True
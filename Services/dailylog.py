'''
4-7-2019
Author: Nicholas Bonat
Create daily log file and write to it
'''

import sys
import os
currentSys = sys.path
sys.path.append('../Models/')
from student import Student
from IOPrototype import readFile
import datetime

#open file, the current date to the daily log, then close it so it can be read in full
now = datetime.datetime.now()
with open('daily.txt', 'a') as file:
	file.write(now.strftime("\n%m-%d-%Y\n\n"))

#open file, add first/last/email, close file
def dailyRemove(name):
	with open('daily.txt', 'a') as file:
		string = name.getFName() + ' ' + name.getLName() + ' ' + name.getEmail()+ "\n"
		file.write(string)

#open file, go to last line and add X, close file
def dailyConcern(name):
	t = open('daily.txt', 'r+')
	last_line = t.readlines()
	last_line[-1] = "X " + name.getFName() + ' ' + name.getLName() + ' ' + name.getEmail() + "\n"
	final_log = open('daily.txt', 'w')
	final_log.writelines(last_line)
	final_log.close()

def summary():
	studentQ = []
	roster = readFile(studentQ)
	print(roster[0].getCorrectQ())


	
	


'''
4-7-2019
Author: Nicholas Bonat
Create daily log file and write to it
'''

from student import Student
from IOPrototype import readFile
import datetime
import sys
import csv

sys.path.append('../Resources/')

#open file, the current date to the daily log, then close it so it can be read in full
now = datetime.datetime.now()
with open('daily.txt', 'w+') as file:
	file.write('Cold Caller Daily Log\n')
	file.write(now.strftime("%m-%d-%Y\n\n"))

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

#create the summary file
def summary():
	with open("Resources/InternalRoster.tsv", 'r') as roster_file:
		with open('summary.txt', 'w+') as sum_file:
			reader = csv.reader(roster_file, delimiter='\t')
			sum_file.write("Summary Performace\n\n")
			for row in reader:
				string = '	'.join(row[0:8]) +"\n"
				sum_file.writelines(string)
	


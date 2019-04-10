'''
CIS 422 Project 1
Contributors: Nicholas Bonat, 
'''

class Student:
	def __init__(self, firstName, lastName, uoID, email, pSpelling, reveal):
		self.fname = firstName
		self.lname = lastName
		self.id = uoID
		self.email = email
		self.pspell = pSpelling
		self.reveal = reveal

	def getFName(self):
		return self.fname

	def getLName(self):
		return self.lname

	def getID(self):
		return self.id

	def getEmail(self):
		return self.email
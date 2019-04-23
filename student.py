'''
April 7
Author: Nicholas Bonat
'''

class Student:
    def __init__(self, firstName, lastName, uoID, email, pSpelling, reveal):
        self.fname = firstName
        self.lname = lastName
        self.id = uoID
        self.email = email
        self.pspell = pSpelling
        self.reveal = reveal
        self.correctQ = 0
        self.calledOnCount = 0

    def getFName(self):
        return self.fname

    def getLName(self):
        return self.lname

    def getID(self):
        return self.id

    def getEmail(self):
        return self.email

    def getPSpell(self):
        return self.pspell

    def getReveal(self):
        return self.reveal

    def getCorrectQ(self):
        return self.correctQ

    def setCorrectQ(self, correct):
        self.correctQ = correct

    def getCalledOnCount(self):
        return self.calledOnCount

    def setCalledOnCount(self, called):
        self.calledOnCount = called

    def __eq__(self, other):
        if other == None:
            return False
        return ((self.fname == other.fname) and
            (self.lname == other.lname) and
            (self.id == other.id) and
            (self.email == other.email) and
            (self.pspell == other.pspell) and
            (self.reveal == other.reveal))
class Student:
    def __init__(self):
        self.id = 0
        self.firstName = ""
        self.lastName = ""
        self.startingYear = ""
        self.major = None
        self.email = ""

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getStartingYear(self):
        return self.startingYear

    def setStartingYear(self, startingYear):
        self.startingYear = startingYear

    def getMajor(self):
        return self.major

    def setMajor(self, major):
        self.major = major

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email







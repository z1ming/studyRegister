class Course:
    def __init__(self):
        self.code = ""
        self.name = ""
        self.studyPoint = 0
        self.teachers = []

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getStudyPoint(self):
        return self.studyPoint

    def setStudyPoint(self, studyPoint):
        self.studyPoint = studyPoint

    def getTeachers(self):
        return self.teachers

    def addTeacher(self, teacher):
        self.teachers.append(teacher)
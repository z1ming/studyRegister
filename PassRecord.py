class PassRecord:
    def __init__(self):
        self.courseId = ""
        self.studentId = ""
        self.year = ""
        self.grade = ""

    def getCourseId(self):
        return self.courseId

    def getStudentId(self):
        return self.studentId

    def getYear(self):
        return self.year

    def getGrade(self):
        return self.grade

    def setCourseId(self, courseId):
        self.courseId = courseId

    def setStudentId(self, studentId):
        self.studentId = studentId

    def setYear(self, year):
        self.year = year

    def setGrade(self, grade):
        self.grade = grade

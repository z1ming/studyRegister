from datetime import datetime
from typing import List

from Student import Student
import random

studentsFile = "students.txt"
coursesFile = "courses.txt"
passedFile = "passed.txt"

def getStudentIds():
    data = openFile(studentsFile)
    st = set()
    for d in data:
        id = d.split(",")[0]
        st.add(id)
    return st

def generateId():
    return random.randint(10000, 99999)


def addStudent(firstName, lastName, major):
    ids = getStudentIds()
    while True:
        id = generateId()
        if (id not in ids):
            break
    std = str(id) + "," + firstName + "," + lastName + "," + str(datetime.now().year) + "," + major + "," + firstName + lastName + "@lut.fi"
    writeFile(studentsFile, [std])

def searchStudentByName(name):
    ans = []
    data = openFile(studentsFile)
    for student in data:
        arr = student.split(",")
        firstName = arr[1]
        lastName = arr[2]
        if name.lower() in firstName.lower() or name.lower() in lastName.lower():
            std = Student()
            std.setId(arr[0])
            std.setFirstName(arr[1])
            std.setLastName(arr[2])
            std.setStartingYear(arr[3])
            std.setMajor(arr[4])
            std.setEmail(arr[5])
            ans.append(std)
    return ans


def searchStudentById(self, id):
    pass

def searchCourseByName(self, name):
    pass

def searchCourseById(self, id):
    pass

def addCourseCompletion(self, course_id, student_id, grade):
    pass

def showStudentRecord(self, student_id):
    pass

def openFile(fileName):
    data = list()
    try:
        with open(fileName, 'r') as file:
            for line in file:
                # 处理每行数据
                data.append(line.strip())
    except FileNotFoundError:
        print("文件未找到")
    except IOError:
        print("无法读取文件")
    return data

def writeFile(fileName, records):
    with open(fileName, 'a', encoding='utf-8') as file:
        # 在文件后面添加新的记录
        for record in records:
            file.write(record + '\n')
if __name__ == "__main__":
    print(getStudentIds())



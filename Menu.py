import random
from datetime import datetime

from Course import Course
from PassRecord import PassRecord
from Student import Student

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
    std = str(id) + "," + firstName + "," + lastName + "," + str(
        datetime.now().year) + "," + major + "," + firstName + "." + lastName + "@lut.fi"
    writeFile(studentsFile, [std])


def searchStudentByName(name):
    ans = []
    data = openFile(studentsFile)
    for student in data:
        arr = student.split(",")
        firstName = arr[1]
        lastName = arr[2]
        if name.lower() in firstName.lower() or name.lower() in lastName.lower():
            ans.append(toStudent(arr))
    return ans


def searchCourseByName(name):
    ans = []
    data = openFile(coursesFile)
    for course in data:
        arr = course.split(",")
        teachers = []
        courseName = arr[1]
        for i in range(3, len(arr)):
            teachers.append(arr[i])
        match = name.lower() in courseName.lower()
        for teacher in teachers:
            if name.lower() in teacher.lower():
                match = True
                break
        if match:
            cs = Course()
            cs.setCode(arr[0])
            cs.setName(arr[1])
            cs.setStudyPoint(arr[2])
            for teacher in teachers:
                cs.addTeacher(teacher)
            ans.append(cs)
    return ans


def toStudent(arr):
    std = Student()
    std.setId(arr[0])
    std.setFirstName(arr[1])
    std.setLastName(arr[2])
    std.setStartingYear(arr[3])
    std.setMajor(arr[4])
    std.setEmail(arr[5])
    return std


def searchStudentById(id):
    data = openFile(studentsFile)
    for student in data:
        arr = student.split(",")
        studentId = arr[0]
        if studentId == id:
            return toStudent(arr)
    return None


def searchCourseById(id):
    data = openFile(coursesFile)
    for course in data:
        arr = course.split(",")
        courseId = arr[0]
        teachers = []
        for i in range(3, len(arr)):
            teachers.append(arr[i])
        if courseId == id:
            cs = Course()
            cs.setCode(arr[0])
            cs.setName(arr[1])
            cs.setStudyPoint(arr[2])
            for teacher in teachers:
                cs.addTeacher(teacher)
            return cs
    return None


def searchGrade(courseId, studentId):
    data = openFile(passedFile)
    for d in data:
        arr = d.split(",")
        coId = arr[0]
        stId = arr[1]
        if courseId == coId and studentId == stId:
            record = PassRecord()
            record.setCourseId(courseId)
            record.setStudentId(studentId)
            record.setYear(arr[2])
            record.setGrade(arr[3])
            return record
    return None


def searchGrades(studentId):
    ans = []
    data = openFile(passedFile)
    for d in data:
        arr = d.split(",")
        stId = arr[1]
        if studentId == stId:
            record = PassRecord()
            record.setCourseId(arr[0])
            record.setStudentId(arr[1])
            record.setYear(arr[2])
            record.setGrade(arr[3])
            ans.append(record)
    return ans


def addCourseCompletion(courseId, studentId, grade, dt):
    record = searchGrade(courseId, studentId)
    if not record:
        writeFile(passedFile, [courseId + "," + studentId + "," + dt.strftime("%d/%m/%Y") + "," + grade])
    else:
        updateFile(passedFile, courseId + "," + studentId,
                   courseId + "," + studentId + "," + dt.strftime("%d/%m/%Y") + "," + grade + "\n")


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
    file.close()
    return data


def writeFile(fileName, records):
    with open(fileName, 'a', encoding='utf-8') as file:
        # 在文件后面添加新的记录
        for record in records:
            file.write(record + '\n')
    # 关闭文件
    file.close()


def updateFile(fileName, key, param):
    with open(fileName, 'r+') as file:
        lines = file.readlines()

        # 找到要更新的记录
        for i, line in enumerate(lines):
            if line.startswith(key):
                # 更新记录
                lines[i] = param
                break
        # 将更改写回文件
        file.seek(0)
        file.truncate()
        file.writelines(lines)
    file.close()

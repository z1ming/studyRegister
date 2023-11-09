from typing import List



studentsFile = "students.txt"
coursesFile = "courses.txt"
passedFile = "passed.txt"


def addStudent(self, first_name, last_name, major):
    pass

def searchStudentByName(self, name):
    pass

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
    try:
        with open(fileName, 'r') as file:
            for line in file:
                # 处理每行数据
                print(line.strip())  # 打印去除行尾换行符的内容
    except FileNotFoundError:
        print("文件未找到")
    except IOError:
        print("无法读取文件")

def writeFile(fileName, records):
    with open(fileName, 'a', encoding='utf-8') as file:
        # 在文件后面添加新的记录
        for record in records:
            file.write(record + '\n')
if __name__ == "__main__":
    writeFile("courses.txt", ["1","2","3","4"])



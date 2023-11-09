import datetime

import Menu
from MajorEnum import MajorEnum
def printStartMenu():
    print("You may select one of the following:\n" +
          " 1) Add student\n" +
          " 2) Search student\n" +
          " 3) Search course\n" +
          " 4) Add course completion\n" +
          " 5) Show student's record\n" +
          " 0) Exit\n" +
          "What is your selection?")


def printMajorMenu():
    print("Select student's major:\n" +
          " CE: Computational Engineering\n" +
          " EE: Electrical Engineering\n" +
          " ET: Energy Technology\n" +
          " ME: Mechanical Engineering\n" +
          " SE: Software Engineering\n" +
          "What is your selection?")


def checkStudentName(student_name):
    if student_name is None or len(student_name) == 0:
        return False
    if not student_name[0].isupper():
        return False
    for char in student_name:
        if not char.isalpha():
            return False
    return True


class MenuExecutor:
    pass


def addStudent():
    while True:
        print("Names should contain only letters and start with capital letters.")
        first_name = input("Enter the first name of the student: ")
        last_name = input("Enter the last name of the student: ")
        if checkStudentName(first_name) and checkStudentName(last_name):
            break

    while True:
        printMajorMenu()
        major = input()
        if MajorEnum.contains(major):
            break

    Menu.addStudent(first_name, last_name, major)
    print("Student added successfully!")


def checkSearchValue(searchValue):
    if not searchValue:
        return False
    return len(searchValue) >= 3 and " " not in searchValue


def searchStudent():
    while True:
        print("Give at least 3 characters of the student's first or last name:")
        search_value = input()
        if checkSearchValue(search_value):
            break

    students = Menu.searchStudentByName(search_value)

    if students:
        print("Matching students:")
        for student in students:
            print(f"ID: {student.id}, First name: {student.firstName}, Last name: {student.lastName}")


def searchCourse():
    while True:
        searchValue = input("Give at least 3 characters of the name of the course or the teacher:")
        if len(searchValue) >= 3:
            break
    cources = Menu.searchCourseByName(searchValue)
    if not cources:
        for cource in cources:
            print(f"ID: {cource.code}, Name: {cource.name}, Teacher(s): {cource.teacher}")

def addCourseCompletion():
    while True:
        courseId = input("Give the course ID:")
        course = Menu.searchCourseById(courseId)
        if not course:
            break
    while True:
        studentId = input("Give the student ID:")
        student = Menu.searchStudentById(int(studentId))
        if not student:
            break
    while True:
        grade = int(input("Give the grade:"))
        if 1 <= grade <= 5:
            break
        print("Grade is not a correct grade.")
    while True:
        # todo datetime and try catch
        dt = input("Enter a date (DD/MM/YYYY):")
        break
    Menu.addCourseCompletion(course.code, student.id, grade)
    print("Record added!")




def showStudentRecord():
    studentId = input("Student ID:")
    # student = menu.searchStudentById(studentId)
    # courses = menu.searchCourseByName("xxx")
    print("xxxxxx")


if __name__ == "__main__":
    while True:
        exit = False
        printStartMenu()
        userInput = input()

        if userInput == "1":
            addStudent()
        elif userInput == "2":
            searchStudent()
        elif userInput == "3":
            searchCourse()
        elif userInput == "4":
            addCourseCompletion()
        elif userInput == "5":
            showStudentRecord()
        elif userInput == "0":
            exit = True
        else:
            pass
        if exit:
            break



from datetime import date, datetime

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
        print("Give at least 3 characters of the name of the course or the teacher:")
        searchValue = input()
        if len(searchValue) >= 3:
            break
    cources = Menu.searchCourseByName(searchValue)
    if cources:
        for cource in cources:
            teachers = ", ".join(cource.teachers)
            print(f"ID: {cource.code}, Name: {cource.name}, Teacher(s): {teachers}")

def addCourseCompletion():
    global dt
    while True:
        print("Give the course ID:")
        courseId = input()
        course = Menu.searchCourseById(courseId)
        if course:
            break
    while True:
        print("Give the student ID:")
        studentId = input()
        student = Menu.searchStudentById(studentId)
        if student:
            break
    while True:
        print("Give the grade:")
        grade = int(input())
        oldGrade = Menu.searchGrade(courseId, studentId)
        if oldGrade and int(oldGrade.getGrade()) >= grade:
            print("Student has passed this course earlier with grade " + oldGrade.getGrade())
        elif not 1 <= grade <= 5:
            print("Grade is not a correct grade.")
        else:
            break
    while True:
        print("Enter a date (DD/MM/YYYY):")
        dateStr = input()
        try:
            dt = datetime.strptime(dateStr, "%d/%m/%Y").date()
            t = date.today()
            delta = date.today() - dt
            if dt > date.today():
                print("Input date is later than today. Try again!")
            elif delta.days > 30:
                print("Input date is older than 30 days. Contact \"opinto\".")
            else:
                print("Input date is valid.")
                break
        except Exception as e:
            print("Invalid date format. Use DD/MM/YYYY. Try again!")
    Menu.addCourseCompletion(course.getCode(), student.getId(), str(grade), dt)
    print("Record added!")




def showStudentRecord():
    print("Student ID: ")
    studentId = input()
    student = Menu.searchStudentById(studentId)
    if student:
        print("Student ID: " + student.getId() + "\n" +
              "Name: " + student.getFirstName() + ", " + student.getLastName() + "\n" +
              "Starting year: " + student.getStartingYear() + "\n" +
              "Major: " + MajorEnum.get(student.getMajor()) + "\n" +
              "Email: " + student.getEmail() + "\n")
        print("Passed courses:\n")
        totalCredits = 0
        totalCount = 0
        totalGrade = 0
        records = Menu.searchGrades(studentId)
        for record in records:
            course = Menu.searchCourseById(record.getCourseId())
            if course:
                print("Course ID: " + course.getCode() + ", Name: " + course.getName() + ", Credits: " + course.getStudyPoint())
                print("Date: " + record.getYear() + ", Teacher(s): " + ", ".join(course.getTeachers()) + ", grade: " + record.getGrade() + "\n")
                totalCount += 1
                totalCredits += int(course.getStudyPoint())
                totalGrade += int(record.getGrade())
        print("Total credits: " + str(totalCredits) + ", average grade: " + str(totalGrade/totalCount if totalCount != 0 else 0))


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
            print("Please input 0~5!")
        if exit:
            break

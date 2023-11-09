package com.java;

import java.awt.*;
import java.time.LocalDate;
import java.util.List;
import java.util.Scanner;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            boolean exit = false;
            printStartMenu();
            String input = scanner.nextLine();
            switch (input) {
                case "1" -> addStudent();
                case "2" -> searchStudent();
                case "3" -> searchCourse();
                case "4" -> addCourseCompletion();
                case "5" -> showStudentRecord();
                case "0" -> exit = true;
                default -> {
                }
            }
            if (exit) {
                break;
            }
        }
    }

    private static void showStudentRecord() {
    }

    private static void addCourseCompletion() {
        Integer grade;
        LocalDate date;

        Course course;
        Student student;
        MenuExecutor menuExecutor = new MenuExecutor();
        while (true) {
            System.out.println("Give the course ID:");
            String courseId = scanner.nextLine();
            course = menuExecutor.searchCourseById(courseId);
            if (course != null) {
                break;
            }
        }
        while (true) {
            System.out.println("Give the student ID:");
            String studentId = scanner.nextLine();
            student = menuExecutor.searchStudentById(Integer.parseInt(studentId));
            if (student != null) {
                break;
            }
        }
        while (true) {
            System.out.println("Give the grade:");
            grade = Integer.parseInt(scanner.nextLine());
            if (grade >= 1 && grade <= 5) {
                break;
            }
            System.out.println("Grade is not a correct grade.");
        }
        while (true) {
            System.out.println("Enter a date (DD/MM/YYYY):");
            String dt = scanner.nextLine();
            try {
                date = LocalDate.parse(dt);
            } catch (Exception e) {
                System.out.println("Invalid date format. Use DD/MM/YYYY. Try again!");
                continue;
            }
            if (date.isAfter(LocalDate.now())) {
                System.out.println("Input date is later than today. Try again!");
                continue;
            }
            if (date.minusDays(30).isBefore(LocalDate.now())) {
                System.out.println("Input date is older than 30 days. Contact \"opinto\".");
                continue;
            }
            break;
        }

        menuExecutor.addCourseCompletion(course.getCode(), student.getId(), grade);
        System.out.println("Record added!");
    }

    private static void searchCourse() {
        String searchValue;
        while (true) {
            System.out.println("Give at least 3 characters of the name of the course or the teacher:");
            searchValue = scanner.nextLine();
            if (searchValue.length() >= 3) {
                break;
            }
        }
        MenuExecutor menuExecutor = new MenuExecutor();
        List<Course> cources = menuExecutor.searchCourseByName(searchValue);
        if (!cources.isEmpty()) {
            for (Course cource : cources) {
                System.out.println("ID:" + cource.getCode() + ", Name: " + cource.getName() + ", Teacher(s): " + cource.getTeacher());
            }
        }

    }

    private static void searchStudent() {
        String searchValue;
        while (true) {
            System.out.println("Give at least 3 characters of the students first or last name:");
            searchValue = scanner.nextLine();
            if (checkSearchValue(searchValue)) {
                break;
            }
        }
        MenuExecutor menuExecutor = new MenuExecutor();
        List<Student> students = menuExecutor.searchStudentByName(searchValue);
        if (!students.isEmpty()) {
            for (Student student : students) {
                System.out.println("Matching students:\n" +
                        "ID: " + student.getId() + ", First name: " + student.getFirstName() + ", Last name: " + student.getLastName());

            }
        }

    }

    private static boolean checkSearchValue(String searchValue) {
        if (searchValue == null || searchValue.isEmpty()) {
            return false;
        }
        return searchValue.length() >= 3 && !searchValue.contains(" ");
    }

    private static void addStudent() {
        String firstName;
        String lastName;
        while (true) {
            System.out.println("Names should contain only letters and start with capital letters.");
            System.out.println("Enter the first name of the student:");
            firstName = scanner.nextLine();
            System.out.println("Enter the last name of the student:");
            lastName = scanner.nextLine();
            if (checkStudentName(firstName) && checkStudentName(lastName)) {
                break;
            }
        }
        String major;

        while (true) {
            printMajorMenu();
            major = scanner.nextLine();
            if (MajorEnum.contains(major)) {
                break;
            }
        }
        MenuExecutor executor = new MenuExecutor();
        executor.addStudent(firstName, lastName, major);
        System.out.println("Student added successfully!");
    }

    static boolean checkStudentName(String studentName) {
        if (studentName == null || studentName.isEmpty()) {
            return false;
        }
        if (!Character.isUpperCase(studentName.charAt(0))) {
            return false;
        }
        for (int i = 0; i < studentName.length(); i++) {
            if (!Character.isLetter(studentName.charAt(i))) {
                return false;
            }
        }

        return true;
    }

    static void printStudentNameRule() {
        System.out.println("Names should contain only letters and start with capital letters.");
    }

    static void printStartMenu() {
        System.out.println("You may select one of the following:\n" +
                " 1) Add student\n" +
                " 2) Search student\n" +
                " 3) Search course\n" +
                " 4) Add course completion\n" +
                " 5) Show student's record\n" +
                " 0) Exit\n" +
                "What is your selection?");
    }

    static void printMajorMenu() {
        System.out.println("Select student's major:\n" +
                " CE: Computational Engineering\n" +
                " EE: Electrical Engineering\n" +
                " ET: Energy Technology\n" +
                " ME: Mechanical Engineering\n" +
                " SE: Software Engineering\n" +
                "What is your selection?");
    }
}

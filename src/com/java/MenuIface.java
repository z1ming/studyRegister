package com.java;

import java.util.List;

public interface MenuIface {
    void addStudent(String firstName, String lastName, String major);
    List<Student> searchStudentByName(String name);
    Student searchStudentById(Integer id);
    List<Course> searchCourseByName(String name);
    Course searchCourseById(String id);
    void addCourseCompletion(String courseId, Integer studentId, Integer grade);
    Record showStudentRecord(Integer studentId);
}

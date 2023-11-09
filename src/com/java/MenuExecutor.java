package com.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MenuExecutor implements MenuIface {
    @Override
    public void addStudent(String firstName, String lastName, String major) {

    }

    @Override
    public List<Student> searchStudentByName(String name) {
        Student student = new Student();
        student.setId(12112);
        student.setEmail("xxxxxx");
        student.setFirstName("First");
        student.setLastName("Last");
        student.setMajor(MajorEnum.CE);
        return Arrays.asList(student);
    }

    @Override
    public Student searchStudentById(Integer id) {
        return null;
    }

    @Override
    public List<Course> searchCourseByName(String name) {
        List<Course> courses = new ArrayList<>();
        Course course1 = new Course();
        course1.setName("test");
        course1.setCode("xxxx01");
        course1.setStudyPoint(3);
        course1.setTeacher("Teacher");
        courses.add(course1);
        return courses;
    }

    @Override
    public Course searchCourseById(String id) {
        return null;
    }


    @Override
    public void addCourseCompletion(String courseId, Integer studentId, Integer grade) {

    }

    @Override
    public Record showStudentRecord(Integer studentId) {
        return null;
    }
}

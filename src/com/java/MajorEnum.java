package com.java;

public enum MajorEnum {
    CE("Computational Engineering"),
    EE("Electrical Engineering"),
    ET("Energy Technology"),
    ME("Mechanical Engineering"),
    SE("Software Engineering");

    final String desc;

    MajorEnum(String desc) {
        this.desc = desc;
    }

    static boolean contains(String major) {
        for (MajorEnum value : MajorEnum.values()) {
            if (value.name().equals(major)) {
                return true;
            }
        }
        return false;
    }
}

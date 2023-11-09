from enum import Enum

class MajorEnum(Enum):
    CE = "Computational Engineering"
    EE = "Electrical Engineering"
    ET = "Energy Technology"
    ME = "Mechanical Engineering"
    SE = "Software Engineering"

    @staticmethod
    def contains(major):
        return any(major == item.name for item in MajorEnum)


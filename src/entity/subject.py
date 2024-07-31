from enum import Enum
class SubjectType(Enum):
    Chinese = "Chinese"
    Math = "Mathematics"
    English = "English"
    Physics = "Physics"
    Chemistry = "Chemistry"
    Biology = "Biology"
    Politics = "Politics"
    History = "History"
    Geography = "Geography"

    @staticmethod
    def get(subject):
        for subject_type in SubjectType:
            if subject_type.name.lower() == subject.lower():
                return subject_type.value
        raise ValueError("科目类型不存在")

    @staticmethod
    def validate_subject_type(subject_type: str) -> bool:
        subjects = [value.name for value in list(SubjectType)]
        if subject_type not in subjects:
            raise ValueError("科目类型不存在")
        return True
class Marks:
    def __init__(self):
        self.__mark_students = []
        self.__course_credit = 0
        self.__course_id = 0

    def get_course_credit(self):
        return self.__course_credit

    def get_mark_students(self):
        return self.__mark_students

    def get_course_id(self):
        return self.__course_id

    def set_course(self, id, credit):
        self.__course_id = id
        self.__course_credit = credit

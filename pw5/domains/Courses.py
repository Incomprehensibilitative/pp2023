
class Courses:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__marks = []
        self.__credit = 0

    def set_course(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def set_mark(self, temp):
        self.__marks.append(temp)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_mark(self):
        return self.__marks

    def get_credit(self):
        return self.__credit

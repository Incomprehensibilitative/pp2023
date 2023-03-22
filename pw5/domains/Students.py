import numpy as np

class Students:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__dob = ''
        self.__marks = None
        self.__gpa = None

    def set_student(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def set_mark(self, array):
        if self.__marks is None:
            self.__marks = np.array(array)
        else:
            self.__marks = np.concatenate((self.__marks, array), axis=0)

    def get_mark(self):
        return self.__marks

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

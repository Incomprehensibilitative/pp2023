import math
import numpy as np


# classes
class Management:
    def __init__(self):
        self.__number_of_credit = 0
        self.__number_of_student = 0
        self.__number_of_course = 0
        self.__course_list = []
        self.__student_list = []

    def get_course_list(self):
        return self.__course_list

    def get_student_list(self):
        return self.__student_list

    def list_students(self):
        gpa_list = np.array([[0]])
        for c in self.__student_list:
            gpa_list = np.concatenate((gpa_list, [[c.get_gpa()]]), axis=0)
        gpa_list = np.sort(gpa_list, axis=None)
        gpa_list = gpa_list[::-1]

        for g in range(len(gpa_list)):
            for s in self.__student_list:
                if s.get_gpa() == gpa_list[g]:
                    print()
                    print(f'Student ID: {s.get_id()}\n'
                          f'Student name: {s.get_name()}\n'
                          f'Student DoB: {s.get_dob()}\n'
                          f'Student GPA: {s.get_gpa()}\n')

    def list_courses(self):
        for c in self.__course_list:
            print()
            print(f'Course ID: {c.get_id()}\n'
                  f'Course name: {c.get_name()}\n')

    def list_marks(self):
        course_id = input('Please enter the course_id that you want the mark list: ')
        while not validate_id(course_id, self.__course_list):
            print('Wrong course ID')
            course_id = input('Enter the course ID: ')
        print('Students marks for the course')
        for i in self.__course_list:
            if i.get_id() == course_id:
                for s, m in i.get_mark():
                    print(f""" Student ID: {s} \n Student mark: {m}""")
                    print()

    def new_student(self):
        # print('Number of student')
        n = take_a_number('Number of student: ')
        self.__number_of_student += n
        for i in range(n):
            ids = input('Student ID: ')
            name = input('Student name: ')
            dob = input('Student DoB: ')
            student = Students()
            student.set_student(ids, name, dob)
            self.__student_list.append(student)

    def new_course(self):
        # print('Number of course')
        n = take_a_number('Number of course: ')
        self.__number_of_course += n
        for i in range(n):
            ids = input('Course ID: ')
            name = input('Course name: ')
            credit = take_a_number('Course credit: ')
            self.__number_of_credit += credit
            course = Courses()
            course.set_course(ids, name, credit)
            self.__course_list.append(course)

    def new_mark(self):
        course_id = input('Enter the course ID: ')
        student_id = input('Enter the student ID: ')
        while not validate_id(course_id, self.__course_list):
            print('Wrong course ID')
            course_id = input('Enter the course ID: ')
        while not validate_id(student_id, self.__student_list):
            print('Wrong student ID')
            student_id = input('Enter the student ID: ')
        print(f'Enter the Mark for Student_id: {student_id} in Course_id: {course_id}')
        mark = take_a_number('Enter student mark: ')
        temp_credit = 0
        for course in self.__course_list:
            if course.get_id() == course_id:
                temp_credit = course.get_credit()
                temp = [student_id, mark]
                course.set_mark(temp)
        for student in self.__student_list:
            if student.get_id() == student_id:
                temp = np.array([[mark, temp_credit]])
                student.set_mark(temp)

    def get_student_id(self):
        student_id = input('Enter the student ID: ')
        while not validate_id(student_id, self.__student_list):
            print('Wrong student ID')
            student_id = input('Enter the student ID: ')
        return student_id

    def get_student_gpa(self, student_id):
        for student in self.__student_list:
            if student.get_id() == student_id:
                print(f"Student ID: {student_id} - GPA: {student.get_gpa()}")

    def calculate_gpa(self):
        # sum(marks * credits) / total_credits
        for student in self.__student_list:
            student_marks = np.array(student.get_mark())
            product_of_mark_credit = np.prod(student_marks, axis=1)
            divisor = np.sum(product_of_mark_credit)
            gpa = divisor/self.__number_of_credit
            student.set_gpa(math.floor(gpa))


class Students:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__dob = ''
        self.__marks = None
        self.__gpa = 0

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


# General functions
def take_a_number(txt):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print('Invalid input, Try again!')
            continue
        else:
            return n


def validate_id(id, list):
    for i in list:
        if i.get_id() == id:
            return True
    return False


def action(c, system):
    if c == 0:
        exit()
    elif c == 1:
        system.new_student()
    elif c == 2:
        system.new_course()
    elif c == 3:
        system.new_mark()
    elif c == 4:
        system.calculate_gpa()
        system.list_students()
    elif c == 5:
        system.list_courses()
    elif c == 6:
        system.list_marks()
    elif c == 7:
        system.calculate_gpa()
        system.get_student_gpa(system.get_student_id())
    else:
        print('Invalid input. Try again~')


def main():
    system = Management()
    running = True
    while running:
        try:
            b = int(input(' Press 1: Add Student Info'
                          '\n Press 2: to Add Course Info'
                          '\n Press 3: Add student mark'
                          '\n Press 4: To List Student'
                          '\n Press 5: To List Course'
                          '\n Press 6: To show student marks for a given course'
                          '\n Press 7: Calculate student gpa'
                          '\n Press 0: exit'
                          '\n Pressed: '))
        except ValueError:
            print('Invalid input. Try again~')
            continue
        else:
            action(b, system)
            print()


if __name__ == "__main__":
    main()

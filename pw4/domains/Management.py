import numpy as np
import pp2023.pw4.input as ip
import pp2023.pw4.output as op
import Students as st
import Courses as co
import math


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

    def listing_students(self):
        gpa_list = np.array([[0]])
        try:
            for student in self.__student_list:
                gpa_list = np.concatenate((gpa_list, [[student.get_gpa()]]), axis=0)
            gpa_list = np.sort(gpa_list, axis=None)
            gpa_list = gpa_list[::-1]
        except TypeError:
            op.list_students_unsorted(self.__student_list)
            return 0
        op.list_students_sorted(gpa_list, self.__student_list)

    def new_student(self):
        n = ip.take_a_number('Number of student: ')
        self.__number_of_student += n
        for i in range(n):
            ids, name, dob = ip.get_new_student()
            student = st.Students()
            student.set_student(ids, name, dob)
            if ip.validate_id(student.get_id(), self.__student_list):
                op.print_already_existed_id("Student ID", student.get_id())
                break
            self.__student_list.append(student)
        op.print_delimiter()

    def new_course(self):
        n = ip.take_a_number('Number of course: ')
        self.__number_of_course += n
        for i in range(n):
            ids, name, credit = ip.get_new_course()
            self.__number_of_credit += credit
            course = co.Courses()
            course.set_course(ids, name, credit)
            if ip.validate_id(course.get_id(), self.__course_list):
                op.print_already_existed_id("Course ID", course.get_id())
                break
            self.__course_list.append(course)
        op.print_delimiter()

    def new_mark(self):
        course_id, student_id, mark = ip.get_new_mark(self.__course_list, self.__student_list)
        temp_credit = 0
        # check if the mark had already been filled
        for course in self.__course_list:
            if course.get_id() == course_id:
                mark_sheet = course.get_mark()
                for student, grade in mark_sheet:
                    if student == student_id:
                        op.print_already_marked(student, grade)
                        return
                temp_credit = course.get_credit()
                temp = [student_id, mark]
                course.set_mark(temp)
        for student in self.__student_list:
            if student.get_id() == student_id:
                temp = np.array([[mark, temp_credit]])
                student.set_mark(temp)

    def calculate_gpa(self, error):
        # sum(marks * credits) / total_credits
        try:
            for student in self.__student_list:
                student_marks = np.array(student.get_mark())
                product_of_mark_credit = np.prod(student_marks, axis=1)
                divisor = np.sum(product_of_mark_credit)
                gpa = divisor/self.__number_of_credit
                student.set_gpa(math.floor(gpa))
        except np.AxisError:
            op.print_calculate_mark_error(error)

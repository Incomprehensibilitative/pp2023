import pp2023.pw6.input as ip
import pp2023.pw6.output as op
from pp2023.pw6.domains import Students as st
from pp2023.pw6.domains import Courses as co
from pp2023.pw6.domains import Marks as ma
import numpy as np
import bz2
import os.path
import math
import pickle


class Management:
    def __init__(self):
        self.__number_of_credit = 0
        self.__number_of_student = 0
        self.__number_of_course = 0
        self.__course_list = None
        self.__student_list = None
        self.__mark_list = None

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
            self.get_pickled(student, "students", "ab+")
            self.__student_list.append(student)

        op.print_delimiter(0)

    def new_course(self):
        n = ip.take_a_number('Number of course: ')
        self.__number_of_course += n
        for i in range(n):
            ids, name, credit = ip.get_new_course()
            self.__number_of_credit += credit
            course = co.Courses()
            if ip.validate_id(course.get_id(), self.__course_list):
                op.print_already_existed_id("Course ID", course.get_id())
                break
            course.set_course(ids, name, credit)
            self.__course_list.append(course)
            self.get_pickled(course, "courses", "ab+")
        op.print_delimiter(0)

    def new_mark(self):
        course_id, student_id, mark = ip.get_new_mark(self.__course_list, self.__student_list)
        temp_credit = 0
        # create Marks class before hand because it will be use in 2 different for loop
        marking = ma.Marks()
        # check if the mark had already been filled
        for course in self.__course_list:
            if course.get_id() == course_id:
                mark_sheet = course.get_mark()
                for student, grade in mark_sheet:
                    if student == student_id:
                        op.print_already_marked(student, grade)
                        return
                temp_credit = course.get_credit()
                marking.set_course(course_id, temp_credit)
                temp_course_mark = [student_id, mark]
                course.set_mark(temp_course_mark)
        for student in self.__student_list:
            if student.get_id() == student_id:
                temp_student_mark = np.array([[mark, temp_credit]])
                mark_record = marking.get_mark_students()
                mark_record.append([student_id, mark, temp_credit])
                student.set_mark(temp_student_mark)
        self.get_pickled(marking, "marks", "ab+")
        self.__mark_list.append(marking)

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

    def restore(self):
        if self.__course_list is not None:
            for course in self.__course_list:
                self.__number_of_credit += course.get_credit()
        # Ces codes prendra une éternité à exécuter , mais je ne sais pas d'autres moyens, je suis perdu
        if self.__mark_list is not None:
            for mark_sheet in self.__mark_list:
                mark_dict = mark_sheet.get_mark_students()
                for student in self.__student_list:
                    for student_id, mark, credit in mark_dict:
                        if student.get_id() == student_id:
                            temp_student_mark = np.array([[mark, credit]])
                            student.set_mark(temp_student_mark)

    @staticmethod
    def get_pickled(obj, file, mode):
        with open(file, mode) as f:
            pickle.dump(obj, f)
            f.close()

    @staticmethod
    def de_pickling(file):
        object_list = []
        with open(file, 'rb') as f:
            try:
                while True:
                    object_list.append(pickle.load(f))
            except EOFError:
                pass
        return object_list

    @staticmethod
    def reset_file(file):
        with open(file, "wb") as f:
            f.close()
        return True

    @staticmethod
    def compressing_files(f1, f2):
        f2 = bz2.BZ2File(f2, 'wb')
        pickle.dump(f1, f2)
        f2.close()

    @staticmethod
    def decompressing_files(f2):
        f2 = bz2.BZ2File(f2, 'rb')
        pickle.load(f2)
        f2.close()

    def check_files(self):
        path_students = './students.dat'
        path_courses = './courses.dat'
        path_marks = './marks.dat'

        check_students = os.path.isfile(path_students)
        check_courses = os.path.isfile(path_courses)
        check_marks = os.path.isfile(path_marks)
        if check_students:
            self.decompressing_files("students.dat")
            self.__student_list = self.de_pickling("students")
        else:
            self.reset_file("students.dat")
            self.reset_file("students")

        if check_courses:
            self.decompressing_files("courses.dat")
            self.__course_list = self.de_pickling("courses")
        else:
            self.reset_file("courses.dat")
            self.reset_file("courses")

        if check_marks:
            self.decompressing_files("marks.dat")
            self.__mark_list = self.de_pickling("marks")
        else:
            self.reset_file("marks.dat")
            self.reset_file("marks")

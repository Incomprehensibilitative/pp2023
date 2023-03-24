import input as ip
import numpy as np
import output as op
from domains import Students as st
from domains import Courses as co
import zlib
import os.path
import math


class Management:
    def __init__(self):
        self.__number_of_credit = 0
        self.__number_of_student = 0
        self.__number_of_course = 0
        self.__course_list = []
        self.__student_list = []
        self.__mark_list = []

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
        op.print_delimiter(0)

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
        op.print_delimiter(0)

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
                        return 0
                temp_credit = course.get_credit()
                temp = [student_id, mark]
                txt = f"{course_id}, {student_id}, {mark}, {temp_credit}"
                ip.write_to_file("marks.txt", txt, "a")
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
                print(student_marks)
                product_of_mark_credit = np.prod(student_marks, axis=1)
                divisor = np.sum(product_of_mark_credit)
                gpa = divisor/self.__number_of_credit
                student.set_gpa(math.floor(gpa))
        except np.AxisError:
            op.print_calculate_mark_error(error)

    def restore(self):
        # restore student objects
        student_file = open("students.txt", "r")
        student_objects = student_file.readline()
        while student_objects:
            new_student = st.Students()
            student_attr = student_objects.strip().split(", ")
            id = student_attr[0]
            name = student_attr[1]
            dob = student_attr[2]
            new_student.set_student(id, name, dob)
            self.__student_list.append(new_student)
            student_objects = student_file.readline()
        student_file.close()

        # restore course objects
        course_file = open("courses.txt", "r")
        course_objects = course_file.readline()
        while course_objects:
            new_course = co.Courses()
            course_attr = course_objects.strip().split(", ")
            id = course_attr[0]
            name = course_attr[1]
            credit = int(course_attr[2])
            self.__number_of_credit += credit
            new_course.set_course(id, name, credit)
            self.__course_list.append(new_course)
            course_objects = course_file.readline()
        course_file.close()

        mark_file = open("marks.txt", "r")
        mark_objects = mark_file.readline()
        while mark_objects:
            mark_attr = mark_objects.strip().split(", ")
            mark = int(mark_attr[2])
            credit = int(mark_attr[3])
            for student in self.__student_list:
                if student.get_id() == mark_attr[1]:
                    temp = np.array([[mark, credit]])
                    student.set_mark(temp)
            mark_objects = mark_file.readline()
        mark_file.close()


    @staticmethod
    def compressing_files(f1, f2):
        filename_in = f1
        filename_out = f2

        with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
            data = fin.read()
            compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
            fout.write(compressed_data)

    @staticmethod
    def decompressing_files(f1, f2):
        filename_in = f1
        filename_out = f2

        with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
            data = fin.read()
            decompressed_data = zlib.decompress(data)
            fout.write(decompressed_data)

    def check_files(self):
        path_students = './students.dat'
        path_courses = './courses.dat'
        path_marks = './marks.dat'

        check_students = os.path.isfile(path_students)
        check_courses = os.path.isfile(path_courses)
        check_marks = os.path.isfile(path_marks)
        if check_students:
            self.decompressing_files("students.dat", "students.txt")
        else:
            with open('students.txt', 'w') as f:
                f.close()

        if check_courses:
            self.decompressing_files("courses.dat", "courses.txt")
        else:
            with open('courses.txt', 'w') as f:
                f.close()

        if check_marks:
            self.decompressing_files("marks.dat", "marks.txt")
        else:
            with open('marks.txt', 'w') as f:
                f.close()

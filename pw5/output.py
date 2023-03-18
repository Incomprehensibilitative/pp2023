import input as ip


def list_students_unsorted(student_list):
    print("===========================================")
    for student in student_list:
        print(f'Student ID: {student.get_id()}\n'
              f'Student name: {student.get_name()}\n'
              f'Student DoB: {student.get_dob()}\n'
              f'Student GPA: {student.get_gpa()}\n')
        print("===========================================")
        print()


def list_students_sorted(gpa_list, student_list):
    print("===========================================")
    for gpa_idx in range(len(gpa_list) - 1):
        for student in student_list:
            if student.get_gpa() == gpa_list[gpa_idx]:
                print(f'Student ID: {student.get_id()}\n'
                      f'Student name: {student.get_name()}\n'
                      f'Student DoB: {student.get_dob()}\n'
                      f'Student GPA: {student.get_gpa()}\n')
                print("===========================================")
                print()


def list_courses(course_list):
    print("===========================================")
    print("Course list:")
    print("===========================================")
    for course in course_list:
        print(f'Course ID: {course.get_id()}\n'
              f'Course name: {course.get_name()}\n'
              f'Course credit: {course.get_credit()}')
        print("===========================================")
        print()


def list_marks(course_list):
    course_id = ip.get_course_id(course_list)
    print("===========================================")
    print('Students marks for the course')
    print("===========================================")
    for course in course_list:
        if course.get_id() == course_id:
            for student_id, mark in course.get_mark():
                print(f""" Student ID: {student_id} \n Student mark: {mark}""")
                print("===========================================")
                print()


def print_student_gpa(student_id, student_list):
    print("===========================================")
    for student in student_list:
        if student.get_id() == student_id:
            print(f"Student ID: {student_id} - GPA: {student.get_gpa()}")
            print("===========================================")


def print_calculate_mark_error(error_txt):
    if error_txt:
        print("===========================================")
        print('All student mark was not added -> cannot calculate GPA -> cannot list student in descending GPA')
        print("===========================================")
    else:
        return


def print_already_existed_id(txt, id):
    print(f'The {txt}: {id} - already existed')


def print_already_marked(student_id, grade):
    print(f'The student: {student_id} - already marked: {grade}')


def print_delimiter(mode):
    if mode == 0:
        print("=================================================================")
        return 0
    else:
        return "================================================================="


def print_mark_existed():
    print("The mark is already filled")
    print("===========================================")


def print_empty_list(txt):
    print("====================================================")
    print(f'The {txt} is empty -> Cannot carry out the operation')
    print("====================================================")

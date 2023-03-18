import output as op


def get_new_course():
    ids = valid_input_id('Course ID: ')
    name = input('Course name: ')
    credit = validate_credit()
    txt = f"Course ID: {ids}\nCourse name: {name}\nCourse credit: {credit}\n"
    write_to_file("courses.txt", txt, "a")
    write_to_file("courses.txt", op.print_delimiter(1), "a")
    return ids, name, credit


def get_new_student():
    ids = valid_input_id('Student ID: ')
    name = input('Student name: ')
    dob = input('Student DoB: ')
    txt = f"Student ID: {ids}\nStudent name: {name}\nStudent credit: {dob}\n"
    write_to_file("students.txt", txt, "a")
    write_to_file("students.txt", op.print_delimiter(1), "a")
    return ids, name, dob


def get_new_mark(course_list, student_list):
    op.print_delimiter(0)
    course_id = get_course_id(course_list)
    student_id = get_student_id(student_list)
    op.print_delimiter(0)
    print(f'Enter the Mark for Student_id: {student_id} in Course_id: {course_id}')
    mark = valid_mark()
    txt = f"Course ID: {course_id}\nStudent ID: {student_id}\nStudent mark: {mark}\n"
    write_to_file("marks.txt", txt, "a")
    write_to_file("marks.txt", op.print_delimiter(1), "a")
    return course_id, student_id, mark


def take_a_number(txt):
    while True:
        op.print_delimiter(0)
        try:
            n = int(input(txt))
        except ValueError:
            print('Invalid input, Try again!')
            continue
        else:
            return n


def valid_input_id(txt):
    while True:
        op.print_delimiter(0)
        id = input(txt)
        if id.strip() != '':
            return id
        else:
            print('Invalid input, Try again!')


def valid_mark():
    while True:
        op.print_delimiter(0)
        mark = take_a_number('Enter student mark: ')
        if mark < 0 or mark > 20:
            print('Invalid input, Try again!')
        else:
            op.print_delimiter(0)
            return mark


def validate_id(id, list):
    for i in list:
        if i.get_id() == id:
            return True
    return False


def validate_credit():
    while True:
        credit = take_a_number("Course credit: ")
        if credit <= 0:
            print('Invalid input, the credit has to be > 0. Try again!')
        else:
            op.print_delimiter(0)
            return credit


def get_student_id(student_list):
    student_id = input('Enter the student ID: ')
    while not validate_id(student_id, student_list):
        print('Wrong student ID')
        student_id = input('Enter the student ID: ')
    return student_id


def get_course_id(course_list):
    course_id = input('Enter the course ID: ')
    while not validate_id(course_id, course_list):
        print('Wrong course ID')
        course_id = input('Enter the course ID: ')
    return course_id


def get_student_gpa(student_id, student_list):
    op.print_delimiter(0)
    for student in student_list:
        if student.get_id() == student_id:
            print(f"Student ID: {student_id} - GPA: {student.get_gpa()}")
            op.print_delimiter(0)


def is_empty(student_list, course_list):
    if len(student_list) == 0:
        op.print_empty_list("course list")
        return True
    elif len(course_list) == 0:
        op.print_empty_list("student list")
        return True


def write_to_file(file, todo, mode):
    f = open(file, mode)
    f.write(f"{todo}\n")
    f.close()


def action(c, system):
    if c == 0:
        exit()
    elif c == 1:
        system.new_student()
    elif c == 2:
        system.new_course()
    elif c == 3:
        if is_empty(system.get_student_list(), system.get_course_list()):
            return
        else:
            system.new_mark()
    elif c == 4:
        system.calculate_gpa(True)
        system.listing_students()
    elif c == 5:
        op.list_courses(system.get_course_list())
    elif c == 6:
        if is_empty(system.get_student_list(), system.get_course_list()):
            return
        else:
            op.list_marks(system.get_course_list())
    elif c == 7:
        if is_empty(system.get_student_list(), system.get_course_list()):
            return
        else:
            system.calculate_gpa(False)
            op.print_student_gpa(get_student_id(system.get_student_list()), system.get_student_list())
    else:
        print('Invalid input. Try again~')


def print_menu(system):
    running = True
    while running:
        try:
            b = int(input(' Press 1: Add Student Info'
                          '\n Press 2: Add Course Info'
                          '\n Press 3: Add student mark'
                          '\n Press 4: To List Student'
                          '\n Press 5: To List Course'
                          '\n Press 6: To show student marks for a given course'
                          '\n Press 7: Calculate student gpa'
                          '\n Press 0: Exit'
                          '\n Pressed: '))
        except ValueError:
            print('Invalid input. Try again~')
            continue
        else:
            action(b, system)
            print()

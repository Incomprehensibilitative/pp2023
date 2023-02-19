import time


def student_info(ids, name, dob, student_dic):
    student_dic[ids] = [name, dob]
    return student_dic


def course_info(ids, name, course_dic):
    course_dic[ids] = name
    return course_dic


def mark_info(names, course, mark, mark_dic):
    mark_dic[names] = [course, mark]
    return mark_dic


def mark_input(courses, students, marks):
    while course_id not in Courses:
        print('There is no such course ID. Please try again!')
        course_id = input('ID of the course: ')
    student_id = input('ID of the student: ')
    while student_id not in Students:
        print('There is no such student ID. Please try again!')
        student_id = input('ID of the student: ')
    mark = input('Mark of the course: ')
    if course_id in courses:
        if student_id in students:
            mark_info(student_id, course_id, mark, marks)
    return courses


def input_student():
    global Students
    while True:
        try:
            n = int(input('Enter number of Students: '))
        except ValueError:
            print('Invalid input, Try again!')
            continue
        else:
            break
    for i in range(n):
        name = input('Student name: ')
        ids = input('Student ID: ')
        dob = input('Student DoB: ')
        student_info(ids, name, dob, Students)


def input_course():
    global Courses
    while True:
        try:
            n = int(input('Enter number of Students: '))
        except ValueError:
            print('Invalid input, Try again!')
            continue
        else:
            break
    for i in range(n):
        name = input('Course name: ')
        ids = input('Course ID: ')
        course_info(ids, name, Courses)


def list_student():
    global Students
    print('Student list: ')
    for key, value in Students.items():
        print(f""""
            Student ID: {key}
            -------------------
            Student Name: {value[0]}
            Student DoB: {value[1]}
            """)
        time.sleep(2)


def list_course():
    global Courses
    print('Course list: ')
    for key, value in Courses.items():
        print(f""""
            Course name: {key}
            -------------------
            Course ID: {value}
            """)
        time.sleep(2)


def list_mark():
    global Marks
    print('Marks list: ')
    for key, val in Marks.items():
        print(f""""
                Student ID: {key}
                -------------------
                Course ID: {val[0]} 
                Marks: {val[1]}
                -------------------
                """)
        time.sleep(2)


def action(c):
    if c == 0:
        exit()
    elif c == 1:
        input_student()
    elif c == 2:
        input_course()
    elif c == 3:
        mark_input(Courses, Students, Marks)
    elif c == 4:
        list_student()
    elif c == 5:
        list_course()
    elif c == 6:
        list_mark()


if __name__ == "__main__":
    Students = {}
    Courses = {}
    Marks = {}
    running = True
    while running:
        b = int(input('Press 1: Add Student Info'
                      '\n Press 2: to Add Course Info'
                      '\n Press 3: Add student mark'
                      '\n Press 4: To List Student'
                      '\n Press 5: To List Course'
                      '\n Press 6: To show student marks for a given course'
                      '\n Press 0: exit'
                      '\n Pressed: '))
        action(b)
        print()
        print('Processing...')
        time.sleep(2)

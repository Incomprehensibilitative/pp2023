# classes
class Management:
    def __init__(self):
        self.__number_of_student = 0
        self.__number_of_course = 0
        self.__course_list = []
        self.__student_list = []

    def get_course_list(self):
        return self.__course_list

    def get_student_list(self):
        return self.__student_list

    def list_students(self):
        for c in self.__student_list:
            print()
            print(f'Student ID: {c.get_id()}\n'
                  f'Student name: {c.get_name()}\n'
                  f'Student DoB: {c.get_dob()}\n')

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
                for s in i.get_mark():
                    print(s)

    def new_student(self):
        print('Number of student')
        n = take_a_number()
        self.__number_of_student += n
        for i in range(n):
            ids = input('Student ID: ')
            name = input('Student name: ')
            dob = input('Student DoB: ')
            student = Students()
            student.set_student(ids, name, dob)
            self.__student_list.append(student)

    def new_course(self):
        print('Number of course')
        n = take_a_number()
        self.__number_of_course += n
        for i in range(n):
            ids = input('Course ID: ')
            name = input('Course name: ')
            course = Courses()
            course.set_course(ids, name)
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
        print(f'Enter the Mark for Student_id: {student_id} in Course_id {course_id}')
        mark = take_a_number()
        for i in self.__course_list:
            if i.get_id() == course_id:
                temp = [student_id, mark]
                i.set_mark(temp)


class Students:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__dob = ''

    def set_student(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob


class Courses:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__marks = []

    def set_course(self, id, name):
        self.__id = id
        self.__name = name

    def set_mark(self, temp):
        self.__marks.append(temp)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_mark(self):
        return self.__marks


# General functions
def take_a_number():
    while True:
        try:
            n = int(input('Enter a number: '))
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
        system.list_students()
    elif c == 5:
        system.list_courses()
    elif c == 6:
        system.list_marks()
    else:
        print('Invalid input. Try again~')


def main():
    system = Management()
    running = True
    while running:
        try:
            b = int(input('Press 1: Add Student Info'
                          '\n Press 2: to Add Course Info'
                          '\n Press 3: Add student mark'
                          '\n Press 4: To List Student'
                          '\n Press 5: To List Course'
                          '\n Press 6: To show student marks for a given course'
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

import input as ip
import domains as dm
import output as op


def main():
    system = dm.Management()
    ip.write_to_file("courses.txt", "Courses: ", "w")
    ip.write_to_file("courses.txt", op.print_delimiter(1), "a")
    ip.write_to_file("students.txt", "Students: ", "w")
    ip.write_to_file("students.txt", op.print_delimiter(1), "a")
    ip.write_to_file("marks.txt", "Marks: ", "w")
    ip.write_to_file("marks.txt", op.print_delimiter(1), "a")
    ip.print_menu(system)


if __name__ == "__main__":
    main()

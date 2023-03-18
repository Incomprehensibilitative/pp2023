import input as ip
import domains as dm


def main():
    system = dm.Management()
    system.check_files()
    ip.print_menu(system)


if __name__ == "__main__":
    main()

import input as ip
import Management


def main():
    system = Management.Management()
    system.check_files()
    system.restore()
    ip.print_menu(system)


if __name__ == "__main__":
    main()

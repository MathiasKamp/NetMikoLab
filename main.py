import os
import time
import MenuHandler


def cls():
    os.system('cls')


if __name__ == '__main__':

    running = True
    while running:
        cls()
        MenuHandler.print_main_menu()
        user_option = ''
        try:
            user_option = int(input("Enter your choice:"))
        except ValueError:
            print("Wrong input. Please enter a number")

        if user_option == 1:
            cls()
            MenuHandler.print_device_options()
            user_option = int(input("Enter your choice:"))
            if user_option == 1:  # user choose device configuration
                cls()
                MenuHandler.print_device_configuration_options()
                user_option = int(input("Enter your choice:"))

                if user_option == 1:  # user choose to change hostname
                    hostname = input("Enter hostname:")
                    MenuHandler.basis_options_change_hostname(hostname)
                    cls()

                elif user_option == 2:  # user choose to create a new ssh user with full privileges
                    cls()
                    username = input("Enter username:")
                    password = input("Enter password :")
                    MenuHandler.create_ssh_user(username, password)
                    cls()

                elif user_option == 3:  # user choose to implement default settings on the router
                    cls()
                    print("implementing default settings on the device")
                    MenuHandler.implement_default_settings()
                    cls()

                elif user_option == 4:  # user choose to set an ip address of an interface
                    cls()
                    interface = input("Enter interface eg. (fa 0/1) :")
                    ip_add = input("Enter ip address :")
                    subnet = input("Enter subnet :")
                    MenuHandler.add_ip_add_to_interface(interface, ip_add, subnet)
                    print(f"Adding {ip_add} {subnet} to {interface}")
                    time.sleep(2)
                    print("Done")
                    cls()

                elif user_option == 5:  # user choose to go back to main menu
                    cls()
                    print("returning..")
                    continue
            elif user_option == 2:
                cls()
                continue

        elif user_option == 2:
            cls()
            MenuHandler.print_monitoring_options()
            user_option = int(input("Enter your choice:"))
            if user_option == 1:
                cls()
                print("you've chosen to start the network traffic monitor")
                print("if you want to stop the network traffic monitor hold the q key on your keyboard")
                MenuHandler.start_traffic_monitor()
                print("press enter to quit")
                time.sleep(4)
                cls()
            elif user_option == 2:
                cls()
                print("you've chosen to start the trap monitor")
                print("if you want to stop the trap monitor restart program")
                MenuHandler.start_trap_monitor()
                cls()
            elif user_option == 3:
                cls()
                continue


        elif user_option == 3:  # user choose to exit program
            print("closing program")
            time.sleep(2)
            running = False

        else:  # user choose a number that is not on the main menu
            print("Enter a valid number")

import MenuHandler
import sys, os
import netmiko

if __name__ == '__main__':
    while True:
        MenuHandler.print_main_menu()

        user_option = ''
        try:
            user_option = int(input("Enter your choice:"))
        except ValueError:
            print("Wrong input. Please enter a number")

        if user_option == 1:
            os.system('cls')
            MenuHandler.main_menu_option_router_configuration()
            user_option = int(input("Enter your choice:"))
            if user_option == 1:
                os.system('cls')
                MenuHandler.print_basis_options()
                user_option = int(input("Enter your choice:"))
                if user_option == 1:
                    hostname = input("Enter hostname:")
                    MenuHandler.basis_options_change_hostname(hostname)
                    os.system('cls')

        elif user_option == 2:
            os.system('cls')
            MenuHandler.main_menu_option_switch_configuration()
            user_option = int(input("Enter your choice:"))
            if user_option == 1:
                os.system('cls')
                MenuHandler.print_basis_options()
                user_option = int(input("enter your choice:"))
                if user_option == 1:
                    os.system('cls')


        else:
            print("Enter a valid number")

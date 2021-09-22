import CommandHandler

basis_options = {
    1: 'Change hostname',
    2: 'Set ssh',
    3: 'enable secret',
    4: 'banner message of the day',
    5: 'Exit'
}

menu_options = {
    1: 'Router configuration',
    2: 'Switch configuration',
    3: 'Exit'
}

basis_option = {
    1: 'basis options'
}


def print_menu(menu):
    for key in menu.keys():
        print(key, '--', menu[key])


def print_basis_options():
    print_menu(basis_options)


def print_main_menu():
    print_menu(menu_options)


def main_menu_option_router_configuration():
    print_menu(basis_option)


def main_menu_option_switch_configuration():
    print_menu(basis_option)


def basis_options_change_hostname(hostname):
    CommandHandler.change_hostname(hostname)


def test_con():
    CommandHandler.test_methode()

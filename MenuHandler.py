# this file contains methods that are getting executed from the main gui program
# it works as a logic layer between gui and data layer
import CommandHandler
import NetworkTrafficListener
import TrapListener

# dictionary for main menu options
main_menu_options = {
    1: 'Configuration',
    2: 'Monitoring',
    3: 'Exit program'
}

# dictionary for monitoring options
monitoring_options = {
    1: 'network traffic listener',
    2: 'trap listener',
    3: 'Go back to main menu'
}

# dictionary for device options
device_options = {
    1: 'Router configuration',
    2: 'Switch configuration',
    3: 'Go to main menu'
}

# dictionary for basis options
basis_option = {
    1: 'Basic configurations',
    2: 'Show commands',
    3: 'Go to main menu'
}

# dictionary for basic configuration options for router and switch
basic_configuration_options = {
    1: 'Change hostname',
    2: 'Create user for ssh with full privileges',
    3: 'Default settings banner motd, no ip domain-lookup, enable secret etc.',
    4: 'Set ip address of an interface',
    5: 'Go to main menu'
}

# dictionary for basic show commands
show_commands = {
    1: 'Show running-config',
    2: 'Show arp',
    3: 'show vlan interfaces',
    4: 'Show ip interfaces',
    5: 'Write your own show command',
    6: 'Go to main menu'
}


# method to print a specific dictionary
def print_menu(menu):
    for key in menu.keys():
        print(key, '--', menu[key])


# method to print basic configuration
def print_basic_configuration_options():
    print_menu(basic_configuration_options)


def print_device_options():
    print_menu(device_options)


def print_main_menu():
    print_menu(main_menu_options)


def main_menu_option_router_configuration():
    print_menu(basis_option)


def main_menu_option_switch_configuration():
    print_menu(basis_option)


def basis_options_change_hostname(hostname):
    CommandHandler.change_hostname(hostname)


def implement_default_settings():
    CommandHandler.implement_default_settings()


def create_ssh_user(username, password):
    CommandHandler.create_ssh_user(username, password)


def add_ip_add_to_interface(interface, ip_add, subnet):
    CommandHandler.add_ip_add_to_interface(interface, ip_add, subnet)


def get_running_config():
    CommandHandler.get_running_config()


def print_show_commands():
    print_menu(show_commands)


def print_monitoring_options():
    print_menu(monitoring_options)


def start_traffic_monitor():
    NetworkTrafficListener.traffic_monitor()


def start_trap_monitor():
    TrapListener.RunTrap()

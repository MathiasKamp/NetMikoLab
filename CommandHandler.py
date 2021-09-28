# this file contains methods that executes commands on a cisco device
# import ConnectionHandler.py
import ConnectionHandler
# import netMiko
from netmiko import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from paramiko.ssh_exception import SSHException

# list of default commands that always should be executed on a new device
default_settings = [
    "no ip domain-lookup",
    "banner motd #unauthorized access to this device is prohibited!#",
    "service password-encryption",
]


# this method exits the user to user mode
def exit_to_user_mode(net_con):
    state = net_con.find_prompt()
    if state.__contains__("config"):
        net_con.exit_config_mode()
        net_con.exit_enable_mode()
    elif state.__contains__("#"):
        net_con.exit_enable_mode()


# this method navigates to privileged mode (#)
def go_to_privileged_mode(con):
    state = con.find_prompt()
    if state.__contains__(">"):
        con.enable()
    elif state.__contains__("config"):
        con.exit_config_mode()


# this method navigates to global config mode (config#)
def go_to_config_mode(con):
    state = con.find_prompt()
    if state.__contains__(">"):
        con.enable()
        con.config_mode()
    elif state.__contains__("#"):
        con.config_mode()


# this method changes the hostname of the device
def change_hostname(hostname):
    con = None
    try:
        con = ConnectionHandler.con()

    except(EOFError, SSHException, NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
    else:
        con.enable()
        con.config_mode()
        con.send_command(f"hostname {hostname}", expect_string=r"#")
        exit_to_user_mode(con)
    finally:
        con.disconnect()


# this method executes the list of default commands
def implement_default_settings():
    con = None

    try:
        con = ConnectionHandler.con()

    except(EOFError, SSHException, NetmikoTimeoutException, NetmikoAuthenticationException) as error:

        print(error)

    else:
        go_to_config_mode(con)
        con.send_config_set(default_settings)
        go_to_privileged_mode(con)
        con.save_config()

    finally:
        con.disconnect()


# this method creates a user for ssh connection with full privileges
def create_ssh_user(username, password):
    con = None
    try:
        con = ConnectionHandler.con()

    except(EOFError, SSHException, NetmikoTimeoutException, NetmikoAuthenticationException) as error:

        print(error)

    else:
        go_to_config_mode(con)
        con.send_command(f"username {username} privilege 15 password {password}", expect_string=r"#")
        exit_to_user_mode(con)
    finally:
        con.disconnect()


# this method adds a ip address to a specific interface
def add_ip_add_to_interface(interface, ip_add, subnet):
    con = None
    interface_ip_add_command = [
        f'int {interface}',
        f'ip add {ip_add} {subnet}',
        'no shutdown'
    ]
    try:
        con = ConnectionHandler.con()
    except(EOFError, SSHException, NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
    else:
        con.send_config_set(interface_ip_add_command)
    finally:
        con.disconnect()


# this method executes the (show running-config) command
def run_show_command(command):
    con = None
    output = None
    try:
        con = ConnectionHandler.con()
    except(EOFError, SSHException, NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
    else:
        go_to_privileged_mode(con)
        output = con.send_command_timing(command)

    finally:
        con.disconnect()
        return output


# this method runs show ip int brief
def get_ip_interfaces():
    return run_show_command("show ip int brief")


# this method runs show arp command
def get_arp():
    return run_show_command("show arp")


# this method runs show running-config command
def get_running_config():
    return run_show_command("show running-config")


# this method runs the command that the user has inserted
def get_with_user_defined_command(command):
    return run_show_command(command)


# this method runs show vlan brief command
def get_vlan_interfaces():
    return run_show_command("show vlan brief")


# this method runs the show version command
def get_version():
    return run_show_command("show version")



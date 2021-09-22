import ConnectionHandler
from netmiko import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from paramiko.ssh_exception import SSHException


def exit_to_user_mode(net_con):
    state = net_con.find_prompt()
    if state.__contains__("config"):
        net_con.exit_config_mode()
        net_con.exit_enable_mode()
    elif state.__contains__("#"):
        net_con.exit_enable_mode()


def change_hostname(hostname):
    net_conn = None
    try:
        net_conn = ConnectionHandler.con()

    except (EOFError, SSHException, NetmikoTimeoutException, NetmikoAuthenticationException):

        print("no connection to device")
    else:
        net_conn.enable()
        net_conn.config_mode()
        net_conn.send_command(f"hostname {hostname}", expect_string=r"#")
        exit_to_user_mode(net_conn)
    finally:
        net_conn.disconnect()


def show_arp():
    conn = ConnectionHandler.con()
    output = conn.send_command_timing("show arp")
    print(output)
    conn.disconnect()

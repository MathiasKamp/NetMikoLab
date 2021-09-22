# ConnectHandler
# ssh usr = mathias, pass = cisco
# privileged pass = class
from netmiko import Netmiko
from getpass import getpass
from netmiko import ConnectHandler

router = {
    'host': "192.168.1.1",
    'username': "mathias",
    'password': "cisco",
    'secret': "class",
    'device_type': 'cisco_ios'
}


def con():
    return ConnectHandler(**router)

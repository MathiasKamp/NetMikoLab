# ConnectHandler
# this class handles the connection to the different devices
from netmiko import ConnectHandler
# dictionary that holds the routers login information
router = {
    'host': "192.168.1.1",
    'username': "mathias",
    'password': "cisco",
    'secret': "class",
    'device_type': 'cisco_ios'
}


# method to return a connection handler to the router
def con():
    return ConnectHandler(**router)

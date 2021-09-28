# this file contains methods and logic to create an network traffic listener
from datetime import datetime as d
import keyboard
import time
from pysnmp.hlapi import *
import SmnpHandler
import XMLWriter

# basic device information
device_add = '192.168.1.1'
public_community = 'public'
private_community = 'private'
oid_ip_traffic = '1.3.6.1.2.1.4.9.0'
trap_port = 162


# this method starts the traffic monitor
def traffic_monitor():
    # call get command from SmnpHandler and get a dictionary of values back
    traffic_value = SmnpHandler.get(device_add, [oid_ip_traffic], CommunityData(public_community))

    # create a dictionary to to be added to the network traffic dictionary. in order to know when this network
    # traffic has been read
    time_dict = {
        'time': d.now()
    }

    running = True
    while running:
        # if the user is pressing q we quit the network traffic listener
        if keyboard.is_pressed('q'):
            running = False

        else:
            # add the time dictionary to the network traffic dictionary
            traffic_value.update(time_dict)
            # write the dictionary to an xml file
            XMLWriter.dict_to_xml_file(traffic_value, "network_traffic")
            time.sleep(5)

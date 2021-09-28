# this file contains methods and logic to create a handler for smnp
from pysnmp.hlapi import *

# basic device settings
device_ip_add = "192.168.1.1"
snmp_port = 161


# this method is used to get the oid values of the device
def get(target, oids, credentials, port=161, engine=SnmpEngine(), context=ContextData()):
    handler = getCmd(
        engine,
        credentials,
        UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)  # add a list of oid's to be handled
    )
    return fetch(handler, 1)[0]


# this method is returning a list of objectTypes bases on the oid
def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(ObjectType(ObjectIdentity(oid)))
    return object_types


# this method fetches the data from the handler
def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            # next handler
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                # add the data of the handler to an result list
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break
    return result


# this method checks the value value and return it with its corresponding data type.
def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value

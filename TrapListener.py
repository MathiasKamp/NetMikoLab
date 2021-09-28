# this file contains methods and logic to create a trap listener
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import XMLWriter


snmpEngine = engine.SnmpEngine()
# ipaddress and port of the computer running the TrapListener.py
TrapAgentAddress = '192.168.1.2'
Port = 162

# this method sets the default configuration of the transport connection to the snmp-server in this case a router
def initialize_trap_listener_config():
    config.addTransport(
        snmpEngine,
        udp.domainName + (1,),
        udp.UdpTransport().openServerMode((TrapAgentAddress, Port))
    )
    # this part adds the communityName (public) to the config
    config.addV1System(snmpEngine, 'public', 'public')


# this method collects the data whenever the traps gets triggered
def values_collector(snmpEngine, stateReference, contextEngineId, contextName,
          varBinds, cbCtx):
    # convert the data to a dictionary
    dict_of_values = put_trap_values_in_dict(varBinds)
    # write the dictionary to an xml file
    XMLWriter.dict_to_xml_file(dict_of_values, "trap_listener")


# thi method converts the data from the trap into a dictionary
def put_trap_values_in_dict(varBinds):
    result_dict = {}
    for name, val in varBinds:
        temp_dict = {
            name.prettyPrint(): val.prettyPrint()
        }
        result_dict.update(temp_dict)
    return result_dict


# this method starts the trap listener
def RunTrap():
    try:
        # initialize the default config
        initialize_trap_listener_config()
        # sets the notificationReceiver to be values_collector
        ntfrcv.NotificationReceiver(snmpEngine, values_collector)

        snmpEngine.transportDispatcher.jobStarted(1)
        print("Agent is listening SNMP Trap on " + TrapAgentAddress + " , Port : " + str(Port))

        # start the trap listener
        snmpEngine.transportDispatcher.runDispatcher()

    finally:

        # close the trap listener
        snmpEngine.transportDispatcher.closeDispatcher()

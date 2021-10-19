#!/usr/bin/env python
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, context
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext

import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def run_server():

    # Setting up datastore for test slaves all to zero
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0,[1]*100),
        co=ModbusSequentialDataBlock(0,[1]*100),
        hr=ModbusSequentialDataBlock(0,[1]*100),
        ir=ModbusSequentialDataBlock(0, [1]*100))
    
    context = ModbusServerContext(slaves=store, single=True)


    # Setting up server identification
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'CODE ICS Emulation Lab'
    identity.ProductCode = 'Test'
    identity.ProductName = "Modbus Test Server"
    identity.ModelName = "Modbus Test Server"

    # Initialize and start the server
    StartTcpServer(context, identity=identity, address=("",502))


if __name__ == "__main__":
    run_server()

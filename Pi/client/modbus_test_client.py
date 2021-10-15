#!/usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# Error Logging
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Define slave ID
UNIT = 0x1

def run_client():
    client = ModbusClient('localhost', port=5020)
    client.connect()

    log.debug("Reading Coil 1")
    coil = client.read_coils(1, 8, unit=UNIT)
    print(dir(coil))
    print(coil.function_code)
    print(coil.protocol_id)
    print(coil.bits)
    client.close()

if __name__ == "__main__":
    run_client()
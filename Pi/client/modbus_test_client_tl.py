#!/usr/bin/env python
from time import sleep
from sense_hat import SenseHat
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

traffic_light = {
    "green": (0,255,0),
    "yellow": (255,255,0),
    "red": (255,0,0)
}

def run_client():
    client = ModbusClient(host='10.190.27.206', port=502)
    client.connect()

    curr_color = "green"
    sense = SenseHat()
    sense.clear(traffic_light[curr_color])

    while(True):
        log.debug("Reading Coil 1")
        coil = client.read_coils(1, 8, unit=UNIT)
        print(dir(coil))
        print(coil.function_code)
        print(coil.protocol_id)
        print(coil.bits)

        if(coil.bits[0] == True):    
            if(curr_color == "green"):
                curr_color = "yellow"
            elif(curr_color == "yellow"):
                curr_color = "red"
            elif(curr_color == "red"):
                curr_color = "green"

        sense.clear(traffic_light[curr_color])
        sleep(2)

    client.close()


if __name__ == "__main__":
    run_client()
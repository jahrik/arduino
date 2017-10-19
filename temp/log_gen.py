#!/usr/bin/env python
"""
Input temp and humid logs from arduino
Output temp.json
"""
import time
import datetime
import sys
import json
import serial

PORT = sys.argv[1]

try:
    SER = serial.Serial(PORT, 9600, timeout=1)

except serial.SerialException as exc:
    print(exc)

time.sleep(3)
for i in range(0, 10):
    while True:
        try:
            DATA = SER.readline()[:-2]  # the last bit gets rid of the new-line chars
            if DATA:
                stamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                data = json.loads(DATA.decode('utf8'))
                data['date'] = stamp
                with open('temps.json', 'a') as outfile:
                    outfile.write(json.dumps(data, indent=4, sort_keys=True))
                    outfile.write(',\n')

        except serial.SerialException as exc:
            # There is no new data from serial port
            print(exc)

        except TypeError as exc:
            # Disconnect of USB->UART occured
            print(exc)

        except ValueError as exc:
            # json errors
            print(exc)

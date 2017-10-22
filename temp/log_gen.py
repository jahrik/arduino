#!/usr/bin/env python
"""
Input temp and humid logs from arduino
Add timestamp
Convert Celsius to Fahrenheit
Output temp.json
"""
import time
import datetime
import sys
import json
import serial

PORT = sys.argv[1]


def get_serial():
    """
    Connect to serial port
    """
    try:
        ser = serial.Serial(PORT, 9600, timeout=1)

    except serial.SerialException as exc:
        print(exc)

    return ser


def c_to_f(temp_c):
    """
    input Celsius
    output Fahrenheit
    """
    temp_f = int(9.0)/int(5.0) * int(temp_c) + int(32)
    return temp_f


def main():
    """
    main functions
    """
    ser = get_serial()
    time.sleep(3)
    for _int in range(0, 10):
        while True:
            try:
                data = ser.readline()[:-2]  # the last bit gets rid of the new-line chars
                if data:
                    stamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                    json_data = json.loads(data.decode('utf8'))
                    json_data['date'] = stamp
                    temp_f = c_to_f(json_data['temp'])
                    json_data['temp_f'] = str(temp_f)
                    with open('/data/temps.json', 'a') as outfile:
                        outfile.write(json.dumps(json_data, indent=4, sort_keys=True))
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


if __name__ == '__main__':

    main()

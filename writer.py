#!./venv/bin/python

import serial
import time

port_address = "/dev/pts/1"
ser = serial.Serial(port_address, 9600)

while True:
    data = "test_data\n"
    ser.write(data.encode())
    print(f"Sent: {data.strip()}")
    time.sleep(2)
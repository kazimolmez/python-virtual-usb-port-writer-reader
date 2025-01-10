#!./venv/bin/python

import serial

port_address = "/dev/pts/2"
ser = serial.Serial(port_address, 9600)

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print(f"Received: {data}")
        if data == "test_data":
            print("Success...")
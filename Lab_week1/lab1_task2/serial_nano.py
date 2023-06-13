# Poject: Lab1_task3
# Group: G
# Students: Rob Bieman, Mike Nieuweboer
# Date: 8 juni 2023
#
# Python program to communicate with the pre-programmed
# Arduino nano 33 IoT through a serial connection

import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)


def write_read(x):

    # send command
    if x != "status":
        x = x.capitalize()
    arduino.write(x.encode())

    # time for arduino to respond
    time.sleep(1.1)

    # receive data and convert to ascii
    data = arduino.readline().decode('ascii')

    return data


while True:

    # taking input from user
    command = input("command > ")

    # send command and receive response
    response = write_read(command)

    # printing the value
    print(response, end='')

# commandline serial tool

import serial

port = input("Enter port name ")

ser = serial.Serial('com'+port, 9600, timeout = 1)

print(ser)

#print([a for a in dir(ser) if not a.startswith('__')])

#deviceAttributes = dir(__builtins__)

#print(deviceAttributes)

baudrate = ser.baudrate

print(f'The baudrate: {baudrate:}.')

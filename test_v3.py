import serial
from time import sleep
import sys
import numpy as np

COM_PORT='COM7'
BAUD_RATES=9600


if __name__=='__main__':
    print("777")
    ser = serial.Serial(COM_PORT,BAUD_RATES,timeout=0.5)
    sx = 'Green'
    print('888')

    try :
        while True:
            sx = 'Green'
            ser.write(sx.encode('ascii'))
            sleep(2)
            while ser.in_waiting:
                mcu_feedback = ser.readline().decode()
                print('控制板回應:',mcu_feedback)
            sx = 'Red'
            ser.write(sx.encode('ascii'))
            sleep(2)
            while ser.in_waiting:
                mcu_feedback = ser.readline().decode()
                print('控制板回應:',mcu_feedback)
    except KeyboardInterrupt:
        ser.close()
        print('bey eye')
    print("end")
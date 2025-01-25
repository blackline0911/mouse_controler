import serial
from time import sleep
import sys
import numpy as np

COM_PORT='COM7'
BAUD_RATES=9600
def sin(t):
    return np.sin(2*np.pi/20*t)

if __name__=='__main__':
    print("777")
    ser = serial.Serial(COM_PORT,BAUD_RATES,timeout=0.5)
    # sx = 'Green'
    print('888')
    t = 0 
    try :
        while True:
            sx = sin(t)
            print('signal : ',sx)
            ser.write(str( int( sx*255) ).encode('ascii') )
            sleep(3)
            while ser.in_waiting:
                mcu_feedback = ser.readline().decode()
                print('控制板回應:',mcu_feedback)
            t += 1
    except KeyboardInterrupt:
        ser.close()
        print('bey eye')
    print("end")
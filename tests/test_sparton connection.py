#!/usr/bin/env python3

''' test_imu.py  - Tests the basic connection to the IMU, and filters by gathering
    all available data followed by filtering it.   The filtered data will be displayed
    the data to the terminal.
'''
# from imu_framework.imus.imu_9250 import imu_9250
# from imu_framework.imu_tools import imu_tools
import serial
import time

##
# @brief Main test code used to access all information from the IMU(s), filter it, and pass it on
# @param rawImuData initializes the IMU for use
# @param separation Separates the tuple obtained from the IMU(s) into their respective measurements
# @return separation Returns 9 DOF variables
if __name__ == '__main__':
    b = bytes('\r\n\r\nprinttrigger 1 s.p set drop\r\n', 'utf-8')
    endd = bytes('\r\n\r\nprinttrigger 0 s.p set drop\r\n', 'utf-8')
    # wait = bytes('delay 1000 \r\n', 'utf-8')
    # b1 = bytes('accelr di.\r\n', 'utf-8')
    # b2 = bytes('gyror di.\r\n', 'utf-8')
    # b3 = bytes('magr di.\r\n', 'utf-8')
    ser = serial.Serial(timeout=2,xonxoff=1, baudrate=115200)
    ser.port = 'COM4'

    ser.open()
    # ser.write(b)
    # # ser.write(wait)
    # thus1 = ser.read(65)
    # i =0
    # while i<=5:
    #     ser.flush()
    #     thus1 = ser.readline()
    #     ser.flush()
    #     # ser.write(wait)
    #
    #     print('thus  = ', str(thus1))
    #     v = thus1.decode("utf-8").split(',')
    #     print('v3 = ', v[9])
    #     i+=1

    ser.close()

    #
    #
    #
    # # thus2 = ser.read(100)
    # # ser.flush()
    # # print('end = ', thus2)
    #
    # #
    # # ser.write(b2)
    # # thus2 = ser.read(100)
    # # ser.flush()
    # #
    # # ser.write(b3)
    # # thus3 = ser.read(100)
    # # ser.flush()
    # ser.write(endd)
    # ser.close()
    #
    # # print(thus1)
    # # print()
    # # print(thus2)
    # # print()
    # # print(thus3)
from imu_framework.imus.imu_this_is_sparton_no_thread import imu_this_is_starta
if __name__ == '__main__':
    myIMU = imu_this_is_starta()
    rawImuData = 0
    myIMU.connect()
    i = 0
    while i <= 2000:
        myIMU.setData()
        rawImuData = myIMU.getAllAvalableData()

        XAaccel = rawImuData[0]
        YAaccel = rawImuData[1]
        ZAaccel = rawImuData[2]

        XRotGyro = rawImuData[3]
        YRotGyro = rawImuData[4]
        ZRotGyro = rawImuData[5]

        XMagno = rawImuData[6]
        YMagno = rawImuData[7]
        ZMagno = rawImuData[8]

        print('x ', XAaccel, ' y ',YAaccel ,' z ', ZAaccel, ' x ', XRotGyro, ' y ',YRotGyro ,' z ', ZRotGyro,' x ', XMagno, ' y ',YMagno ,' z ', ZMagno)

        i +=1
    myIMU.disconnect()
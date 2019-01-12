import time
import threading
# from Adafruit_BME280 import *
import sqlite3
# import serial
import random

# sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)


# ser = serial.Serial('/dev/ttyAMA0', baudrate=9600)

def current_milli_time():
    return int(round(time.time() * 1000))


def init():
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS temps (time bigint, degree double)")
    c.execute("CREATE TABLE IF NOT EXISTS speeds (time bigint, speed double)")
    c.execute("CREATE TABLE IF NOT EXISTS pressures (time bigint, pressure double)")

    conn.commit()
    conn.close()
    threading.Thread(target=reader, args=()).start()


def reader():
    while 1:
        # Constant testing data
        # add_temp(25)
        # add_pressure(1013)
        # add_speed(10)

        # Random testing data
        add_temp(random.randint(-10, 25))
        add_pressure(random.randint(100000, 105000) / 100)
        add_speed(random.randint(0, 40))

        # Actual data
        # add_temp(sensor.read_temperature())
        # add_pressure(sensor.read_pressure() / 100)
        # if ser.inWaiting() > 0:
        #     add_speed(float(ser.read()))
        time.sleep(1)


def add_temp(temp):
    millis = current_milli_time()
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO temps (time, degree) VALUES ('" + str(millis) + "', '" + str(temp) + "' )")
    conn.commit()
    conn.close()


def add_pressure(pressure):
    millis = current_milli_time()
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO pressures (time, pressure) VALUES ('" + str(millis) + "', '" + str(pressure) + "' )")
    conn.commit()
    conn.close()


def add_speed(speed):
    millis = current_milli_time()
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO speeds (time, speed) VALUES ('" + str(millis) + "', '" + str(speed) + "' )")
    conn.commit()
    conn.close()

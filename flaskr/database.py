import time
import threading
from Adafruit_BME280 import *
import sqlite3
import serial
import random

ser = serial.Serial("/dev/ttyUSB0", 9600)
ser.flushInput()
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

def current_milli_time():
    return int(round(time.time() * 1000))


def init():
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS temps (time bigint, degree int)")
    c.execute("CREATE TABLE IF NOT EXISTS speeds (time bigint, speed double)")
    c.execute("CREATE TABLE IF NOT EXISTS presures (time bigint, speed double)")
    conn.commit()
    conn.close()
    threading.Thread(target=reader, args=()).start()


def reader():
    add_temp(sensor.read_temperature())
    add_presure(sensor.read_pressure()/100)
    add_speed(random.randint(0, 40))


def add_temp(temp):
    time = current_milli_time()
    # Keep list at length 5 History will be added latestx
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO temps (time, degree) VALUES ('" + str(time) + "', '" + str(temp) + "' )")
    conn.commit()
    conn.close()


def add_presure(presure):
    time = current_milli_time()
    # Keep list at length 5 History will be added latestx
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO presures (time, presure) VALUES ('" + str(time) + "', '" + str(presure) + "' )")
    conn.commit()
    conn.close()


def add_speed(speed):
    time = current_milli_time()
    # Keep list at length 5 History will be added latest
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO speeds (time, speed) VALUES ('" + str(time) + "', '" + str(speed) + "' )")
    conn.commit()
    conn.close()

import time
import threading
import random
import sqlite3
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)
ser.flushInput()


def current_milli_time():
    return int(round(time.time() * 1000))


def init():
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS temps (time bigint, degree int)")
    c.execute("CREATE TABLE IF NOT EXISTS speeds (time bigint, speed double)")
    conn.commit()
    conn.close()
    threading.Thread(target=reader, args=()).start()


def reader():
    while 1:
        linein = ser.readline()
        if linein != "":
            print(linein)


def add_temp(temp):
    time = current_milli_time()
    # Keep list at length 5 History will be added latestx
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO temps (time, degree) VALUES ('" + str(time) + "', '" + str(temp) + "' )")
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

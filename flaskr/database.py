import time
import threading
import random
import sqlite3


def current_milli_time():
    return int(round(time.time() * 1000))


def init():
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS temps (time bigint, degree int)")
    c.execute("CREATE TABLE IF NOT EXISTS speeds (time bigint, speed double)")
    conn.commit()
    conn.close()
    threading.Thread(target=dummy_data, args=()).start()


def dummy_data():
    while 1:
        add_temp(random.randint(-10, 30))
        add_speed(random.uniform(0.0, 50.0))
        time.sleep(1)


def add_temp(temp):
    time = current_milli_time()
    # Keep list at length 5 History will be added latest
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

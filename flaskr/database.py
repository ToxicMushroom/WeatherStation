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
    conn.commit()
    conn.close()
    threading.Thread(target=dummy_data, args=()).start()


def dummy_data():
    while 1:
        add_temp(random.randint(-10, 30))
        time.sleep(1)


def add_temp(temp):
    time = current_milli_time()
    # Keep list at length 5 History will be added latest
    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("INSERT INTO temps (time, degree) VALUES ('" + str(time) + "', '" + str(temp) + "' )")
    conn.commit()
    conn.close()

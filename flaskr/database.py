import time
import threading
import random

temperatuur_list = {"temperaturen": []}


def current_milli_time():
    return int(round(time.time() * 1000))


def init():
    threading.Thread(target=dummy_data, args=()).start()

def dummy_data():
    while 1:
        add_temp(random.randint(-10, 30))
        time.sleep(5)


def add_temp(temp):
    temperatuur_list["temperaturen"].append({'time': current_milli_time(), 'temp': temp})


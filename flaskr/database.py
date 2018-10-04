import time
import threading
import random

stats_list = {"temperaturen": []}


def current_milli_time():
    return int(round(time.time() * 1000))


def init():
    threading.Thread(target=dummy_data, args=()).start()

def dummy_data():
    while 1:
        add_temp(random.randint(-10, 30))
        time.sleep(5)


def add_temp(temp):
    #Keep list at length 5 History will be added latest
    if len(stats_list["temperaturen"]) > 4:
        stats_list["temperaturen"][0] = stats_list["temperaturen"][1]
        stats_list["temperaturen"][1] = stats_list["temperaturen"][2]
        stats_list["temperaturen"][2] = stats_list["temperaturen"][3]
        stats_list["temperaturen"][3] = stats_list["temperaturen"][4]
        stats_list["temperaturen"].pop()

    stats_list["temperaturen"].append({'time': current_milli_time(), 'temp': temp})


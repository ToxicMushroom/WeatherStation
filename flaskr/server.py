import math
import sqlite3
import re

from flask import Flask, render_template, jsonify, request
import database

app = Flask(__name__)
pattern = re.compile("\\d+")

database.init()


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/api/temperatuur", methods=['GET'])
def api_temp():
    size = request.args.get('size')
    minuten = request.args.get('minuten')

    if not pattern.match(str(size)):
        size = 5
    else:
        size = int(request.args.get('size'))

    if not pattern.match(str(minuten)):
        minuten = 1
    else:
        minuten = int(request.args.get('minuten'))

    volledige_lijst = []

    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("SELECT time, degree FROM temps WHERE time > " + str(database.current_milli_time() - minuten * 60 * 1000))
    for row in c.fetchall():
        volledige_lijst.append({'time': row[0], 'degree': row[1]})
    conn.close()

    lijst = []

    start = 0
    end = len(volledige_lijst)
    step = int(math.ceil(len(volledige_lijst) / size))

    for i in range(start, end, step):
        average = volledige_lijst[i].copy()
        loops = 1
        for b in range(i, i + step):
            if b < len(volledige_lijst) and b is not i:
                loops += 1
                average['degree'] += volledige_lijst[b]['degree']
        average['degree'] = average['degree'] / loops
        lijst.append(average)
    return jsonify(lijst)


@app.route("/api/druk", methods=['GET'])
def api_pressure():
    size = request.args.get('size')
    minuten = request.args.get('minuten')

    if not pattern.match(str(size)):
        size = 5
    else:
        size = int(request.args.get('size'))

    if not pattern.match(str(minuten)):
        minuten = 1
    else:
        minuten = int(request.args.get('minuten'))

    volledige_lijst = []

    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute(
        "SELECT time, pressure FROM pressures WHERE time > " + str(database.current_milli_time() - minuten * 60 * 1000))
    for row in c.fetchall():
        volledige_lijst.append({'time': row[0], 'pressure': row[1]})
    conn.close()

    lijst = []

    start = 0
    end = len(volledige_lijst)
    step = int(math.ceil(len(volledige_lijst) / size))

    for i in range(start, end, step):
        average = volledige_lijst[i].copy()
        loops = 1
        for b in range(i, i + step):
            if b < len(volledige_lijst) and b is not i:
                loops += 1
                average['pressure'] += volledige_lijst[b]['pressure']
        average['pressure'] = average['pressure'] / loops
        lijst.append(average)
    return jsonify(lijst)


@app.route("/api/windsnelheid", methods=['GET'])
def api_speed():
    size = request.args.get('size')
    minuten = request.args.get('minuten')

    if not pattern.match(str(size)):
        size = 5
    else:
        size = int(request.args.get('size'))

    if not pattern.match(str(minuten)):
        minuten = 1
    else:
        minuten = int(request.args.get('minuten'))

    volledige_lijst = []

    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute(
        "SELECT time, speed FROM speeds WHERE time > " + str(database.current_milli_time() - minuten * 60 * 1000))
    for row in c.fetchall():
        volledige_lijst.append({'time': row[0], 'speed': row[1]})
    conn.close()

    lijst = []

    start = 0
    end = len(volledige_lijst)
    step = int(math.ceil(len(volledige_lijst) / size))

    for i in range(start, end, step):
        average = volledige_lijst[i].copy()
        loops = 1
        for b in range(i, i + step):
            if b < len(volledige_lijst) and b is not i:
                loops += 1
                average['speed'] = average['speed'] + volledige_lijst[b]['speed']
        average['speed'] = average['speed'] / loops
        lijst.append(average)
    return jsonify(lijst)


if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')

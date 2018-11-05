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
    last_i = 0
    for i in range(0, len(volledige_lijst), math.ceil(len(volledige_lijst) / size)):
        gemmidelde = volledige_lijst[i]
        if i != 0:
            for b in range(last_i, i):
                gemmidelde['degree'] = gemmidelde['degree'] + volledige_lijst[b]['degree']
            gemmidelde['degree'] = gemmidelde['degree'] / math.ceil(len(volledige_lijst) / size)
        lijst.append(gemmidelde)
        last_i = i

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
    last_i = 0
    for i in range(0, len(volledige_lijst), math.ceil(len(volledige_lijst) / size)):
        gemmidelde = volledige_lijst[i]
        if i != 0:
            for b in range(last_i, i):
                gemmidelde['speed'] = gemmidelde['speed'] + volledige_lijst[b]['speed']
            gemmidelde['speed'] = gemmidelde['speed'] / math.ceil(len(volledige_lijst) / size)
        lijst.append(gemmidelde)
        last_i = i

    return jsonify(lijst)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


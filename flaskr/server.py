import math
import sqlite3

from flask import Flask, render_template, jsonify, request
import database

app = Flask(__name__)

database.init()


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/api/temperatuur", methods=['GET'])
def api():
    size = request.args.get('size')
    minuten = request.args.get('minuten')

    if size is None:
        size = 5
    else:
        size = int(request.args.get('size'))

    if minuten is None:
        minuten = 1
    else:
        minuten = int(request.args.get('minuten'))

    lijst = []

    conn = sqlite3.connect('stats.db')
    c = conn.cursor()
    c.execute("SELECT time, degree FROM temps WHERE time > " + str(database.current_milli_time() - minuten * 60 * 1000))
    for row in c.fetchall():
        lijst.append({'time': row[0], 'degree': row[1]})
    conn.close()

    math.ceil(len(lijst)/size)
    return jsonify(lijst)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

from flask import Flask, render_template, jsonify
import database

app = Flask(__name__)

database.init()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/")
def api():
    return jsonify(database.temperatuur_list)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

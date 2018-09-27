from flask import Flask
import random
import js

app = Flask(__name__)

styles = """
* {
  padding: 0;
  margin: 0;
  color: white;
  font-family: Roboto, Arial, Helvetica, sans-serif;
}

body {
  background-color: #36393f;
}

div.main-wrapper {
  margin: 5px;
}

div.subtitle {
    text-align:center;
    margin: 30px auto;
}
"""

shart_script = """
window.onload = function () {

var temp-chart = new CanvasJS.Chart('temp-graph', {
  animationEnabled: true,
  theme: 'dark1',
    title:{
        text: 'Temperatuur'
    },
    axisY:{
        includeZero: false
    },
    data: [{        
        type: 'line',       
        dataPoints: [
            {x: 0, y: 450 },
            {x: 1, y: 414 },
            {x: 2, y: 520 },
            {x: 3, y: 460 },
            {x: 4, y: 450 },
            {x: 5, y: 500 },
            {x: 6, y: 480 },
            {x: 7, y: 480 },
            {x: 8, y: 410 },
            {x: 9, y: 500 },
            {x: 10, y: 480 },
            {x: 11, y: 510 }
        ]
    }]
});
temp-chart.render();
}
"""


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>stats</title>
        <style>
        """ + styles + """
        </style>
        
    </head>
    <body>
        <div class='main-wrapper'>
        <div id='temp-block'>
            <div class='subtitle'>Temperature</div>
            <div id='temp-graph' class='graph'></div> 
        </div>
        </div>
            <script type="text/javascript">""" + js.canvasjs + """</script>
            <script type="text/javascript">""" + shart_script + """</script>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


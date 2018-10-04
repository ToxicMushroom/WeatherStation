let tempChart;

window.onload = function () {
    tempChart = new CanvasJS.Chart("temp-graph", {
        backgroundColor: "#202225",
        animationEnabled: true,
        theme: 'dark2',
        axisX: {
            title: "Tijd"
        },
        axisY: {
            title: "Graden Celcius",
            includeZero: false
        },
        data: [{
            type: 'area',
            dataPoints: [
                {x: 0, y: 0}
            ]
        }]
    });
    tempChart.render();
    console.log(tempChart.options.data[0].dataPoints);
    dataUpdater()
};

function dataUpdater() {
    const httpreq = new XMLHttpRequest();
    httpreq.open("GET", "http://localhost/api/", false);
    httpreq.send(null);
    var list = [];
    var temps = JSON.parse(httpreq.responseText)["temperaturen"];
    for (var key in temps) {
        list.push({label: msToTime(temps[key]["time"]), y: temps[key]["temp"]});
    }
    console.log(list);
    tempChart.options.data[0].dataPoints = list;
    tempChart.render();
    setTimeout(dataUpdater, 5000);
}

function msToTime(duration) {
    var seconds = parseInt((duration / 1000) % 60),
        minutes = parseInt((duration / (1000 * 60)) % 60),
        hours = parseInt((duration / (1000 * 60 * 60)) % 24);

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    return hours + ":" + minutes + ":" + seconds;
}

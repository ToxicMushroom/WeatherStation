let tempChart;
let tempSize = 5;
let tempMinuten = 1;


window.onload = function () {
    tempChart = new CanvasJS.Chart("temp-graph", {
        backgroundColor: "#202225",
        animationEnabled: true,
        theme: 'dark2',
        title: {
            text: "Temperatuur",
            fontWeight: "normal",
            fontFamily: "roboto",
            fontSize: 30
        },
        axisX: {
            title: "Tijd",
            titleFontWeight: "normal",
            titleFontFamily: "roboto",
            fontSize: 20
        },
        axisY: {
            title: "Graden Celcius",
            titleFontWeight: "normal",
            titleFontFamily: "roboto",
            fontSize: 20,
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
    httpreq.open("GET", "http://localhost/api/temperatuur?size=" + tempSize + "&minuten=" + tempMinuten, false);
    httpreq.send(null);
    var list = [];
    var temps = JSON.parse(httpreq.responseText);
    for (var key in temps) {
        list.push({label: msToTime(temps[key]["time"]), y: temps[key]["degree"]});
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

function updateInput(val) {

}

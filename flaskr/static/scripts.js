let tempChart;
let tempSize = 5;
let tempMinuten = 1;


let speedChart;
let speedSize = 5;
let speedMinuten = 1;


let presureChart;
let presureSize = 5;
let presureMinuten = 1;

const host = "localhost";

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
speedChart = new CanvasJS.Chart("speed-graph", {
    backgroundColor: "#202225",
    animationEnabled: true,
    theme: 'dark2',
    title: {
        text: "WindSnelheid",
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
        title: "Snelheid in km/h",
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

presureChart = new CanvasJS.Chart("presure-graph", {
    backgroundColor: "#202225",
    animationEnabled: true,
    theme: 'dark2',
    title: {
        text: "LuchtDruk",
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
        title: "Druk in hPa",
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

speedChart.render();
tempChart.render();
presureChart.render();
tempDataUpdater();
speedDataUpdater();
presureDataUpdater();

function tempDataUpdater() {
    const httpreq_temp = new XMLHttpRequest();
    httpreq_temp.open("GET", "http://" + host + "/api/temperatuur?size=" + tempSize + "&minuten=" + tempMinuten, false);
    httpreq_temp.send(null);
    var list = [];
    var temps = JSON.parse(httpreq_temp.responseText);
    for (var key in temps) {
        list.push({label: msToTime(temps[key]["time"]), y: temps[key]["degree"]});
    }
    tempChart.options.data[0].dataPoints = list;
    tempChart.render();
    setTimeout(tempDataUpdater, 5000);
}

function speedDataUpdater() {
    const httpreq_speed = new XMLHttpRequest();
    httpreq_speed.open("GET", "http://" + host + "/api/windsnelheid?size=" + speedSize + "&minuten=" + speedMinuten, false);
    httpreq_speed.send(null);
    var list = [];
    var speeds = JSON.parse(httpreq_speed.responseText);
    for (var key in speeds) {
        list.push({label: msToTime(speeds[key]["time"]), y: speeds[key]["speed"]});
    }
    speedChart.options.data[0].dataPoints = list;
    speedChart.render();
    setTimeout(speedDataUpdater, 5000);
}

function presureDataUpdater() {
    const httpreq_speed = new XMLHttpRequest();
    httpreq_speed.open("GET", "http://" + host + "/api/druk?size=" + presureSize + "&minuten=" + presureMinuten, false);
    httpreq_speed.send(null);
    var list = [];
    var presures = JSON.parse(httpreq_speed.responseText);
    for (const key in presures) {
        list.push({label: msToTime(presures[key]["time"]), y: presures[key]["presure"]});
    }
    presureChart.options.data[0].dataPoints = list;
    presureChart.render();
    setTimeout(presureDataUpdater, 5000);
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

window.onload = () => {
    document.querySelectorAll("input[type=number]").forEach(input => {
        let elem = input;
        elem.addEventListener("change", commitChanges);
        elem.addEventListener("click", commitChanges);
        elem.addEventListener("keyup", commitChanges);
    });
};


function commitChanges() {
    let tempSizeDom = document.getElementById("temp-size");
    tempSize = tempSizeDom.value;
    let tempMinutenDom = document.getElementById("temp-minuten");
    tempMinuten = tempMinutenDom.value;
    let speedSizeDom = document.getElementById("speed-size");
    speedSize = speedSizeDom.value;
    let speedMinutenDom = document.getElementById("speed-minuten");
    speedMinuten = speedMinutenDom.value;
    let presureSizeDom = document.getElementById("presure-size");
    presureSize = presureSizeDom.value;
    let presureMinutenDom = document.getElementById("presure-minuten");
    presureMinuten = presureMinutenDom.value;
}





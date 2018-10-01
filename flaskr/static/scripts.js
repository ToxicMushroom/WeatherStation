let tempChart;

window.onload = function () {
     tempChart = new CanvasJS.Chart("temp-graph", {
        backgroundColor: "#202225",
        animationEnabled: true,
        theme: 'dark2',
        axisY: {
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
    dataUpdater()
};

function dataUpdater() {
    const httpreq = new XMLHttpRequest();
    httpreq.open("GET", "http://localhost/api/",false);
    httpreq.send(null);
    console.log(JSON.parse(httpreq.responseText));
    setTimeout(dataUpdater, 1000);
}

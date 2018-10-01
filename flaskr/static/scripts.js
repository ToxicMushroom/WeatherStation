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
    var list = [];
    var temps = JSON.parse(httpreq.responseText)["temperaturen"];
    for (var key in temps) {
        list.push({x: temps[key]["time"], y: temps[key]["temp"]});
    }
    console.log(list);
    tempChart.options.data[0] = list;
    tempChart.render();
    setTimeout(dataUpdater, 1000);
}

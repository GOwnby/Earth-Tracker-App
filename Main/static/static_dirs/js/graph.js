google.charts.load('45', {
    packages:['corechart']
});

var year = new Date().getFullYear();
var latestDataYear = 0;

var chart;

var dataCO2;
var optionsCO2;
var dataN2O;
var optionsN2O;
var dataCH4;
var optionsCH4;
var dataCFC11;
var optionsCFC11;
var dataCFC12;
var optionsCFC12;
var dataTemperature;
var optionsTemperature;

var jsonData;
var currentData;
var CO2Data;

var startYear;
var endYear;

$(document).ready(function() {
    $("#CO2Selector").click(function () {
        loadCO2();
    });

    $("#N2OSelector").click(function () {
        loadN2O();
    });

    $("#CH4Selector").click(function () {
        loadCH4();
    });

    $("#CFC11Selector").click(function () {
        loadCFC11();
    });

    $("#CFC12Selector").click(function () {
        loadCFC12();
    });

    $("#TemperatureSelector").click(function () {
        loadTemperature();
    });
});

function loadCO2() {
    dataCO2 = new google.visualization.DataTable();

    dataCO2.addColumn('string', 'Year');
    dataCO2.addColumn('number', 'CO2 Actual');
    dataCO2.addColumn('number', 'CO2 Projected');

    if (CO2DataActual.hasOwnProperty((year - 2).toString())){
        latestDataYear = (year - 2);
    }
    if (CO2DataActual.hasOwnProperty((year - 1).toString())){
        latestDataYear = (year - 1);
    }
    if (CO2DataActual.hasOwnProperty(year.toString())){
        latestDataYear = year;
    }
        
    for (i = 1979; i < latestDataYear ; i = i + 1)
    {
        stringI = i.toString();
        dataCO2.addRow([stringI, CO2DataActual[stringI], null]);
    }

    dataCO2.addRow([latestDataYear.toString(), CO2DataActual[latestDataYear], CO2DataActual[latestDataYear] ]);

    if (CO2DataBasicProjection.hasOwnProperty((year + 2).toString())){
        startYear = (year + 2);
    }
    if (CO2DataBasicProjection.hasOwnProperty((year + 1).toString())){
        startYear = (year + 1);
    }
    if (CO2DataBasicProjection.hasOwnProperty(year.toString())){
        startYear = year;
    }
    if (CO2DataBasicProjection.hasOwnProperty((year - 1).toString())){
        startYear = (year - 1);
    }

    if (CO2DataBasicProjection.hasOwnProperty((year + 100 - 1).toString())){
        endYear = (year + 100 - 1);
    }
    if (CO2DataBasicProjection.hasOwnProperty((year + 100).toString())){
        endYear = (year + 100);
    }
    if (CO2DataBasicProjection.hasOwnProperty((year + 100 + 1).toString())){
        endYear = (year + 100 + 1);
    }
    if (CO2DataBasicProjection.hasOwnProperty((year + 100 + 2).toString())){
        endYear = (year + 100 + 2);
    }

    for (i = startYear; i <= endYear; i = i + 1) {
        stringI = i.toString();
        dataCO2.addRow([stringI, null, CO2DataBasicProjection[stringI]]);
    }

    optionsCO2 = {
        title: 'Carbon Dioxide (ppm) vs Time (Years)',
        curveType: 'function',
        legend: {position: 'bottom'},
        width: 900,
        height: 500,
        series :
            {
                1: { lineDashStyle: [10, 2] }
            }
    };

    chart = new google.visualization.LineChart(document.getElementById('linechart_'));
    chart.draw(dataCO2, optionsCO2);
}

function loadN2O() {
    dataN2O = new google.visualization.DataTable();

    dataN2O.addColumn('string', 'Year');
    dataN2O.addColumn('number', 'N2O Actual');
    dataN2O.addColumn('number', 'N2O Projected');

    if (N2ODataActual.hasOwnProperty((year - 2).toString())){
        latestDataYear = (year - 2);
    }
    if (N2ODataActual.hasOwnProperty((year - 1).toString())){
        latestDataYear = (year - 1);
    }
    if (N2ODataActual.hasOwnProperty(year.toString())){
        latestDataYear = year;
    }
        
    for (i = 1977; i < latestDataYear ; i = i + 1)
    {
        stringI = i.toString();
        dataN2O.addRow([stringI, N2ODataActual[stringI], null ]);
    }

    dataN2O.addRow([latestDataYear.toString(), N2ODataActual[latestDataYear], N2ODataActual[latestDataYear] ]);

    if (N2ODataBasicProjection.hasOwnProperty((year + 2).toString())){
        startYear = (year + 2);
    }
    if (N2ODataBasicProjection.hasOwnProperty((year + 1).toString())){
        startYear = (year + 1);
    }
    if (N2ODataBasicProjection.hasOwnProperty(year.toString())){
        startYear = year;
    }
    if (N2ODataBasicProjection.hasOwnProperty((year - 1).toString())){
        startYear = (year - 1);
    }

    if (N2ODataBasicProjection.hasOwnProperty((year + 100 - 1).toString())){
        endYear = (year + 100 - 1);
    }
    if (N2ODataBasicProjection.hasOwnProperty((year + 100).toString())){
        endYear = (year + 100);
    }
    if (N2ODataBasicProjection.hasOwnProperty((year + 100 + 1).toString())){
        endYear = (year + 100 + 1);
    }
    if (N2ODataBasicProjection.hasOwnProperty((year + 100 + 2).toString())){
        endYear = (year + 100 + 2);
    }

    for (i = startYear; i <= endYear; i = i + 1) {
        stringI = i.toString();
        dataN2O.addRow([stringI, null, N2ODataBasicProjection[stringI]]);
    }

    optionsN2O = {
        title: 'Nirous Oxide (ppb) vs Time (Years)',
        curveType: 'function',
        legend: {position: 'bottom'},
        width: 900,
        height: 500,
        series :
            {
                1: { lineDashStyle: [10, 2] }
            }
    };

    chart = new google.visualization.LineChart(document.getElementById('linechart_'));
    chart.draw(dataN2O, optionsN2O);
}

function loadCH4() {
    dataCH4 = new google.visualization.DataTable();

    dataCH4.addColumn('string', 'Year');
    dataCH4.addColumn('number', 'CH4 Actual');
    dataCH4.addColumn('number', 'CH4 Projected');

    if (CH4DataActual.hasOwnProperty((year - 2).toString())){
        latestDataYear = (year - 2);
    }
    if (CH4DataActual.hasOwnProperty((year - 1).toString())){
        latestDataYear = (year - 1);
    }
    if (CH4DataActual.hasOwnProperty(year.toString())){
        latestDataYear = year;
    }
        
    for (i = 1984; i < latestDataYear ; i = i + 1)
    {
        stringI = i.toString();
        dataCH4.addRow([stringI, CH4DataActual[stringI], null ]);
    }

    dataCH4.addRow([latestDataYear.toString(), CH4DataActual[latestDataYear], CH4DataActual[latestDataYear] ]);

    if (CH4DataBasicProjection.hasOwnProperty((year + 2).toString())){
        startYear = (year + 2);
    }
    if (CH4DataBasicProjection.hasOwnProperty((year + 1).toString())){
        startYear = (year + 1);
    }
    if (CH4DataBasicProjection.hasOwnProperty(year.toString())){
        startYear = year;
    }
    if (CH4DataBasicProjection.hasOwnProperty((year - 1).toString())){
        startYear = (year - 1);
    }

    if (CH4DataBasicProjection.hasOwnProperty((year + 100 - 1).toString())){
        endYear = (year + 100 - 1);
    }
    if (CH4DataBasicProjection.hasOwnProperty((year + 100).toString())){
        endYear = (year + 100);
    }
    if (CH4DataBasicProjection.hasOwnProperty((year + 100 + 1).toString())){
        endYear = (year + 100 + 1);
    }
    if (CH4DataBasicProjection.hasOwnProperty((year + 100 + 2).toString())){
        endYear = (year + 100 + 2);
    }

    for (i = startYear; i <= endYear; i = i + 1) {
        stringI = i.toString();
        dataCH4.addRow([stringI, null, CH4DataBasicProjection[stringI]]);
    }

    optionsCH4 = {
        title: 'Methane (ppb) vs Time (Years)',
        curveType: 'function',
        legend: {position: 'bottom'},
        width: 900,
        height: 500,
        series :
            {
                1: { lineDashStyle: [10, 2] }
            }
    };

    chart = new google.visualization.LineChart(document.getElementById('linechart_'));
    chart.draw(dataCH4, optionsCH4);
}

function loadCFC11() {
    dataCFC11 = new google.visualization.DataTable();

    dataCFC11.addColumn('string', 'Year');
    dataCFC11.addColumn('number', 'CFC11 Actual');
    dataCFC11.addColumn('number', 'CFC11 Projected');

    if (CFC11DataActual.hasOwnProperty((year - 2).toString())){
        latestDataYear = (year - 2);
    }
    if (CFC11DataActual.hasOwnProperty((year - 1).toString())){
        latestDataYear = (year - 1);
    }
    if (CFC11DataActual.hasOwnProperty(year.toString())){
        latestDataYear = year;
    }
        
    for (i = 1977; i < latestDataYear ; i = i + 1)
    {
        stringI = i.toString();
        dataCFC11.addRow([stringI, CFC11DataActual[stringI], null ]);
    }

    dataCFC11.addRow([latestDataYear.toString(), CFC11DataActual[latestDataYear], CFC11DataActual[latestDataYear] ]);

    if (CFC11DataBasicProjection.hasOwnProperty((year + 2).toString())){
        startYear = (year + 2);
    }
    if (CFC11DataBasicProjection.hasOwnProperty((year + 1).toString())){
        startYear = (year + 1);
    }
    if (CFC11DataBasicProjection.hasOwnProperty(year.toString())){
        startYear = year;
    }
    if (CFC11DataBasicProjection.hasOwnProperty((year - 1).toString())){
        startYear = (year - 1);
    }

    if (CFC11DataBasicProjection.hasOwnProperty((year + 100 - 1).toString())){
        endYear = (year + 100 - 1);
    }
    if (CFC11DataBasicProjection.hasOwnProperty((year + 100).toString())){
        endYear = (year + 100);
    }
    if (CFC11DataBasicProjection.hasOwnProperty((year + 100 + 1).toString())){
        endYear = (year + 100 + 1);
    }
    if (CFC11DataBasicProjection.hasOwnProperty((year + 100 + 2).toString())){
        endYear = (year + 100 + 2);
    }

    for (i = startYear; i <= endYear; i = i + 1) {
        stringI = i.toString();
        dataCFC11.addRow([stringI, null, CFC11DataBasicProjection[stringI]]);
    }

    optionsCFC11 = {
        title: 'Trichlorofluoromethane-11 (ppt) vs Time (Years)',
        curveType: 'function',
        legend: {position: 'bottom'},
        width: 900,
        height: 500,
        series :
            {
                1: { lineDashStyle: [10, 2] }
            }
    };

    chart = new google.visualization.LineChart(document.getElementById('linechart_'));
    chart.draw(dataCFC11, optionsCFC11);
}

function loadCFC12() {
    dataCFC12 = new google.visualization.DataTable();

    dataCFC12.addColumn('string', 'Year');
    dataCFC12.addColumn('number', 'CFC12 Actual');
    dataCFC12.addColumn('number', 'CFC12 Projected');

    if (CFC12DataActual.hasOwnProperty((year - 2).toString())){
        latestDataYear = (year - 2);
    }
    if (CFC12DataActual.hasOwnProperty((year - 1).toString())){
        latestDataYear = (year - 1);
    }
    if (CFC12DataActual.hasOwnProperty(year.toString())){
        latestDataYear = year;
    }
        
    for (i = 1977; i < latestDataYear ; i = i + 1)
    {
        stringI = i.toString();
        dataCFC12.addRow([stringI, CFC12DataActual[stringI], null ]);
    }

    dataCFC12.addRow([latestDataYear.toString(), CFC12DataActual[latestDataYear], CFC12DataActual[latestDataYear] ]);

    if (CFC12DataBasicProjection.hasOwnProperty((year + 2).toString())){
        startYear = (year + 2);
    }
    if (CFC12DataBasicProjection.hasOwnProperty((year + 1).toString())){
        startYear = (year + 1);
    }
    if (CFC12DataBasicProjection.hasOwnProperty(year.toString())){
        startYear = year;
    }
    if (CFC12DataBasicProjection.hasOwnProperty((year - 1).toString())){
        startYear = (year - 1);
    }

    if (CFC12DataBasicProjection.hasOwnProperty((year + 100 - 1).toString())){
        endYear = (year + 100 - 1);
    }
    if (CFC12DataBasicProjection.hasOwnProperty((year + 100).toString())){
        endYear = (year + 100);
    }
    if (CFC12DataBasicProjection.hasOwnProperty((year + 100 + 1).toString())){
        endYear = (year + 100 + 1);
    }
    if (CFC12DataBasicProjection.hasOwnProperty((year + 100 + 2).toString())){
        endYear = (year + 100 + 2);
    }

    for (i = startYear; i <= endYear; i = i + 1) {
        stringI = i.toString();
        dataCFC12.addRow([stringI, null, CFC12DataBasicProjection[stringI]]);
    }

    optionsCFC12 = {
        title: 'Trichlorofluoromethane-12 (ppt) vs Time (Years)',
        curveType: 'function',
        legend: {position: 'bottom'},
        width: 900,
        height: 500,
        series :
            {
                1: { lineDashStyle: [10, 2] }
            }
    };

    chart = new google.visualization.LineChart(document.getElementById('linechart_'));
    chart.draw(dataCFC12, optionsCFC12);
}

function loadTemperature() {
    dataTemperature = new google.visualization.DataTable();

    dataTemperature.addColumn('string', 'Year');
    dataTemperature.addColumn('number', 'Temperature Average Actual');
    dataTemperature.addColumn('number', 'Temperature Average Projected');

    if (TemperatureDataActual.hasOwnProperty((year - 2).toString())){
        latestDataYear = (year - 2);
    }
    if (TemperatureDataActual.hasOwnProperty((year - 1).toString())){
        latestDataYear = (year - 1);
    }
    if (TemperatureDataActual.hasOwnProperty(year.toString())){
        latestDataYear = year;
    }
        
    for (i = 1880; i < latestDataYear ; i = i + 1)
    {
        stringI = i.toString();
        dataTemperature.addRow([stringI, TemperatureDataActual[stringI], null ]);
    }

    dataTemperature.addRow([latestDataYear.toString(), TemperatureDataActual[latestDataYear], TemperatureDataActual[latestDataYear] ]);

    if (TemperatureDataBasicProjection.hasOwnProperty((year + 2).toString())){
        startYear = (year + 2);
    }
    if (TemperatureDataBasicProjection.hasOwnProperty((year + 1).toString())){
        startYear = (year + 1);
    }
    if (TemperatureDataBasicProjection.hasOwnProperty(year.toString())){
        startYear = year;
    }
    if (TemperatureDataBasicProjection.hasOwnProperty((year - 1).toString())){
        startYear = (year - 1);
    }

    if (TemperatureDataBasicProjection.hasOwnProperty((year + 100 - 1).toString())){
        endYear = (year + 100 - 1);
    }
    if (TemperatureDataBasicProjection.hasOwnProperty((year + 100).toString())){
        endYear = (year + 100);
    }
    if (TemperatureDataBasicProjection.hasOwnProperty((year + 100 + 1).toString())){
        endYear = (year + 100 + 1);
    }
    if (TemperatureDataBasicProjection.hasOwnProperty((year + 100 + 2).toString())){
        endYear = (year + 100 + 2);
    }

    for (i = startYear; i <= endYear; i = i + 1) {
        stringI = i.toString();
        dataTemperature.addRow([stringI, null, TemperatureDataBasicProjection[stringI]]);
    }

    optionsTemperature = {
        title: 'Global Average Temperature (Celsius) vs Time (Years)',
        curveType: 'function',
        legend: {position: 'bottom'},
        width: 900,
        height: 500,
        series :
            {
                1: { lineDashStyle: [10, 2] }
            }
    };

    chart = new google.visualization.LineChart(document.getElementById('linechart_'));
    chart.draw(dataTemperature, optionsTemperature);
}
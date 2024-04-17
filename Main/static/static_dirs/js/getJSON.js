var CO2DataActual;
var dataOne = $.getJSON("/static/CO2Data.json", function (data){
    CO2DataActual = dataOne.responseJSON;
});

var CO2DataBasicProjection;
var dataTwo = $.getJSON("/static/CO2DataBasicProjection.json", function (data){
    CO2DataBasicProjection = dataTwo.responseJSON;
});

var N2ODataActual;
var dataThree = $.getJSON("/static/N2OData.json", function (data){
    N2ODataActual = dataThree.responseJSON;
});

var N2ODataBasicProjection;
var dataFour = $.getJSON("/static/N2ODataBasicProjection.json", function (data){
    N2ODataBasicProjection = dataFour.responseJSON;
});

var CH4DataActual;
var dataFive = $.getJSON("/static/CH4Data.json", function (data){
    CH4DataActual = dataFive.responseJSON;
});

var CH4DataBasicProjection;
var dataSix = $.getJSON("/static/CH4DataBasicProjection.json", function (data){
    CH4DataBasicProjection = dataSix.responseJSON;
});

var CFC11DataActual;
var dataSeven = $.getJSON("/static/CFC11Data.json", function (data){
    CFC11DataActual = dataSeven.responseJSON;
});

var CFC11DataBasicProjection;
var dataEight = $.getJSON("/static/CFC11DataBasicProjection.json", function (data){
    CFC11DataBasicProjection = dataEight.responseJSON;
});

var CFC12DataActual;
var dataNine = $.getJSON("/static/CFC12Data.json", function (data){
    CFC12DataActual = dataNine.responseJSON;
});

var CFC12DataBasicProjection;
var dataTen = $.getJSON("/static/CFC12DataBasicProjection.json", function (data){
    CFC12DataBasicProjection = dataTen.responseJSON;
});

var TemperatureDataActual;
var dataEleven = $.getJSON("/static/TemperatureData.json", function (data){
    TemperatureDataActual = dataEleven.responseJSON;
});

var TemperatureDataBasicProjection;
var dataTwelve = $.getJSON("/static/TemperatureDataBasicProjectionLong.json", function (data){
    TemperatureDataBasicProjection = dataTwelve.responseJSON;
});
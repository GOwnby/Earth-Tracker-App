import urllib.request
import os

# Download all required data
def retrieve_All():
    # Carbon Dioxide (CO2) Data Source
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_annmean_mlo.txt'
    dirPath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CO2Data.txt'
    dataFile = open(dirPath, 'w')
    urllib.request.urlretrieve(url, dirPath)

    # Nitrous Oxide (N2O) Data Source
    url = 'ftp://ftp.cmdl.noaa.gov/hats/n2o/combined/HATS_global_N2O.txt'
    dirPath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'N2OData.txt'
    dataFile = open(dirPath, 'w')
    urllib.request.urlretrieve(url, dirPath)

    # Methane (CH4) Data Source
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/ch4/ch4_annmean_gl.txt'
    dirPath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CH4Data.txt'
    dataFile = open(dirPath, 'w')
    urllib.request.urlretrieve(url, dirPath)

    # Trichlorofluoromethane 11 (CFC-11) Data Source
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc11/combined/HATS_global_F11.txt'
    dirPath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CFC11Data.txt'
    dataFile = open(dirPath, 'w')
    urllib.request.urlretrieve(url, dirPath)

    # Trichlorofluoromethane 12 (CFC-12) Data Source
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc12/combined/HATS_global_F12.txt'
    dirPath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CFC12Data.txt'
    dataFile = open(dirPath, 'w')
    urllib.request.urlretrieve(url, dirPath)

    # Global Temperature Average Data Source
    url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
    dirPath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'TemperatureData.txt'
    dataFile = open(dirPath, 'w')
    urllib.request.urlretrieve(url, dirPath)
    dataFile.close()
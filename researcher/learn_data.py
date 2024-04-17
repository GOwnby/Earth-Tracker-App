import json
import datetime
import math
import re
import os

# Project all features using a basic projection based on the rate of change
# Project Temperature using the relationship defined between a change in net radiative flux and global mean surface temperature
def learn_all():
    basicProjection('CO2')
    basicProjection('N2O')
    basicProjection('CH4')
    basicProjection('CFC11')
    basicProjection('CFC12')
    basicProjection('Temperature')

    basicProjectionLong('Temperature', 1945)

    projectTemperature()

# Returns the current year
def currentYear():
    currentYear = datetime.datetime.now().year
    return currentYear

# Find the starting year of each dataset by scanning the file again, 
# this time looking only for the first year to appear
def findStartYear(dataset):
    thisDataset = ''
    if dataset == 'CO2':
        thisDataset = 'CO2Data.json'
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CH4':
        thisDataset = 'CH4Data.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'
    if dataset == 'Temperature':
        thisDataset = 'TemperatureData.json'

    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    try:
        fp = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + thisDataset)
    except Exception:
        fp = ''

    for line in fp:
        if not(re.search('#', line)):
            match_year = re.match(pattern_year, line) # Read the first year that returns a match for a year in the data

    return match_year

# Find the ending year of each dataset by scanning the file again, 
# this time looking only for the last year at the end of the file
def findEndYear(dataset):
    thisDataset = ''
    if dataset == 'CO2':
        thisDataset = 'CO2Data.json'
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CH4':
        thisDataset = 'CH4Data.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'
    if dataset == 'Temperature':
        thisDataset = 'TemperatureData.json'

    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    countLines = 0 
    try: # Count the number of lines in the file
        fp = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + thisDataset)
        for line in fp:
            countLines += 1
    finally: # Go to the final line of the file and read the year
        thisLine = 0
        fp = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + thisDataset)
        for line in fp:
            thisLine += 1
            if thisLine == (countLines - 1):
                match_year = re.match(pattern_year, line)
                if match_year is not None:
                    return match_year
            elif thisLine == countLines:
                match_year = re.match(pattern_year, line)
                if match_year is not None:
                    return match_year

# Find the Common starting year between all datasets by calling findStartYear(dataset)
def findCommonStartYear():
    startYearDataCO2 = findStartYear('CO2')
    startYearDataN2O = findStartYear('N2O')
    startYearDataCH4 = findStartYear('CH4')
    startYearDataCFC11 = findStartYear('CFC11')
    startYearDataCFC12 = findStartYear('CFC12')
    startYearDataTemperature = findStartYear('Temperature')

    lowestCommonYear = startYearDataCO2
    if lowestCommonYear <= startYearDataN2O:
        lowestCommonYear = startYearDataN2O
    if lowestCommonYear <= startYearDataCH4:
        lowestCommonYear = startYearDataCH4
    if lowestCommonYear <= startYearDataCFC11:
        lowestCommonYear = startYearDataCFC11
    if lowestCommonYear <= startYearDataCFC12:
        lowestCommonYear = startYearDataCFC12
    if lowestCommonYear <= startYearDataTemperature:
        lowestCommonYear = startYearDataTemperature

    return lowestCommonYear

# Find the Common ending year between all datasets by calling findEndYear(dataset)
def findCommonEndYear():
    endYearDataCO2 = findEndYear('CO2')
    endYearDataN2O = findEndYear('N2O')
    endYearDataCH4 = findEndYear('CH4')
    endYearDataCFC11 = findEndYear('CFC11')
    endYearDataCFC12 = findEndYear('CFC12')
    endYearDataTemperature = findEndYear('Temperature')

    highestCommonYear = endYearDataCO2
    if highestCommonYear >= endYearDataN2O:
        highestCommonYear = endYearDataN2O
    if highestCommonYear >= endYearDataCH4:
        highestCommonYear = endYearDataCH4
    if highestCommonYear >= endYearDataCFC11:
        highestCommonYear = endYearDataCFC11
    if highestCommonYear >= endYearDataCFC12:
        highestCommonYear = endYearDataCFC12
    if highestCommonYear >= endYearDataTemperature:
        highestCommonYear = endYearDataTemperature

    return highestCommonYear

# A Basic Projection using the rate of change over the last year
def basicProjection(dataset):
    thisDataset = ''
    if dataset == 'CO2':
        thisDataset = 'CO2Data.json'
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CH4':
        thisDataset = 'CH4Data.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'
    if dataset == 'Temperature':
        thisDataset = 'TemperatureData.json'

    projectedSet = {}
    startYear = currentYear()
    thisYear = currentYear()
    endYear = startYear + 100

    filePath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + thisDataset

    data = open(filePath)
    data = json.load(data)
        
    startLoad = ""
    counter = 0
    while len(startLoad) < 2: # Find the most recent data by checking for data for this year going backwards
        try:
            startYear = thisYear + counter
            startLoad = data[str(startYear)]
            startLoad = str(startLoad)
        except Exception:
            counter = counter - 1

    startLoad = float(startLoad)
    precedingLoad = float(data[str(startYear - 1)])
    changeInLoad = startLoad - precedingLoad # Find the rate of change between the most recent year and the year before it
    projectedSet[startYear + 1] = startLoad + changeInLoad
    startYear += 2

    # Write the projected values from the start year until the end year using the rate of change
    while startYear <= endYear:
        projectedSet[startYear] = projectedSet[startYear - 1] + changeInLoad
        startYear += 1

    # Output the data JSON file
    filePath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + dataset + 'DataBasicProjection.json'
    outfile = open(filePath, 'w')
    json.dump(projectedSet, outfile)
    outfile.close()

# A Long Basic Projection using the rate of change from a year in the past to present
def basicProjectionLong(dataset, yearPast):
    thisDataset = ''
    if dataset == 'CO2':
        thisDataset = 'CO2Data.json'
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CH4':
        thisDataset = 'CH4Data.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'
    if dataset == 'Temperature':
        thisDataset = 'TemperatureData.json'

    projectedSet = {}
    startYear = currentYear()
    thisYear = currentYear()
    endYear = startYear + 100

    filePath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + thisDataset

    data = open(filePath)
    data = json.load(data)
        
    startLoad = ""
    counter = 0
    while len(startLoad) < 2: # Find the most recent data by checking for data for this year going backwards
        try:
            startYear = thisYear + counter
            startLoad = data[str(startYear)]
            startLoad = str(startLoad)
        except Exception:
            counter = counter - 1

    startLoad = float(startLoad)
    precedingLoad = float(data[str(yearPast)])
    changeInLoad = (startLoad - precedingLoad) / (startYear - yearPast)  # Find the rate of change between the most recent year and year given
    projectedSet[startYear + 1] = startLoad + changeInLoad
    startYear += 2

    # Write the projected values from the start year until the end year using the rate of change
    while startYear <= endYear:
        projectedSet[startYear] = projectedSet[startYear - 1] + changeInLoad
        startYear += 1

    # Output the data JSON file
    filePath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + dataset + 'DataBasicProjectionLong.json'
    outfile = open(filePath, 'w')
    json.dump(projectedSet, outfile)
    outfile.close()

# Calculates the Radiative Forcing or Flux using the relationship defined by the National Oceanic and Atmospheric Administration(NOAA)
# https://www.esrl.noaa.gov/gmd/aggi/aggi.html
# Represents the change in radiative flux in searchYear compared to the year before it, maybe this should include a start year instead of the year before it
def calculateChangeInRadiativeFlux(searchYear):
    thisYear = currentYear()
    filePath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep

    # Contains initial values of: CO2 PPM, N2O PPB, CH4 PPB, CFC-11 PPT, CFC-12 PPT
    initialValues = []
    # Contains final values of: CO2 PPM, N2O PPB, CH4 PPB, CFC-11 PPT, CFC-12 PPT
    finalValues = []
    # Contains the changes in radiative flux due to: CO2, N2O, CH4, CFC-11, CFC-12
    changesInRadiativeFlux = []
    
    datasets = ['CO2', 'N2O', 'CH4', 'CFC11', 'CFC12']
    thisSet = 0

    # If the year we are searching for is less than this year, use the Actual Data for each dataset
    if searchYear < thisYear:
        for eachSet in datasets:
            with open(filePath + eachSet + 'Data.json') as json_file:
                data = json.load(json_file)
                finalValues.append(data[str(searchYear)])
                initialValues.append(data[str(searchYear - 1)])
                thisSet += 1
    elif searchYear > thisYear: # If the year we are searching for is greater than this year, use the Projected Data for each dataset
        for eachSet in datasets:
            with open(filePath + eachSet + 'DataBasicProjection.json') as json_file:
                data = json.load(json_file)
                finalValues.append(data[str(searchYear)])
                initialValues.append(data[str(searchYear - 1)])
                thisSet += 1
    elif searchYear == thisYear: # If the year we are searching for is equal to this year, use the Projected Data for this year and the Actual Data for last year
        for eachSet in datasets:
            with open(filePath + eachSet + 'DataBasicProjection.json') as json_file:
                data = json.load(json_file)
                finalValues.append(data[str(searchYear)])
                with open(filePath + datasets[thisSet] +'Data.json') as json_file:
                    data = json.load(json_file)
                    initialValues.append(data[str(searchYear - 1)])
                    thisSet += 1
    
    # Append to an array the respective changes in radiative flux due to each dataset
    changesInRadiativeFlux.append(calculateChangeInRadiativeFluxDueToCO2(initialValues[0], finalValues[0], finalValues[1]))
    changesInRadiativeFlux.append(calculateChangeInRadiativeFluxDueToN2O(initialValues[1], finalValues[1], finalValues[0], finalValues[2]))
    changesInRadiativeFlux.append(calculateChangeInRadiativeFluxDueToCH4(initialValues[2], finalValues[2], finalValues[1]))
    changesInRadiativeFlux.append(calculateChangeInRadiativeFluxDueToCFC11(initialValues[3], finalValues[3]))
    changesInRadiativeFlux.append(calculateChangeInRadiativeFluxDueToCFC12(initialValues[4], finalValues[4]))
    
    # Sum the changes in radiative flux
    changeInRadiativeFlux = changesInRadiativeFlux[0] + changesInRadiativeFlux[1] + changesInRadiativeFlux[2] + \
        changesInRadiativeFlux[3] + changesInRadiativeFlux[4]
    
    return changeInRadiativeFlux

# The equation for a change in Radiative Flux due to CO2
def calculateChangeInRadiativeFluxDueToCO2(initialCO2PPM, finalCO2PPM, finalN2OPPB):
    return ( (5.2488 + (-2.48E-07 * math.pow(finalCO2PPM - initialCO2PPM, 2)) + \
        (-0.000125 * (finalCO2PPM - initialCO2PPM) ) ) + \
        (-2.15E-03 * math.sqrt(finalN2OPPB))) * \
        math.log((finalCO2PPM / initialCO2PPM))

# The equation for a change in Radiative Flux due to N2O
def calculateChangeInRadiativeFluxDueToN2O(initialN2OPPB, finalN2OPPB, finalCO2PPM, finalCH4PPB):
    return ( (-0.000342 * math.sqrt(finalCO2PPM)) + (0.0002546 * math.sqrt(finalN2OPPB)) + \
        (-0.000244 * math.sqrt(finalCH4PPB)) ) * (math.sqrt(finalN2OPPB) - math.sqrt(initialN2OPPB))

# The equation for a change in Radiative Flux due to CH4                   
def calculateChangeInRadiativeFluxDueToCH4(initialCH4PPB, finalCH4PPB, finalN2OPPB):
    return ( (-8.96E-05 * math.sqrt(finalCH4PPB)) + (-0.000125 * math.sqrt(finalN2OPPB)) + \
        0.045194) * (math.sqrt(finalCH4PPB) - math.sqrt(initialCH4PPB))

# The equation for a change in Radiative Flux due to CFC-11
# The value (1) needs to be changed to "ω" given in Smith et al. (2021) as stated by NOAA https://www.esrl.noaa.gov/gmd/aggi/aggi.html
def calculateChangeInRadiativeFluxDueToCFC11(initialCFC11PPT, finalCFC11PPT):
    return (1) * (finalCFC11PPT - initialCFC11PPT)

# The equation for a change in Radiative Flux due to CFC-12
# The value (1) needs to be changed to "ω" given in Smith et al. (2021) as stated by NOAA https://www.esrl.noaa.gov/gmd/aggi/aggi.html
def calculateChangeInRadiativeFluxDueToCFC12(initialCFC12PPT, finalCFC12PPT):
    return (1) * (finalCFC12PPT - initialCFC12PPT)

# Find the change in Temperature between the search year and the year before it, maybe this should include a start year instead of the year before it
def calculateChangeInTemperature(searchYear):
    filePath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep
    with open(filePath + 'TemperatureData.json') as json_file:
        data = json.load(json_file)

        finalTemp = data[str(searchYear)]
        initialTemp = data[str(searchYear - 1)]
        changeInTemperature = finalTemp - initialTemp
        return changeInTemperature

# Find the change of the change in Temperature between the search year and the year before it, maybe this should include a start year instead of the year before it
def calculateChangeOfChangeInTemperature(searchYear):
    finalChange = calculateChangeInTemperature(searchYear)
    initialChange = calculateChangeInTemperature(searchYear - 1)
    changeOfChangeInTemperature = finalChange - initialChange
    return changeOfChangeInTemperature

def calculateClimateSensitivityParameter():
    '''
    I dont know what I was thinking here, I thought I was solving for a constant based a change between radiative flux and temperature
    It seems like this value is simply 14 micrometers as defined on page 44 (file page 8) of UT lecture notes
    http://www.geo.utexas.edu/courses/387H/Lectures/chap2.pdf

    The lecture also says that the climate sensitivity parameter multiplied by the temperature is a constant
    The IPCC says that the change in temperature divided by the climate sensitivity parameter is equal to the radiative forcing(page 664), so how could there be a constant
    https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter08_FINAL.pdf

    This leads to the problem on line 413 of this program... We want to find how the climate sensitivity parameter is changing as 
    temperatures and greenhouse gases change in the future... but does it change at all or is it constant? Maybe disregard UT altogether, or was interpreted wrong.
    It being constant doesnt make much sense to me as there wouldnt be any affect of radiative forcing at least looking at how radiative forcing is applied in IPCC section 8.1.1.1
    Maybe the UT lecture is old or means something else, it looks like it comes from some textbook

    Need to make sure lecture and IPCC are referring to same parameter... additional sources needed

    lowestCommonYear = findCommonStartYear() + 1
    highestCommonYear = findCommonEndYear()

    counter = 0
    sumClimateSensitivityParameter = 0
    startYear = lowestCommonYear
    while startYear < highestCommonYear:
        changeOfChangeInTemperature = calculateChangeOfChangeInTemperature(startYear)
        changeInRadiativeFlux = calculateChangeInRadiativeFlux(startYear)
        sumClimateSensitivityParameter += changeOfChangeInTemperature / changeInRadiativeFlux
        startYear += 1
        counter += 1

    climateSensitivityParameter = sumClimateSensitivityParameter / counter
    '''

    return 14E-6 # The value the UT lecture documents give

# If the climate sensitivity parameter is constant then there is no change
def calculateChangeInClimateSensitivityParameter(searchYear):
    changeOfChangeInTemperatureFinal = calculateChangeOfChangeInTemperature(searchYear)
    changeInRadiativeFluxFinal = calculateChangeInRadiativeFlux(searchYear)

    finalClimateSensitivityParameter = changeOfChangeInTemperatureFinal / changeInRadiativeFluxFinal

    changeOfChangeInTemperatureInitial = calculateChangeOfChangeInTemperature(searchYear - 1)
    changeInRadiativeFluxInitial = calculateChangeInRadiativeFlux(searchYear - 1)

    initialClimateSensitivityParameter = changeOfChangeInTemperatureInitial / changeInRadiativeFluxInitial

    changeInClimateSensitivityParameter = finalClimateSensitivityParameter - initialClimateSensitivityParameter
    return changeInClimateSensitivityParameter

'''
Models Earth's Temperature using the relationship defined between an instantaneous change in net radiative flux and global mean surface temperature
Outlined in Section 8.1.1.1 of the Fifth Assessment of the IPCC

Myhre, G., D. Shindell, F.-M. Bréon, W. Collins, J. Fuglestvedt, J. Huang, D. Koch, J.-F. Lamarque, D. Lee, B. Mendoza, T. Nakajima, A. Robock, G. Stephens,
T. Takemura and H. Zhang, 2013: Anthropogenic and Natural Radiative Forcing. In: Climate Change 2013: The Physical Science Basis. Contribution of Working 
Group I to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change [Stocker, T.F., D. Qin, G.-K. Plattner, M. Tignor, S.K. Allen, 
J. Boschung, A. Nauels, Y. Xia, V. Bex and P.M. Midgley (eds.)]. Cambridge University Press, Cambridge, United Kingdom and New York, NY, USA

https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter08_FINAL.pdf
---------------------------------------------------------------------------------------------------
Projects temperature for the year succeeding real data,
Attempts to calculate the change in Radiative Flux and Climate Sensitivity Parameter; to project the succeeding years' temperature in a continuous fashion.
Changes in radiative flux are a function of projected changes in atmospheric composition, changes in climate sensitivity parameter are unknown

Changes in the Climate Sensitivity Parameter are a function of projected changes in radiative flux and the rate of change of the rate of change of temperature (IPCC section 8.1.1.1)
In other words, second derivative of temperature = first derivative of climate sensitivity parameter * first derivative of radiative flux (IPCC section 8.1.1.1) 
The problem is that NOAA only defines equations for changes in radiative flux. There needs to be a equation to find the total radiative flux so that we do not need to
solve the problem using the second derivative of temperature which is dependent of the first derivative of radiative flux and first derivative of the climate sensitivity parameter.
Thats a problem if the first derivative of climate sensitivity parameter is 0 as in the UT lecture documents. Either an equation for total radiative flux or an equation
for the first derivative of the climate sensitivity parameter is needed.

We could find total radiative flux maybe using a value of zero for the initial values used in the functions to calculate changes in radiative flux
Still, the radiative flux will be off until the radiative flux due to CFC11/CFC12 is found in Smith et al. (2021)... Seems like insufficient info given by NOAA to find that paper
'''
# Function Unfinished, produces erroneous data regardless of whether calculateClimateSensitivityParameter() function is commented out or not
def projectTemperature():
    filePath = os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep
    startYear = currentYear()
    nextCentury = startYear + 100
    changesOfChangeInTemperature = {}
    changesOfClimateSensitivityParameter = {}

    changesOfChangeInTemperature[startYear] = (calculateChangeInClimateSensitivityParameter(startYear - 1)) * (calculateChangeInRadiativeFlux(startYear - 1))
    
    changeOfChangeInTemperatureFinal = changesOfChangeInTemperature[startYear]
    changeInRadiativeFluxFinal = calculateChangeInRadiativeFlux(startYear)

    finalClimateSensitivityParameter = changeOfChangeInTemperatureFinal / changeInRadiativeFluxFinal

    changeOfChangeInTemperatureInitial = calculateChangeOfChangeInTemperature(startYear - 1)
    changeInRadiativeFluxInitial = calculateChangeInRadiativeFlux(startYear - 1)

    initialClimateSensitivityParameter = changeOfChangeInTemperatureInitial / changeInRadiativeFluxInitial

    changesOfClimateSensitivityParameter[startYear] = finalClimateSensitivityParameter - initialClimateSensitivityParameter
        
    startYear +=  1
    changesOfChangeInTemperature[startYear] = (changesOfClimateSensitivityParameter[startYear - 1]) * (calculateChangeInRadiativeFlux(startYear - 1))

    while startYear <= nextCentury:
        changeOfChangeInTemperatureFinal = changesOfChangeInTemperature[startYear]
        changeInRadiativeFluxFinal = calculateChangeInRadiativeFlux(startYear)

        finalClimateSensitivityParameter = changeOfChangeInTemperatureFinal / changeInRadiativeFluxFinal

        changeOfChangeInTemperatureInitial = changesOfChangeInTemperature[startYear - 1]
        changeInRadiativeFluxInitial = calculateChangeInRadiativeFlux(startYear - 1)

        initialClimateSensitivityParameter = changeOfChangeInTemperatureInitial / changeInRadiativeFluxInitial

        changesOfClimateSensitivityParameter[startYear] = finalClimateSensitivityParameter - initialClimateSensitivityParameter
        
        startYear +=  1
        changesOfChangeInTemperature[startYear] = (changesOfClimateSensitivityParameter[startYear - 1]) * (calculateChangeInRadiativeFlux(startYear - 1))
    
    outfile = open(filePath + 'TemperatureProjection.json', 'w')
    json.dump(changesOfChangeInTemperature, outfile)
    outfile.close()
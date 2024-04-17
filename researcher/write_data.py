import json
import re
from . import learn_data
import os

# Read all required data and output the data in JSON format to be read by Javascript
def write_All():
    write_CO2()
    write_N2O()
    write_CH4()
    write_CFC11()
    write_CFC12()
    write_Temperature()

# Open the CO2 data file and use regular expressions to read the data and output JSON
def write_CO2():
    data = {} # The dictionary object that will be used to generate a JSON object
    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    pattern_ppm = r'[0-9][0-9][0-9].[0-9][0-9]' # A regular expression for scanning the data file and finding the CO2 PPM data on that line

    dataFile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CO2Data.txt') # Open the file
    for line in dataFile: # For each line in this file
        if not(re.search('#', line)): # If there is not a '#' character on this line, then the raw data has began and continues until the end of the file
            match_year = re.search(pattern_year, line) # If there is a match for a year found on this line, save that year
            match_ppm = re.search(pattern_ppm, line) # If there is a match for CO2 PPM on this line succeeding the year match, then save the data corresponding to that year
            if match_year is not None: # Check if a match was found for a year on this line
                if match_ppm is not None: # Check if a match was found for CO2 PPM on this line
                    data[int(match_year.group(0))] = float(match_ppm.group(0)) # If a match was found then save it to the data dictionary object

    dataFile.close() # Close the file
    outfile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CO2Data.json', 'w') # Open the output file
    json.dump(data, outfile) # Output the data to the output file
    outfile.close() # Close the output file

# Open the N2O data file and use regular expressions to read the data and output JSON
def write_N2O():
    data = {} # The dictionary object that will be used to generate a JSON object
    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    pattern_ppb1 = r'[n0123456789][a0123456789][n0123456789]' # A regular expression for scanning the data file and finding the N2O PPB data on that line which might be "nan"
    pattern_ppb2 = r'.[0-9][0-9][0-9]' # A regular expression for scanning the data file and finding part of the N2O PPB data on that line succeeding the decimal

    dataFile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'N2OData.txt') # Open the file
    lastYearSeen = 0 # This data file lists the average for each month rather than each year, keep track of this and average months over the year
    lastMovingAverage = 0.0 # Keep a moving average to average the N2O PPB over the year
    for line in dataFile: # For each line in this file
        if not(re.match('#', line)): # If there is not a '#' character on this line, then the raw data has began and continues until the end of the file
            if re.match(pattern_year, line): # If there is a match for a year found on this line, True will be returned and the program continues
                match_year = re.match(pattern_year, line) # Save the match for the year found on this line
                lineEdited = line.replace(str(match_year.group(0)), '') # Save an edited version of the line with the year removed from the beginning
                lineEdited = lineEdited[7:] # Save an edited version of the line with the blank space removed from the beginning
                match_ppb1 = re.match(pattern_ppb1, lineEdited) # Search for a match for the first part of the N2O PPB regular expression
                if (str(match_ppb1.group(0)) != 'nan'): # As long as our match isnt "nan", continue
                    lineEdited = lineEdited[3:] # Save an edited version of the line removing the first part of the N2O PPB expression found so that it will not be found again
                    match_ppb2 = re.match(pattern_ppb2, lineEdited) # Search for a match for the second part of the N2O PPB regular expression
                    this_year = match_year.group(0) # Save the match for the year found on this line
                    this_ppb = match_ppb1.group(0) + match_ppb2.group(0) # Save both parts of the N2O PPB matches concatenated together
                    if lastYearSeen == int(this_year): # If the year on this line is the same as the last year seen, we need to continue averaging this year
                        lastMovingAverage = (lastMovingAverage + float(this_ppb)) / 2.0 # Take the moving average for N2O PPB this year 
                    else: # If the year on this line is not the same as the last year seen, a new year has began
                        if lastYearSeen != 0: # If the last year seen is not zero, then it is a valid year to save to the data dictionary
                            data[lastYearSeen] = float(lastMovingAverage)
                        lastYearSeen = int(this_year) # Set the last seen year to this year before going to the next line
                        lastMovingAverage = float(this_ppb) # Set the last moving average to this N2O PPB before moving to the next line

    dataFile.close() # Close the file
    outfile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'N2OData.json', 'w') # Open the output file
    json.dump(data, outfile) # Output the data to the output file
    outfile.close() # Close the output file

# Open the N2O data file and use regular expressions to read the data and output JSON
def write_CH4():
    data = {} # The dictionary object that will be used to generate a JSON object
    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    pattern_ppb = r'[0-9][0-9][0-9][0-9].[0-9][0-9]' # A regular expression for scanning the data file and finding the CH4 PPB data on that line

    dataFile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CH4Data.txt') # Open the file
    for line in dataFile: # For each line in this file
        if not(re.search('#', line)): # If there is not a '#' character on this line, then the raw data has began and continues until the end of the file
            match_year = re.search(pattern_year, line) # Save the match for the year found on this line
            match_ppb = re.search(pattern_ppb, line) # If there is a match for CH4 PPB on this line succeeding the year match, then save the data corresponding to that year
            if match_year is not None: # Check if a match was found for a year on this line
                if match_ppb is not None: # Check if a match was found for CH4 PPB on this line
                    data[int(match_year.group(0))] = float(match_ppb.group(0)) # If a match was found then save it to the data dictionary object

    dataFile.close() # Close the file
    outfile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CH4Data.json', 'w') # Open the output file
    json.dump(data, outfile) # Output the data to the output file
    outfile.close() # Close the output file

# Open the CFC-11 data file and use regular expressions to read the data and output JSON
def write_CFC11():
    data = {} # The dictionary object that will be used to generate a JSON object
    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]' # A regular expression for scanning the data file and finding the CFC-11 PPT data on that line which might be "nan"
    pattern_ppt2 = r'.[0-9][0-9][0-9]' # A regular expression for scanning the data file and finding part of the CFC-11 PPT data on that line succeeding the decimal

    dataFile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CFC11Data.txt') # Open the file
    lastYearSeen = 0 # This data file lists the average for each month rather than each year, keep track of this and average months over the year
    lastMovingAverage = 0.0 # Keep a moving average to average the CFC-11 PPT over the year
    for line in dataFile: # For each line in this file
        if not(re.match('#', line)): # If there is not a '#' character on this line, then the raw data has began and continues until the end of the file
            if re.match(pattern_year, line): # If there is a match for a year found on this line, True will be returned and the program continues
                match_year = re.match(pattern_year, line) # Save the match for the year found on this line
                lineEdited = line.replace(str(match_year.group(0)), '') # Save an edited version of the line with the year removed from the beginning
                lineEdited = lineEdited[7:] # Save an edited version of the line with the blank space removed from the beginning
                match_ppt1 = lineEdited[0:3] # Read the next 3 characters to find a match for the CFC-11 PPT data
                if (match_ppt1 != '   '): # If those 3 characters are not blank, continue
                    lineEdited = lineEdited[3:] # Since those 3 characters are not blank, save a new edited line with those characters removed
                    match_ppt2 = re.match(pattern_ppt2, lineEdited) # Search for a match for the second part of the CFC-11 PPT regular expression
                    this_year = match_year.group(0) # Save the match for the year found on this line
                    this_ppt = match_ppt1 + match_ppt2.group(0) # Save both parts of the CFC-11 PPT matches concatenated together
                    if lastYearSeen == int(this_year): # If the year on this line is the same as the last year seen, we need to continue averaging this year
                        lastMovingAverage = (lastMovingAverage + float(this_ppt)) / 2.0 # Take the moving average for CFC-11 PPT this year 
                    else: # If the year on this line is not the same as the last year seen, a new year has began
                        if lastYearSeen != 0: # If the last year seen is not zero, then it is a valid year to save to the data dictionary
                            data[lastYearSeen] = float(lastMovingAverage)
                        lastYearSeen = int(this_year) # Set the last seen year to this year before going to the next line
                        lastMovingAverage = float(this_ppt) # Set the last moving average to this CFC-11 PPT before moving to the next line

    dataFile.close() # Close the file
    outfile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CFC11Data.json', 'w') # Open the output file
    json.dump(data, outfile) # Output the data to the output file
    outfile.close() # Close the output file

# Open the CFC-12 data file and use regular expressions to read the data and output JSON
def write_CFC12():
    data = {} # The dictionary object that will be used to generate a JSON object
    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]' # A regular expression for scanning the data file and finding the CFC-12 PPT data on that line which might be "nan"
    pattern_ppt2 = r'.[0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the CFC-12 PPT data on that line which might be "nan"

    dataFile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CFC12Data.txt') # Open the file
    lastYearSeen = 0 # This data file lists the average for each month rather than each year, keep track of this and average months over the year
    lastMovingAverage = 0.0  # Keep a moving average to average the CFC-12 PPT over the year
    for line in dataFile: # For each line in this file
        if not(re.match('#', line)): # If there is not a '#' character on this line, then the raw data has began and continues until the end of the file
            if re.match(pattern_year, line): # If there is a match for a year found on this line, True will be returned and the program continues
                match_year = re.match(pattern_year, line) # Save the match for the year found on this line
                lineEdited = line.replace(str(match_year.group(0)), '') # Save an edited version of the line with the year removed from the beginning
                lineEdited = lineEdited[7:] # Save an edited version of the line with the blank space removed from the beginning
                match_ppt1 = lineEdited[0:3] # Read the next 3 characters to find a match for the CFC-12 PPT data
                if (match_ppt1 != '   '): # If those 3 characters are not blank, continue
                    lineEdited = lineEdited[3:] # Since those 3 characters are not blank, save a new edited line with those characters removed
                    match_ppt2 = re.match(pattern_ppt2, lineEdited) # Search for a match for the second part of the CFC-12 PPT regular expression
                    this_year = match_year.group(0) # Save the match for the year found on this line
                    this_ppt = match_ppt1 + match_ppt2.group(0) # Save both parts of the CFC-12 PPT matches concatenated together
                    if lastYearSeen == int(this_year): # If the year on this line is the same as the last year seen, we need to continue averaging this year
                        lastMovingAverage = (lastMovingAverage + float(this_ppt)) / 2.0 # Take the moving average for CFC-11 PPT this year 
                    else: # If the year on this line is not the same as the last year seen, a new year has began
                        if lastYearSeen != 0: # If the last year seen is not zero, then it is a valid year to save to the data dictionary
                            data[lastYearSeen] = float(lastMovingAverage)
                        lastYearSeen = int(this_year) # Set the last seen year to this year before going to the next line
                        lastMovingAverage = float(this_ppt) # Set the last moving average to this CFC-11 PPT before moving to the next line

    dataFile.close() # Close the file
    outfile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'CFC12Data.json', 'w') # Open the output file
    json.dump(data, outfile) # Output the data to the output file
    outfile.close() # Close the output file

# Open the Temperature data file and use regular expressions to read the data and output JSON
def write_Temperature():
    data = {} # The dictionary object that will be used to generate a JSON object
    pattern_year = r'[0-9][0-9][0-9][0-9]' # A regular expression for scanning the data file and finding the year for the data on that line
    pattern_temp = r'[-]?[0-9][.][0-9][0-9]' # A regular expression for scanning the data file and finding the Temperature data on that line

    dataFile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'TemperatureData.txt') # Open the file
    for line in dataFile: # For each line in this file
        match_year = re.search(pattern_year, line) # If there is a match for a year found on this line, save that year
        match_temp = re.search(pattern_temp, line) # If there is a match for Temperature on this line succeeding the year match, then save the data corresponding to that year
        if match_year is not None: # Check if a match was found for a year on this line
            if match_temp is not None: # Check if a match was found for Temperature on this line
                data[int(match_year.group(0))] = float(match_temp.group(0)) # If a match was found then save it to the data dictionary object

    dataFile.close() # Close the file
    outfile = open(os.path.dirname(os.path.realpath(__file__) ) + os.sep + 'data' + os.sep + 'TemperatureData.json', 'w') # Open the output file
    json.dump(data, outfile) # Output the data to the output file
    outfile.close() # Close the output file
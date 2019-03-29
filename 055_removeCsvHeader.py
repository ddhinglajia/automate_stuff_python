#!/usr/bin/env python3
# removes the header from all csv files in current working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# loop through every fie in the current working directory

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skips non csv files
    
    print ('Removing header from ' + csvFilename + '...')

    # read the csv file in (skipping the first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num ==1:
            continue # skips the first row
        csvRows.append(row)
    csvFileObj.close()

    # writee out the csv file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',, newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
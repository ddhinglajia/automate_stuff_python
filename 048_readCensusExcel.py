#! /usr/bin/python3 

#tabulates population and number of census tracts for each country

import openpyxl, pprint

print('Opening wrkbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading rows...')

for row in range(2, sheet.get_highest _row()+1):
    # Each row in the spreadsheet has data for one census tracr.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value



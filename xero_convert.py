import sys
import csv
import datetime
import calendar
import os
import json
from datetime import timedelta

data = {}
go_live_date = '01-01-2022'


def get_month_end(date):
    date_obj = datetime.datetime.strptime(
            date,
            '%d-%b-%Y'
    )
    month_end_day = calendar.monthrange(
            date_obj.year,
            date_obj.month
    )[1]
    date_obj = date_obj.replace(
        day = month_end_day
    )
    reversal = date_obj + timedelta(days=1)
    dates = [
        ( date_obj.strftime('%d-%m-%Y'), 1),
        # Uncomment if you want the balances to reverse
        # ( reversal.strftime('%d-%m-%Y'), -1)
    ]
    return dates

export_dir = 'xero_export'
for file in os.listdir(export_dir):
    with open(export_dir+ '/' + file, 'r') as input_file:
        year = file.split('_')[3]
        csv_reader = csv.reader(input_file, delimiter='\t')
        next(csv_reader)
        for row in csv_reader:
            if row != []:
                for month_end, multiplier in get_month_end(row[1]):
                    month_end_obj = datetime.datetime.strptime(month_end, '%d-%m-%Y')
                    month_end_obj_test = datetime.datetime.strptime(go_live_date, '%d-%m-%Y')
                    if month_end_obj <= month_end_obj_test:
                        nominal = row[3]

                        department = row[9].lower()
                        location = row[10].lower()

                        value = float( row[5] ) * multiplier
                        
                        if year not in data:
                            data[year] = {}
                        
                        if month_end not in data[year]:
                            data[year][month_end] = {}
                        
                        if nominal not in data[year][month_end]:
                            data[year][month_end][nominal] = {}
                        
                        if location not in data[year][month_end][nominal]:
                            data[year][month_end][nominal][location] = {}

                        if department not in data[year][month_end][nominal][location]:
                            data[year][month_end][nominal][location][department] = 0
                        
                        data[year][month_end][nominal][location][department] += value


with open('converted/output.txt', 'w') as outputfile:
    outputfile.write(json.dumps(data, indent=4))

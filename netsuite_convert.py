import sys
import csv
import datetime
import calendar
import os
import json
from datetime import timedelta
from uuid import uuid4

f = open('converted/output.txt')
data = json.load(f)
f.close()

headings = [
    'tranId',
    'trandate',
    'subsidiary',
    'currency',
    'exchangerate',
    'postingperiod',
    'lane7_reference',
    'journalItemLine_memo',
    'journalItemLine_location',
    'journalItemLine_account',
    'journalItemLine_debitAmount',
    'journalItemLine_creditAmount',
    'journalItemLine_grossAmount',
    'journalItemLine_department',
    'journalItemLine_tax_account',
    'journalItemLine_tax_code',
    'journalItemLine_vat_amt'
]

subsidiary = 'Xero Demot UK Ltd'

with open('converted/netsuite_journals.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows([headings])
    r = 1
    for year in data:
        for month_end in data[year]:
            doc_no = month_end
            for nominal in data[year][month_end]:
                for location in data[year][month_end][nominal]:
                    for department in data[year][month_end][nominal][location]:
                        description = year + ' O/Bal Non-Cumulative'
                        value = data[year][month_end][nominal][location][department]
                        if round(value, 2) != 0:
                            if value > 0:
                                debit = abs(value)
                                credit = ''
                            else:
                                debit = ''
                                credit = abs(value)
                            csv_writer.writerows([
                                [
                                    str( uuid4() ), #'tranId',
                                    month_end, #'trandate',
                                    subsidiary, #'subsidiary',
                                    'GBP', #'currency',
                                    '', #'exchangerate',
                                    month_end, #'postingperiod',
                                    doc_no, #'reference',
                                    description, #'journalItemLine_memo',
                                    location, #'journalItemLine_location',
                                    nominal, #'journalItemLine_account',
                                    debit, #'journalItemLine_debitAmount',
                                    credit, #'journalItemLine_creditAmount',
                                    value, #'journalItemLine_grossAmount',
                                    department, #'journalItemLine_department',
                                    '', #'journalItemLine_tax_account',
                                    '', #'journalItemLine_tax_code',
                                    '', #'journalItemLine_vat_amt'
                                ]
                            ])
                            r += 1
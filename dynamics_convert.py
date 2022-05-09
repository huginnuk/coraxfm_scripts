import sys
import csv
import datetime
import calendar
import os
import json
from datetime import timedelta

f = open('converted/output.txt')
data = json.load(f)
f.close()

headings = [
    'Journal Template Name',
    'Journal Batch Name',
    'Line No.',
    'Account Type',
    'Account No.',
    'Posting Date',
    'Document Type',
    'Document No.',
    'Description',
    'Bal. Account No.',
    'Currency Code',
    'Amount',
    'Debit Amount',
    'Credit Amount',
    'Amount (LCY)',
    'Shortcut Dimension 1 Code',
    'Shortcut Dimension 2 Code',
    'Due Date',
    'VAT Amount',
    'Payment Terms Code',
    'Gen. Posting Type',
    'Gen. Bus. Posting Group',
    'Gen. Prod. Posting Group',
    'Bal. Account Type',
    'Bal. Gen. Posting Type',
    'Bal. Gen. Bus. Posting Group',
    'Bal. Gen. Prod. Posting Group',
    'VAT Base Amount',
    'Document Date',
    'External Document No.',
    'VAT Bus. Posting Group',
    'VAT Prod. Posting Group',
    'Bal. VAT Bus. Posting Group',
    'Bal. VAT Prod. Posting Group',
]

with open('converted/dynamics_journals.csv','w') as csv_file:
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
                                'GENERAL', # 'Journal Template Name',
                                'DEFAULT', # 'Journal Batch Name',
                                r, # 'Line No.',
                                'G/L Account', # 'Account Type',
                                nominal, # 'Account No.',
                                month_end, # 'Posting Date',
                                '', # 'Document Type',
                                doc_no, # 'Document No.',
                                description, # 'Description',
                                '', # 'Bal. Account No.',
                                '', # 'Currency Code',
                                value, # 'Amount',
                                debit, # 'Debit Amount',
                                credit, # 'Credit Amount',
                                '', # 'Amount (LCY)',
                                location, # 'Shortcut Dimension 1 Code',
                                department, # 'Shortcut Dimension 2 Code',
                                '', # 'Due Date',
                                '', # 'VAT Amount',
                                '', # 'Payment Terms Code',
                                '', # 'Gen. Posting Type',
                                '', # 'Gen. Bus. Posting Group',
                                '', # 'Gen. Prod. Posting Group',
                                '', # 'Bal. Account Type',
                                '', # 'Bal. Gen. Posting Type',
                                '', # 'Bal. Gen. Bus. Posting Group',
                                '', # 'Bal. Gen. Prod. Posting Group',
                                '', # 'VAT Base Amount',
                                '', # 'Document Date',
                                '', # 'External Document No.',
                                '', # 'VAT Bus. Posting Group',
                                '', # 'VAT Prod. Posting Group',
                                '', # 'Bal. VAT Bus. Posting Group',
                                '', # 'Bal. VAT Prod. Posting Group'
                                ]
                            ])
                            r += 1
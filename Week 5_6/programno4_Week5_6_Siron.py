'''Implement a program to read a CSV file 
and display its contents in a tabular format'''

import csv

f = ["Name","Year","GPA"]

r =[
    ["Siron","2008","3.71"],
    ["Sanita","2007","3.50"],
    ["Garima","2006","3.15"],
    ["Arika","2006","2.95"]
]

fn = "program4.csv"

with open(fn,'w',newline= '') as csvfile:
    csv_content = csv.writer(csvfile)
    csv_content.writerow(f)
    csv_content.writerow(r)
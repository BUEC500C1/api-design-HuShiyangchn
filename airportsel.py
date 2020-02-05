import csv
filename='airport-codes.csv'
outfilename='us-airport-codes.csv'
#select US airport information from airport-codes.csv
with open(filename) as f, open(outfilename,'w') as out:
    reader = csv.reader(f)
    writer = csv.writer(out)
    for row in reader:
        if row[5]=="US":
            writer.writerow(row)
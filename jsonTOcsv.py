import sys
import json
import csv

with open(sys.argv[1], 'r|') as inf:
    data = json.load(inf)
    with open(sys.argv[2], 'w|') as outf:
        writerFile = csv.writer(outf)
        writerFile.writerow(data[0].keys())
        for row in data:
            writerFile.writerow(row.values()) 

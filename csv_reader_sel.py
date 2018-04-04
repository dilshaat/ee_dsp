import csv

with open('dsp_targets.csv', 'r') as f:
    lines = csv.reader(f, delimiter='\t')
    counter = 0
    for line in lines:
        counter += 1
        print(str(counter) + " " + str(line))
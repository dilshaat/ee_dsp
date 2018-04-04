import csv

with open('test_object.csv', 'r') as f:
    lines = csv.reader(f, delimiter='\t')
    counter = 0
    for line in lines:
        counter += 1
        print(str(counter) + " " + str(line))
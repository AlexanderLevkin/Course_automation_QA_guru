import csv

with open('resources/username.csv') as csvfile:
    csvfile = csv.reader(csvfile)
    for r in csvfile:
        print(r)

with open('resources/names.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Anna", "Pavel", "Petr"])
    csvwriter.writerow(["Anna", "Pavel", "Petr"])

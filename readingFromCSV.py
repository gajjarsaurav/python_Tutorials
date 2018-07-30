import csv

with open('/Users/gajjarsaurabh/Classified/python/python_practice/ex.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
        print(row)
        print(row[2])
        print(row[1], row[2])


# when we wan't to store something in column, then
with open('/Users/gajjarsaurabh/Classified/python/python_practice/ex.csv') as csvfile:
    read = csv.reader(csvfile, delimiter = ',')
    dates = []
    colors = []
    for r in read:
        date = r[1]
        color = r[4]
        dates.append(date)
        colors.append(color)
print(dates)
print(colors)
# So we just learned how to fill an empty list as columns of a csv file

# code snippet for pirnting out the corresponding color for an index of a color
# implementing try and except error handling
ch = 'y'                # IMP: in pyhon to declare a variable it needs to be assigned
while ch is 'y':        # using while loop
    try:
        getColor = input('choose a color:')
        colorIndex = colors.index(getColor.lower())
        reqDate = dates[colorIndex]
        print(reqDate)
    except Exception as a:
        print(a)

    print('continue...')
    ch = input('enter y or n')

#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
from itertools import islice


if len(sys.argv) < 6:
    print("usage: graph file columns_per_row x_column y_column x_label y_label")

datafile = open(sys.argv[1])
columnsperrow = int(sys.argv[2])
columnx = int(sys.argv[3])
columny = int(sys.argv[4])

labelx = sys.argv[5]
labely = sys.argv[6]

datalines = [x.split() for x in datafile.readlines()]
datafile.close()

data = [float(element) for sublist in datalines for element in sublist]

print(data)

datax = data[columnx::columnsperrow]
datay = data[columny::columnsperrow]

plt.plot(datax,datay)
plt.xlabel(labelx)
plt.ylabel(labely)
plt.show()

#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
from itertools import islice


if len(sys.argv) < 6:
    print("usage: graph file title columns_per_row x_column_name x_column y_column_name y_column x_label y_label")

datafile = open(sys.argv[1])
title = sys.argv[2]
columnsperrow = int(sys.argv[3])

legandx = sys.argv[4]
columnx = int(sys.argv[5])

legandy = sys.argv[6]
columny = int(sys.argv[7])

labelx = sys.argv[8]
labely = sys.argv[9]

datalines = [x.split() for x in datafile.readlines()]
datafile.close()

data = [float(element) for sublist in datalines for element in sublist]

datax = data[columnx::columnsperrow]
datay = data[columny::columnsperrow]

frames = np.arange(len(datalines))
plt.gca().set_prop_cycle(cycler('color', ['red', 'green', 'blue', 'yellow']))

plt.plot(frames, datax, label=legandx)
plt.plot(frames, datay, label=legandy)
plt.xlabel(labelx)
plt.ylabel(labely)
plt.title(title)

plt.legend(loc='upper left')
plt.show()

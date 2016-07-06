#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

if len(sys.argv) < 4:
    print "usage: graph file x_label y_label"

datafile = open(sys.argv[1])
datalines = datafile.readlines()
datafile.close()

data = [float(x) for x in datalines]

plt.plot(data)
plt.xlabel(sys.argv[2])
plt.ylabel(sys.argv[3])
plt.show()

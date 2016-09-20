#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
from itertools import islice
from enum import Enum

'''
Config file format

GraphType[1D|2D]
title
columns per row
x axis label
y axis label
columnindexA (This is the x-axis in 2D graphs)
columnnameA
columnindexB
columnnameB
...
'''

class GraphInfo:
    class GraphType(Enum):
        plot1D = 1
        plot2D = 2

    def readconfig(self, configfilename):
        configfile = open(configfilename)

        self.graphtype = self.string2graphtype(configfile.readline());
        self.title = configfile.readline()
        self.columnsperrow = int(configfile.readline())

        self.labelx = configfile.readline()
        self.labely = configfile.readline()

        self.columnlines = zip(*[iter(configfile.readlines())] * 2)

    def graphdata(self, datafilename):
        datafile = open(datafilename)
        datalines = [line.split() for line in datafile.readlines()]
        datafile.close()
        data = [float(element) for sublist in datalines for element in sublist]

        if self.graphtype == self.GraphType.plot1D:
            self.graph1dplot(data, len(datalines))
        elif self.graphtype == self.GraphType.plot2D:
            self.graph2dplot(data)

    def graph1dplot(self, data, numlines):
        frames = np.arange(numlines)
        for plot in self.columnlines:
            index = int(plot[0])
            legend = plot[1]
            plotdata = data[index::self.columnsperrow]
            plt.plot(frames, plotdata, label=legend)

        self.setupgraph()
        plt.show()

    def graph2dplot(self, data):
        xdata = None
        for plot in self.columnlines:
            index = int(plot[0])
            legend = plot[1]
            plotdata = data[index::self.columnsperrow]

            if xdata == None:
                xdata = plotdata
            else:
                plt.plot(xdata, plotdata, label=legend)

        self.setupgraph()
        plt.show()

    def string2graphtype(self, string):
        if "1D" in string:
            return self.GraphType.plot1D
        elif "2D" in string:
            return self.GraphType.plot2D

    def setupgraph(self):
        plt.gca().set_prop_cycle(cycler('color', ['red', 'green', 'blue', 'yellow', 'purple', 'orange']))
        plt.xlabel(self.labelx)
        plt.ylabel(self.labely)
        plt.title(self.title)
        plt.legend(loc='upper left')

if len(sys.argv) != 3:
    print("usage: graph config_file data_file")

graphinfo = GraphInfo ()

graphinfo.readconfig(sys.argv[1])
graphinfo.graphdata(sys.argv[2])
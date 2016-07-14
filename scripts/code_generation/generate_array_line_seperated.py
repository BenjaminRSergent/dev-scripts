#!/usr/bin/python
import sys

if len(sys.argv) != 5:
    print "Usage: generate_array type array_name input_file output_file"

data_file = open(sys.argv[3], 'r')
data = [int(line) for line in data_file.readlines()]
data_file.close()

array_str = sys.argv[1] + " " + sys.argv[2] + "[] = {"

for datum in data:
    array_str = array_str + str(datum) + ","

array_str = array_str[0:-3]

array_str += "};"

output_file = open(sys.argv[4], 'w+')

output_file.write(array_str)

output_file.close()





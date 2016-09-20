#!/usr/bin/python

# By: Cowart, Dominique A 9.17.16

# file io lib
import sys

# Goal: open a text file and change words "free" to "proprietary"

# define the path to the file
in_file = "manifesto"
out_file = "manifesto_out"

# obtain a file handle to open
fh = open(in_file, "r")
fh2 = open(out_file, "w")

# read each line and remove the newlines
for line in fh:
    line = line.strip('\n')
    line2 = line.replace("free", "proprietary") + "\n"
    print line2
    fh2.write(line2)

fh.close()
fh2.close()

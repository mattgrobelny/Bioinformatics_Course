#!/usr/bin/python

import sys

# importing file
in_file = "Mus_musculus.GRCm38.out"
fh1 = open(in_file, 'r')

mapped_once = 0
not_mapped = 0
for line in fh1:
    line = line.strip('/n')
    if line[0] != "@":
        # split columns by tabs
        line_columns = line.split('\t')

        #collect flag
        flag = int(line_columns[1])

        # if read is mapped and mapped only once then mapped_once ++ 1
        if((flag & 4) != 4) and ((flag & 256) != 256):
            mapped_once += 1

        # if read is not mapped at all then not_mapped ++ 1
        elif ((flag & 4) == 4):
            not_mapped += 1

print "Number of mapped reads mapped once:", mapped_once
print "Number of reads not mapped:", not_mapped

# Number of mapped reads mapped once: 2020536
# Number of reads not mapped: 118939

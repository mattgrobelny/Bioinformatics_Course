#!/usr/bin/python

in_file = '~/shell/fst/batch_2.fst_1-2.Chr_only.tsv'
fst_total = 0
count = 0


fh = open(in_file, 'r')

# Iterate over each line in the file
for line in fh:
    # Remove new lines
    line = line.strip('\n')
    # We can split TSV files
    parts = line.split('\t')

    # print the fst value
    print parts[8]
    count = count + 1
    fst_total = parts[8] + fst_total

# print avg fst
print fst_total / count

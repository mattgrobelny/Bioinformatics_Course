#!/usr/bin/python

import sys
import getopt
import matplotlib
import numpy as np
matplotlib.use("Agg")  # Force matplotlib to not use Xwindows backend.

import matplotlib.pyplot as plt

kmer = 0
file_name = ""
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hk:f:")
except getopt.GetoptError:
    print 'kmer.py -k <kmer_size> -f <inputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'kmer.py -k <kmer_size> -f <inputfile>'
        sys.exit()
    elif opt in ("-k"):
        kmer = arg
    elif opt in ("-f"):
        file_name = arg
print "Kmer size is: ", kmer
print "Input file is: ", file_name

# Dictionary storing kmers
kmer_dic = {}

# importing file
in_file = file_name
fh1 = open(in_file, 'r')
count = 0
record_count = 0
# skip first line
next(fh1)

for line in fh1:
    count = count + 1
    if count % 4 == 1:
        line.strip('\n')
        record_count += 1
        line_length = len(line)

        # Starting kmer parsing 0 to length of line minus kmer size
        for kmer_start_index in range(0, (int(line_length) - int(kmer))):

            # range for kmer
            kmer_end_index = kmer_start_index + int(kmer)

            # collect khmer for this iteraton
            kmer_string = line[kmer_start_index: kmer_end_index]

            # check for kmer in dictionary and ++ if not present add to dic and equal 1
            kmer_dic[kmer_string] = kmer_dic.get(kmer_string, 0) + 1

# khmer freq dictionary
kmer_dic_freq = {}

# count the number of count of kmers
for val in kmer_dic.values():
    kmer_dic_freq[val] = kmer_dic_freq.get(val, 0) + 1


print " "
print "#-----------------------------------------------------------------------#"

list_of_kmer_counts = []
list_of_kmer_counts.append([])
list_of_kmer_counts.append([])

# Print out list of counts of count of K-mers
print "K-mer Frequency  Number of K-mers in this category"
for key in sorted(kmer_dic_freq.keys()):
    print key, " ", kmer_dic_freq[key]
    list_of_kmer_counts[0].append(key)
    list_of_kmer_counts[1].append(kmer_dic_freq[key])

print " "
print "#-----------------------------------------------------------------------#"
# Plot
plt.bar(list_of_kmer_counts[0], list_of_kmer_counts[1])
t = np.arange(0, 10, 10000)
plt.semilogy(t, np.exp(10))
plt.xlabel('Number of K-mers')
plt.ylabel('Number of Appearances')
plt.title('Counts of the number of Kmer Occurences')
plt.annotate('K-mer size = %s' % (kmer), xy=(100, 100), xytext=(3, 4))
plt.grid(True)

print "\nSaving Plot of: kmer_freq.png"
# Save first graph
plt.savefig('kmer_freq_with_Ksize_%s.png' % (kmer))
plt.close()

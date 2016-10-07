#!/usr/bin/python

import sys
import getopt
import matplotlib
import numpy as np
matplotlib.use("Agg")  # Force matplotlib to not use Xwindows backend.

import matplotlib.pyplot as plt

kmer = 11
file_name = ""
xmax = 2000
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hk:x:f:")
except getopt.GetoptError:
    print 'kmer.py -k <kmer_size> -x <x_axis_max> -f <inputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print "K-mer frequnecy graphing script \n"
        print "Usage: \n"
        print 'kmer.py -k <kmer_size> -x <x_axis_max> -f <inputfile> \n\n'
        print "Goals:
        print "1) Take in fastq file and kmerize it and output kmer occurence frequnecy\n"
        print "2) Output graph of kmer occurence frequnecy\n"
        print "3) Output kmer occurence frequnecy to .tsv file\n"
        print "\n"

        sys.exit()
    elif opt in ("-k"):
        kmer = arg
    elif opt in ("-x"):
        xmax = arg
    elif opt in ("-f"):
        file_name = arg
print "Kmer size is:", kmer
print "X-axis max kmer count is:", xmax
print "Input file is:", file_name
print " "


###############################################################################
# Progress bar is not my own work from:
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
#
def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()
##################################################

# Dictionary storing kmers
kmer_dic = {}

# importing file
in_file = file_name
fh1 = open(in_file, 'r')

# Count number of lines in a file
num_lines = sum(1 for line in fh1)
fh1.close
if num_lines >= 100000:
    print "Your file has %s number of lines..." % (num_lines)
    print "This may take a while to process..."
    print "...so be patience..."
    print " "

fh2 = open(in_file, 'r')
# skip first line
next(fh2)

count = 0

print "K-merizing the reads..."
for line in fh2:
    progress(count, num_lines, suffix='done')
    count = count + 1
    if count % 4 == 1:
        line.strip('\n')
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

list_of_kmer_occurences = []
list_of_kmer_occurences.append([])
list_of_kmer_occurences.append([])

# Print out list of counts of count of K-mers
print "K-mer Frequency  Number of K-mers in this category"
for key in sorted(kmer_dic_freq.keys()):
    print key, " ", kmer_dic_freq[key]
    list_of_kmer_occurences[0].append(key)
    list_of_kmer_occurences[1].append(kmer_dic_freq[key])

print " "
print "#-----------------------------------------------------------------------#"

# Open file for writing
file_out = "./%s_kmer_freq_data_Ksize_%s.tsv" % (file_name[:-6], kmer)
fh_out = open(file_out, 'w')

fh_out.write("K-mer Frequency\tNumber of K-mers in this category\n")
for key in sorted(kmer_dic_freq.keys()):
    fh_out.write("%s\t%s\n" % (key, kmer_dic_freq[key]))
fh_out.close

# Ploting
print "Graphing Kmers..."

plt.bar(kmer_dic_freq.keys(), kmer_dic_freq.values(), edgecolor="none", width=1.0, log=True)
plt.xlim(0, int(xmax))
plt.xlabel('Number of K-mers')
plt.ylabel('Number of Appearances')
plt.title('Counts of the number of Kmer Occurences')
plt.annotate('K-mer size = %s' % (kmer), xy=(1, 3), xytext=((int(xmax)- 489), 21))
plt.grid(True)

print "\nPrinting %s_kmer_freq_hist_Ksize_%s.png" % (file_name[:-6], kmer)
# Save first graph
plt.savefig("%s_kmer_freq_hist_Ksize_%s.png" % (file_name[:-6], kmer))
plt.close()

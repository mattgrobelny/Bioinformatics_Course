#!/usr/bin/python

import sys
import getopt
import matplotlib
import numpy as np
matplotlib.use("Agg")  # Force matplotlib to not use Xwindows backend.

import matplotlib.pyplot as plt

# default parameters
kmer = 11
file_name = ""
xmax = 2000
file_type = "fasta"
bar_stat = 0
bar_Y_N = "Off"
output_dir = "./"
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hpk:x:f:t:d:")
except getopt.GetoptError:
    print 'kspec.py -k <kmer_size> -x <x_axis_max> -t <type>[fasta|fastq] -p[progress bar on] -d <output_dir> [./] -f <inputfile> \n'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print "#--- K-mer frequency graphing script ---#\n"
        print "Usage:"
        print 'kspec.py -k <kmer_size> -x <x_axis_max> -t <type>[fasta|fastq] -p[progress bar on] -d <output_dir> [./] -f <inputfile> \n'
        print "Goals:"
        print "1) Take in fastq file and kmerize it and output kmer occurence frequnecy"
        print "2) Output graph of kmer occurence frequnecy"
        print "3) Output kmer occurence frequnecy to .tsv file"
        print "\n"

        sys.exit()
    elif opt in ("-k"):
        kmer = arg
    elif opt in ("-x"):
        xmax = arg
    elif opt in ("-f"):
        file_name = arg
    elif opt in ("-t"):
        file_type = arg
    elif opt in ("-p"):
        bar_stat = 1
        bar_Y_N = "On"
    elif opt in ("-d"):
        output_dir = arg
print "Input file:", file_name
print "Input file type:", file_type
print "Kmer size:", kmer
print "X-axis max kmer count:", xmax
print "Progress Bar:", bar_Y_N
print "Output Dir:", output_dir
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
seq_total = ""
count = 0
kmer_range = 0
if str(file_type) == "fastq":
    print "K-merizing the reads..."
    for line in fh2:
        if bar_stat == 1:
            progress(count, num_lines, suffix='done')
        count = count + 1
        if count % 4 == 1:

            # strip new line char
            line = line.strip('\n')

            # determine range of kmer
            line_length = len(line)
            kmer_range = line_length - int(kmer) + 1

            # Starting kmer parsing 0 to length of line minus kmer size
            for kmer_start_index in range(kmer_range):

                # range for kmer
                kmer_end_index = kmer_start_index + int(kmer)

                # collect khmer for this iteraton
                kmer_string = line[kmer_start_index: kmer_end_index]

                # check for kmer in dictionary and ++ if not present add to dic and equal 1
                kmer_dic[kmer_string] = kmer_dic.get(kmer_string, 0) + 1

elif file_type == "fasta":
    for line in fh2:
        if bar_stat == 1:
            progress(count, num_lines, suffix='done')
        if line[0] != ">":
            line = line.strip('\n')
            seq_total = seq_total + line
            count += 1
            continue
        elif line[0] == ">":
            # determine range of kmer
            line_length = len(seq_total)
            kmer_range = line_length - int(kmer) + 1

            # Starting kmer parsing 0 to length of line minus kmer size
            for kmer_start_index in range(kmer_range):

                # range for kmer
                kmer_end_index = kmer_start_index + int(kmer)

                # collect khmer for this iteraton
                kmer_string = seq_total[kmer_start_index: kmer_end_index]
                # check for kmer in dictionary and ++ if not present add to dic and equal 1
                kmer_dic[kmer_string] = kmer_dic.get(kmer_string, 0) + 1
            count += 1
            seq_total = ""
            continuecd
# procces file name
file_name_out = file_name.split('/')
file_name_split = file_name_out[-1]


# Open file for writing
file_out = str(output_dir) + "%s_raw_kmer_data_Ksize_%s.tsv" % (file_name_split[:-6], kmer)
fh_out = open(file_out, 'w')

fh_out.write("K-mer\tNumber of K-mers\n")
for key in kmer_dic.keys():
    fh_out.write("%s\t%s\n" % (key, kmer_dic[key]))
fh_out.close

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
file_out = str(output_dir) + "%s_kmer_freq_data_Ksize_%s.tsv" % (file_name_split[:-6], kmer)
fh_out = open(file_out, 'w')
print "Writing to: file_out"

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

print "\nPrinting to %s%s_kmer_freq_hist_Ksize_%s.png" % (output_dir, file_name_split[:-6], kmer)
# Save first graph
plt.savefig(str(output_dir) + "%s_kmer_freq_hist_Ksize_%s.png" % (file_name_split[:-6], kmer))
plt.close()

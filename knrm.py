#!/usr/bin/python

from datetime import datetime
startTime = datetime.now()
import sys
import getopt
import numpy as np

# default parameters
kmer = 15
coverage = 10
file_name = ""

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hk:f:c:")
except getopt.GetoptError:
    print 'knorm.py -k <kmer_size>[15] -c <coverage>[10] -f <inputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print "#--- Read Normalization Script ---#\n"
        print "Usage:"
        print "knorm.py -k <kmer_size>[15] -c <coverage>[10] -f <inputfile>\n"
        print "Goals:"
        print "1) Input fastq reads"
        print "2) K-merize and filter out reads based on desired coverage"
        print "3) Save reads with coverage less than or equal to coverage threshold in new file"
        print ""
        print "Output:"
        print "FILENAME_k_KMER#_cov_COVERAGE#_norm.fastq"

        sys.exit()
    elif opt in ("-k"):
        kmer = arg
    elif opt in ("-f"):
        file_name = arg
    elif opt in ("-c"):
        coverage = arg
print "Input file: ", file_name
print "Kmer size: ", kmer
print "Desired coverage: %sx" % (coverage)



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

# Importing file for line count
in_file = file_name
fh1 = open(in_file, 'r')

# Count number of lines in a file
num_lines = sum(1 for line in fh1)
fh1.close
if num_lines >= 100000:
    print "Your file has %s number of lines..." % (num_lines)
    print "This may take a while to process..."
    print "...so be patience..."
    print " \n"

# re-open input file for processing
fh2 = open(in_file, 'r')

# open output file for reads to be kept
out_file = str("%s_k_%s_cov_%s_norm.fastq" % (file_name[:-6], kmer, coverage))
fh_out = open(out_file, 'w')

# Init dictionary for storing kmers
kmer_dic = {}

# Init array for storing kmer occurence for each read
cov_array = []

# Iteration counter
count = 1

# variables for outputing read data
read_name = ""
read_seq = ""
read_plus = "+"
read_quality = ""

print "K-merizing the reads..."
for line in fh2:
    line = line.strip('\n')
    progress(count, num_lines, suffix='done')

    # save read header
    if count % 4 == 1:
        read_name = line
        count += 1
    # save sequence string and kmerize sequence
    elif count % 4 == 2:
        read_seq = line
        line_length = len(line)

        # Starting kmer parsing 0 to length of line minus kmer size
        for kmer_start_index in range(0, (int(line_length) - int(kmer) + 1)):

            # range for kmer
            kmer_end_index = kmer_start_index + int(kmer)

            # collect khmer for this iteraton
            kmer_string = line[kmer_start_index: kmer_end_index]

            # check for kmer in dictionary and ++ if not present add to dic and equal 1
            kmer_dic[kmer_string] = kmer_dic.get(kmer_string, 0) + 1

            # append the coverage for each k-mer onto the coverage array
            cov_array.append(kmer_dic[kmer_string])

        count += 1
    # add counter for plus line
    elif count % 4 == 3:
        count += 1

    # save quality line
    elif count % 4 == 0:
        read_quality = line

        # determine if median of coverage array is <= coverage
        if np.median(cov_array) <= int(coverage):

            # write header, seq, +, quality score to file
            fh_out.write("%s\n%s\n%s\n%s\n" % (read_name, read_seq, read_plus, read_quality))
            cov_array = []
        else:
            cov_array = []  # clear array
        count += 1

# close out files
fh2.close
fh_out.close

print "\nFinish! \nDone in:", datetime.now() - startTime
print "Normalized reads were stored in :", out_file

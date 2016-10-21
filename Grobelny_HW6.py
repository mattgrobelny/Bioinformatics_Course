# Hw 6
import sys
import re
import getopt

# default parameters
file_name = ""
kmer = ""
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hk:f:")
except getopt.GetoptError:
    print 'velvethg_qc.py -f <inputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print "#--- Velveth Assembly Quality script ---#\n"
        print "Usage:"
        print 'velvethg_qc.py -k <kmerlength>-f <inputfile> \n'
        print "Goals:"
        print ""
        print ""
        print ""
        print "\n"

        sys.exit()
    elif opt in ("-k"):
        kmer = int(arg)
    elif opt in ("-f"):
        file_name = arg
print "Input file:", file_name
print " "

fh = open(file_name, 'r')
# Requirements
# Using Python regular expressions,extract k-mer length of each contig(in red below).
# In addition, extract the k-mer coverage for the contig (in green).
# >NODE_11_length_3717_cov_19.315845

# count variables
num_contigs = 0
contig_length_data = []
contig_cov_data = []

# pre compile pattern
regex_pat = re.compile(r'^>NODE_\d+_length_(\d+)_cov_(\d+\.\d+)')

# loop to collect kmer length and cov --> append each variable to its own list
for line in fh:
    line = line.strip('\n')
    if line[0] == ">":
        contig_data = re.findall(regex_pat, str(line))

        kmer_len, kmer_cov = contig_data[0]

        # convert to contig physical length
        contig_nuc_len = kmer_len * (kmer - 1)

        # add contig length data to list
        contig_length_data.append(int(contig_nuc_len))

        # add contig cov data to list
        contig_cov_data.append(float(kmer_cov))

        # add one to contig count
        num_contigs += 1

# Adjust the k-mer length to represent the physical length.
# Calculate:
# -the number of contigs
# -the maximum contig length
# -the mean contig length
# -total length of the genome across all the contigs.
# -mean depth of coverage for the contigs
# -N50 value of your assembly

# sort data
contig_length_data_sorted = sorted(contig_length_data)
contig_cov_data_sorted= sorted(contig_cov_data)

# Distribution of contigs
# Calculate the distribution of contig lengths,and bucket the contig lengths
# into groups of 100bp. So, all contigs with lengths between 0 and 99 would be
# in the 0 bucket, those with lengths between 100 and 199 would be in the 100 bucket

# Convert lengths of contigs --> round and based on round assign to bin
# Print distribution

# Hw 6

# default parameters
file_name = ""
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "hf:")
except getopt.GetoptError:
    print 'velvethg_qc.py -f <inputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print "#--- Velveth Assembly Quality script ---#\n"
        print "Usage:"
        print 'velvethg_qc.py -f <inputfile> \n'
        print "Goals:"
        print ""
        print ""
        print ""
        print "\n"

        sys.exit()
    elif opt in ("-f"):
        file_name = arg
print "Input file:", file_name
print " "


# Requirements
# Using Python regular expressions,extract k-mer length of each contig(in red below).
# In addition, extract the k-mer coverage for the contig (in green).
# >NODE_11_length_3717_cov_19.315845

# Adjust the k-mer length to represent the physical length.
# Calculate:
# -the number of contigs
# -the maximum contig length
# -the mean contig length
# -total length of the genome across all the contigs.
# -mean depth of coverage for the contigs
# -N50 value of your assembly

# Distribution of contigs
# Calculate the distribution of contig lengths,and bucket the contig lengths
# into groups of 100bp. So, all contigs with lengths between 0 and 99 would be
# in the 0 bucket, those with lengths between 100 and 199 would be in the 100 bucket

# Convert lengths of contigs --> round and based on round assign to bin
# Print distribution

#!/usr/bin/python

# IN CLASS 8

# Part 1
# Goal open a Illumina fastq file of and count the number of barcodes
in_file = "/home/a-m/ib501_stud12/shell/s_1_sequence.txt"

# open file
fh = open(in_file, 'r')

# make barcodes dictionary
barcodes = {}
count = 0

# skip record name
next(fh)

for line in fh:
    count = count + 1
    line = line[0:5]
    if count % 4 == 1:
        # make uniq barcode if it doesnt exist or increment by one if it does
        barcodes[line] = barcodes.get(line, 0) + 1
fh.close

# print uniq barcodes and their counts
print barcodes.items()

# Part 2
# Goal:
# - Translate the quality scores for each FASTQ record
# - count the number of nucleotides below a quality score threshold.
# - Tally the number of reads that fall below the threshold
# - Print the number of sequences read and the number dropped.

fh2 = open(in_file, 'r')

# quality threshold parameters
phred_thresh = 50
perc_highQ_nucs = 0.8

quality = {}
count = 0
num_bad_reads = 0
num_good_reads = 0

# skill record name, seq, quality name
next(fh2)
next(fh2)
next(fh2)

for line in fh2:
    count = count + 1
    good_nuc = 0
    bad_nuc = 0
    qual_type = ""
    if count % 4 == 1:
        for i in line:
            # convert ASCII to ints offset by 33
            q_score_for_nuc = ord(str(i)) - 33

            # asign good qual threshold
            if int(q_score_for_nuc) > phred_thresh:
                good_nuc = good_nuc + 1
            else:
                bad_nuc = bad_nuc + 1

        # Determine whether read is high qual
        if float(good_nuc) / (float(bad_nuc) + float(good_nuc)) > perc_highQ_nucs:
            qual_type = "High_qual"
            num_good_reads = num_good_reads + 1
            quality[count] = [good_nuc, bad_nuc, qual_type]
        else:
            qual_type = "Bad_qual"
            num_bad_reads = num_bad_reads + 1
            quality[count] = [good_nuc, bad_nuc, qual_type]
    else:
        continue
fh2.close
# print quality.items()
total_reads = num_bad_reads + num_good_reads

print "\nThere were %s number of good reads out of %s total reads" % (num_good_reads, total_reads)
print "* Good reads = %s percent of nucleotides in a read had a phred score > %s" % (perc_highQ_nucs * 100, phred_thresh)
print num_bad_reads, "were bad reads and would be dropped "

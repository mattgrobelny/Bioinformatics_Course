#!/usr/bin/python

# Hw 3

id_name   = "@GAAATG_1_1101_4446_2137_1"
seq = "TGCAGGTTGAGTTCTCGCTGTCCCGCCCCCATCTCTTCTCTTCCAGTCTGGCTCTGGAGCAGTTGAGCCCAGCTCAGGTCCGCCGGAGGAGACCG"
phred = "FFHHHHHJJJJIJIJJJIJJJJJJIIIJJJEHJJJJJJJIJIDGEHIJJFIGGGHFGHGFFF@EEDE@C??DDDDDDD@CDDDDBBDDDBDBDD@"

def convert_phred(asiic_score):
        q_score_for_nuc = ord(str(asiic_score)) - 33
        return q_score_for_nuc

def qual_score(encoded_phred_score):
    total_score = 0
    count = 0
    for i in encoded_phred_score:
        total_score = convert_phred(i) + total_score
        count += 1
    # return avg quality score for encoded_phred_score
    return float(total_score) / float(count)

count = 0
for i in phred:
    print count, ":", i, "- ", convert_phred(i)
    count += 1

print "Avg quality for phred string"
print "\n", qual_score(phred)

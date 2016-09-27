#!/usr/bin/python/2.7.9
# Runs on python/2.7.9 from cluster
import sys
import numpy as np
import matplotlib.pyplot as plt

# Grobelny HW 4

# progress bar is not my own work from:
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

def convert_phred(asiic_score):
        q_score_for_nuc = ord(str(asiic_score)) - 33
        return q_score_for_nuc

print "constructing arrays\n"
# make 2d array
qual_list = []
qual_list.append([])  # [0] = base number
qual_list.append([])  # [1] = total quality score
qual_list.append([])  # [2] = avg quality score

# make 2nd 2d array
var_std_dev_list = []
var_std_dev_list.append([])  # [0] = base number
var_std_dev_list.append([])  # [1] = variance totals
var_std_dev_list.append([])  # [2] = variance
var_std_dev_list.append([])  # [3] = standard dev

median_list_output = []
median_list_output.append([])
median_list_output.append([])


for i in range(101):
    # add base numbers to each array
    qual_list[0].append(i)
    var_std_dev_list[0].append(i)
    median_list_output[0].append(i)
    # intialize array values
    qual_list[1].append(0.0)
    qual_list[2].append(0.0)
    var_std_dev_list[1].append(0.0)
    var_std_dev_list[2].append(0.0)
    var_std_dev_list[3].append(0.0)
    median_list_output[1].append(0.0)

# open file
# in_file = "/home/a-m/ib501_stud12/shell/lane1_NoIndex_L001_R1_003.fastq"
in_file = "/home/a-m/ib501_stud12/shell/lane1.short.fastq"
fh1 = open(in_file, 'r')

# file length
#file_length = 4000000 * 4
file_length = 1000

# line counter
count = 0

# record counter
record_count = 0

# skip record name, seq, quality name
next(fh1)
next(fh1)
next(fh1)

print "\nCalculating Avg quality per base..."
for line in fh1:
    count = count + 1
    if count % 4 == 1:
        record_count += 1
        # update progress bar
        progress(count, file_length, suffix='Percent done')
        for i in range(101):
            # convert ASCII to ints offset by 33
            qual_score = convert_phred(line[i])

            # add up qual scores at base number
            qual_list[1][i] = qual_list[1][i] + float(qual_score)

    else:
        continue
fh1.close

# calculating avg stats for each base
for i in range(101):
    qual_list[2][i] = float(qual_list[1][i]) / float(record_count)

print qual_list
print count

###############################################################################
# Part 2
# open file
fh2 = open(in_file, 'r')

# skip record name, seq, quality name
next(fh2)
next(fh2)
next(fh2)
count2 = 0

print "\nCalculating variance and standard dev per base..."
for line in fh2:
    count2 = count2 + 1
    if count2 % 4 == 1:
        # update progress bar
        progress(count2, file_length, suffix='Percent done')
        for i in range(101):
            # convert ASCII to ints offset by 33
            variance_score = abs(convert_phred(line[i]) - qual_list[2][i])
            # add up qual scores at base number
            var_std_dev_list[1][i] = var_std_dev_list[1][i] + float(variance_score ** 2)

    else:
        continue
fh2.close

for i in range(101):
    # Calc variance
    var_std_dev_list[2][i] = float(var_std_dev_list[1][i]) / float(record_count)
    # Calc standard dev
    var_std_dev_list[3][i] = float(np.sqrt(var_std_dev_list[2][i]))
print var_std_dev_list


###############################################################################
# Part 3

median_list = []

for i in range(101):
    median_list.append([])

# open file
fh3 = open(in_file, 'r')

# skip record name, seq, quality name
next(fh3)
next(fh3)
next(fh3)
count3 = 0
print "\nCalculating median quality per base..."
for line in fh3:
    count3 = count3 + 1
    if count3 % 4 == 1:
        # update progress bar
        progress(count3, file_length, suffix='Percent done')
        for i in range(101):
            median_list[i].append(convert_phred(line[i]))
    else:
        continue
fh3.close

for i in range(101):
    median_list_output[1][i] = np.median(median_list[i])
#print median_list[1]
print median_list_output


###############################################################################
# Plot data
plt.errorbar(qual_list[0], qual_list[2], yerr=var_std_dev_list[3], fmt='o')

# Add labels
plt.xlabel('Base #')
plt.ylabel('Quality Score (phred)')
plt.title('Avg Quality per Base')
plt.grid(True)

print "Saving Plot of: avg_qual_per_base.png"
# Save first graph
plt.savefig('avg_qual_per_base.png')


# Plot data
for i in [5, 95]:
    xlist = range(43)
    plot.hist(xlist, median_list[i])

    # Add labels
    plt.xlabel('Quality Score (phred)')
    plt.ylabel('Quality Score Freq')
    plt.title('Distribution of Quality scores at %s Base') % (i)
    plt.grid(True)

    print "Saving Plot of: dis_of_qual_at_base%s.png" % (i)
    # Save first graph
    plt.savefig("dis_of_qual_at_base%s.png") % (i)
###############################################################################
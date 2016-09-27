#!/usr/bin/python
import sys

# Grobelny HW 4

# progress bar is not my own work from:
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

print "constructing arrays\n"
# make 2d array
qual_list = []
qual_list.append([])  # [0] = base number
qual_list.append([])  # [1] = total quality score
qual_list.append([])  # [2] = avg quality score

# make 2nd 2d array
var_std_dev_list = []
var_std_dev_list.append([])  # [0] = base number
var_std_dev_list.append([])  # [1] = variance
var_std_dev_list.append([])  # [2] = standard dev

# make 3rd 2d array
median_list = []
median_list.append([])  # [0] = base number
median_list.append([])  # [1] = median val dictionary
median_list.append([])  # [2] = median val

for i in range(101):
    # add base numbers to each array
    qual_list[0].append(i)
    var_std_dev_list[0].append(i)
    median_list[0].append(i)
    # intialize array values
    qual_list[1].append(0.0)
    qual_list[2].append(0.0)
    var_std_dev_list[1].append(0.0)
    var_std_dev_list[2].append(0.0)
    median_list[1].append({})
    median_list[2].append(0)

print qual_list

# open file
in_file = "/home/a-m/ib501_stud12/shell/lane1_NoIndex_L001_R1_003.fastq"
fh2 = open(in_file, 'r')

# line counter
count = 0

# record counter
record_count = 0

# skip record name, seq, quality name
next(fh2)
next(fh2)
next(fh2)

print "\nCalculating Avg quality per base..."
for line in fh2:
    count = count + 1
    if count % 4 == 1:
        record_count += 1
        # update progress bar
        progress(count, 4000000 * 4, suffix='Percent done')
        for i in range(101):
            # convert ASCII to ints offset by 33
            qual_score = ord(str(line[i])) - 33

            # add up qual scores at base number
            qual_list[1][i] = qual_list[1][i] + float(qual_score)

    else:
        continue
fh2.close
print qual_list
print record_count

# calculating avg stats for each base
for i in range(101):
    qual_list[2][i] = float(qual_list[1][i]) / float(record_count)

print qual_list

###############################################################################
# open file
in_file = "/home/a-m/ib501_stud12/shell/lane1_NoIndex_L001_R1_003.fastq"
fh2 = open(in_file, 'r')

# skip record name, seq, quality name
next(fh2)
next(fh2)
next(fh2)

print "\nCalculating variance and standard dev per base..."
for line in fh2:
    count = count + 1
    if count % 4 == 1:
        # update progress bar
        progress(count, 4000000 * 4, suffix='Percent done')
        for i in range(101):
            # convert ASCII to ints offset by 33
            variance_score = (abs((ord(str(line[i])) - 33) - qual_list[2][i])) ** 2

            # add up qual scores at base number
            var_std_dev_list[1][i] = var_std_dev_list[1][i] + float(variance_score)

    else:
        continue
fh2.close

for i in range(101):
    # Calc variance
    var_std_dev_list[2][i] = float(var_std_dev_list[1][i]) / float(record_count)
    # Calc standard dev
    var_std_dev_list[3][i] = float(sqrt(var_std_dev_list[2][i]))
print var_std_dev_list


###############################################################################
# import matplotlib.pyplot as plt
#
# # Plot data
# plt.plot(qual_list[0], qual_list[2])
#
# # Add labels
# plt.xlabel('Base #')
# plt.ylabel('Quality Score (phred)')
# plt.title('Avg Quality per Base')
# plt.grid(True)
#
# print "Saving Plot of: avg_qual_per_base.png"
# # Save first graph
# plt.savefig('avg_qual_per_base.png')
###############################################################################

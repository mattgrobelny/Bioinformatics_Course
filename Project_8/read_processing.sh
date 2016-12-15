#!/bin/bash -x

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=12,mem=20GB
#PBS -N stacks_script
# ----------------Load Modules-------------------- #

module load stacks
module load bwa

# ------------------------------------------------ #

  # process_radtags [-f in_file | -p in_dir [-P] [-I] | -1 pair_1 -2 pair_2] -b barcode_file -o out_dir -e enz [-c] [-q] [-r] [-t len] [-D] [-w size] [-s lim] [-h]
  # f: path to the input file if processing single-end sequences.
  # i: input file type, either 'bustard' for the Illumina BUSTARD format, 'bam', 'fastq' (default), or 'gzfastq' for gzipped FASTQ.
  # y: output type, either 'fastq', 'gzfastq', 'fasta', or 'gzfasta' (default is to match the input file type).
  # p: path to a directory of files.
  # P: files contained within directory specified by '-p' are paired.
  # I: specify that the paired-end reads are interleaved in single files.
  # 1: first input file in a set of paired-end sequences.
  # 2: second input file in a set of paired-end sequences.
  # o: path to output the processed files.
  # b: path to a file containing barcodes for this run.
  # c: clean data, remove any read with an uncalled base.
  # q: discard reads with low quality scores.
  # r: rescue barcodes and RAD-Tags.
  # t: truncate final read length to this value.
  # E: specify how quality scores are encoded, 'phred33' (Illumina 1.8+, Sanger, default) or 'phred64' (Illumina 1.3 - 1.5).
  # D: capture discarded reads to a file.
  # w: set the size of the sliding window as a fraction of the read length, between 0 and 1 (default 0.15).
  # s: set the score limit. If the average score within the sliding window drops below this value, the read is discarded (default 10).
  # h: display this help messsage.

file_dir="/home/a-m/ib501_stud12/shell/stacks/clean/lane1/"
barcodes="/home/a-m/ib501_stud12/shell/stacks/lane1_barcodes"
output="/home/a-m/ib501_stud12/shell/stacks/clean/samples/"
#process_radtags -p $file_dir -b $barcodes -o $output -e 'sbfI' -i 'gzfastq' -c -q -r
# done with process RAD-Tags

#Based on the barcode file, how many samples were multiplexed together in this RAD library?
# How many raw reads were there?
# 16000000

# How many were retained?
# 12926707

# Of those discarded, what were the reasons?
# The discarded barcodes fell into these three categories.
# 1 Ambiguous Barcodes - 920001
# 2 Low Quality - 1472833
# 3 Ambiguous RAD-Tag - 680459

# file_name_list=$(ls -1 /home/a-m/ib501_stud12/shell/stacks/clean/samples)
# num_start=1
# indivdual="indv_"
# fq=".fq"
# for file_name in $file_name_list:
# do
#   #padded
#   num_stat=$(printf "%02d"$num_start)
#   mv $output$file_name $output$indivdual$num_start$fq
#   let 'num_start++'
# done

###############################################################################
bwa index -p sb -a bwtsw SB_ref.fasta

# bwa mem [-aCHMpP] [-t nThreads] [-k minSeedLen] [-w bandWidth] [-d zDropoff]
# [-r seedSplitRatio] [-c maxOcc] [-A matchScore] [-B mmPenalty] [-O gapOpenPen]
# [-E gapExtPen] [-L clipPen] [-U unpairPen] [-R RGline] [-v verboseLevel]
# db.prefix reads.fq [mates.fq]

bwa mem -t 12 sb sb_reads.fa

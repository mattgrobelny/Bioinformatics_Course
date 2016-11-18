#!/bin/bash -x

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=15,mem=20GB
#PBS -N stacks_script
# ----------------Load Modules-------------------- #

module load stacks
module load bwa
module load samtools

files='s13_an_01.fa.gz
s13_an_02.fa.gz
s13_an_03.fa.gz
s13_an_04.fa.gz
s13_an_05.fa.gz
s13_an_06.fa.gz
s13_an_07.fa.gz
s13_an_08.fa.gz
s13_fw_01.fa.gz
s13_fw_02.fa.gz
s13_fw_03.fa.gz
s13_fw_04.fa.gz
s13_fw_05.fa.gz
s13_fw_06.fa.gz
s13_fw_07.fa.gz
s13_fw_08.fa.gz'

working_dir="/home/a-m/ib501_stud12/shell/stacks/clean/scan/samples/"
output_dir="/home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/"
output_file_tag=".aln_out.sam"
# Usage: bwa mem [options] <idxbase> <in1.fq> [in2.fq]
#
# Algorithm options:
#
#        -t INT     number of threads [1]
#        -k INT     minimum seed length [19]
#        -w INT     band width for banded alignment [100]
#        -d INT     off-diagonal X-dropoff [100]
#        -r FLOAT   look for internal seeds inside a seed longer than {-k} * FLOAT [1.5]
#        -c INT     skip seeds with more than INT occurrences [10000]
#        -S         skip mate rescue
#        -P         skip pairing; mate rescue performed unless -S also in use
#        -A INT     score for a sequence match [1]
#        -B INT     penalty for a mismatch [4]
#        -O INT     gap open penalty [6]
#        -E INT     gap extension penalty; a gap of size k cost {-O} + {-E}*k [1]
#        -L INT     penalty for clipping [5]
#        -U INT     penalty for an unpaired read pair [17]
#
# Input/output options:
#
#        -p         first query file consists of interleaved paired-end sequences
#        -R STR     read group header line such as '@RG\tID:foo\tSM:bar' [null]
#
#        -v INT     verbose level: 1=error, 2=warning, 3=message, 4+=debugging [3]
#        -T INT     minimum score to output [30]
#        -a         output all alignments for SE or unpaired PE
#        -C         append FASTA/FASTQ comment to SAM output
#        -M         mark shorter split hits as secondary (for Picard/GATK compatibility)
#

# for reads_file in $files
# do
#   file_w_dir=$working_dir$reads_file
#   fileout_w_dir=$output_dir$reads_file$output_file_tag
#   bwa mem -t 15 /home/a-m/ib501_stud12/shell/stacks/clean/scan/samples/bwa/sb $file_w_dir > $fileout_w_dir
# done

# sam_files="s13_an_01.fa.gz.aln_out.sam
# s13_an_02.fa.gz.aln_out.sam
# s13_an_03.fa.gz.aln_out.sam
# s13_an_04.fa.gz.aln_out.sam
# s13_an_05.fa.gz.aln_out.sam
# s13_an_06.fa.gz.aln_out.sam
# s13_an_07.fa.gz.aln_out.sam
# s13_an_08.fa.gz.aln_out.sam
# s13_fw_01.fa.gz.aln_out.sam
# s13_fw_02.fa.gz.aln_out.sam
# s13_fw_03.fa.gz.aln_out.sam
# s13_fw_04.fa.gz.aln_out.sam
# s13_fw_05.fa.gz.aln_out.sam
# s13_fw_06.fa.gz.aln_out.sam
# s13_fw_07.fa.gz.aln_out.sam
# s13_fw_08.fa.gz.aln_out.sam"

# Convert sam to bam
# **** samtools not working?****

# bam_file=".bam"
# for sam_file in $sam_files
# do
#   file_name=$(echo $sam_file | sed -E 's/(s13_[a|f][n|w]_[0-9]+).fa.gz.aln_out.sam/\1/')
#   #samtools view -b -S $sam_file > $output_dir$file_name$bam_file
# done

# Remove all sam files
# rm $sam_files

# Run stacks pipeline
stacks_output_dir="/home/a-m/ib501_stud12/shell/stacks/clean/scan/stacks"

# ref_map.pl -b 1 -S -T 15 \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_01.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_02.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_03.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_04.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_05.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_06.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_07.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_an_08.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_01.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_02.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_03.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_04.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_05.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_06.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_07.sam \
# -s /home/a-m/ib501_stud12/shell/stacks/clean/scan/aligned/s13_fw_08.sam \
# -o $stacks_output_dir

#####
# Running populations

popmap_out_dir="/home/a-m/ib501_stud12/shell/stacks/clean/scan/popmap/"
popmap_file="popmap_samples.tsv"
populations -P $stacks_output_dir -b 1 -O $popmap_out_dir  -M $popmap_out_dir$popmap_file -t 15 \
--fstats --kernel_smoothed -p 1 -r 0.7

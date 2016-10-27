#!/bin/bash

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=8,mem=10000mb
# ----------------Load Modules-------------------- #
module load python/2.7.9
# ----------------Your Commands------------------- #


################################################################################
# function to pass in assembly file and return stats
get_stats(contigs_file_dir, kmer_size)
{
python velvethg_qc.py -k kmer_size -s 1 -f contigs_file_dir
}


################################################################################

# collect list of assembly directories
file_list=$(ls -1)

stats_out="_velvetg_qc_stats.txt"
slash="/"
current_dir=$(pwd)
for file in file_list
do
  working_dir=$current_dir$file

  kmer_size=$(echo file| grep -Eo "[0-9]+"| head -n 1)
  get_stats($working_dir, $kmer_size) > $working_dir$slash$file$stats_out
done

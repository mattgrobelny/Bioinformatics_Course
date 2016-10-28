#!/bin/bash -x

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=8,mem=10000mb
# ----------------Load Modules-------------------- #
module load python/2.7.9
# ----------------Your Commands------------------- #

# collect list of assembly directories
file_list="velvetout_kmer_31
velvetout_kmer_31_opts_min_contig_len_500
velvetout_kmer_41
velvetout_kmer_41_opts_min_contig_len_500
velvetout_kmer_49
velvetout_kmer_49_opts_4
velvetout_kmer_49_opts_4min_contig_len_500
velvetout_kmer_49_opts_8
velvetout_kmer_49_opts_8min_contig_len_500
velvetout_kmer_49_opts_auto
velvetout_kmer_49_opts_automin_contig_len_500
velvetout_kmer_49_opts_min_contig_len_500"

stats_out="_velvetg_qc_stats.txt"
slash="/"
contig_file="contigs.fa"
current_dir="/home/a-m/ib501_stud12/shell/Grobelny_hw6_output"
velvethg_qc="velvethg_qc.py"

master_log_file_data="master_Log.txt"
assembly_log_file="Log"
echo "#----- Start of Velvet Log files ----# " > $current_dir$slash$master_log_file_data
echo " " >> $current_dir$slash$master_log_file_data

for file in $file_list
do
  working_dir=$current_dir$slash$file

  kmer_size=$(echo $file| grep -Eo "[0-9]+"| head -n 1)
  python $current_dir$slash$velvethg_qc -k $kmer_size -s -n $working_dir$slash$file -f $working_dir$slash$contig_file > $working_dir$slash$file$stats_out

  #collect last line of log file from each assembly
  echo $file >> $current_dir$slash$master_log_file_data
  tail -n 1 $working_dir$slash$assembly_log_file >> $current_dir$slash$master_log_file_data
  echo "" >> $current_dir$slash$master_log_file_data
done

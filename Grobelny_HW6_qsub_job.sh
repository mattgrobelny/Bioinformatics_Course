#!/bin/bash

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=8,mem=12000mb
# ----------------Load Modules-------------------- #
module load python/2.7.9
module load velvet/1.2.10
module load python/2.7.9
# ----------------Your Commands------------------- #

files="/home/classroom/ib501/assembly/samples/rs_female_1983.13.1.fil.fq.gz
/home/classroom/ib501/assembly/samples/rs_female_1983.13.2.fil.fq.gz"

kmers="31
41
49"

kmer_49_options="4x
8x
auto"

directory="/home/a-m/ib501_stud12/shell/Grobelny_hw6_output"
outfile="/kmer_"
opts="_opts_"
min_contig_len="500"
min_contig_len_string="_Min_contig_len_500"

mkdir $directory
./velveth directory hash_length {[-file_format][-read_type][-separate|-interleaved] filename1 [filename2 ...]} {...} [options]

for kmer in $kmers
do
  if (kmer == "49")
  # compute default assembly for 49
  dir_out_name=$directory$outfile$kmer
  velveth $dir_out_name $kmer $files[0] $files[1]
  velvethg $dir_out_name

  # compute default assembly for 49 w/ min contig length at 500
  dir_out_name=$directory$outfile$kmer$min_contig_len_string
  velveth $dir_out_name $kmer $files[0] $files[1]
  velvethg $dir_out_name -min_contig_lgth $min_contig_len

  do
    for kmer_opt in $kmer_49_options
    do
      # compute default parameters w/ cov cutt off
      dir_out_name=$directory$outfile$kmer$opts$kmer_opt
      velveth $dir_out_name $kmer $files[0] $files[1]
      velvethg $dir_out_name -cov_cutoff $kmer_opt

      # compute default parameters w/ cov cutt off
      dir_out_name=$directory$outfile$kmer$opts$kmer_opt
      velveth $dir_out_name $kmer $files[0] $files[1]
      velvethg $dir_out_name -cov_cutoff $kmer_opt -min_contig_lgth

  else
    velveth
    velvethg

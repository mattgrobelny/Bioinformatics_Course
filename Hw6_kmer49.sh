#!/bin/bash

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=8,mem=12GB
#PBS -N Velvet49_matt
# ----------------Load Modules-------------------- #
#module load python/2.7.9
module load velvet
# ----------------Your Commands------------------- #

file1="/home/classroom/ib501/assembly/samples/rs_female_1983.13.1.fil.fq.gz"
file2="/home/classroom/ib501/assembly/samples/rs_female_1983.13.2.fil.fq.gz"

directory="/home/a-m/ib501_stud12/shell/Grobelny_hw6_output"
outfile="/velvetout_kmer_"
opts="_opts_"
min_contig_len="500"
min_contig_len_string="min_contig_len_500"
#./velveth directory hash_length {[-file_format][-read_type][-separate|-interleaved] filename1 [filename2 ...]} {...} [options]

kmer="49"
options="-shortPaired -fastq.gz"
mkdir $directory
# compute standard parameters output
dir_out_name=$directory$outfile$kmer
mkdir $dir_out_name
velveth $dir_out_name $kmer $options $file1 $file2
velvetg $dir_out_name

# compute standard parameters output w/ min contig len at 500
dir_out_name=$directory$outfile$kmer$opts$min_contig_len_string
mkdir $dir_out_name
velveth $dir_out_name $kmer $options $file1 $file2
velvetg $dir_out_name -min_contig_lgth 500

kmer_49_options="4x
8x
auto"


for kmer_opt in $kmer_49_options
do
  # compute standard parameters output
  dir_out_name=$directory$outfile$kmer$opts$kmer_opt
  mkdir $dir_out_name
  velveth $dir_out_name $kmer $options $file1 $file2
  velvetg $dir_out_name -cov_cutoff $kmer_opt

  # compute standard parameters output w/ min contig len at 500
  dir_out_name=$directory$outfile$kmer$opts$kmer_opt$min_contig_len_string
  mkdir $dir_out_name
  velveth $dir_out_name $kmer $options $file1 $file2
  velvetg $dir_out_name -cov_cutoff $kmer_opt -min_contig_lgth 500
done

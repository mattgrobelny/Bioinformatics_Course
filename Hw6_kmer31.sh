#!/bin/bash -x

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=8,mem=12GB
#PBS -N Velvet31
#PBS -k oe
# ----------------Load Modules-------------------- #
#module load python/2.7.9
module load velvet
# ----------------Your Commands------------------- #

file1="/home/classroom/ib501/assembly/samples/rs_female_1983.13.1.fil.fq.gz"
file2="/home/classroom/ib501/assembly/samples/rs_female_1983.13.2.fil.fq.gz"

directory="/home/a-m/ib501_stud12/shell/Grobelny_hw6_output"
outfile="/velvetout_kmer_"
opts="_opts_"
min_contig_len_string="min_contig_len_500"

kmer="31"
cov="58"
((ck=$cov*(100-$kmer+1)/100))

options="-shortPaired -fastq.gz"
mkdir $directory

# compute assembly standard parameters output
dir_out_name=$directory$outfile$kmer
mkdir $dir_out_name
velveth $dir_out_name $kmer $options $file1 $file2
velvetg $dir_out_name -ins_length 500 -exp_cov $ck

# compute assembly standard parameters output w/ min contig len at 500
dir_out_name=$directory$outfile$kmer$opts$min_contig_len_string
mkdir $dir_out_name
velveth $dir_out_name $kmer $options $file1 $file2
velvetg $dir_out_name -min_contig_lgth 500 -ins_length 500 -exp_cov $ck

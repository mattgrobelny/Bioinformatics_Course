#!/bin/bash

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=8,mem=12000mb
# ----------------Load Modules-------------------- #
module load python/2.7.9
module load velvet/1.2.10
# ----------------Your Commands------------------- #

files="/home/classroom/ib501/assembly/samples/rs_female_1983.13.1.fil.fq.gz
/home/classroom/ib501/assembly/samples/rs_female_1983.13.2.fil.fq.gz"

kmers="31
41
49"

kmer_49_options="4x
8x
auto"

for kmer in $kmers
do
  if (kmer == "49")
  do
    for kmer_opt in kmer_49_options
    do

      velveth
      velvethg
  else
    velveth
    velvethg

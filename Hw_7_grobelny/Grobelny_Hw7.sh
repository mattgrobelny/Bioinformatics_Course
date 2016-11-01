#!/bin/bash -x

# ----------------QSUB Parameters----------------- #
#PBS -S /bin/bash
#PBS -q classroom
#PBS -l nodes=1:ppn=8,mem=10GB
#PBS -N gmap_script
# ----------------Load Modules-------------------- #

module load gmap/2016-09-23

# ----------------Your Commands------------------- #


# wget http://ftp.ensembl.org/pub/release-76/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna.toplevel.fa.gz

# wget http://ftp.ensembl.org/pub/current_gtf/mus_musculus/Mus_musculus.GRCm38.86.gtf.gz


directory="/home/a-m/ib501_stud12/shell/Hw7/mmu/"
genome="/home/a-m/ib501_stud12/shell/Hw7/mmu/Mus_musculus.GRCm38.dna.toplevel.fa"
database_dir="/home/a-m/ib501_stud12/shell/Hw7/mmu/Mus_musculus.GRCmgsnap38"

gmap_build -D $directory -d Mus_musculus.GRCm38 $genome

# prep gtf file
cat Mus_musculus.GRCm38.86.gtf | gtf_splicesites > Mus_musculus.GRCm38.splicesites

cat Mus_musculus.GRCm38.splicesites | iit_store -o Mus_musculus.GRCm38.splicesites

mv Mus_musculus.GRCm38.splicesites.iit Mus_musculus.GRCm38/Mus_musculus.GRCm38.maps/.

# alaign reads to reference
reads="/home/classroom/ib501/alignment/mmu_700_tumor_cells.fq.gz"
splicesites="Mus_musculus.GRCm38.splicesites.iit"
output="/home/a-m/ib501_stud12/shell/Hw7/mmu/Mus_musculus.GRCm38.out"
gsnapl -D $directory -d Mus_musculus.GRCm38 -t 8 -o $output -A sam --gunzip -s $splicesites $reads

# load samtools
module load samtools/1.3.1

# process with sam tools

# 1. covert from sam to bam
samtools view -Sb Mus_musculus.GRCm38.out > Mus_musculus.GRCm38.out.bam

# 2. sort
samtools sort Mus_musculus.GRCm38.out.bam > Mus_musculus.GRCm38.out.sort.bam

# 3. extract all reads from chrom 1 into new sam file
# index
samtools index Mus_musculus.GRCm38.out.sort.bam

# get names of chromosomes
$ samtools idxstats Mus_musculus.GRCm38.out.sort.bam

# collect chrom 1 (1) aligned reads
samtools view -h Mus_musculus.GRCm38.out.sort.bam 1 > Mus_musculus.GRCm38.out.sort.chr1_a.sam

# collect stats from alaignment
samtools stats Mus_musculus.GRCm38.out.sort.bam | grep ^SN | cut -f 2-

############################################
# Answers to questions:

# How many raw reads?
# raw total sequences:	2139475

# How many alaigned reads?
# reads mapped:	2020536

# How many reads alaigned to chr 1?
# 170446

#### Whole alignment stats
# raw total sequences:	2139475
# filtered sequences:	0
# sequences:	2139475
# is sorted:	1
# 1st fragments:	2139475
# last fragments:	0
# reads mapped:	2020536
# reads mapped and paired:	0	# paired-end technology bit set + both mates mapped
# reads unmapped:	118939
# reads properly paired:	0	# proper-pair bit set
# reads paired:	0	# paired-end technology bit set
# reads duplicated:	0	# PCR or optical duplicate bit set
# reads MQ0:	23008	# mapped and MQ=0
# reads QC failed:	0
# non-primary alignments:	1767285
# total length:	156102591	# ignores clipping
# bases mapped:	150375676	# ignores clipping
# bases mapped (cigar):	145969307	# more accurate
# bases trimmed:	0
# bases duplicated:	0
# mismatches:	1270586	# from NM fields
# error rate:	8.704473e-03	# mismatches / bases mapped (cigar)
# average length:	72
# maximum length:	95
# average quality:	33.1
# insert size average:	0.0
# insert size standard deviation:	0.0
# inward oriented pairs:	0
# outward oriented pairs:	0
# pairs with other orientation:	0
# pairs on different chromosomes:	0


### Chr1 alaigment stats

samtools stats Mus_musculus.GRCm38.out.sort.chr1_a.sam | grep ^SN | cut -f 2-
# raw total sequences:	170446
# filtered sequences:	0
# sequences:	170446
# is sorted:	1
# 1st fragments:	170446
# last fragments:	0
# reads mapped:	170446
# reads mapped and paired:	0	# paired-end technology bit set + both mates mapped
# reads unmapped:	0
# reads properly paired:	0	# proper-pair bit set
# reads paired:	0	# paired-end technology bit set
# reads duplicated:	0	# PCR or optical duplicate bit set
# reads MQ0:	18673	# mapped and MQ=0
# reads QC failed:	0
# non-primary alignments:	621933
# total length:	12560667	# ignores clipping
# bases mapped:	12560667	# ignores clipping
# bases mapped (cigar):	12226590	# more accurate
# bases trimmed:	0
# bases duplicated:	0
# mismatches:	102951	# from NM fields
# error rate:	8.420254e-03	# mismatches / bases mapped (cigar)
# average length:	73
# maximum length:	95
# average quality:	33.3
# insert size average:	0.0
# insert size standard deviation:	0.0
# inward oriented pairs:	0
# outward oriented pairs:	0
# pairs with other orientation:	0
# pairs on different chromosomes:	0

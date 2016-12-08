#HW 9 - SQL
# accessing the db
mysql -u s12 -p

# pass: jazzduck

# # create  a gene id, seq and translation seq tsv
# mysql -u s12 -p -e "USE gene_db; SELECT gene.gene_id ,trans_id, sequence, translation
# INTO OUTFILE '/home/grobeln2/geneid_transcript_prot2.tsv' FIELDS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '""' LINES TERMINATED BY '\n'
# FROM gene,transcript limit 10;"
#
# FIELDS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n';
# #####
# # Convert tsv of geneid trans and prot seq to fasta
#
# #!/bin/bash
# #rm gene_db_trans_seq.fasta
# #rm gene_db_prot_seq.fasta
#
# # collect gene id and transc and transl seq into lists
# gene_id=$(cat geneid_transcript_prot2.tsv | cut -f 1)
# trans_id=$(cat geneid_transcript_prot2.tsv | cut -f 2)
# transcript_seq_list=$(cat geneid_transcript_prot2.tsv | cut -f 3)
# translation_seq_list=$(cat geneid_transcript_prot2.tsv | cut -f 4)
# line_count=$(wc -l geneid_transcript_prot2.tsv)
# # change lists into arrays
# gene_id_array=($gene_id)
# trans_id_array=($trans_id)
# transcript_seq=($transcript_seq_list)
# translation_seq=($translation_seq_list)
#
# greater=">"
# underscr="_"
#
# # loop over each array and interweave geneid with seqs for each prot and trans seq
# for counter in {1..48829}
# do
# 	gene_id_it=${gene_id_array[$counter]}
# 	trans_id_it=${trans_id_array[$counter]}
# 	transc_seq_it=${transcript_seq[$counter]}
# 	transl_seq_it=${translation_seq[$counter]}
# 	printf "$greater$gene_id_it$underscr$trans_id_it\n" >> gene_db_trans_seq.fasta
# 	printf "$transc_seq_it\n" >> gene_db_trans_seq.fasta
#
# 	printf "$greater$gene_id_it$underscr$trans_id_it\n" >> gene_db_prot_seq.fasta
#   printf "$transl_seq_it\n" >> gene_db_prot_seq.fasta
# done

# make blast db
makeblastdb -in hsa.fa -parse_seqids -dbtype prot

# run blastp of database genes agains the human gene protein seqeunces
blastx -query trans.fasta -db hsa.fa -outfmt 6 -out gene_db_prot_vs_hsa_blast_out2.tsv


# create a table to hold the blastout
USE s12;
CREATE TABLE Blast_output
(
qseqid VARCHAR(225),
sseqid VARCHAR(225),
pident FLOAT,
length INT,
mismatch INT,
gapopen INT,
qstart INT,
qend INT,
sstart INT,
send  INT,
evalue FLOAT,
bitscore FLOAT,
blast_out_id int NOT NULL AUTO_INCREMENT,
PRIMARY KEY (blast_out_id)
);

# Import blast output file into s12 db
LOAD DATA LOCAL INFILE '/home/grobeln2/gene_db_prot_vs_hsa_blast_out2.tsv'
INTO TABLE Blast_output
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';

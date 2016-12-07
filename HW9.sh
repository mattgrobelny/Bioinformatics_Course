#HW 9 - SQL
# accessing the db
mysql -u s12 -p

# pass: jazzduck

# create  a gene id, seq and translation seq tsv
USE gene_db;
SELECT gene_id , sequence, translation
FROM transcript INTO OUTFILE ‘/home/shell/geneid_transcript_prot.tsv’ ;
FIELDS TERMINATED BY '\t' ;
OPTIONALLY ENCLOSED BY '"' ;
LINES TERMINATED BY '\n';

#####
# Convert tsv of geneid trans and prot seq to fasta

#!/bin/bash
#rm gene_db_trans_seq.fasta
#rm gene_db_prot_seq.fasta

# collect gene id and transc and transl seq into lists
gene_id=$(cat geneid_transcript_prot.tsv | cut -f 1)
transcript_seq_list=$(cat geneid_transcript_prot.tsv | cut -f 2)
translation_seq_list=$(cat geneid_transcript_prot.tsv | cut -f 3)

# change lists into arrays
gene_id_array=($gene_id)
transcript_seq=($transcript_seq_list)
translation_seq=($translation_seq_list)

greater=">"

# loop over each array and interweave geneid with seqs for each prot and trans seq
for counter in {1..48829}
do
	gene_id_ti=${gene_id_array[$counter]}
	transc_seq_it=${transcript_seq[$counter]}
	transl_seq_it=${translation_seq[$counter]}

	printf "$greater$gene_id_ti\n" >> gene_db_trans_seq.fasta
	printf "$transc_seq_it\n" >> gene_db_trans_seq.fasta

	printf "$greater$gene_id_ti\n" >> gene_db_prot_seq.fasta
        printf "$transl_seq_it\n" >> gene_db_prot_seq.fasta
done

# make blast db
makeblastdb -in hsa.fa -parse_seqids -dbtype prot

# run blastp of database genes agains the human gene protein seqeunces
blastp -query gene_db_prot_seq.fasta -db hsa.fa -outfmt 6 -out gene_db_prot_vs_hsa_blast_out.tsv


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
LOAD DATA LOCAL INFILE '/home/grobeln2/gene_db_prot_vs_hsa_blast_out.tsv'
INTO TABLE Blast_output
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';

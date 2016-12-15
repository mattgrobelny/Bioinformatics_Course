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
                              

#!/usr/bin/python
import mysql.connector

### Start up connection

dbh_gene_db = mysql.connector.connect(user='s12', password='jazzduck', database='gene_db')
cursor_gene_db = dbh_gene_db.cursor()

# select all gene + transcripts from trancript table
query = ("SELECT gene.gene_id ,trans_id, sequence, translation FROM gene, transcript WHERE gene.id=transcript.gene_id;")
cursor_gene_db.execute(query)

trans_out = "/home/grobeln2/trans.fasta"
prot_out = "/home/grobeln2/prot.fasta"
fh_trn = open(trans_out, 'w')
fh_prt = open(prot_out, 'w')

for line in cursor_gene_db:
    # generate seq name
    seq_name = ">" + line[0] + "_" + line[1]

    # write to file
    fh_trn.write("%s\n%s\n" % (seq_name, line[2]))
    fh_prt.write("%s\n%s\n" % (seq_name, line[3]))

# close files
fh_trn.close
fh_prot_out.close

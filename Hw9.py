#!/usr/bin/python
import mysql.connector

### Start up connections to both DBs

dbh_s12 = mysql.connector.connect(user='s12', password='jazzduck', database='s12')
cursor_s12 = dbh_s12.cursor()

dbh_gene_db = mysql.connector.connect(user='s12', password='jazzduck', database='gene_db')
cursor_gene_db = dbh_gene_db.cursor()

# Set up queries for both DBs

###############################################################################
# Queries for DB S12

# Collect Unique blast hitting genes
blast_hitting_genes_query = ("SELECT DISTINCT qseqid FROM Blast_output")

query_blast_out = ("SELECT sseqid, evalue FROM Blast_output WHERE qseqid=%s AND MIN(evalue)")

cursor_s12.execute(blast_hitting_genes_query)

# capture list of hitting genes
hits_gene_list = []
for value in cursor_s12:
    split_val = value[0].split("_")
    hits_gene_list.append(split_val)

###############################################################################
# Queries for DB gene_db

# Pull out transcript seq for specfic blast outputBlast_out
transcript_seq_blast_hit = ("SELECT sequence FROM transcript WHERE gene_id=%s")


###############################################################################
# ----- Blast Output ----- #

print "Gene id", '\t', "Trans_id", '\t' "Blast hit", '\t', "E-value"'\t', "Transcript"
for gene_id in hits_gene_list[0:20]:

    # Query lowest evalue blast hit
    cursor_s12.execute(query_blast_out, (gene_id[0],))
    blast_hit = cursor_s12 # two outputs hit seq and eval

    # Query transcript
    cursor_gene_db.execute(transcript_seq_blast_hit, (gene_id[0],))
    transcript_out = cursor_gene_db[0]

    # output in tsv
    print gene_id[0], '\t', gene_id[1], '\t', blast_hit[0], '\t', blast_hit[1], '\t', transcript_out[0]

# Closes out connections
cursor_s12.close()
dbh_s12.close()

cursor_gene_db.close()
dbh_gene_db.close()

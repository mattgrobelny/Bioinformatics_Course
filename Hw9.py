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

query_blast_out = ("SELECT sseqid, evalue FROM gene WHERE qseqid=%s AND MIN(evalue)")

cursor_s12.execute(blast_hitting_genes_query)

# capture list of hitting genes
hits_gene_list = []
for value in cursor_s12:
    hits_gene_list.append(value[0])

###############################################################################
# Queries for DB gene_db

# Convert to actual gene id
id_to_gene_id = ("SELECT gene_id FROM gene WHERE id=%s")

# Pull out transcript seq for specfic blast outputBlast_out
transcript_seq_blast_hit = ("SELECT sequence FROM transcript WHERE gene_id=%s")


###############################################################################
# ----- Blast Output ----- #

print "Gene id", "\t", "Blast hit", "\t", "Transcript"
for gene_id in hits_gene_list[0:20]:

    # Print out actual gene id
    cursor_gene_db.execute(id_to_gene_id, (gene_id,))
    gene_name = cursor_gene_db

    # Query lowest evalue blast hit
    cursor_s12.execute(query_blast_out, (gene_id,))
    blast_hit = cursor_s12

    # Query transcript
    cursor_gene_db.execute(transcript_seq_blast_hit, (gene_id,))
    transcript_out = cursor_gene_db

    # output in tsv
    print gene_name[0], "\t", blast_hit[0], "\t", transcript_out[0]

# Closes out connections
cursor_s12.close()
dbh_s12.close()

cursor_gene_db.close()
dbh_gene_db.close()

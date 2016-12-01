#!/usr/bin/python
import mysql.connector
#
# Connect and get a database handle.
#

### Start up connections to both DBs

dbh_s12 = mysql.connector.connect(user='s12', password='jazzduck', database='s12')
cursor_s12 = dbh_s12.cursor()
test1=("SELECT * FROM Blast_output LIMIT 10;")
cursor_s12.execute(test1)

dbh_gene_db = mysql.connector.connect(user='s12', password='jazzduck', database='gene_db')
cursor_gene_db = dbh_gene_db.cursor()
test2=("SELECT * FROM gene_db LIMIT 10;")
cursor_gene_db.execute(test2)
# Set up queries for both DBs

###############################################################################
# Queries for DB S12

# Collect Unique blast hitting genes
blast_hitting_genes_query = ("SELECT DISTINCT qseqid FROM Blast_out")

query_blast_out = ("SELECT sseqid, evalue FROM gene WHERE qseqid=%s AND MIN(evalue)")

blast_hitting_genes_query_output = cursor_s12.execute(blast_hitting_genes_query)

###############################################################################
# Queries for DB gene_db

# Covert to actual gene id
gene_id_to_actual_gene_id = ("SELECT gene_id FROM gene WHERE id=%s")

# Pull out transcript seq for specfic blast output
transcript_seq_blast_hit = ("SELECT sequence FROM transcript WHERE gene_id=%s")


###############################################################################

print "# ----- Blast Output ----- #"
for gene_id in blast_hitting_genes_query_output:

    # Print out actual gene id
    print "Gene id:", cursor_gene_db.execute(gene_id_to_actual_gene_id, (gene_id))

    # print out top blast hit
    print  "Blast hit:", cursor_s12.execute(query_blast_out, (gene_id))
    print "Transcript:", cursor_gene_db.execute(transcript_seq_blast_hit, (gene_id))

# Closes out connections
cursor_s12.close()
dbh_s12.close()

cursor_gene_db.close()
dbh_gene_db.close()

import mysql.connector
#
# Connect and get a database handle.
#
dbh    = mysql.connector.connect(user='s12', password='jazzduck',database='gene_db')
cursor = dbh.cursor()
#
# Form the query with placeholders for variables.
#
query  = ("SELECT gene_id, chromosome, start_base " \
"FROM gene "\
"WHERE chromosome=%s AND start_base>%s")
#
# Execute the query.
#
cursor.execute(query, ("17", 10000000))
for (gene_id, chr, bp) in cursor:
    print "Gene ID:", gene_id, "; Chromosome:", chr, "; start bp:", bp
cursor.close()
dbh.close()

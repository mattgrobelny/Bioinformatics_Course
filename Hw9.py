#!/usr/bin/python
import mysql.connector
#
# Connect and get a database handle.
#

### Start up connections to both DBs
dbh_s12 = mysql.connector.connect(user='s12', password='jazzduck', database='s12')
cursor_s12 = dbh_s12.cursor()

dbh_gene_db = mysql.connector.connect(user='s12', password='jazzduck', database='gene_db')
cursor_gene_db= dbh_gene_db.cursor()

# Set up queries for both DBs

### Queries for DB S12

# Collect Unique blast hitting genes
blast_hitting_genes_query = ("SELECT DISTINCT qseqid FROM s12.Blast_out;")

query_blast_out = ("SELECT qseqid, sseqid, evalue"
"FROM gene "
"WHERE qseqid=%s and MIN(evalue)")

blast_hitting_genes_query_output = cursor.execute(blast_hitting_genes_query)


for gene_id in blast_hitting_genes_query_output:
    cursor.execute(query_blast_out, (gene_id))


cursor_s12.close()
dbh_s12.close()


# Execute the query.
#
# qseqid | sseqid | pident | length | mismatch | gapopen | qstart | qend | sstart | send | evalue | bitscore | blast_out_id |
cursor.execute(query, ("17", 10000000))
for (gene_id, chr, bp) in cursor:
    print "Gene ID:", gene_id, "; Chromosome:", chr, "; start bp:", bp
cursor.close()
dbh.close()

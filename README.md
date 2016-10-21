# Bioinformatics_Course
Backup of lecture notes, hws, scripts

## Best Scripts:
- kspec.py  
- knorm.py
- velvethg_qc.py  
- ...  

----
### K-mer frequency graphing script
`kspec.py -k <kmer_size> -x <x_axis_max> -f <inputfile>  
`   

Goals:  
1) Take in fastq file and kmerize it and output kmer occurence frequnecy  
2) Output graph of kmer occurence frequnecy  
3) Output kmer occurence frequnecy to .tsv file

Output:  
1) Graphs of kmer frequency vs number of Occurences
2) Kmer occurence vs frequency output to file  

----
### Read Normalization Script

`knorm.py -k <kmer_size>[15] -c <coverage>[10] -f <inputfile>
`  

Goals:  
1) Input fastq reads  
2) K-merize and filter out reads based on desired coverage  
3) Save reads with coverage less than or equal to coverage threshold in new file  

Output:  
`FILENAME_k_KMER#_cov_COVERAGE#_norm.fastq` 

---  

### Velvetg Output QC

`velvethg_qc.py -h <help> -k <kmerlength> -s <stat_print_yes> -n <output_name> -f <inputfile> \n
`  

Goals:   
1) Gather kmer contig length and coverage from fasta headers  
2) Output stats based on contig length and coverage  
3) Output histogram of contig lengths  

# Hw 6 Questions
## Mateusz Grobelny

### 1.
Looking at major parameters, going from a kmer size of 31 to 49 increased the
N50 increased  however the total length of the assembly decreased getting closer to the
32mb size of chrom 4.

The additional of the min contig length of 500, parameter had no effect on the N50
or total size of the assembly.

The coverage cutoff parameter had a large impact on the assembly for kmer 49, increasing
the N50 of the assembly and setting the cutoff to auto resulted in the largest N50
of 

---
#----- Start of Velvet Log files ----#

velvetout_kmer_31
Final graph has 399713 nodes and n50 of 519, max 9944, total 36283149, using 17649260/18682510 reads

velvetout_kmer_31_opts_min_contig_len_500
Final graph has 399713 nodes and n50 of 519, max 9944, total 36283149, using 11642179/18682510 reads

velvetout_kmer_41
Final graph has 230532 nodes and n50 of 768, max 14134, total 35151953, using 17360263/18682510 reads

velvetout_kmer_41_opts_min_contig_len_500
Final graph has 230532 nodes and n50 of 768, max 14134, total 35151953, using 13316396/18682510 reads

velvetout_kmer_49
Final graph has 135915 nodes and n50 of 1068, max 17743, total 34087243, using 17186493/18682510 reads

velvetout_kmer_49_opts_cutoff_4
Final graph has 88033 nodes and n50 of 1482, max 25665, total 32708924, using 17232834/18682510 reads

velvetout_kmer_49_opts_cutoff_4min_contig_len_500
Final graph has 88033 nodes and n50 of 1482, max 25665, total 32708924, using 14851056/18682510 reads

velvetout_kmer_49_opts_cutoff_8
Final graph has 64905 nodes and n50 of 1777, max 25665, total 30695881, using 17094405/18682510 reads

velvetout_kmer_49_opts_cutoff_8min_contig_len_500
Final graph has 64905 nodes and n50 of 1777, max 25665, total 30695881, using 15024020/18682510 reads

velvetout_kmer_49_opts_cutoff_auto
Final graph has 40681 nodes and n50 of 2143, max 25126, total 28162518, using 16740588/18682510 reads

velvetout_kmer_49_opts_cutoff_automin_contig_len_500
Final graph has 40681 nodes and n50 of 2143, max 25126, total 28162518, using 14985301/18682510 reads

velvetout_kmer_49_opts_min_contig_len_500
Final graph has 135915 nodes and n50 of 1068, max 17743, total 34087243, using 14233561/18682510 reads

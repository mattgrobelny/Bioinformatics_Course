# Problem Set 2  
Matt Grobelny

### Q1.
I already downloaded all of the files from root/unix folder.
So I don't need to run this command.

### Q2.
`$ zcat batch_2.genepop.gz | sed -n '2p' |tr "," "\n"
`
### Q3.

`$ zcat batch_2.genepop.gz | sed -n '2p' |tr "," "\n" | sed -E 's/([0-9]+)_[0-9]+/\1/'
`
### Q4.
`$ zcat batch_2.genepop.gz | sed -n '2p' |tr "," "\n" | sed -E 's/([0-9]+)_[0-9]+/\1/' | sort -n | uniq -d`

### Q5.

mkdir grobelny_hw2
cd grobelny_hw2

script
#500 random loci:  
zcat ../batch_2.genepop.gz | sed -n '2p' |tr "," "\n" | sed -E 's/([0-9]+)_[0-9]+/\1/' | sort -n | uniq -d | shuf -n 500 > 500_loci.tsv
#1000 random loci:  
zcat ../batch_2.genepop.gz | sed -n '2p' |tr "," "\n" | sed -E 's/([0-9]+)_[0-9]+/\1/' | sort -n | uniq -d | shuf -n 1000 > 1000_loci.tsv
#10000 random loci:  
zcat ../batch_2.genepop.gz | sed -n '2p' |tr "," "\n" | sed -E 's/([0-9]+)_[0-9]+/\1/' | sort -n | uniq -d | shuf -n 10000 > 10000_loci.tsv
wc -l *.tsv
head *.tsv
exit
$ a2ps -B -l 120 -R  --print-anyway 1 typescript -o - | ps2pdf - typescript.pdf

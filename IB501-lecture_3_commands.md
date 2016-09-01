# Lecture commands 8.29.16

## RegEx
Example used within grep   

  `grep -E  "^.{5}" my_textfile.txt
`
## sed  
 Stream editor -->search and replace on data flowing through a pipe  
 's/pattern/replace/'  
 (pattern) <-- remember this pattern store as \1 or \2  

  ` sed -E 's/[a-z]+ [a-z]+/foo/'
`  
tab in command line == cntrl + v + tab  or use `/t`

*Additional examples:*
```
grep "consensus" fish_310.tags.tsv | cut -f 3,9 | sed -E 's/([0-9]+)\t([ATCG]+)/\2\t\1/'

grep "consensus" fish_310.tags.tsv | cut -f 3,9 | sed -E 's/([0-9]+)\t([ATCG]+)/\2\t\1/' | sed -E 's/([ATCG]+)\t([0-9]+)/\2\t\1/' | sed -E 's/^/>/' |tr '\t' '\n'
```

## awk
  Programming language --> useful in processing within pipelines  

  `awk '$1>500 {count=count+1} END {print("here is how many I counted more then 500:" count)}'
`  
## uniq
Counts uniq occurs, needs strings sorted before

`uniq -c `

## sort
  Sorts lines -h (human readable) -n numerical etc...  

  `sort -h`

## tr
  Translate characters etc
  `tr "/t" "/s"`

## zcat
  Open zipped text file
  `zcat file.txt.gz`

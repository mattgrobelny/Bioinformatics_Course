#!/bin/bash
# In class 5

cd seqs
rm indiv_1_to_5.fq

ls -1 | while read line ; do wc -l $line; done |awk '{total_lines=total_lines+$1} END {print(total_lines)}'

total_lines=$(ls -1 | while read line ; do wc -l $line; done |awk '{total_lines=total_lines+$1} END {print(total_lines)}')

echo "total lines: $total_lines"

cat *.fq > indiv_1_to_5.fq

wc -l indiv_1_to_5.fq

lines_from_cated_file=$(wc -l indiv_1_to_5.fq | grep -Eo "[0-9]{5}")

if (($lines_from_cated_file = $total_lines ));
then
  echo "Total lines from the 5 files:"
  echo "$total_lines"
  echo "Lines from catted file:"
  echo "$lines_from_cated_file"
  echo "Everything checks out"
fi

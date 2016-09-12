#!/bin/bash
cd fst
rm batch_2.fst_1-2.Chr_only.tsv
rm batch_2.fst_1-3.Chr_only.tsv
rm batch_2.fst_2-3.Chr_only.tsv

cat batch_2.fst_1-2.tsv | grep -vwE "scaffold_[0-9]+" > batch_2.fst_1-2.Chr_only.tsv

cat batch_2.fst_1-3.tsv | grep -vwE "scaffold_[0-9]+" > batch_2.fst_1-3.Chr_only.tsv

cat batch_2.fst_2-3.tsv | grep -vwE "scaffold_[0-9]+" > batch_2.fst_2-3.Chr_only.tsv

# collect list of Chr and store as var
chr_list=$(cut -f 5 "batch_2.fst_2-3.Chr_only.tsv" | sed 1d | sort | uniq |sort)

# make list of files to work with
files_Chr_only="batch_2.fst_1-2.Chr_only.tsv
batch_2.fst_1-3.Chr_only.tsv
batch_2.fst_2-3.Chr_only.tsv"

# make dir for output of all files 
mkdir CA_6_output
cd CA_6_output


for file in $files_Chr_only
do
  echo "working on $file"

  for i in $chr_list
  do
    echo "working on $i group from $file"

    file_name=$(echo "$file" | grep -oE "batch_2.fst_[12]-[23].Chr_only.")
    tsv=".tsv"
    it_file_name="$file_name$i$tsv"

    grep -wE ""$i"" $file > "$it_file_name"
  done
done

cd ..

cd ..

#Tests
echo "Testing how many groupI were in orginal file batch_2.fst_1-2.Chr_only.tsv"
grep -wE "groupI" ~/shell/fst/batch_2.fst_1-2.Chr_only.tsv | wc -l

echo "Testing how many lines in batch_2.fst_1-2.Chr_only.groupI.tsv"
wc -l ~/shell/fst/batch_2.fst_1-2.Chr_only.groupI.tsv

echo "If above numbers are not the same something went wrong"

echo "Checking for presence of other group numbers in batch_2.fst_1-2.Chr_only.groupI.tsv"

grep -E 'groupII' ~/shell/fst/batch_2.fst_1-2.Chr_only.groupI.tsv | wc -l

echo " if above numeber is not zero then something went wrong "

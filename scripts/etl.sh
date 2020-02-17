#!/usr/bin/env bash
mkdir output
for file in *.gz; do zcat "$file" | awk -F "\"*\t\"*" '{print $8"\t"$9"\t"$10"\t"$11"\t"$12"\t"$13"\t"$14"\t"$15}' | tr '[A-Z]' '[a-z]' | sed -e 's/<[^>]*>//g' >"output/$file.tsv"; done

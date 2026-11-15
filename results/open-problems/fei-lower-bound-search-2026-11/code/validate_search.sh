#!/bin/bash
# validate_search.sh - short runs of fei_search against values known from the exhaustive census.
# Expected: n=6 obj 4 monotone 6.347067498702 (balanced max of H/(I-1) at n = 6, 7); n=7 obj 0 2.954683814183.
cd "$(dirname "$0")" || exit 1
cc -O3 -march=native -o fei_search fei_search.c -lm || exit 2
mkdir -p val && rm -f val/v_n*.txt
./fei_search 6 4 12 1 val/v_n6_o4.txt 60000 0.05 0.001 0 0.1
./fei_search 7 0 15 2 val/v_n7_o0.txt 60000
./fei_search 6 4 12 3 val/v_n6_o4g.txt 60000 0.05 0.001 1
./fei_search 12 0 20 4 val/v_n12_o0.txt 2000
./fei_search 12 4 20 5 val/v_n12_o4.txt 2000
./fei_search 12 4 20 6 val/v_n12_o4g.txt 2000 0.05 0.001 1
for f in val/v_n6_o4.txt val/v_n7_o0.txt val/v_n6_o4g.txt val/v_n12_o0.txt val/v_n12_o4.txt val/v_n12_o4g.txt; do
  echo "== $f"
  grep -v '^#' "$f" | cut -d'|' -f1,2 | sort -k4 -g -r | head -2
  tail -1 "$f"
done

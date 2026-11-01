#!/bin/bash
# three-valued b (6, 2, -1), momentum: (n beta2 beta1) triples at fixed n d, d -> 0
cd "$(dirname "$0")"
mkdir -p r3m_out
printf '%s\n' "50 0.98 0.9" "100 0.99 0.9" "200 0.995 0.9" "400 0.9975 0.9" \
  "50 0.98 0.5" "100 0.99 0.5" "200 0.995 0.5" \
  "100 0.98 0.5" "200 0.99 0.5" "400 0.995 0.5" |
xargs -P 4 -L 1 bash -c 'f=r3m_out/root_$0_$1_$2.txt; python -X utf8 rrm3m.py $0 $1 $2 > $f.tmp 2>&1 && mv $f.tmp $f'
touch r3m_out/DONE

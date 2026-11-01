#!/bin/bash
# three-valued b (6, 2, -1), momentum with eps 1: (n beta2 beta1) at n d 1, d -> 0
cd "$(dirname "$0")"
mkdir -p r3me_out
printf '%s\n' "50 0.98 0" "100 0.99 0" "200 0.995 0" "50 0.98 0.5" "100 0.99 0.5" "200 0.995 0.5" \
  "50 0.98 0.9" "100 0.99 0.9" "200 0.995 0.9" "400 0.9975 0.9" |
xargs -P 4 -L 1 bash -c 'f=r3me_out/root_e1_$0_$1_$2.txt; EPS=1 python -X utf8 rrm3m.py $0 $1 $2 > $f.tmp 2>&1 && mv $f.tmp $f'
touch r3me_out/DONE

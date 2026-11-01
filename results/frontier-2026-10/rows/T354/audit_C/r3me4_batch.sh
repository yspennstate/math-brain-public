#!/bin/bash
# three-valued b (6, 2, -1), eps 3, n d 2: beta1 0 and 0.9, d -> 0
cd "$(dirname "$0")"
mkdir -p r3me4_out
printf '%s\n' "800 0.9975 0.9" "400 0.995 0.9" "200 0.99 0.9" "100 0.98 0.9" "400 0.995 0" "200 0.99 0" "100 0.98 0" |
xargs -P 4 -L 1 bash -c 'f=r3me4_out/root_e3_$0_$1_$2.txt; EPS=3 python -X utf8 rrm3m.py $0 $1 $2 > $f.tmp 2>&1 && mv $f.tmp $f'
touch r3me4_out/DONE

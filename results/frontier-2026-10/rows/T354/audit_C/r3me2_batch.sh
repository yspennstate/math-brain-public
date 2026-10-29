#!/bin/bash
# three-valued b (6, 2, -1), eps 1, n d 2, beta1 0 and 0.5: (n beta2 beta1), d -> 0
cd "$(dirname "$0")"
mkdir -p r3me_out
printf '%s\n' "100 0.98 0" "200 0.99 0" "400 0.995 0" "100 0.98 0.5" "200 0.99 0.5" "400 0.995 0.5" |
xargs -P 3 -L 1 bash -c 'f=r3me_out/root_e1_$0_$1_$2.txt; EPS=1 python -X utf8 rrm3m.py $0 $1 $2 > $f.tmp 2>&1 && mv $f.tmp $f'
touch r3me_out/DONE2

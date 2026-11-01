#!/bin/bash
# beta1 -> 1 on b (6, 2, -1), eps 0, n d 1: (n beta2 beta1); tests 'Uniform in beta1' (agent_B/NOTE.md) on the exact root
cd "$(dirname "$0")"
mkdir -p r3mu_out
printf '%s\n' "50 0.98 0.99" "100 0.99 0.99" "200 0.995 0.99" "50 0.98 0.999" "100 0.99 0.999" "200 0.995 0.999" "50 0.98 0.9999" "100 0.99 0.9999" |
xargs -P 3 -L 1 bash -c 'f=r3mu_out/root_$0_$1_$2.txt; python -X utf8 rrm3m.py $0 $1 $2 > $f.tmp 2>&1 && mv $f.tmp $f'
touch r3mu_out/DONE

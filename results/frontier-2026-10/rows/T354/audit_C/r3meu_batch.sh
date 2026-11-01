#!/bin/bash
# beta1 -> 1 with eps 1 on b (6, 2, -1), n d 1: (n beta2 beta1); the eps > 0 case of the uniform-in-beta1 bound on the exact root
cd "$(dirname "$0")"
mkdir -p r3meu_out
printf '%s\n' "50 0.98 0.99" "100 0.99 0.99" "50 0.98 0.999" "100 0.99 0.999" "50 0.98 0.9999" "100 0.99 0.9999" |
xargs -P 3 -L 1 bash -c 'f=r3meu_out/root_e1_$0_$1_$2.txt; EPS=1 python -X utf8 rrm3m.py $0 $1 $2 > $f.tmp 2>&1 && mv $f.tmp $f'
touch r3meu_out/DONE

#!/bin/bash
# Three-valued b (6, 2, -1 on 0.1, 0.1, 0.8) exact roots for AUDIT_CCLOSED, d .02/.01/.005 at fixed n d (agent C, 20 Oct 2026)
cd "$(dirname "$0")"
mkdir -p r3v_out
printf '%s\n' "10 0.98" "20 0.99" "40 0.995" "50 0.98" "100 0.99" "400 0.9975" "100 0.98" "400 0.995" \
  "250 0.98" "500 0.99" "500 0.98" "1000 0.99" "1000 0.995" |
xargs -P 5 -L 1 bash -c 'f=r3v_out/root_$0_$1.txt; [ -s "$f" ] || { python -X utf8 rrm3v.py $0 $1 > "$f.tmp" 2>&1 && mv "$f.tmp" "$f"; }'
touch r3v_out/DONE

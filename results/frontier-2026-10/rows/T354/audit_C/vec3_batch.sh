#!/bin/bash
# one exact root per job line, each into its own file (parallel appends to one file splice lines on Windows)
cd "$(dirname "$0")"
run() { set -- $1; python vec3_audit.py $1 $2 $3 $4 > vec3_out/H$1_b1$2_b2$3_e$4.txt 2>&1; }
export -f run
xargs -P 6 -I{} bash -c 'run "{}"' < vec3_jobs.txt
echo DONE > vec3_out/DONE

#!/bin/bash
# eps > 0 large-n roots and E2 values, one file per run (no shared appends)
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
lane() { for c in "$@"; do set -- $c; f=rre_out/$(echo "$c" | tr ' ' '_').txt; python -X utf8 rrm_eps.py $c > $f 2>&1; done; }
for e in 1 3; do
  lane "root 100 0.99 $e" "root 200 0.995 $e" "root 500 0.998 $e" &
  lane "root 500 0.99 $e" "root 1000 0.995 $e" &
  lane "root 2500 0.998 $e" &
  lane "root 1000 0.99 $e" "root 2000 0.995 $e" &
  lane "e2 100 0.99 $e 0.1" "e2 200 0.995 $e 0.1" "e2 400 0.9975 $e 0.1" &
done
wait; echo DONE > rre_out/DONE

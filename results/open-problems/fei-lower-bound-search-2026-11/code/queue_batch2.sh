#!/bin/bash
# queue_batch2.sh - write the second batch of fillq jobs on a Mac mini (run there: bash queue_batch2.sh).
# Each job: one core, 2 h, a few MB.  Output ~/fei_agent/fs_n<n>_o<obj>_<m|g>_<seed>.txt, one line per run.
Q=~/fillq/queue
D=~/fei_agent
mk() {  # n obj seed iters gen
  local tag; if [ "$5" = 1 ]; then tag=g; else tag=m; fi
  local name="50_agent_fs_n$1_o$2_${tag}_$3"
  local f="$Q/$name.job"
  printf '#!/bin/bash\n# cores: 1\n# mem_mb: 60\ncd %s || exit 1\nexec ./fei_search %s %s 7200 %s fs_n%s_o%s_%s_%s.txt %s 0.05 0.0005 %s 0.1\n' \
    "$D" "$1" "$2" "$3" "$1" "$2" "$tag" "$3" "$4" "$5" > "$f.tmp"
  chmod +x "$f.tmp" && mv "$f.tmp" "$f"
}
s=200
# tower score H/(I-1) on balanced monotone functions
for n in 8 9; do for k in 1 2; do s=$((s+1)); mk $n 4 $s 2000000 0; done; done
for n in 10 11; do for k in 1 2; do s=$((s+1)); mk $n 4 $s 3000000 0; done; done
for n in 12 13 14; do for k in 1 2; do s=$((s+1)); mk $n 4 $s 4000000 0; done; done
# tower score on balanced general functions (swap moves)
for n in 7 8 9 10; do s=$((s+1)); mk $n 4 $s 3000000 1; done
# best-coordinate ratio and sum form, monotone, beyond 10 variables
for n in 11 12 13; do for k in 1 2; do s=$((s+1)); mk $n 0 $s 1000000 0; done; done
for n in 11 12; do s=$((s+1)); mk $n 2 $s 1000000 0; done
ls "$Q" | grep -c 50_agent_fs

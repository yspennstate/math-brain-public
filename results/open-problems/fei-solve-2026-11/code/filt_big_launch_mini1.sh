#!/bin/bash
# Launch three filt_big.py lanes on Mac mini 1 (nice 10, at most 2 threads each, well under 1 GiB each).
# Stop: kill the PIDs in ~/fei_solve_agent/big_run/pid_*.txt (by PID only).
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
CODE=$HOME/fei_solve_agent/code
RUN=$HOME/fei_solve_agent/big_run
mkdir -p "$RUN"
cd "$CODE" || exit 1
for lane in "graph6,graph7" "plane,cyclic" "misc"; do
  tag=$(echo "$lane" | tr ',' '_')
  nohup nice -n 10 env OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 VECLIB_MAXIMUM_THREADS=2 \
    python3 "$CODE/filt_big.py" "$lane" > "$RUN/out_$tag.txt" 2>&1 < /dev/null &
  echo $! > "$RUN/pid_$tag.txt"
  echo "started $tag pid $(cat "$RUN/pid_$tag.txt")"
done

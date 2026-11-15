#!/bin/sh
# Launch the best-coordinate search (hill_rho.py) on Mac mini 2: nice 10, one thread each, PID files, stop file hill/STOP.
# Usage: sh hill_launch_mini2.sh SECONDS
cd "$HOME/fei_agent" || exit 1
SEC="${1:-10800}"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
rm -f hill/STOP
launch() {
  # n objective seed start
  tag="n$1_$2_s$3"
  nohup nice -n 10 ./venv/bin/python code/hill_rho.py "$1" "$2" "$SEC" "$3" hill "$4" > "hill/out_$tag.txt" 2>&1 &
  echo $! > "hill/pid_$tag.txt"
  echo "started $tag pid $!"
}
launch 6 rhoD 11 random
launch 7 rhoD 12 random
launch 8 rhoD 13 sparse
launch 8 rhoD 14 tribes
launch 9 rhoD 15 sparse
launch 9 rhoD 16 tribes
launch 10 rhoD 17 sparse
launch 10 rhoD 18 tribes
launch 8 HmI 19 sparse
launch 9 PsiI 20 tribes

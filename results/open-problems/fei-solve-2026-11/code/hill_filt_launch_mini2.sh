#!/bin/sh
# Launch the filtration-witness search (hill_filt.py) on Mac mini 2: nice 10, one thread each, PID files in hillF/,
# stop file hillF/STOP.   Usage: sh hill_filt_launch_mini2.sh SECONDS
# (10 Nov 04:2x: the first version wrote no PID files, because "cd code && nohup ... &" put the cd in the background
#  list; the PIDs of that run were recorded afterwards by hill_filt_pids.sh.)
cd "$HOME/fei_agent/code" || exit 1
SEC="${1:-14400}"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
mkdir -p ../hillF
rm -f ../hillF/STOP
launch() {
  # n objective seed start
  tag="n$1_$2_s$3"
  nohup nice -n 10 ../venv/bin/python hill_filt.py "$1" "$2" "$SEC" "$3" ../hillF "$4" > "../hillF/out_$tag.txt" 2>&1 < /dev/null &
  echo $! > "../hillF/pid_$tag.txt"
  echo "started $tag pid $!"
}
launch 8 rhoF 32 random
launch 8 rhoF 33 sparse
launch 8 rhoF 34 tribes
launch 9 rhoF 35 sparse
launch 9 rhoF 36 tribes
launch 9 rhoF 37 random
launch 10 rhoF 38 sparse
launch 10 rhoF 39 tribes
launch 8 gap 40 random
launch 9 gap 41 sparse

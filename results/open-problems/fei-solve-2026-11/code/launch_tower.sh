#!/bin/bash
# Launch the tower-search lanes on Mac mini 2 (CPU only, nice 10, one thread each, under 100 MB each).
# Usage: bash launch_tower.sh      Stop: touch ~/fei_agent/tower/STOP   (or bash stop_tower.sh)
cd ~/fei_agent/code || exit 1
OUT=~/fei_agent/tower
mkdir -p "$OUT"
rm -f "$OUT/STOP"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
PY=~/fei_agent/venv/bin/python
launch() {  # a b seed sweeps init temperature
  nohup nice -n 10 "$PY" tower_hill.py "$1" "$2" "$3" "$4" "$OUT" "$5" "$6" > "$OUT/out_a$1_b$2_s$3.txt" 2>&1 < /dev/null &
  echo $! > "$OUT/pid_a$1_b$2_s$3.txt"
}
launch 3 3 31 3000 pm33 0.02
launch 3 4 32 1500 random 0.05
launch 1 13 33 600 random 0.05
launch 3 5 34 250 random 0.05
sleep 2
ls "$OUT"

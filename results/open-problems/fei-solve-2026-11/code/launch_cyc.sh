#!/bin/bash
# Launch the cyclic-function search lanes on Mac mini 2 (CPU only, nice 10, one thread each, about 50-300 MB each).
# Usage: bash launch_cyc.sh      Stop: touch ~/fei_agent/cyc/STOP   (or kill the PIDs in ~/fei_agent/cyc/pid_*.txt)
cd ~/fei_agent/code || exit 1
OUT=~/fei_agent/cyc
mkdir -p "$OUT"
rm -f "$OUT/STOP"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
PY=~/fei_agent/venv/bin/python
launch() {  # n objective seed sweeps init temperature-factor
  nohup nice -n 10 "$PY" cyc_hill.py "$1" "$2" "$3" "$4" "$5" "$OUT" "$6" > "$OUT/out_n$1_$2_$5_s$3.txt" 2>&1 < /dev/null &
  echo $! > "$OUT/pid_n$1_$2_$5_s$3.txt"
}
launch 14 G 21 1500 random 0.5
launch 14 G 22 1500 tribes3 0.02
launch 15 G 23 800 tribes3 0.02
launch 16 G 24 300 random 0.5
launch 16 G 25 300 tribes4 0.02
launch 18 G 26 40 tribes4 0.02
sleep 2
ls "$OUT"

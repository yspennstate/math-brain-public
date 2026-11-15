#!/bin/bash
# Launch one niced single-thread ov_hill.py lane.
# Usage: bash launch_ovhill.sh <python> <codedir> <outdir> <n> <obj> <lam> <seed> <hours>
# Writes <outdir>/pid_ovhill_n<n>_<obj>_l<lam>_s<seed>.txt ; stop: touch <outdir>/STOP (or kill that pid).
PY="$1"; CODE="$2"; OUT="$3"; N="$4"; OBJ="$5"; LAM="$6"; SEED="$7"; HRS="$8"
mkdir -p "$OUT"
if [ -e "$OUT/STOP" ]; then echo "STOP present in $OUT - not launching"; exit 3; fi
TAG="ovhill_n${N}_${OBJ}_l${LAM}_s${SEED}"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
nohup nice -n 10 "$PY" "$CODE/ov_hill.py" "$N" "$OBJ" "$LAM" "$SEED" "$OUT" "$HRS" > "$OUT/$TAG.out.txt" 2>&1 < /dev/null &
echo $! > "$OUT/pid_$TAG.txt"
echo "started $TAG pid $(cat "$OUT/pid_$TAG.txt")"

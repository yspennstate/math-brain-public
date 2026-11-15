#!/bin/bash
# Launch exhaustive symmetric-function tower searches (sym_enum.py): CPU only, nice 10, one thread, about 200 MB each.
# Usage: bash launch_enum.sh <python> <codedir> <outdir> <groups> <lane> <nlanes> [<groups> <lane> <nlanes> ...]
#   <groups> may be a comma-separated list, run one after the other.
# Stop: touch <outdir>/STOP   or   bash stop_enum.sh <outdir>   (kills by the PIDs recorded here, never by name)
PY=$1; CODE=$2; OUT=$3; shift 3
cd "$CODE" || exit 1
mkdir -p "$OUT"
rm -f "$OUT/STOP"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
while [ $# -ge 3 ]; do
  g=$1; l=$2; n=$3; shift 3
  tag=$(echo "$g" | tr ',' '_')
  if [ -n "$ENUM_PATS" ]; then   # sign patterns, e.g. ENUM_PATS=mm,mp,pm (see sym_enum.py)
    tag="${tag}_$(echo "$ENUM_PATS" | tr -d ',')"
    nohup nice -n 10 "$PY" sym_enum.py "$g" "$OUT" "$l" "$n" 2048 14 "$ENUM_PATS" > "$OUT/out_${tag}_l${l}of${n}.txt" 2>&1 < /dev/null &
    echo $! > "$OUT/pid_${tag}_l${l}of${n}.txt"
    continue
  fi
  nohup nice -n 10 "$PY" sym_enum.py "$g" "$OUT" "$l" "$n" > "$OUT/out_${tag}_l${l}of${n}.txt" 2>&1 < /dev/null &
  echo $! > "$OUT/pid_${tag}_l${l}of${n}.txt"
done
sleep 2
ls "$OUT"

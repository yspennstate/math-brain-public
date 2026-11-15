#!/bin/bash
# Stop the sym_enum.py lanes started by launch_enum.sh, by the PIDs recorded at launch (never by name).
# Usage: bash stop_enum.sh <outdir>
OUT=$1
[ -d "$OUT" ] || exit 1
for f in "$OUT"/pid_*.txt; do
  [ -f "$f" ] || continue
  p=$(cat "$f")
  if kill -0 "$p" 2>/dev/null; then
    if ps -p "$p" -o command= | grep -q sym_enum.py; then kill "$p" && echo "stopped $p ($f)"; else echo "pid $p is not ours, left alone"; fi
  fi
done

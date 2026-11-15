#!/bin/bash
# Stop the tower-search lanes on Mac mini 2 by the PIDs recorded at launch (never by name).
OUT=~/fei_agent/tower
for f in "$OUT"/pid_*.txt; do
  [ -f "$f" ] || continue
  p=$(cat "$f")
  if kill -0 "$p" 2>/dev/null; then
    if ps -p "$p" -o command= | grep -q tower_hill.py; then kill "$p" && echo "stopped $p ($f)"; else echo "pid $p is not ours, left alone"; fi
  fi
done

#!/bin/bash
# Stop the cyclic-search lanes on Mac mini 2 by the PIDs recorded at launch (never by name), then archive the run folder.
OUT=~/fei_agent/cyc
for f in "$OUT"/pid_*.txt; do
  [ -f "$f" ] || continue
  p=$(cat "$f")
  if kill -0 "$p" 2>/dev/null; then
    if ps -p "$p" -o command= | grep -q cyc_hill.py; then kill "$p" && echo "stopped $p ($f)"; else echo "pid $p is not ours, left alone"; fi
  fi
done
sleep 1
if [ -n "$1" ]; then mkdir -p "$OUT/$1" && mv "$OUT"/pid_*.txt "$OUT"/log_*.txt "$OUT"/out_*.txt "$OUT"/best_*.txt "$OUT/$1"/ 2>/dev/null; echo "archived to $OUT/$1"; fi

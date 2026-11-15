#!/bin/bash
# Stop selected sym_enum.py lanes by their recorded PID files (never by name).
# Usage: bash stop_enum_some.sh <outdir> <pidfile basename> [<pidfile basename> ...]
OUT=$1; shift
for b in "$@"; do
  f="$OUT/$b"
  [ -f "$f" ] || { echo "no $f"; continue; }
  p=$(cat "$f")
  if kill -0 "$p" 2>/dev/null; then
    if ps -p "$p" -o command= | grep -q sym_enum.py; then kill "$p" && echo "stopped $p ($b)"; else echo "pid $p is not ours, left alone"; fi
  else
    echo "pid $p already gone ($b)"
  fi
done

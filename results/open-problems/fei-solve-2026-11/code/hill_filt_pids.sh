#!/bin/sh
# Record the PIDs of the running hill_filt.py processes of this user into ~/fei_agent/hillF/pid_<tag>.txt
# (tag = n<n>_<objective>_s<seed>, read from each process's own arguments).  Prints one line per process.
cd "$HOME/fei_agent/hillF" || exit 1
ps -U "$(id -u)" -o pid=,args= | grep "hill_filt.py" | grep -v grep | while read pid rest; do
  set -- $rest
  # args: python hill_filt.py n objective seconds seed outdir start
  while [ "$#" -gt 0 ] && [ "$1" != "hill_filt.py" ]; do shift; done
  [ "$#" -ge 5 ] || continue
  tag="n$2_$3_s$5"
  echo "$pid" > "pid_$tag.txt"
  echo "$tag $pid"
done

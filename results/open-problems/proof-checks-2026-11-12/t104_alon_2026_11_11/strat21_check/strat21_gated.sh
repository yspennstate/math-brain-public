#!/bin/bash
# an agent: wait until memory free >= 25%, then replay STRAT21 once
cd ~/agent_run/STRAT21_REPLAY || exit 1
while true; do
  f=$(memory_pressure | tail -1 | sed -E "s/.*: ([0-9]+)%.*/\1/")
  [ "$f" -ge 25 ] && break
  echo "$(date +%H:%M) free $f% waiting" >> ../strat21_gate.log; sleep 60
done
echo "$(date +%H:%M) start" >> ../strat21_gate.log
/usr/bin/time -l /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 replay_all.py > ../strat21_myreplay.out 2> ../strat21_myreplay.time < /dev/null
echo "$(date +%H:%M) exit $?" >> ../strat21_gate.log

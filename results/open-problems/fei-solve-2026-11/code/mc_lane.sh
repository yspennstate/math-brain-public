#!/bin/bash
# One lane of mc_chain.py jobs on a Mac mini.  usage: mc_lane.sh TAG
# Jobs are the lines "name words batches seed" of $RUN/jobs_TAG.txt, run one after another.
# Stop between jobs: touch $RUN/STOP.
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
CODE=${MC_CODE:-$HOME/fei_solve_agent/code}
RUN=${MC_RUN:-$HOME/fei_solve_agent/mc_run}
PY=${MC_PY:-python3}
tag=$1
while read -r name words batches seed; do
  [ -z "$name" ] && continue
  [ -e "$RUN/STOP" ] && break
  safe=$(echo "$name" | tr ':' '_')
  "$PY" "$CODE/mc_chain.py" run "$name" "$words" "$batches" "$seed" "$RUN/${safe}_s${seed}.json" \
    >> "$RUN/out_$tag.txt" 2>&1 < /dev/null
done < "$RUN/jobs_$tag.txt"
echo "lane $tag finished $(date)" >> "$RUN/out_$tag.txt"

#!/bin/bash
# neg_loop.sh FIRST LAST - rounds of (screen every input negation against the last table, value iteration from it).
# Round r reads W_run<r-1>.txt and keep<r-1>.txt, writes neg<r>.lib/.coin, W_run<r>.txt, keep<r>.txt, and refreshes
# W_cur.txt, the table the queued searches read.  Run on Mac mini 2 in ~/fei_agent.
cd ~/fei_agent || exit 1
for r in $(seq "$1" "$2"); do
  q=$((r-1))
  nice -n 10 python3 neg_screen.py W_run$q.txt neg$r --lib keep$q.txt --coin rec18.lab --coin coins_t0.txt --nmax 12 --topk 3 > neg$r.log 2>&1 || exit 2
  nice -n 10 python3 tower_vi2.py --nobase --grid 9601 --span 24 --sweeps 3000 --libfile keep$q.txt --libfile neg$r.lib \
    --coinfile rec18.lab --coinfile keep$q.txt.coin --coinfile neg$r.coin --init W_run$q.txt --dump W_run$r.txt --keep keep$r.txt > vi_run$r.txt 2>&1 || exit 3
  cp W_run$r.txt W_cur.txt.tmp && mv W_cur.txt.tmp W_cur.txt
done

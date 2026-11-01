#!/bin/bash
# One-command finish for the C9 tube: four-piece chain check (bfull14, brst10, flow599 to row 887, plain888g8 = plain
# clustered frame at C9_DELTA 0.01 with C9_LNSUB 8), then the trap at the exact end radius in the frame the tube ends in
# (C9_TRAP_FRAMEB=1: frame_b at the last node under FLOWCOL 0, DELTA 0.01). usage: bash finish_c9.sh [--partial]
# Writes logs/finish_5.out and appends the verdict to ../NOTES.md. The trap is skipped on --partial.
set -u
export C9_ARB=1 C9_CLUSTER=1 C9_U=99/10000000 C9_KAPPA=1/500 C9_FACE=section C9_HMAX=0.5
out=logs/finish_5${1:+_partial}.out
python c9_bcheck5.py logs/bfull14.jsonl 199 logs/brst10.jsonl 599 logs/flow599.jsonl 887 logs/plain888g8.jsonl ${1:-} > $out 2>&1
rc=$?
r=$(grep '^r_end_exact' $out | awk '{print $2}')
if [ $rc -ne 0 ] || [ -z "$r" ]; then
  printf "%s finish_c9 %s: chain check FAILED rc %s (see scripts/%s)\n" "$(date +%H:%M)" "${1:-final}" $rc $out >> ../NOTES.md; exit 1
fi
if [ -n "${1:-}" ]; then
  printf "%s finish_c9 --partial: CHAIN OK so far, r at last row %s (scripts/%s)\n" "$(date +%H:%M)" "$r" $out >> ../NOTES.md; exit 0
fi
C9_FLOWCOL=0 C9_DELTA=0.01 C9_TRAP_FRAMEB=1 python c9_run.py trap 820 0.004 $r logs/trap_plain888g8.jsonl >> $out 2>&1
pass=$(grep -c '"PASS"' logs/trap_plain888g8.jsonl)
printf "%s finish_c9: CHAIN OK, r_end_exact %s, trap PASS rows %s (scripts/%s, logs/trap_plain888g8.jsonl)\n" "$(date +%H:%M)" "$r" $pass $out >> ../NOTES.md

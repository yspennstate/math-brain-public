#!/bin/bash
# After finish_c9.sh: copy the chain's logs and verdict into rows/T240/C9_recovery, write SHA256SUMS, add a moves.jsonl
# row and a DOSSIER line, push. Refuses unless finish_5.out says CHAIN OK and the trap log has a PASS. (agent H)
set -eu
W=(local file); R=(local file); T=06_math_research/frontier/rows/T240
cd $W/scripts
grep -q 'CHAIN OK' logs/finish_5.out || { echo "no CHAIN OK"; exit 3; }
pass=$(grep -c '"PASS"' logs/trap_plain888g8.jsonl || true); [ "$pass" -ge 1 ] || { echo "trap not PASS"; exit 3; }
r=$(grep '^r_end_exact' logs/finish_5.out | awk '{print $2}')
D=$R/$T/C9_recovery; mkdir -p $D/logs $D/scripts
python fill_draft.py
cp logs/bfull14.jsonl logs/brst10.jsonl logs/flow599.jsonl logs/plain888g8.jsonl logs/finish_5.out logs/trap_plain888g8.jsonl $D/logs/
cp *.py *.sh $D/scripts/; cp $W/C9_post_exit_DRAFT.md $W/NOTES.md $D/
printf "C9 recovery (agent H, 18 Oct 2026): the post-exit block tube from the exit face to t = 820 in four pieces\n(bfull14, brst10, flow599 rows to 887, plain888g8), chain checked exactly by scripts/c9_bcheck5.py (logs/finish_5.out),\nthen the trap at the exact end radius in the tube's own end frame (logs/trap_plain888g8.jsonl). Re-run: bash scripts/finish_c9.sh.\nC9_post_exit_DRAFT.md is lead-authored and needs an independent reviewer.\n" > $D/README.md
(cd $D && find . -type f ! -name SHA256SUMS | sort | xargs sha256sum > SHA256SUMS)
python - "$R/$T" "$r" "$pass" <<'PY'
import io, json, sys, time
from fractions import Fraction as F
d, r, p = sys.argv[1], sys.argv[2], sys.argv[3]
row = {"at": time.strftime("%Y-%m-%dT%H:%M:%S+03:00"), "by": "agent H", "kind": "special", "claim": "C9",
       "text": "C9 (lead-authored, unreviewed): post-exit recovery tube to t = 820 closed in four pieces, chain exact (c9_bcheck5), "
               "r_end = %.3e, trap PASS (%s rows) in the tube's end frame; files rows/T240/C9_recovery/. Needs an independent reviewer." % (float(F(r)), p)}
io.open(d + "/moves.jsonl", "a", encoding="utf-8", newline="\n").write(json.dumps(row) + "\n")
s = io.open(d + "/DOSSIER.md", encoding="utf-8").read()
s += "\n- C9 (18 Oct, agent H, lead-authored, unreviewed): post-exit recovery tube closed to t = 820, r_end = %.3e, trap PASS; rows/T240/C9_recovery/README.md.\n" % float(F(r))
io.open(d + "/DOSSIER.md", "w", encoding="utf-8", newline="\n").write(s)
PY
cd $R && timeout 300 bash ~/.claude/dreaming/push_paths.sh $R "T240 C9 recovery tube closed" $T/moves.jsonl $T/DOSSIER.md $(find $T/C9_recovery -type f) | tail -1

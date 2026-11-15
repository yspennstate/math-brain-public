#!/bin/zsh
# Round 5 (15 Nov, an agent, T-20261114-032): a continuation brief for every round 4 problem whose REPORT.md says
# VERDICT: PARTIAL or PROVED (a subclass). The worker reads the round 4 folder (read-only) and pushes the next piece.
B=$HOME/codex_op_1114r4
R=$HOME/codex_op_1114r5
mkdir -p $R/briefs || exit 1
cp $B/pool.sh $R/pool.sh
sed -i '' 's#codex_op_1114r4#codex_op_1114r5#' $R/pool.sh
n=0
for rep in $B/briefs/*/REPORT.md(N); do
  head -1 $rep | grep -qE '^VERDICT: (PARTIAL|PROVED)' || continue
  id=${rep:h:t}; d=$R/briefs/$id
  [[ -d $d ]] && continue
  mkdir -p $d
  {
    sed -n '1,/^Your job for this session/p' $B/briefs/$id/PROMPT.md | sed '$d'
    print -r -- "Later work: a round 4 worker built on that session. Its folder is $B/briefs/$id (read it,"
    print -r -- "never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start."
    print -r -- ""
    print -r -- "Your job for this session: take the NEXT checkable step on this problem, building on that work."
    print -r -- "1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was"
    print -r -- "   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop."
    print -r -- "2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and"
    print -r -- "   write in LOG.md whether it holds. If it does not hold, that finding is your result."
    print -r -- "3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,"
    print -r -- "   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in"
    print -r -- "   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md."
    print -r -- "4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss."
    print -r -- "5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED"
    print -r -- "   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier"
    print -r -- "   report, the commands, what failed, what you are unsure of, and what the next worker should do."
    print -r -- ""
    sed -n '/^Rules (the author/,/^----- earlier REPORT.md -----/p' $B/briefs/$id/PROMPT.md | sed '$d'
    print -r -- ""
    print -r -- "----- earlier REPORT.md -----"
    head -c 12000 $rep
  } > $d/PROMPT.md
  n=$((n+1))
done
echo "round 5 briefs: $n"
grep -c '' $R/briefs/*/PROMPT.md(N) | head -3
grep -n '^B=' $R/pool.sh

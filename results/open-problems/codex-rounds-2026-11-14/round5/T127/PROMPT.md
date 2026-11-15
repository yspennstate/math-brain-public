# Open problem T127: Recurrence of the frog model on 3-ary and 4-ary trees

Statement: On the rooted d-ary tree, place one sleeping frog at each vertex and an active frog at the root; active frogs perform independent simple random walks and wake every frog they visit. Decide for d = 3 and d = 4 whether the root is visited infinitely often almost surely (recurrence) or finitely often (transience).

Caveat: Hoffman, Johnson and Junge settled d = 2 and d ≥ 5 and left the two middle cases; the problem is to find the transition.

Source: C. Hoffman, T. Johnson and M. Junge, Recurrence and transience for the frog model on trees, Ann. Probab. 45 (2017)

Where it stands (checked by us, Nov 2026): Recurrent for d = 2 and transient for d ≥ 5 (Hoffman–Johnson–Junge, arXiv:1404.6238); with Poisson(μ) sleeping frogs per site the critical μ is known to grow linearly in d (Johnson–Junge, Electron. Commun. Probab. 21 (2016)). Mathews (arXiv:2309.14443) still treats d = 3 and d = 4 as known only from simulation. With one frog per site, d = 3 and d = 4 are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T127 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T127 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T127 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.



----- earlier REPORT.md -----
VERDICT: PARTIAL retrieved the outside full-solution paper and checked that its statements match T127

The next step named by the preceding report is now completed: the full
[paper source](https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/paper/main.tex)
and [statement map](https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/STATEMENTS.md)
were retrieved. SOLVED_ELSEWHERE.md gives the exact attribution and reference.
The claimed conclusions are recurrence for d=3 and transience for d=4 in
the stated model. No arXiv id was identified.

This advances the earlier evidence from a repository announcement to an
accessible proof text with applicable theorem statements. It does not
independently certify correctness. The formal model files remained
inaccessible, and neither the Lean build nor its certificates was replayed.
The label PARTIAL reflects this limit.

Stopped under step 1 of the task. No new proof or computation was undertaken,
and the earlier Bernoulli certificates were not rerun. They are neither
confirmed anew nor contradicted here. No claim that T127 has been independently
resolved is made.

Commands: read-only shell reads of predecessor artifacts, memory index,
protocol and compute state; web search/open calls listed in LOG.md. No
mathematical programs were run. All new files are in this folder.

What failed: retrieval of the Zenodo record and individual formal model and
solution files. What remains uncertain: correctness of the complete outside
argument and correspondence of the actual formal definitions to the paper.

Next worker: start from the now accessible paper and statement map, obtain
the formal definitions and certificate inputs, and audit/replay the claimed
solution before committing further effort to the diluted packet model.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 04:55 Asia/Tbilisi.

# Open problem T116: Worst-case trace reconstruction

Statement: An unknown binary string x of length n is observed through independent traces, each obtained by deleting every bit independently with probability q ∈ (0, 1). Determine the order of the number of traces needed to reconstruct every x with high probability; in particular decide whether polynomially many traces suffice.

Caveat: For a uniformly random x far fewer traces are needed, exp(O(log^{1/3} n)) (Holden–Pemantle–Peres–Zhai 2020); for the worst case the gap is now between polynomial and quasipolynomial bounds.

Source: T. Batu, S. Kannan, S. Khanna and A. McGregor, Reconstructing strings from random traces, Proc. SODA 2004; F. Nazarov and Y. Peres, Trace reconstruction with exp(O(n^{1/3})) samples, Proc. STOC 2017

Where it stands (checked by us, Nov 2026): exp(O(n^{1/3})) traces suffice (De–O'Donnell–Servedio 2017; Nazarov–Peres 2017), improved to exp(Õ(n^{1/5})) (Chase 2021) and then to quasipolynomially many, for every retention probability at least 1/polylog n (Burudgunte–Valiant–Wang, arXiv:2607.04073). The best lower bound is Ω̃(n^{3/2}) (Chase, Ann. Inst. Henri Poincaré Probab. Stat. 57 (2021)), after n^{5/4} (Holden–Lyons, Ann. Appl. Probab. 30 (2020)). Whether polynomially many traces suffice is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T116 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T116 (read it,
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
VERDICT: PARTIAL independently rechecked the reported resolution and audited the comparator statement

The earlier literature finding holds: the cited preprint reports a negative answer to the polynomial-sample question. See SOLVED_ELSEWHERE.md for the precise theorem, reference, identifier status and limits. The exact asymptotic order is not determined. Following the requested literature-stop branch, no separate research extension was attempted.

New beyond the earlier report: AUDIT.md checks the actual Lean comparator definitions and quantifiers against the task. This is a statement-level check; it is not a formal proof verification. LOG.md independently re-derives the fixed-channel consequence in two ways and tests the relevant boundary cases.

Commands: `OMP_NUM_THREADS=1 nice -n 15 python3 -B` for small local reads and the final file audit; web searches and opened primary-source URLs are recorded in LOG.md. No numerical computation, git, subagents, external messages or writes outside this folder were used.

What failed or remains uncertain: the nice wrapper emitted a priority warning; the final process's effective priority was independently verified as nice 20. No heavy job ran. No arXiv identifier was located. The full lower-bound construction and proof implementation remain unaudited here; no Lean checker was run. No new post-report result changing the remaining gap was found in the short search.

Next worker: check the implementation and comparator together in an environment with the appropriate Lean dependencies and permitted resource budget. Inspect assumptions and the dependency closure, then examine the auxiliary-observation-to-genuine-trace transfer. Do not interpret successful parsing of a comparator statement as proof certification.

Task: “take the NEXT checkable step on this problem, building on that work.” — T116, November 15, 2026, 01:30 Asia/Tbilisi.

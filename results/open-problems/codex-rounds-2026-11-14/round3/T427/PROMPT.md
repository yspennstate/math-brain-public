# Open problem T427: The second-order term in the two-dimensional random matching problem

Statement: Let X1,...,Xn be iid uniform points in the unit square, mu_n=(1/n)sum_i delta_Xi, and let lambda be uniform probability measure on the square. Does c_square=lim_{n to infinity}[n E W_2(mu_n,lambda)^2-(log n)/(4 pi)] exist as a finite number, and what is its value?

Caveat: The two-empirical-sample problem has a different leading coefficient. No unchecked predicted numerical value is asserted.

Source: Ambrosio-Stra-Trevisan, A PDE approach to a 2-dimensional matching problem (arXiv:1611.04960); Ambrosio-Glaudo, Finer estimates (arXiv:1810.07002); Caracciolo et al. (arXiv:1402.6993).

Where it stands (checked by us, Nov 2026): The leading logarithmic term is proved. Finer error estimates and nonconstant-density leading asymptotics do not identify the finite semidiscrete next-order constant. The heuristic source does not constitute a proof of this limit.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T427 (read it,
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
VERDICT: PARTIAL existence settled in arXiv:2610.40509v1 as stated; numerical value remains unevaluated

Found Yunzong Xu's 29 October 2026 preprint within the ten-minute search window. Its Corollary 2 directly covers the requested square semidiscrete limit. The formula, reference, normalization, and remaining unknown are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

No new proof or numerical computation was undertaken, following the instruction to stop on finding a substantial literature advance. [LOG.md](LOG.md) records the exact search queries, opened sources, shell commands, and algebraic audit.

The PDF screenshot request failed with a cache miss; PDF text and HTML were accessible. No numerical value was inferred. The unresolved issue is evaluation of the universal semidiscrete constant; the preprint's full proof also remains independently unaudited here.

File validation passed. The environment denied `nice -n 15` for that tiny read-only check but still executed it; no numerical workload was run. Initial shell reads were also unwrapped. Details and exact output are in LOG.md.

Next worker: read the equal-mass parts of Proposition 3.1, Theorem 4, and Appendix C before relying on the theorem, then investigate evaluation of the universal constant. Do not conflate it with the bipartite constant.

Task: “push this problem forward by one checkable piece.” Session clock: 14 November 2026, 22:14 Asia/Tbilisi (18:14 UTC).

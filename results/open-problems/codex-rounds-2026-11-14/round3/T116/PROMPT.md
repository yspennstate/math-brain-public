# Open problem T116: Worst-case trace reconstruction

Statement: An unknown binary string x of length n is observed through independent traces, each obtained by deleting every bit independently with probability q ∈ (0, 1). Determine the order of the number of traces needed to reconstruct every x with high probability; in particular decide whether polynomially many traces suffice.

Caveat: For a uniformly random x far fewer traces are needed, exp(O(log^{1/3} n)) (Holden–Pemantle–Peres–Zhai 2020); for the worst case the gap is now between polynomial and quasipolynomial bounds.

Source: T. Batu, S. Kannan, S. Khanna and A. McGregor, Reconstructing strings from random traces, Proc. SODA 2004; F. Nazarov and Y. Peres, Trace reconstruction with exp(O(n^{1/3})) samples, Proc. STOC 2017

Where it stands (checked by us, Nov 2026): exp(O(n^{1/3})) traces suffice (De–O'Donnell–Servedio 2017; Nazarov–Peres 2017), improved to exp(Õ(n^{1/5})) (Chase 2021) and then to quasipolynomially many, for every retention probability at least 1/polylog n (Burudgunte–Valiant–Wang, arXiv:2607.04073). The best lower bound is Ω̃(n^{3/2}) (Chase, Ann. Inst. Henri Poincaré Probab. Stat. 57 (2021)), after n^{5/4} (Holden–Lyons, Ann. Appl. Probab. 30 (2020)). Whether polynomially many traces suffice is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T116 (read it,
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
VERDICT: PARTIAL located a later preprint ruling out polynomial worst-case trace complexity

The literature check found OpenAI, *Quantitative lower bounds for trace reconstruction* (September 24, 2026). Its main theorem gives a superpolynomial lower bound for complete deletion traces at every fixed deletion probability. The model is the one in the task, with unrestricted computation. See [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) for the precise theorem, primary links, identifier status, and the October algorithmic follow-up.

This follows the instructed stop branch. No new proof, finite computation, or counterexample search was undertaken. The precise asymptotic order remains unsettled by the cited bounds.

Checks: read the theorem and model definitions in the primary TeX; cross-checked title, author and date against the release citation and manuscript header; read the final transfer section for exact lengths and success quantifiers. Independently checked the fixed-channel consequence in two forms: log(q^3 log n)=log log n+3 log q diverges, and the logarithm of the displayed bound divided by log n diverges. Thus every fixed polynomial is eventually exceeded. The condition excludes q tending to zero too quickly; it includes every fixed q in (0,1).

Commands and tool calls: web searches and exact opened source paths are recorded in [LOG.md](LOG.md). Local commands were tiny reads/writes under `OMP_NUM_THREADS=1 nice -n 15 python3 -B`; there was no numerical run or dataset. `ps -o pid,ppid,ni,comm -p $$ -p $PPID` was blocked by the sandbox. The nice wrapper also emitted a priority warning, so effective priority was not verified.

Limitations: repository directory fetches and PDF extraction failed; the primary manuscript TeX was accessible. No arXiv identifier was located for either new preprint. Their full proofs and Lean artifacts were not independently verified here, and no journal acceptance was established.

Next worker: review the lower-bound construction or run its Lean comparator and check the formal statement against ordinary deletion traces before treating the reported resolution as independently certified. For new research, update the starting bounds and target the remaining superpolynomial-to-quasipolynomial gap.

Task: “push this problem forward by one checkable piece” — T116, November 14, 2026, 22:00 Asia/Tbilisi (session start).

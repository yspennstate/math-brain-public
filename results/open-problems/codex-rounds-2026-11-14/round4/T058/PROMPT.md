# Open problem T058: Concentration of the chromatic number of G(n, 1/2)

Statement: Determine the width of concentration of χ(G(n, 1/2)): conjecturally, for a set of n of density one, the shortest interval containing χ(G(n, 1/2)) with probability tending to 1 has length n^{1/2+o(1)}.

Caveat: The exact form of the conjecture (most n versus all n) is to verify.

Source: E. Shamir and J. Spencer, Sharp concentration of the chromatic number on random graphs G_{n,p}, Combinatorica 7 (1987); B. Bollobás, How sharp is the concentration of the chromatic number?, Combin. Probab. Comput. 13 (2004); A. Heckel and O. Riordan, How does the chromatic number of a random graph vary?, J. London Math. Soc. 108 (2023) 1769–1815

Where it stands (checked by us, Nov 2026): Concentration on an interval of length about √n (Shamir–Spencer 1987); not concentrated on fewer than n^{1/4−ε} values for infinitely many n (Heckel, arXiv:1906.11808), improved to n^{1/2−ε} (Heckel–Riordan, J. Lond. Math. Soc. 108 (2023)). The behaviour for typical n is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T058 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T058 (read it,
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
VERDICT: PARTIAL proved joint second-moment estimates for the two independent-set counts on fixed interior phase bands

The earlier deterministic phase-density result holds. Its finite counts, density constants and theta calculation were independently reproduced; see LOG.md and earlier_recheck.json.

The new piece is probabilistic. Put k=floor(f(n)), where f is the independence-number approximation in the earlier report, and let X_j count independent j-sets in G(n,1/2), with mean mu_j. Uniformly when delta <= {f(n)} <= 1-delta for any fixed 0<delta<1/2, [PROOF.md](PROOF.md) proves

\[
\operatorname{Var}X_k\sim\mu_k,\qquad
\operatorname{Var}X_{k-1}\sim\mu_{k-1},\qquad
\operatorname{Cov}(X_k,X_{k-1})\sim k\mu_k.
\]

In particular,

\[
\operatorname{Corr}(X_k,X_{k-1})
\sim\sqrt{\frac{k(n-k+1)}{2^{k-1}}}
\sim\frac{2\sqrt2}{e}\,2^{\{f(n)\}/2}
                 \frac{(\log_2n)^{3/2}}{\sqrt n}\longrightarrow0.
\]

The best affine prediction of X_(k-1) from X_k leaves mean-square error asymptotic to mu_(k-1). Contained pairs give the leading covariance; a complete overlap bound makes every other contribution smaller. This extends the earlier report from deterministic phase frequencies to explicit joint moments of the two random counts motivating the Zigzag Conjecture. The band [1/4,3/4] has the positive lower density 1/(1+2^(1/4)) established earlier.

This proves no new concentration bound for chi and makes no literature-novelty claim. Annika Heckel and Oliver Riordan, [*How does the chromatic number of a random graph vary?*, arXiv:2103.14014](https://arxiv.org/html/2103.14014), already discuss approximately Poisson marginal counts; the present piece gives a self-contained joint second-moment estimate on a specified band. The missing relation between these counts and chi is not resolved. Small correlation alone supplies neither independence nor a joint Gaussian law.

Reproduce all checks from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 recheck_earlier.py
OMP_NUM_THREADS=1 nice -n 15 python3 verify_moments.py
OMP_NUM_THREADS=1 nice -n 15 python3 audit_extension.py
```

All final runs passed. The first reproduces the earlier four counts and density constants. The second enumerates all 1024 graphs on five vertices and 32768 on six, and compares exact rational moments with two overlap formulas. The third uses a separate descending recurrence, Decimal inversion, and exact rational checks of the proof's bounds at n approximately 2^320. Runs took 0.051, 3.349 and 20.082 seconds, respectively; peak RSS stayed below 20 MB. The launcher emits a priority diagnostic because nice is already 20; every script verifies actual nice >=15 before computing. Full output is in the three JSON files, with commands and relevant values in LOG.md.

One initial diagnostic failed: a demand for variance relative error below 1e-6 at n approximately 2^160 was unjustified. At phase .75 the actual error is about .0187; at n approximately 2^320 it is 5.108702812850075e-13. The threshold was removed, and no finite uniform cutoff is claimed. [AUDIT.md](AUDIT.md) records hand calculations, endpoint cases and the limitations of the conclusion.

The literature check, under five minutes, found no solution of fixed-p=1/2 concentration. It did find an omission in the earlier summary: Oliver Riordan's Oxford talk, [*Cube-root concentration of the chromatic number of G(n,1/2) – sometimes*, 18 February 2025](https://www.maths.ox.ac.uk/node/70763), announces joint work with Rob Morris giving an O*(n^(1/3)) upper bound for certain n. No paper, arXiv id, precise phase range or proof was located within the search budget; this announcement is not used as a theorem here. Zhifei Yan's opened [*Exponential tails for factors and the chromatic number of random graphs*, arXiv:2609.12700](https://arxiv.org/abs/2609.12700), concerns edge probabilities tending to one. Neither establishes a solution of the present fixed-p problem.

The next worker should obtain the precise statement and proof behind the Morris–Riordan cube-root announcement before attempting a new concentration bound. For the probabilistic route here, the next missing estimate is a conditional relation between chi and the two counts, or their joint law plus a proved sensitivity estimate. The moment calculation alone cannot provide that transfer.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first recorded local clock 01:03:37 +04.

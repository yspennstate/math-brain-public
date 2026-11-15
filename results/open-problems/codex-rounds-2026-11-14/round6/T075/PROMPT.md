# Open problem T075: Absolute continuity of Bernoulli convolutions at transcendental parameters

Statement: For every transcendental λ ∈ (1/2, 1), the Bernoulli convolution ν_λ (the law of Σ_{n≥0} ±λ^n with independent fair signs) is absolutely continuous.

Caveat: It is the form of Erdős's problem that the 2026 Salem counterexamples (T026, retired) leave untouched.

Source: P. Erdős, On a family of symmetric Bernoulli convolutions, Amer. J. Math. 61 (1939); P. P. Varjú, Recent progress on Bernoulli convolutions, in European Congress of Mathematics (EMS, 2018) 847–867

Where it stands (checked by us, Nov 2026): Dimension one for every transcendental λ (Varjú, arXiv:1810.08905, Ann. Math. 2019); absolutely continuous for almost every λ (Solomyak 1995) and outside a set of Hausdorff dimension zero (Shmerkin, arXiv:1303.3992, GAFA 2014); for algebraic λ close to 1 in terms of the Mahler measure (Varjú, arXiv:1602.00261, JAMS 2019; Kittle, arXiv:2103.12684, Ann. Sci. ENS). Kittle–Kogler (arXiv:2610.10511, Oct 2026, not yet refereed) prove the exact overlaps conjecture and its entropy version on the line, which gives the dimension of every Bernoulli convolution; absolute continuity is not covered. Pisot reciprocals (Erdős 1939) and quartic Salem reciprocals (Cheng–Fang–Ma–Zhang, arXiv:2610.12072, Oct 2026) give singular measures. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T075 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T075 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T075 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T075 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PARTIAL proved arbitrarily long small-cap prefixes at singular parameters in (1/2,1); T075 remains open

The earlier conditional L^p result holds. Its multiplier
4c theta/(c-1) was independently re-derived, and its script reproduced
all reported checks. The five-minute literature check found no solution
of T075. Samuel Kittle and Constantin Kogler's
[arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1) still assumes
absolute continuity in its higher-integrability theorem.

The new result strengthens the earlier finite-depth warning, whose
singular example lambda=1/3 lay outside the target interval. For the
same prefix concentration statistic, PROOF.md establishes

    A_n(delta) <= min(1, delta(1-lambda)/2
                        + n(2lambda-1)(1-lambda)/lambda)
               <= min(1, delta/4+n(2lambda-1)).

The proof computes the exact one-step total variation defect of the
uniform law on the support, then uses Markov contraction and telescoping.

Let beta_k be the root in (1,2) of x^k-x^(k-1)-...-x-1 and put
lambda_k=1/beta_k. A self-contained proof shows that nu_(lambda_k) is
singular and 0<2lambda_k-1<2^(-k). Therefore, for any delta/4<theta<1
and any finite N, choosing N*2^(-k)<theta-delta/4 gives

    A_n(delta)<theta for every 0<=n<=N,
    but A_n(delta)->1 as n->infinity.

For delta=1/64 and theta=1/36, the singular parameter lambda_20 passes
every test through depth 25,031. The certified margin below the threshold
is 1/9,437,184. At k=40 the certified depth is 26,247,022,364. These are
analytic certificates, not enumerations of all prefixes at those depths.

Commands, run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T075/check_constants.py > earlier_recheck.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 check_obstruction.py > computation.txt 2>&1
```

Both exited 0. The new script checked 39 exact one-step defects, 72
prefix TV distances, 288 cap inequalities, and 39 rational root brackets
against independent 120-digit Newton calculations. Runtime was 0.717 s;
peak RSS 17,022,976 bytes; one thread; actual priority 20. LOG.md contains
the output and the independent arithmetic and failure-case audit.

What failed: no concentration estimate at unbounded depths for a specified
transcendental parameter was obtained. The construction uses different
algebraic parameters for different finite horizons. It does not refute a
criterion using transcendence or additional arithmetic hypotheses.

Uncertainty: the elementary obstruction is not asserted novel or optimal.
No formal proof verification was run. The literature search was bounded,
and no quantitative time to eventual concentration was established.

Next worker: a propagation lemma must use information beyond a fixed
finite list of small caps uniformly over real parameters. Investigate a
quantitative condition on arithmetic separation across infinitely many
scales that distinguishes a chosen transcendental parameter from these
multinacci controls. The previous conditional L^p theorem remains usable
once its infinite-subsequence hypothesis is proved.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15, first recorded clock 07:57:34 +04:00.

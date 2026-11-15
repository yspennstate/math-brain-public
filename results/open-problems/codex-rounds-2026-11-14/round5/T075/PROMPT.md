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
VERDICT: PARTIAL improved the conditional prefix-concentration L^p criterion from theta<1/18 to theta<1/4; T075 remains open

The earlier concentration criterion holds. Its proof was independently
re-derived, its script passed all original checks, and all twelve reported
prefix caps were independently reproduced with integer coordinates. The
bounded literature check found no solution of T075. Samuel Kittle and
Constantin Kogler's [arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1)
still assumes absolute continuity in its higher-integrability theorem.

The new result is a sharper one-dimensional quantitative implication,
proved in full in PROOF.md. Retain the earlier statistic A_n(delta), the
largest mass on a set of length delta under the n-sign prefix plus a
uniform tail, and put D=2/(1-lambda). If

    liminf_n A_n(delta) < theta < 1/4,   0 < delta <= D,

then nu_lambda is absolutely continuous. For every c>1/(1-4 theta), its
density belongs to L^p for every

    1 < p < 1 + log((c-1)/(4c theta)) / log(4cD/(delta lambda)).

The threshold for this explicit estimate improves from 1/18 to 1/4.
The absolute-continuity conclusion itself already followed from the
earlier qualitative criterion with any theta<1.

For theta<1/12, a simple admissible exponent is

    p = 1 + log(1/(12 theta)) / log(8D/(delta lambda)).

It strictly improves the earlier exponent throughout its range. At the
earlier conditional example lambda=2/3, delta=1/64, theta=1/36, it gives
p=1.130236012180298 instead of 1.065189685675672. Neither number certifies
the required infinite-subsequence bound at that parameter.

The proof replaces the dilation-by-three covering step in the analytic
lemma with a multiplicity-two cover by intervals. It establishes

    F((c/epsilon)t) <= (4c theta/(c-1)) F(t)

for large t. This yields the exponents by layer-cake integration. The
analytic argument is self-contained. No claim of priority over existing
one-dimensional reverse-Hölder estimates is made.

Commands, run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T075/prefix_concentration.py > earlier_recheck.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 check_constants.py > computation.txt 2>&1
```

Both exited 0. The new script checked 4,943 exact interval families,
12 prefix caps, 18 recurrence/exponent cases, and a 1,000-point exponent
comparison. The logarithms agree with independent 60-digit arithmetic.
It ran in 0.125 seconds with peak RSS 21,069,824 bytes, one thread, actual
priority 20. Full commands, output, and failure-case checks are in LOG.md.

What failed: no estimate propagating a concentration bound to unbounded
depths was obtained. A single favorable finite value remains insufficient,
as the singular lambda=1/3 control demonstrates. No specified
transcendental parameter is newly proved absolutely continuous.

Uncertainty: no formal proof verification was run; the constants are not
asserted optimal. The literature check was bounded to five minutes and
does not establish novelty of the analytic sharpening. The proof does
not include the endpoint exponent in its open range.

Next worker: establish A_{n_j}(delta)<=theta<1 along an unbounded sequence
for one specified transcendental lambda. For quantitative integrability,
theta<1/4 now suffices with the displayed exponents. Further improvements
of the covering constants do not remove this missing estimate.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15, first recorded clock 04:37:30 +04:00.

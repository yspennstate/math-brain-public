# Open problem T075: Absolute continuity of Bernoulli convolutions at transcendental parameters

Statement: For every transcendental λ ∈ (1/2, 1), the Bernoulli convolution ν_λ (the law of Σ_{n≥0} ±λ^n with independent fair signs) is absolutely continuous.

Caveat: It is the form of Erdős's problem that the 2026 Salem counterexamples (T026, retired) leave untouched.

Source: P. Erdős, On a family of symmetric Bernoulli convolutions, Amer. J. Math. 61 (1939); P. P. Varjú, Recent progress on Bernoulli convolutions, in European Congress of Mathematics (EMS, 2018) 847–867

Where it stands (checked by us, Nov 2026): Dimension one for every transcendental λ (Varjú, arXiv:1810.08905, Ann. Math. 2019); absolutely continuous for almost every λ (Solomyak 1995) and outside a set of Hausdorff dimension zero (Shmerkin, arXiv:1303.3992, GAFA 2014); for algebraic λ close to 1 in terms of the Mahler measure (Varjú, arXiv:1602.00261, JAMS 2019; Kittle, arXiv:2103.12684, Ann. Sci. ENS). Kittle–Kogler (arXiv:2610.10511, Oct 2026, not yet refereed) prove the exact overlaps conjecture and its entropy version on the line, which gives the dimension of every Bernoulli convolution; absolute continuity is not covered. Pisot reciprocals (Erdős 1939) and quartic Salem reciprocals (Cheng–Fang–Ma–Zhang, arXiv:2610.12072, Oct 2026) give singular measures. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T075 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T075 (read it,
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
VERDICT: PARTIAL proved a finite-prefix concentration criterion with a conditional explicit L^p exponent; T075 remains open

The earlier result holds. Samuel Kittle and Constantin Kogler's [arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1), Theorem 1.1, assumes absolute continuity and concludes higher integrability. The bounded literature update found no subsequent solution of T075. The earlier folder has no PROOF.md or scripts.

The extension is in PROOF.md. Let f_n be the density of the n-sign prefix plus an independent uniform variable on the exact remaining tail interval, and let A_n(delta) be its largest mass on any set of Lebesgue measure at most delta. For every 0<lambda<1,

    nu_lambda is absolutely continuous
    iff liminf_n A_n(delta)<1 for some delta>0.

If nu_lambda is singular, A_n(delta) tends to one for every delta>0. If it is absolutely continuous, sup_n A_n(delta) tends to zero as delta decreases to zero. The proof derives pure type and establishes the useful uniform comparison A_n(delta)<=2 omega_nu(delta), where omega_nu is the small-set mass modulus.

Under the stronger, unproved hypothesis

    liminf_n A_n(delta)<theta<1/18,  0<delta<=D=2/(1-lambda),

the density belongs to L^p for

    p = 1 + log(1/(18 theta))/log(72D/(delta lambda)).

This uses the cited paper's Lemma 2.1 after proving absolute continuity. It does not assume a density in the sufficiency direction. These are elementary reductions beyond the earlier literature-only report; no claim of priority over existing criteria is made.

The exact-rational script computes A_n by sorting the overlaps of prefix intervals. Run:

~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 prefix_concentration.py > computation.txt 2>&1
~~~

It passed 72 independent midpoint/convex-dual comparisons and 112 comparisons with exact formulas at lambda=1/2 and lambda=1/3. Runtime was 1.180 seconds; peak RSS was 28,082,176 bytes; actual priority was 20 and OMP_NUM_THREADS was 1. Full output and the commands are in computation.txt and LOG.md.

What failed: the finite-depth calculations do not establish any infinite-subsequence bound for lambda=2/3 or any transcendental parameter. The singular control lambda=1/3 passes the threshold theta=1/36 at depth 4 but reaches A_14(1/64)=1. A finite favorable value therefore cannot replace the hypothesis. This control lies outside (1/2,1).

Uncertainty: the conditional regularity exponent uses a new preprint's analytic lemma; its level-set constants were independently checked, but no Lean verification or exhaustive literature review was performed. No specified transcendental Bernoulli convolution is newly proved absolutely continuous.

Next worker: prove a bound A_{n_j}(delta)<=theta<1 along an unbounded sequence for one specified transcendental lambda. A bound theta<1/18 also gives the displayed exponent. The exact sweep provides a verification target, but additional finite depths alone will not close the gap. A promising lemma would propagate such a bound to arbitrarily large depths; no such propagation is proved here.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15, first recorded local clock 01:10:23 +04:00.

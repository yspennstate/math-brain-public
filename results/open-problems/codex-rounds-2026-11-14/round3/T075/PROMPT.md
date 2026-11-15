# Open problem T075: Absolute continuity of Bernoulli convolutions at transcendental parameters

Statement: For every transcendental λ ∈ (1/2, 1), the Bernoulli convolution ν_λ (the law of Σ_{n≥0} ±λ^n with independent fair signs) is absolutely continuous.

Caveat: It is the form of Erdős's problem that the 2026 Salem counterexamples (T026, retired) leave untouched.

Source: P. Erdős, On a family of symmetric Bernoulli convolutions, Amer. J. Math. 61 (1939); P. P. Varjú, Recent progress on Bernoulli convolutions, in European Congress of Mathematics (EMS, 2018) 847–867

Where it stands (checked by us, Nov 2026): Dimension one for every transcendental λ (Varjú, arXiv:1810.08905, Ann. Math. 2019); absolutely continuous for almost every λ (Solomyak 1995) and outside a set of Hausdorff dimension zero (Shmerkin, arXiv:1303.3992, GAFA 2014); for algebraic λ close to 1 in terms of the Mahler measure (Varjú, arXiv:1602.00261, JAMS 2019; Kittle, arXiv:2103.12684, Ann. Sci. ENS). Kittle–Kogler (arXiv:2610.10511, Oct 2026, not yet refereed) prove the exact overlaps conjecture and its entropy version on the line, which gives the dimension of every Bernoulli convolution; absolute continuity is not covered. Pisot reciprocals (Erdős 1939) and quartic Salem reciprocals (Cheng–Fang–Ma–Zhang, arXiv:2610.12072, Oct 2026) give singular measures. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T075 (read it,
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
VERDICT: PARTIAL substantial recent regularity advance located; T075 remains unresolved

The literature check found [Samuel Kittle and Constantin Kogler, arXiv:2611.17277v1](https://arxiv.org/abs/2611.17277v1), submitted 12 November 2026, absent from the supplied status. Its precise result and relevance are recorded in SOLVED_ELSEWHERE.md. Step 1's substantial-advance branch is therefore used, with no original research result claimed.

The abstract, HTML theorem, and PDF theorem were checked against each other. Applicability was checked from the first-sign decomposition of the random series and independently from its finite-prefix distributions. The reverse implication in the stated equivalence follows from the meaning of “has a density.” No uniform exponent or implication from dimension one is claimed.

Commands and web queries are recorded in LOG.md. All local Python commands used `OMP_NUM_THREADS=1 nice -n 15 python3`; actual inherited priority was 20. There was no numerical experiment, and no numerical bound is asserted. All writes stayed in this folder.

What failed: the search did not locate a proof of the universal transcendental-parameter assertion. The regularity theorem assumes the property T075 asks to prove. Its algebraic criteria do not fill that gap.

Uncertainty: this was a search lasting less than ten minutes, not an exhaustive literature review or a complete proof audit of the preprint. Publication or referee status was not established. No Lean verification was run.

Next worker: update the status with the new theorem, then examine whether its small-set mass criterion can be established directly for a specified transcendental parameter. Merely knowing dimension one will not supply the missing absolute-continuity assumption.

Task: “push this problem forward by one checkable piece” — 2026-11-14; first recorded local clock 20:52:00 +04:00.

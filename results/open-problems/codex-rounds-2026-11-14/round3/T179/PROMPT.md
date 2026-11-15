# Open problem T179: Uniqueness in law for the stochastic heat equation with non-degenerate Hölder noise coefficient below exponent 2/3

Statement: On the one-dimensional torus T consider ∂_t u = Δu + g(u)Ẇ with Ẇ space-time white noise, where g is uniformly elliptic (|g| bounded away from 0) and globally β-Hölder continuous. Weak uniqueness (uniqueness in law) is known for β > 2/3. Does it hold for every β ∈ (0, 2/3], or at least for β > 1/2?

Caveat: Without ellipticity uniqueness can fail: Mueller, Mytnik and Perkins constructed non-unique solutions for g(x) = |x|^γ with γ < 3/4, as described by Han, so the role of the condition |g| ≥ c > 0 is the whole question. Pathwise uniqueness for β > 3/4, without ellipticity, is due to Mytnik and Perkins. The finite-dimensional analogue (uniqueness in law for SDEs with uniformly elliptic continuous diffusion coefficient, Stroock–Varadhan) suggests that ellipticity alone might give uniqueness for every β > 0, and Han records that no counterexample is known for any β > 0.

Source: Y. Han, Stochastic heat equation with nondegenerate Hölder diffusion coefficient: uniqueness below the three-fourth threshold, arXiv:2608.01279 (2026)

Where it stands (checked by us, Nov 2026): Mytnik and Perkins (Probab. Theory Related Fields 149 (2011) 1–96) proved pathwise uniqueness for β > 3/4. Mueller, Mytnik and Perkins (Ann. Probab. 42 (2014) 2032–2112) gave non-uniqueness, both in law and pathwise, for the non-elliptic coefficient |u|^γ with γ < 3/4. Bass and Perkins proved uniqueness for elliptic coefficients 1/2 + ε-Hölder in an enhanced norm that does not cover pointwise coefficients. Han's generalized coupling method gave weak uniqueness for elliptic g with β > 3/4, and Han (arXiv:2608.01279) lowered this to β > 2/3. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T179 (read it,
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
VERDICT: PARTIAL reduction of the remaining L2-initial-data case to uniform continuity of bounded-start transition laws

The literature has advanced: Yi Han's [arXiv:2611.07310v1](https://arxiv.org/abs/2611.07310),
submitted 5 November 2026, covers every positive Hölder exponent for bounded
initial data, including unbounded diffusion coefficients. It also covers
arbitrary L2 initial data for bounded diffusion. The remaining source-level
corner is unbounded g, initial data in L2 without a spatial bound, and
0<beta<=2/3. See SOLVED_ELSEWHERE.md for exact theorem locations and scope.

PROOF.md gives a sufficient continuity criterion for that corner. Let P_s be
the already unique transition operator from bounded initial functions. If,
for each bounded Lipschitz f, P_s f is uniformly continuous in the L2 distance
on L2 balls, uniformly for s in compact intervals away from zero, then weak
uniqueness extends to every deterministic L2 initial state. The modulus must
be independent of the initial functions' spatial suprema.

The proof establishes positive-time boundedness and the bound
E||U_delta-S_delta u0||_2^2 <= C sqrt(delta) directly from L2 initial data.
It gives explicit comparison bounds (5)-(6), then identifies full path laws
by conditional restart. The root-mean-square exponent 1/4 is sharp already
for constant diffusion.

Checks: the constant-noise variance was derived independently from Fourier
modes and periodized Gaussians. Both give leading constant 1/sqrt(2 pi).
The computation command was:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_heat.py
```

All five comparisons passed; data are in heat_check.csv and full output is
in LOG.md. Peak RSS was 13.89 MiB. The process verified inherited nice=20;
the launcher warning is explained in LOG.md. An initial resource-limit setter
failed before calculation and was removed.

What failed: fixed spatial-cutoff localization at time zero does not extend
to general L2 data. PROOF.md gives an explicit singular initial function with
every fixed cutoff's exit-time infimum equal to zero.

What remains uncertain: the required uniform continuity estimate is unproved.
No uniqueness claim is made for the residual case. The new preprint's theorem
statements were checked, but its entire proof was not independently audited.

Next worker: prove (UC) in PROOF.md, or a bound
|P_s f(v)-P_s f(w)| <= K_(R,a,b,f)||v-w||_2^alpha with any alpha>0,
where K is independent of ||v||_infinity and ||w||_infinity. The reduction
then applies without further initial-time localization.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:19 Asia/Tbilisi.

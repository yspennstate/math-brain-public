# Open problem T179: Uniqueness in law for the stochastic heat equation with non-degenerate Hölder noise coefficient below exponent 2/3

Statement: On the one-dimensional torus T consider ∂_t u = Δu + g(u)Ẇ with Ẇ space-time white noise, where g is uniformly elliptic (|g| bounded away from 0) and globally β-Hölder continuous. Weak uniqueness (uniqueness in law) is known for β > 2/3. Does it hold for every β ∈ (0, 2/3], or at least for β > 1/2?

Caveat: Without ellipticity uniqueness can fail: Mueller, Mytnik and Perkins constructed non-unique solutions for g(x) = |x|^γ with γ < 3/4, as described by Han, so the role of the condition |g| ≥ c > 0 is the whole question. Pathwise uniqueness for β > 3/4, without ellipticity, is due to Mytnik and Perkins. The finite-dimensional analogue (uniqueness in law for SDEs with uniformly elliptic continuous diffusion coefficient, Stroock–Varadhan) suggests that ellipticity alone might give uniqueness for every β > 0, and Han records that no counterexample is known for any β > 0.

Source: Y. Han, Stochastic heat equation with nondegenerate Hölder diffusion coefficient: uniqueness below the three-fourth threshold, arXiv:2608.01279 (2026)

Where it stands (checked by us, Nov 2026): Mytnik and Perkins (Probab. Theory Related Fields 149 (2011) 1–96) proved pathwise uniqueness for β > 3/4. Mueller, Mytnik and Perkins (Ann. Probab. 42 (2014) 2032–2112) gave non-uniqueness, both in law and pathwise, for the non-elliptic coefficient |u|^γ with γ < 3/4. Bass and Perkins proved uniqueness for elliptic coefficients 1/2 + ε-Hölder in an enhanced norm that does not cover pointwise coefficients. Han's generalized coupling method gave weak uniqueness for elliptic g with β > 3/4, and Han (arXiv:2608.01279) lowered this to β > 2/3. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T179 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T179 (read it,
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
VERDICT: PROVED uniform continuity of bounded-start laws and extension of bounded-start uniqueness to every L2 initial state

The earlier reduction checks. The new piece supplies its missing (UC): for
bounded initial states v,w in an L2 ball, and a<=t<=b with a>0,

    |P_t f(v)-P_t f(w)| <= C_(R,a,b) ||v-w||_2^(1/2)

for bounded functions f with L2 Lipschitz constant at most one. The constant
is independent of both initial spatial suprema.

The argument first proves the stronger, exact L1 contraction

    |P_t f(v)-P_t f(w)| <= Lip_L1(f) ||v-w||_1.

Smooth globally Lipschitz coefficient approximations admit synchronous
comparison. Solutions from v and w lie between solutions from min(v,w)
and max(v,w). The enclosing gap is nonnegative and its expected spatial
mass is conserved. This gives the L1 estimate without a bound on the
approximating Lipschitz constants. Uniform positive-time supremum moments
and ||D||_2^2<=||D||_1||D||_infinity give the L2 exponent 1/2.

Consequently weak existence and uniqueness extend to every deterministic
L2 initial state, allowing unbounded globally beta-Hölder g, for all
0<beta<1 with |g|>=c>0. The beta=1 case is the usual Lipschitz theory.
This conclusion uses Yi Han's bounded-start theorem, Proposition 8.1 in
[*Weak uniqueness for the stochastic heat equation with nondegenerate
diffusion: the full Hölder regime*, arXiv:2611.07310v1](https://arxiv.org/html/2611.07310v1),
as an external input. It is an initial-data extension of that theorem;
its proof is not an independent proof or audit of Han's full positive
Hölder theorem. The short literature check found no later resolution of
the residual initial-data case.

PROOF.md contains the approximation, tightness, comparison, martingale
identification and restart details. It closes the rough initial time in
two ways: the L2 modulus gives a restart error O(delta^(1/8)), while
bounded L1-Lipschitz tests give O(delta^(1/4)) directly. Fourier
characteristic functions in the latter class determine the L2-valued laws.

Validation: independently re-derived the earlier reduction, its heat
exponents, and its sharp constant-noise variance coefficient. Audited
signed crossing states, concentrating unit-L2 spikes, and beta near one.
The exact-arithmetic diagnostic was:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_estimates.py
```

It passed all checks, with actual nice=20 and peak RSS 13.67 MiB.
Full output is in LOG.md. The launcher's priority warning reflects the
already inherited nice=20; the script verified priority before computing.
The diagnostic checks arithmetic identities, not stochastic uniqueness.

What failed: a fixed spatial cutoff at time zero still fails for general
L2 data, as in the earlier report. A draft edit failed context matching
and was reapplied; no calculation failed. Neither pathwise uniqueness
nor vector-valued comparison is established. Without bounded-start
uniqueness the approximation argument only selects some limiting law,
so it does not contradict the nonelliptic nonuniqueness examples.

Uncertainty: the external bounded-start theorem has not been audited in
full. No unresolved estimate is assumed in the extension proof itself.
The next worker should independently audit the comparison limit and
martingale identification in PROOF.md. If those check, the natural next
extension is Han's localized Girsanov argument for measurable linear-growth
drift with unbounded diffusion and general L2 initial states.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 01:38 Asia/Tbilisi.

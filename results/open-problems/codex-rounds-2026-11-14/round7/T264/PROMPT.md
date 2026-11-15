# Open problem T264: Tempered overfitting of interpolating ReLU networks in fixed dimension

Statement: Mallinar et al. propose a taxonomy (benign, tempered, catastrophic) of interpolation with noisy labels and conjecture that interpolating ReLU networks in fixed input dimension are tempered: the excess risk stays bounded but does not vanish as n → ∞. For minimum-norm (or GD-trained) interpolating two-layer ReLU networks with inputs in a fixed dimension d ≥ 2 and label noise, determine whether the limiting excess risk is zero, finite and positive, or infinite.

Caveat: For univariate inputs (d = 1) the question is settled: tempered for some losses/norms, catastrophic for others (Kornowski–Yehudai–Shamir; Joshi–Vardi–Srebro).

Source: N. Mallinar et al., Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting, arXiv:2207.06569 (2022); G. Kornowski, G. Yehudai and O. Shamir, arXiv:2305.15141 (2023); N. Joshi, G. Vardi and N. Srebro, arXiv:2307.15396 (2023)

Where it stands (checked by us, Nov 2026): d = 1 settled; d ≥ 2 open as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T264 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T264 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T264 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T264 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 6 worker built on the latest of these. Its folder is ~/codex_op_1114r6/briefs/T264 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece of the round 7 brief below (A or B), a wider special case, a sharper constant,
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





----- round 7 brief -----
# T264 round 7 brief (an agent, 15 Nov 2026; corrected the same day)

Already proved (round 5, REPORT copied in round 6's PROMPT.md): for n iid uniform inputs on S^(d-1), Rademacher labels
and zero regression function, every measurable minimum-norm selection has E[R_n^r] = infinity for every n >= 3 and
r >= (d-1)/2, so E[R_n] = infinity in d = 2 and d = 3. The event used has probability 2^(3-n), so this is not
divergence in probability. Round 6 showed antipodal extra points cancel the blow-up, so the hemisphere geometry matters.
An earlier draft of this brief asked for that iid statement; it is not needed.

Pick ONE and say which in LOG.md first.

A. Lower bound with high probability (not benign). Karhadkar, Sietsema, Needell, Montufar (arXiv:2602.00825) prove
   near-minimal W^{k,p} interpolants of noisy labels keep excess risk >= c > 0 w.h.p. Two-layer ReLU min-norm
   interpolation in d >= 2 minimizes the R-norm of Ongie, Willett, Soudry, Srebro (arXiv:1910.01635). Find the
   inequality that replaces their Sobolev inequality for the R-norm and prove liminf R_n >= c > 0 w.h.p. A proof in
   d = 2 alone is a result. (Upper bounds, i.e. tempered rather than catastrophic in probability, are the other half.)

B. Mean risk for d >= 4. Round 5 leaves E[R_n] open for d >= 4 (its tail exponent (d-1)/2 exceeds 1). Decide it:
   either a second mechanism with a heavier tail, or a proof that E[R_n] < infinity.

Same compute rules as round 6: one thread, nice 15, under 1 GB, 20 minutes a run, no GPU.

----- earlier REPORT.md (round 6) -----
VERDICT: PROVED Exact antipodal four-point minimum-norm ReLU interpolation has bounded positive collision-limit risk.

The preceding all-fixed-n hemisphere result holds. A fresh analytic recheck
and independent scalar verifier recover its localization inequality, correction
construction, risk coefficient 2/d, joint probability 2^(2-n), and critical
moment (d-1)/2. Its infinite expected risks in d=2,3 are unaffected.

The new result solves the precise fourth-point geometry proposed in that report.
Let a=cos(theta/2), b=sin(theta/2), s=sin(theta), and consider

```text
x1=a e1+b e2, x2=a e1-b e2, x3=e2, x4=-e2,
labels=(1,-1,A,B).
```

For every fixed ambient d>=2 and bounded extra labels, every minimum-norm
interpolant has, as theta decreases to zero,

```text
theta Qmin -> 4,
theta ftheta -> 0 uniformly on the unit ball,
R(ftheta) -> [1+(A^2+B^2)/2]/d.
```

Thus the limiting conditional risk is finite and strictly positive: 1/d for
zero extra labels, and 2/d for all four Rademacher extra-label choices.
Unlike the one-hemisphere case, the diverging coefficients cancel in the
function. A close opposite-label pair alone therefore does not force a
theta^-2 population-risk lower bound after further interpolation constraints.

The exact optimizer is unique as a function. Write u=b e1+a e2 and
v=-b e1+a e2. Whenever 0<theta<pi and
A<=1/(2b), B>=-1/(2b), it is

```text
f(x) = (|u.x|-|v.x|)/s + A sigma(v.x)/a + B sigma((-u).x)/a,
Qmin = 4/s + (B-A)/a.
```

The sign conditions hold uniformly over any bounded label set at sufficiently
small angles. The base term equals
sign(x1*x2) min(|x1|/a, |x2|/b). Its bounded pointwise limit outside the
equator is x1 sign(x2). Adding the two correction limits gives
x1 sign(x2)+A sigma(x2)+B sigma(-x2), whose risk is the displayed constant.
The unscaled function does not converge uniformly; the limit is discontinuous
across the equator.

PROOF.md gives every step, the exact finite-angle risk, and its first-order
expansion. The dual certificate has absolute price
min(a|p|,b|q|)/(ab)<=1. Its equality cases force exactly four planar directions,
including when off-plane weights are allowed. The resulting response matrix
fixes all coefficient totals. This proves optimality and uniqueness without
a discretized optimizer. Independent quadrant integration and odd/even
decomposition recover the risk limit.

The model is homogeneous two-layer ReLU regression with objective one half
the sum of squared parameters in both layers, no biases, skips or output
intercept, and unrestricted width or any fixed width m>=4. Test inputs are
uniform on S^(d-1), and risk is measured against zero. The deterministic
antipodal configuration has probability zero under iid continuous sampling.
This theorem does not classify random-design large-sample risk or GD selection.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_prior.py > prior_output.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_antipodal.py > verification_output.txt
```

Both final commands passed. The new verifier checks 109 admissible angle/label
cases, exact continuous pricing, independently recovered multipliers, two
circle integrals, the quadrant formula, and 9,000 signed ambient directions.
Maximum normalized risk discrepancy is 4.64e-10; maximum interpolation error
is 1.82e-12. Direct activation-arc integration also checks the finite limits
at theta=1e-6, with dimensions 2,3,7 and six label pairs. An independent S^2
surface integral checks the ambient normalization. The final run took 0.2533
seconds, peak RSS 16,252,928 bytes, one thread, actual nice 20. The prior
recheck took 0.1913 seconds and 15,548,416 bytes peak RSS. Commands, output,
and audits are recorded in LOG.md; detailed values are in the JSON files.

Attempts to break the result recovered an instructive boundary. Taking
A=1/(2b), B=-1/(2b) with theta<pi/2 removes two atoms and returns exactly the
earlier two-point minimum, including its theta^-2 risk. Those labels grow
without bound, so they do not contradict the bounded-label limit. Crossing
the sign boundary gives a forbidden coefficient sign and a strict gap above
the displayed dual value. Neither the exact formula nor the bounded-label
conclusion was extrapolated beyond its hypotheses.

What failed: the first prior-recheck run used an arbitrary excess-cost
threshold of 8 for a new feasible competitor. Its actual bounded excess cost
is about 16.47. Correcting that audit threshold made the check pass; no earlier
theorem or new optimizer formula changed. The sandbox denied nice's attempted
priority adjustment, but every run checked compliant inherited nice 20 before
computation. No extension mathematical check failed.

The literature check ended within five minutes. No later resolution was found;
the opened primary sources and their distinct settings are recorded in LOG.md.
No SOLVED_ELSEWHERE.md was warranted. The result is new relative to the
predecessor reports; no broader novelty claim is made.

What remains uncertain: whether this cancellation survives fixed perturbations
away from antipodality, the leading optimal cost and risk for generic extras
in opposite separation hemispheres, random-design typical risk, expected risk
in d>=4, biases, and GD. A finite collision-limit risk for this four-point
family is not a tempered-overfitting theorem as n tends to infinity.

Next worker: perturb the fourth location away from -e2, first within the sample
plane, while keeping its separation coordinate negative and labels bounded.
Determine the leading atomic cost and scaled function for each fixed
perturbation, and whether bounded unscaled risk holds on an open set or only
at exact antipodality. The present dual's four isolated equality atoms give
an exact base case; their kink equalities do not justify assuming stability.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 11:34 +04.

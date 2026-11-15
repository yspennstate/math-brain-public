# Open problem T264: Tempered overfitting of interpolating ReLU networks in fixed dimension

Statement: Mallinar et al. propose a taxonomy (benign, tempered, catastrophic) of interpolation with noisy labels and conjecture that interpolating ReLU networks in fixed input dimension are tempered: the excess risk stays bounded but does not vanish as n → ∞. For minimum-norm (or GD-trained) interpolating two-layer ReLU networks with inputs in a fixed dimension d ≥ 2 and label noise, determine whether the limiting excess risk is zero, finite and positive, or infinite.

Caveat: For univariate inputs (d = 1) the question is settled: tempered for some losses/norms, catastrophic for others (Kornowski–Yehudai–Shamir; Joshi–Vardi–Srebro).

Source: N. Mallinar et al., Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting, arXiv:2207.06569 (2022); G. Kornowski, G. Yehudai and O. Shamir, arXiv:2305.15141 (2023); N. Joshi, G. Vardi and N. Srebro, arXiv:2307.15396 (2023)

Where it stands (checked by us, Nov 2026): d = 1 settled; d ≥ 2 open as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T264 (read it,
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
VERDICT: PARTIAL Exact two-sample minimum-norm ReLU risk and moment threshold in fixed dimension.

For two independent uniform points on S^{d-1} with independent Rademacher label noise, `PROOF.md` identifies the exact minimum-parameter-norm homogeneous two-layer ReLU interpolant. The width may be any value at least two. The objective is one half the sum of squared parameters in both layers, with no skip or output intercept.

For opposite labels and sample angle theta <= pi/2, the minimum objective is `2/sin(theta)`, and the conditional squared excess risk is exactly

```text
R_d(theta) = [pi - sin(theta) + theta*cos(theta)] / [pi*d*sin(theta)^2].
```

Thus `R_d(theta) ~ 1/(d*theta^2)` at small separation. The proof gives the obtuse-angle formula as well and proves uniqueness as a function through equality in an explicit dual certificate.

Writing `C_d = Gamma(d/2)/(sqrt(pi)*Gamma((d-1)/2))`, the unconditional risk tail is

```text
P(R > t) ~ C_d / [2*(d-1)*d^((d-1)/2)] * t^(-(d-1)/2).
```

Consequently `E[R^q]` is finite exactly when `q < (d-1)/2`. The mean squared excess risk is infinite in d=2 and d=3, and finite and positive in d>=4. Every sampled network has finite conditional risk almost surely. These statements concern sample size two, not a large-sample limit.

Two exact opposite-label conditional means are

```text
d=4: 3/8 + 1/(3*pi) - 13/(9*pi^2) = 0.334750474578...
d=5: 55/256 = 0.21484375.
```

The same tail coefficient and moment threshold hold when hidden biases are included and penalized in the Euclidean parameter norm. The proof gives an explicit minimizer and elementary pointwise bounds. Separately, homogeneity transfers the homogeneous result to a full-dimensional annulus: `X=rho*U`, `Y=rho*epsilon`, with rho uniform on [1,2]. The input density is bounded above and below on the annulus, label noise is bounded and heteroscedastic, and all risks are multiplied by `7/3`.

The bounded literature search found no complete resolution of the stated fixed-dimension problem. Opened primary sources and their scope are listed in `LOG.md`. In particular, [Park, Blöbaum and Kasiviswanathan, arXiv:2410.06191](https://arxiv.org/html/2410.06191v1) require growing dimension; [El Harzli, Nam, Kuzborskij, Cuenca Grau and Louis, arXiv:2602.13910](https://arxiv.org/html/2602.13910v1) give conditional stability results; and [Li, Shi and Zhou, arXiv:2611.01105](https://arxiv.org/html/2611.01105v1) address noise-free variation-space approximation. No `SOLVED_ELSEWHERE.md` was created.

Reproduction, from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_two_point.py > verification_output.txt
```

The final run passed all assertions in 1.57 seconds, with peak RSS 15,826,944 bytes, one thread, and actual nice value 20. The sandbox denied `nice`'s attempted adjustment; the inherited priority already met the requirement, and the script asserts it. Complete output is in `verification_output.txt` and `LOG.md`; data are in `verification_data.json` and `angle_checks.csv`.

Checks include direct circle integration of the network, separate S^2 surface quadrature, exhaustive planar atomic pricing, direct interpolation, biased pointwise bounds, gamma normalizers checked by a sine-integral recurrence, risk-tail constants, and independent quadrature of both finite conditional means and the radial multiplier. The maximum relative circle-risk discrepancy was 2.87e-9. The linear odd component gives a separate analytic derivation of the singular coefficient.

The first audit failed a 3e-5 tolerance with a coarse three-dimensional quadrature grid. Refining that grid resolved the discrepancy. No mathematical claim was changed to accommodate the failure.

What remains uncertain: whether a close pair still forces comparable global risk after arbitrarily many further interpolation constraints; whether corresponding estimates hold for a full-dimensional design with independent homoscedastic noise and penalized biases; and the relationship to GD-selected interpolants. Infinite mean risk at n=2 supplies no conclusion about convergence in probability, or expected risk, as n tends to infinity. No novelty claim is made for the elementary two-point optimization itself.

The next worker should solve the three-constraint atomic problem for a close opposite-label pair and a third point at a fixed nonzero angle. Determine whether the forced odd linear component persists or is canceled by additional optimal atoms. This tests the precise obstruction to extending the present calculation beyond two observations. Any asymptotic statement should specify whether risk is conditional, averaged over training samples, or controlled in probability.

Task: T264, "push this problem forward by one checkable piece" — 2026-11-14, approximately 21:23 +04.

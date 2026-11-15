# Open problem T265: Benign overfitting of two-layer networks outside the nearly orthogonal regime

Statement: Gradient-descent-trained two-layer networks that interpolate noisy labels are known to generalize near-optimally (benign overfitting) when the dimension d is much larger than the sample size n, so that training points are nearly orthogonal (Frei, Chatterji and Bartlett; Cao, Chen, Belkin and Gu). Determine whether, and for which data distributions, benign overfitting of GD-trained two-layer ReLU networks holds when n ≥ d, for instance for a Gaussian mixture with n/d → infinity.

Caveat: With n ≫ d the near-orthogonality used by all current proofs fails; tempered behaviour is expected in fixed dimension (T264).

Source: S. Frei, N. S. Chatterji and P. L. Bartlett, Benign Overfitting without Linearity, arXiv:2202.05928 (2022); Y. Cao, Z. Chen, M. Belkin and Q. Gu, Benign Overfitting in Two-layer Convolutional Neural Networks, arXiv:2202.06526 (2022); P. L. Bartlett, P. M. Long, G. Lugosi and A. Tsigler, Benign Overfitting in Linear Regression, arXiv:1906.11300 (2019)

Where it stands (checked by us, Nov 2026): Hashimoto (arXiv:2505.16204) proves benign overfitting for fixed-width leaky ReLU two-layer networks trained by gradient descent on mixture data that need not be nearly orthogonal, through directional convergence of the parameters; whether this reaches n ≥ d is to verify. Open for ReLU and for n/d → infinity.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T265 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T265 (read it,
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
VERDICT: PARTIAL explicit Bayes-consistent bias-free ReLU interpolation when n/d diverges; GD selection remains unresolved

The earlier affine obstruction is correct. An independent likelihood derivation recovers its interpolation bound; recheck.py verifies its numerical example and ten exact lower-tail inequalities. The bounded literature check found no verified solution of the main GD/ReLU question. Opened sources and their scope are in [LITERATURE.md](LITERATURE.md).

The new result is an explicit *data-only* interpolation rule for the same noisy Gaussian mixture, in every d>=2. It uses at most 6n+2 bias-free two-layer ReLU neurons and satisfies f_n(X_i)=Y_i exactly. It starts with the sample-mean linear score g_n(x)=(n^{-1}sum_i Y_i X_i)^T x, then adds triangular corrections on pairs of narrow antipodal cones. The conditional population probability that f_n and g_n differ as scores is at most

\[
\frac{2C_s}{n^2},\qquad C_s=\frac1\pi+\frac{s}{\sqrt{2\pi}},
\quad s=\|\mu\|/\sigma.
\]

Let alpha=eta+(1-2eta)Phi(-s), the Bayes classification risk, and V=(d+4eta(1-eta)s^2)/n. For s>0,

\[
\mathbb E R(f_n)-\alpha\le
\sqrt{\frac2\pi}\min\left\{\sqrt V,
\frac{V}{(1-2\eta)s}\right\}+\frac{2C_s}{n^2}.
\]

The square-root bound remains valid at s=0. Thus the rule is Bayes consistent for bounded signal strength when n/d tends to infinity, and has an O(d/n+n^{-2}) excess-risk bound for fixed s>0 and fixed eta<1/2. Combined with the earlier result, this gives a concrete interpolating classifier that differs from every affine classifier on Theta(n) training decisions while disagreeing with its own affine baseline on vanishing population probability. This settles the representational part of the earlier localization target. It does not provide the GD trajectory requested in the main problem.

For the earlier example n=10000,d=20,s=2,eta=0.1, the width bound is 60002, the score-disagreement bound is 2.2323889e-8, and expected excess classification risk is at most 0.00106918764. Bayes risk is 0.11820010556. These are evaluations of proved bounds, not training measurements.

The full proof, including the zero-signal and zero-baseline cases, measurability, exact neuron coefficients, and parameter costs, is in [PROOF.md](PROOF.md). This is an elementary construction; no novelty claim relative to all prior interpolation constructions is made.

Run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Both exited 0. The final construction audit checked 360 exact triangular identities, 139 exact network evaluations, 42 Gaussian density values, six density normalizations, 18 cone-mass bounds, exact sample-mean moments, and 72 baseline-risk cases. Cartesian and polar calculations independently verify the density constant; exact rational arithmetic checks the finite networks and the numerical risk factor. Output is in [LOG.md](LOG.md), [recheck_results.json](recheck_results.json), and [audit_results.json](audit_results.json). Both runs took less than a second, used about 15–16 MB RSS, and verified actual niceness 20 despite the sandbox denying the wrapper's priority adjustment.

What failed: isolated one-sided cones conflict with the shallow network's linear odd part; paired cones are necessary for this construction. Exact projected ray collisions cannot be handled in general, though they occur with probability zero here. A nearly antipodal test originally needed no correction; changed labels forced nonzero corrections and the revised audit passed. No failed mathematical assertion remained. See [AUDIT.md](AUDIT.md).

What remains uncertain: GD selection, fixed-width behavior, norm control, and finite-precision stability. The construction can have enormous path norm; one stress sample reaches about 2.56e26. Nothing here shows that a margin or norm minimizing GD limit chooses these cones. No population squared-loss or minimax-rate claim is made.

Next worker: analyze the implicit objective before attempting a trajectory theorem. Determine whether a maximum-margin or minimum-path-norm bias-free ReLU interpolant can have the required paired-cone localization. Compare its norm against a less localized interpolant; Section 7 supplies exact costs and a lower bound for the constructed corrections. A GD result requires a separate selection or dynamical argument. Existence alone is now verified for this mixture.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 03:40 Asia/Tbilisi.

# Open problem T265: Benign overfitting of two-layer networks outside the nearly orthogonal regime

Statement: Gradient-descent-trained two-layer networks that interpolate noisy labels are known to generalize near-optimally (benign overfitting) when the dimension d is much larger than the sample size n, so that training points are nearly orthogonal (Frei, Chatterji and Bartlett; Cao, Chen, Belkin and Gu). Determine whether, and for which data distributions, benign overfitting of GD-trained two-layer ReLU networks holds when n ≥ d, for instance for a Gaussian mixture with n/d → infinity.

Caveat: With n ≫ d the near-orthogonality used by all current proofs fails; tempered behaviour is expected in fixed dimension (T264).

Source: S. Frei, N. S. Chatterji and P. L. Bartlett, Benign Overfitting without Linearity, arXiv:2202.05928 (2022); Y. Cao, Z. Chen, M. Belkin and Q. Gu, Benign Overfitting in Two-layer Convolutional Neural Networks, arXiv:2202.06526 (2022); P. L. Bartlett, P. M. Long, G. Lugosi and A. Tsigler, Benign Overfitting in Linear Regression, arXiv:1906.11300 (2019)

Where it stands (checked by us, Nov 2026): Hashimoto (arXiv:2505.16204) proves benign overfitting for fixed-width leaky ReLU two-layer networks trained by gradient descent on mixture data that need not be nearly orthogonal, through directional convergence of the parameters; whether this reaches n ≥ d is to verify. Open for ReLU and for n/d → infinity.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T265 (read it,
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
VERDICT: PARTIAL quantitative obstruction to interpolating linear-boundary network limits when n/d diverges

The main ReLU/GD benign-overfitting question remains open in this work. A complete elementary reduction is proved in [PROOF.md](PROOF.md): for iid binary data with Bayes error `alpha`,

\[
 \Pr\{\text{some affine classifier makes at most }k\text{ training errors}\}
 \le \min\left\{1,
 2\sum_{j=0}^{\min(d,n-1)}{n-1\choose j}
 \Pr\{\operatorname{Bin}(n,\alpha)\le k\}\right\}.
\]

For `X=S mu+sigma G` with balanced `S`, isotropic standard Gaussian `G`, and independent label flips of probability `eta<1/2`, the error parameter is exactly
`alpha=eta+(1-2eta)Phi(-||mu||/sigma)`.

Consequently, if `n/d -> infinity` and `alpha` stays positive, every affine classifier misses at least `(alpha-o(1))n` training labels with high probability. Every interpolating network must differ from every affine classifier on at least that many training decisions. This excludes positive-margin network limits with linear decision boundaries, regardless of width. Without label flips, affine interpolation is also excluded when `s^2 <= (2-epsilon)log(n/d)` eventually, for fixed `epsilon>0` and `s=||mu||/sigma`. This is an obstruction below that scale, not a sharp threshold.

Example: `n=10000,d=20,s=2,eta=0.1` gives `alpha=0.1182001056` and affine-interpolation probability at most `exp(-1115.3559)`. The finite 99% confidence lower bound on every affine classifier's training error fraction is `0.0324240892`.

The literature check took under five minutes. [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) records the opened sources, including why Hashimoto's probabilistic sufficient conditions exclude a diverging sample/dimension ratio. It also records a concrete rank/trace defect in another paper's claimed NTK eigenvalue bound. No verified solution of the whole problem was identified.

Validation command, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

The guarded run exited 0. It verified 34 exact prediction counts, 2,482 polynomial certificates, 36 fixed-noise tail bounds, six variable-posterior bounds, and three unconditional iid bounds by enumerating 32,768 joint samples. Gaussian tail integrals and large counts were calculated by independent methods. Data are in [audit_results.json](audit_results.json); output and commands are in [LOG.md](LOG.md); limitations and attempted counterexamples are in [AUDIT.md](AUDIT.md). Actual niceness was 20 and peak memory about 17 MB. The sandbox denied `nice`'s adjustment, but inherited priority met the requirement; the script checks priority before computing. An initial `/usr/bin/time -l` wrapper exited 1 because its resource query was denied, after the mathematical checks completed.

What this does not prove: failure or success of benign overfitting by nonlinear ReLU networks; interpolation impossibility at arbitrarily strong signal without flips; exclusion of directional limits with zero margins. The counting/noise argument is a standard elementary capacity argument, not a claimed new general learning principle. It identifies a quantitative obstruction relevant to this problem.

Next worker: study nonlinear limits rather than extending a positive-margin linear-boundary conclusion into the fixed-noise regime. A concrete remaining target is a Gaussian-mixture ReLU/GD trajectory whose final classifier differs from every affine classifier on `Theta(n)` training points, while those additional decisions occupy vanishing population probability. Proving or disproving this localization would address what the present reduction leaves open.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 21:26 Asia/Tbilisi.

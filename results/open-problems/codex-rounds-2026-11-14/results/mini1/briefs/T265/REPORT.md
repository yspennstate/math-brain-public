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

# fleet03/B08 — full baseline reread plus threshold-reduction audit

Run: `20260924T131732Z-fleet03-B08-fixedmult-audit-r56`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Verdict: **PASS on this continuation reread of the 17-eigenvalue manuscript; no new fatal gap found.** This is not a second independent reviewer identity relative to this worker's earlier B08 audit. The unrestricted three-eigenvalue conjecture remains open.

## What was reread

I reread the full 790-line source in contiguous chunks, including:

- theorem/scaling and exact quantifiers;
- Gaussian regularization, Fourier inversion and negative-half-potential identity;
- singular-value perturbation and the principal-Schur spectral count;
- the heat-flow proof of the geometric rank-one Brascamp--Lieb inequality;
- product projection densities and integrated Fourier powers;
- cross-block decoupling and the regularized determinant estimate;
- scalar, definite-pair and indefinite hyperbolic pivot estimates;
- quarter-power concentration and logarithmic potential;
- all definitions and proofs in the disjoint-minor/interpolation section;
- the random-cut conversion, no-pivot consequences, pivot compiler, normalized main theorem and scaling back to general `K,s`.

No step in this reread introduced rotated independence, moments, bounded support, log-concavity, or a pointwise law-uniform van-der-Corput estimate.

## B08 focus: nonsymmetric interpolation and both rank bounds

For a sampled disjoint seed `S,T` of size `r`, with `B=A[S,T]` and `L=(S union T)^c`, the source defines
\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot}.
\]
The two exact interpolation identities are
\[
P_{S,\cdot}=A_{S,\cdot},\qquad P_{\cdot,T}=A_{\cdot,T}.
\]
After putting the off-diagonal residual on `L x L` into `E` and the diagonal residual into `D`, one has
\[
A=D+R+E,
\qquad R_{L,L}=P_{L,L}.
\]
Hence
\[
\operatorname{rank}R_{L,L}\le r.
\]
Furthermore `R-P` vanishes on rows `S`, columns `T`, and all of `L x L`; every remaining entry has its row in `T` or its column in `S`. Splitting these two supports gives rank at most `r+r`, and therefore
\[
\operatorname{rank}R\le\operatorname{rank}P+2r\le3r.
\]
The proof uses these as genuinely different bounds. At a bad ratio, rank perturbation first spends `3r` globally to force `r+1` large entries of `D`; because `D` vanishes on `S union T`, those entries lie in `L`; strict diagonal dominance then produces an `(r+1)`-rank submatrix of `R_{L,L}`, contradicting the **restricted** rank `r`. I again find this logic correct. The fact that `R,E,P` can be nonsymmetric is harmless because the perturbation step is explicitly stated for singular values of general real matrices.

The exact normal-form analysis of fleet01/B08 additionally shows that the `3r` and `r` ranks are simultaneously support-sharp inside the no-pivot entry class, so simply replacing either rank count by a smaller number is not a valid threshold reduction.

## Source package status changed since the earlier B08 audit

The reproducibility gap noted in the earlier B08 report has been repaired. On the current master I found and read:

- `SOURCE_MANIFEST.json`, pinning the unchanged 47,883-byte / 790-line source and its SHA-256;
- `verify.py`, which checks the source hash before running exact symbolic interpolation/rank/volume assertions and separate floating diagnostics;
- `checks.json`, reporting `PASS` for 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict sampling cases, 240 numerical Schur-threshold cases and 30 graph-weight cases;
- `proof_map.csv` is again present in the root listing.

The manifest correctly states that this is a new reproducibility suite, not formal verification and not a recreation of the historical self-audit counts. I agree with that scope. These finite checks support the algebra but are not used as a substitute for the written proof.

## Threshold update from this run

The sibling improvement report

`improvements/fleet03/B08/20260924T131732Z-fleet03-B08-fixedmult-audit-r56/S8_MULTI_DELETE_RIGIDITY.md`

proves a new reduction for the first unresolved `s_8` chamber. In particular, every one- or two-coordinate deletion child retains at least six or four unit-scale singular directions respectively. Applying the completed fleet04/B08 affine-uniform child-window result after conditioning on any finite set of original coordinates gives `<64` and a `C_0` density whenever any such child has a diffuse `1/64` spectral window. If all these gates fail, a spectral-variance identity converts the repeated leverage witnesses into three nested physical off-diagonal stars, each of norm greater than
\[
\frac9{6400\sqrt2}s
=0.0009943689110435824\ldots\,s.
\]
Combined with the previous B08 `r=2` interpolation-saturation theorem, this strictly narrows the remaining `s_8` endpoint but does not close it.

## Status

- Baseline 17-eigenvalue theorem: **PASS in this continuation reread; source unchanged.**
- Previously reconstructed 9-eigenvalue candidate: **still supported by this worker's earlier proof reconstruction; independent-review gate is a separate fleet-level status.**
- New 8-eigenvalue theorem: **NOT PROVED.**
- Full three-eigenvalue conjecture: **OPEN.**
- Full-target continuity: **OPEN.**

No public release or theorem-status promotion is asserted here.

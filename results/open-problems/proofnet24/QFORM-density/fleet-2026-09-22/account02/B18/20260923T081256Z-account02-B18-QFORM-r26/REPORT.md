# account02/B18 — QFORM literature-to-proof transfer r26

## Status

**Full target remains OPEN.** No counterexample is produced. This report proves a target-valid whole-line density estimate in the diffuse residual Schur-isotropic regime and, at the same time, isolates a quantitative obstruction showing that the pinned single-cut 3-volume theorem cannot by itself be shear-uniform.

Claim label: `QFORM-SHEAR-CROSSVOLUME-MSS-BARRIER-v1`.

Target: independent real inputs with one-dimensional densities bounded by 1; real symmetric physical matrix with at least three eigenvalues of modulus at least 1. No moments, support bounds, log-concavity, spectral-coordinate independence, or continuity assumption is introduced.

First unpaid implication after this result: `QFORM-NONPLANAR-ONEPLUS2-AGGREGATE-v1` — derive an original-coordinate/product-preserving asymmetric 1+2 estimate that spends the full residual Pluecker mass and sees the scale `r^2 |det D|`, not the squared-determinant scale of a single 3-volume cut.

## Canonical Schur-isotropic setup

Work in the exact-rank-three Schur-isotropic branch already established by the live QFORM proof network:

\[
Q=(Y+r nX_0)^T D(Y+r nX_0),\qquad Y=V^T X_R,
\]
with `D` real symmetric nonsingular `3 x 3`, `V^T V=I_3`, `||n||=1`, and
\[
n^T Dn=0.
\]
Write the physical coefficient rows as
\[
u_0=rn,\qquad u_j=v_j\quad(j\in R),
\]
so that the physical quadratic-form matrix is
\[
A=UDU^T,
\]
where `U` has rows `u_i` and
\[
U^TU=I_3+r^2nn^T.
\]
Assume the three nonzero eigenvalues of `A` all have modulus at least `s>0`.

## Lemma 1: spectral-product ledger

The three nonzero eigenvalues of `UDU^T` equal the eigenvalues of the nonzero compression, so their product in modulus is
\[
|\det_{\ne0}A|=|\det D|\det(U^TU)=|\det D|(1+r^2).
\]
Hence
\[
\boxed{|\det D|(1+r^2)\ge s^3.}
\]
For the normalized target `s=1`, this reads `|det D|(1+r^2)>=1`.

## Lemma 2: exact cross-volume factorization

For any disjoint physical coordinate sets `I,J`, let
\[
M=A_{IJ}=U_IDU_J^T,
\]
and define the pinned e5f cross-volume
\[
Z=e_3(M^TM)=\sum_{|S|=|T|=3}\det(M_{S,T})^2,
\]
where `S subset I`, `T subset J`.

For each `S,T`, since all matrices in the determinant are `3 x 3`,
\[
\det(M_{S,T})=\det(U_S)\det(D)\det(U_T).
\]
Therefore the sum of squared minors factors, and Cauchy–Binet gives
\[
\boxed{
Z=|\det D|^2\det(G_I)\det(G_J),
}
\]
where
\[
G_I=U_I^TU_I,\qquad G_J=U_J^TU_J.
\]
This identity is purely in the original physical coordinates.

## Primary-source transfer: MSS Corollary 1.5

Marcus–Spielman–Srivastava, *Interlacing Families II: Mixed characteristic polynomials and the Kadison–Singer problem*, Annals of Mathematics 182 (2015), 327–350, Corollary 1.5, states: if vectors `u_i` satisfy
\[
\sum_i u_iu_i^*=I,\qquad \|u_i\|^2\le\delta,
\]
then for every positive integer `q` there is a partition into `q` sets such that each partial Gram operator has norm at most
\[
(1/\sqrt q+\sqrt\delta)^2.
\]
This is a deterministic vector-partition theorem; it has no probabilistic input-law assumptions. DOI: 10.4007/annals.2015.182.1.8.

Apply it with `q=2` to the residual Parseval frame `{v_j}`. Let
\[
\delta:=\max_j\|v_j\|^2\le 1/18.
\]
There is a partition `R=S disjoint_union T` for which
\[
G_S:=\sum_{j\in S}v_jv_j^T\le(1/\sqrt2+\sqrt\delta)^2I.
\]
Because `G_T=I-G_S`, and symmetrically the same upper bound holds for `G_T`, both blocks satisfy
\[
G_S,G_T\ge c_\delta I,
\qquad
c_\delta:=1-(1/\sqrt2+\sqrt\delta)^2
=\frac12-\sqrt{2\delta}-\delta.
\]
At `delta=1/18`, `c_delta=1/9`.

This consumes the completed partner result account03/B18 r25 (`QFORM-MSS-VOLUME-STABILITY-1OVER18-v1`) with its primary-source hypotheses checked exactly.

## Theorem: diffuse MSS cut + pinned e5f Theorem D

Take the physical cut
\[
I=S,\qquad J=\{0\}\cup T.
\]
The row-side volume-sampling marginal required by pinned e5f Theorem D is
\[
\alpha_i=v_i^TG_S^{-1}v_i.
\]
Since `G_S >= c_delta I`,
\[
\alpha_i\le \frac{\|v_i\|^2}{c_\delta}
\le\frac{\delta}{c_\delta}.
\]
For `delta<=1/18`, `delta/c_delta<=1/2`, exactly matching the theorem's row-marginal hypothesis. No condition is needed on the `J`-side marginals.

Moreover
\[
G_J=G_T+r^2nn^T.
\]
By the matrix determinant lemma,
\[
\det G_J=\det G_T\bigl(1+r^2n^TG_T^{-1}n\bigr).
\]
Because `G_T<=I`, one has `G_T^{-1}>=I`; because `G_T>=c_delta I`, one has `det G_T>=c_delta^3`. Hence
\[
\det G_J\ge c_\delta^3(1+r^2),
\qquad
\det G_S\ge c_\delta^3.
\]
The exact cross-volume factorization therefore gives
\[
\boxed{
Z\ge |\det D|^2c_\delta^6(1+r^2).
}
\]

Pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, Theorem D states that under the row marginal condition,
\[
\|p_Q\|_\infty\le6\sqrt e\,Z^{-1/6}.
\]
Substitution yields
\[
\|p_Q\|_\infty
\le
\frac{6\sqrt e}{c_\delta}
|\det D|^{-1/3}(1+r^2)^{-1/6}.
\]
Using the spectral-product ledger `|det D| >= s^3/(1+r^2)`,
\[
\boxed{
\|p_Q\|_\infty
\le
\frac{6\sqrt e}{s\,c_\delta}(1+r^2)^{1/6}.
}
\]
At the clean threshold `delta<=1/18`,
\[
\boxed{
\|p_Q\|_\infty
\le
54\sqrt e\,s^{-1}(1+r^2)^{1/6}.
}
\]
This is a genuine whole-line essential-density estimate for arbitrary cap-one product inputs in the diffuse residual branch. It does **not** assert continuity.

## Real obstruction: one pinned 3-volume cut cannot remove the shear exponent

The preceding growth is not merely a poor lower bound on `G_S,G_T`; it is forced by the scale visible to pinned Theorem D.

For every disjoint physical cut, if neither side contains the hub then `G_I,G_J<=I`, so
\[
Z\le|\det D|^2.
\]
If one side, say `J`, contains the hub, then `G_I<=I` and
\[
G_J\le I+r^2nn^T,
\]
so
\[
Z\le|\det D|^2(1+r^2).
\]
For a normalized exact-spectrum family with
\[
|\det_{\ne0}A|=1,
\]
we have `|det D|=(1+r^2)^{-1}`. Consequently every hub cut obeys
\[
Z\le(1+r^2)^{-1},
\]
and every residual-only cut obeys
\[
Z\le(1+r^2)^{-2}.
\]
Thus the **certificate** `6 sqrt(e) Z^{-1/6}` from a single Theorem-D cut necessarily carries at least a `(1+r^2)^{1/6}` factor on the best possible hub cut (and `(1+r^2)^{1/3}` on a residual-only cut). This is a method obstruction only: it is not a lower bound on the true density and is not a QFORM counterexample.

## Stress test: circular Parseval frame

For the previous B18 circular frame
\[
v_j=
\left(m^{-1/2},\sqrt{2/m}\cos(2\pi j/m),\sqrt{2/m}\sin(2\pi j/m)\right),
\]
one has `V^TV=I_3` and `delta=3/m`. Hence for `m>=54`, the theorem applies. In the normalized Schur-isotropic family whose nonzero spectrum is exactly `{-1,1,1}`,
\[
\boxed{
\|p_Q\|_\infty\le54\sqrt e\,(1+r^2)^{1/6}.
}
\]
The same circular family has no dimension-free exact two-plane bank, so this result genuinely spends nonplanar aggregate volume. It also exhibits why a single 3-volume cut is the wrong final large-shear mechanism.

## Source and correction ledger

- Pinned internal source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, Theorem D, exact constant `6 sqrt(e)` and row volume-marginal threshold `1/2`.
- Pinned companion reports read: `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`; neither supplies a full counterexample, and both warn that pure cross-volume mechanisms degrade in shear/star-like regimes.
- Completed partner consumed: account03/B18 r25, `QFORM-MSS-VOLUME-STABILITY-1OVER18-v1`.
- Primary source checked: Marcus–Spielman–Srivastava, Annals of Mathematics 182 (2015), Corollary 1.5, DOI 10.4007/annals.2015.182.1.8.
- Live corrections respected: no post-rotation independence; no substitution of conditional caps for independence; no generic bounded joint-density/two-sheet trace shortcut; no assumption that diffuse geometry supplies an exact two-plane bank.

## Consequence and next mechanism

`QFORM-SHEAR-CROSSVOLUME-MSS-BARRIER-v1` is proved within the stated Schur-isotropic exact-rank-three branch. It closes bounded-shear diffuse survivors quantitatively and converts the nonplanar Pluecker mass into a real whole-line density inequality. It simultaneously proves that repeating a single-cut Theorem-D cross-volume argument cannot be the shear-uniform endpoint.

The next mechanism must be asymmetric. The exact unpaid implication is:

`QFORM-NONPLANAR-ONEPLUS2-AGGREGATE-v1`: from the residual Parseval identity
\[
\sum_{i<j}\det(n,v_i,v_j)^2=1,
\]
build an original-coordinate/product-preserving 1+2 aggregate estimate which retains a coefficient scale comparable to `r^2 |det D|`. The circular frame is the required stress test. This must be proved before conditioning destroys the product provenance.

Full-problem status change: `OPEN -> OPEN`.
Independent end-to-end review: false.
Execution mode: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no native learned-memory receiver use occurred).

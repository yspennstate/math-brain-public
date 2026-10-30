# Improvement attempt: a single full-row-rank physical cross bank gives direct density smoothing

Run: `20260924T120640Z-fleet01-B01-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript source: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved supporting theorem; no multiplicity reduction claimed.**

## Theorem

Let `I,J` be disjoint sets of original independent coordinates whose densities are bounded by one. Put `d=|I|>=3`. Let `M` be a real `d x |J|` matrix of full row rank and define

`Delta = det(M M^T)>0`.

For arbitrary real measurable functions `F(X_I), G(X_J)` that are finite almost surely, consider

`Z = F(X_I) + 2 X_I^T M X_J + G(X_J)`.

Arbitrary affine terms on either bank are included by absorbing them into `F,G`. Then for every real `t`,

\[
\boxed{
 |\phi_Z(t)|
 \le
 \min\left\{1,\;\pi^{d/2}e^{d/4}\Delta^{-1/4}|t|^{-d/2}\right\}.
}
\tag{1}
\]

Consequently `Z` has a bounded continuous density and

\[
\boxed{
 \|p_Z\|_\infty
 \le
 \frac{d}{d-2}\sqrt e\,\Delta^{-1/(2d)}.
}
\tag{2}
\]

For `d=3`,

\[
 \|p_Z\|_\infty\le3\sqrt e\,\Delta^{-1/6}.
\]

If `M` is square `3 x 3`, this becomes

\[
 \|p_Z\|_\infty\le3\sqrt e\,|\det M|^{-1/3}.
\]

The proof preserves original-coordinate independence and permits completely arbitrary same-bank quadratic curvature or other measurable phases in `F,G`.

## Proof

For fixed `t`, define on `R^d`

\[
 h_t(x)=\left(\prod_{i\in I}f_i(x_i)\right)e^{itF(x)}.
\]

Then

\[
 \|h_t\|_2^2
 =\prod_{i\in I}\int f_i(x)^2\,dx
 \le\prod_{i\in I}\int f_i(x)\,dx=1,
\tag{3}
\]

because `0<=f_i<=1`.

Let `L=M X_J`. Since `M` has full row rank, set

\[
 U=M^T(MM^T)^{-1/2}.
\]

Then `U^TU=I_d` and

\[
 L=(MM^T)^{1/2}U^TX_J.
\]

The product-projection lemma proved in the baseline manuscript gives a density for `U^TX_J` bounded by `e^{d/2}`. The linear Jacobian therefore gives a density `p_L` satisfying

\[
 \|p_L\|_\infty
 \le \frac{e^{d/2}}{\sqrt{\det(MM^T)}}
 =e^{d/2}\Delta^{-1/2}.
\tag{4}
\]

Integrating first in the `I`-coordinates gives

\[
 \phi_Z(t)
 =\mathbb E_{X_J}\left[e^{itG(X_J)}\widehat h_t(2tMX_J)\right].
\]

Condition on `L=MX_J`. A regular conditional expectation produces a measurable factor `a_t(l)` with `|a_t(l)|<=1` such that

\[
 \phi_Z(t)=\int a_t(l)\widehat h_t(2tl)p_L(l)\,dl.
\]

Hence, by Cauchy--Schwarz with respect to the probability density `p_L`, then (4),

\[
\begin{aligned}
 |\phi_Z(t)|^2
 &\le \int |\widehat h_t(2tl)|^2p_L(l)\,dl\\
 &\le e^{d/2}\Delta^{-1/2}
       \int |\widehat h_t(2tl)|^2\,dl.
\end{aligned}
\tag{5}
\]

With the manuscript Fourier convention, `d`-dimensional Plancherel is

\[
 \int_{\mathbb R^d}|\widehat h_t(\xi)|^2\,d\xi
 =(2\pi)^d\int|h_t(x)|^2\,dx.
\]

Changing variables `xi=2t l` in (5) and using (3) gives, for `t!=0`,

\[
\begin{aligned}
 |\phi_Z(t)|^2
 &\le e^{d/2}\Delta^{-1/2}(2|t|)^{-d}(2\pi)^d\\
 &=e^{d/2}\Delta^{-1/2}\pi^d|t|^{-d}.
\end{aligned}
\]

Taking square roots and adjoining the trivial bound `|phi_Z|<=1` proves (1).

Write `p=d/2>1` and

\[
 a=\pi\sqrt e\,\Delta^{-1/(2d)}.
\]

Then the second term in (1) is exactly `(a/|t|)^p`. The power-envelope lemma proved in the baseline manuscript therefore yields

\[
 \|p_Z\|_\infty
 \le\frac{ap}{\pi(p-1)}
 =\frac d{d-2}\sqrt e\,\Delta^{-1/(2d)},
\]

which is (2). Since (1) is integrable for `d>=3`, Fourier inversion also gives continuity of this density. QED.

## Relation to the 17-eigenvalue threshold

This theorem is analytically stronger than the baseline determinant receiver when a **single quantitatively nondegenerate physical cross bank** of row rank at least three is already available: it gives `|t|^{-d/2}` directly, while allowing arbitrary same-bank phases.

It does **not** by itself lower the fixed-multiplicity theorem from 17. The baseline no-pivot argument supplies a lower bound on an aggregate order-five crossing volume, not a dimension-free lower bound on one specified `3 x 3` or `4 x 4` minor. Passing from the aggregate to a single minor can lose a dimension-dependent combinatorial factor, which is forbidden in the target theorem.

The terminal `s_16`, `r=4` interpolation chamber makes the obstruction explicit. On a saturated four-set `H` in the seed complement,

\[
 P_{H,H}=A_{H,T}B^{-1}A_{S,H},
\]

so, when the square factors are invertible,

\[
 \det P_{H,H}
 =\frac{\det A_{H,T}\,\det A_{S,H}}{\det B}.
\tag{6}
\]

Diagonal dominance of `P_{H,H}` forces the two physical cross factors to be invertible, but (6) gives no uniform lower bound on either determinant because the sampled seed determinant `det B` can be arbitrarily small. Thus the new Plancherel receiver does not close `17 -> 16` without an additional quantitative structural lemma.

## Next exact obligation

A genuine threshold reduction can use this theorem if one proves, under the full no-pivot `s_m(A)>=1` hypotheses with `m<17`, a dimension-free lower bound on `det(MM^T)` for some original-coordinate cross bank `M` of row rank at least three, or an aggregate version of the same Plancherel mechanism that does not select a single minor. Otherwise the remaining terminal problem is still the `r=4` saturation chamber / order-four endpoint.

No Gaussianity, moments, bounded support, log-concavity, diagonal structure, exact-rank assumption, or rotated-coordinate independence has been added.

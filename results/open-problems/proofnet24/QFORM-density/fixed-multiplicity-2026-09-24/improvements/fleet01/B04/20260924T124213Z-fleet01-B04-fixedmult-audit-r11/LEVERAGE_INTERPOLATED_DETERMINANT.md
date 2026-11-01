# Leverage-interpolated geometric determinant bound

Run: `20260924T124213Z-fleet01-B04-fixedmult-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved supporting theorem and conditional lower-multiplicity branches; no unconditional reduction below 17 is claimed.**

The argument continuously interpolates between the manuscript's fourth-power determinant proof and the second-power leverage-half proof. Its value is that order four becomes directly invertible for every physical crossing whose maximum row leverage is bounded by any fixed constant strictly below one; order three becomes directly invertible for every crossing with maximum row leverage strictly below `3/4`.

## Theorem 1 — q-interpolated determinant inequality

Let

\[
Z=F(X_I)+2X_I^TMX_J+G(X_J),
\]

where `I,J` are disjoint original-coordinate banks, all coordinates are independent and have densities bounded by one, and `F,G` are arbitrary real measurable functions finite almost surely. Write the physical rows of `M` as `m_i^T`. Define

\[
\ell_i=m_i^T(M^TM)^\dagger m_i,
\]

with `ell_i=0` for a zero row, and put `h=max_i ell_i`. These are the diagonal entries of the orthogonal projection `M(M^TM)^dagger M^T`, hence `0<=ell_i<=1`.

For any

\[
1\le q\le2,\qquad h\le q/2,
\]

one has, for every real `t`,

\[
\boxed{
|\phi_Z(t)|
\le
\det\!\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/(4q)}.
}
\tag{1}
\]

No within-bank quadratic terms or affine terms are removed, and no rotated random coordinates are declared independent.

### Proof

The manuscript's second-power decoupling inequality is

\[
|\phi_Z(t)|^2\le \mathbb E_D\prod_i
|\widehat f_i(2t(MD)_i)|,
\tag{2}
\]

where the coordinates of `D=X_J-X'_J` are independent with densities bounded by one. For `q>=1`, convexity gives

\[
|\phi_Z(t)|^{2q}
\le
\mathbb E_D\prod_i
|\widehat f_i(2t(MD)_i)|^q.
\tag{3}
\]

Set `a=2t` and

\[
\alpha=(2\pi e)^2\frac{2}{q},\qquad
H=\alpha I+a^2M^TM.
\]

As in the manuscript define

\[
c_j=\alpha e_j^TH^{-1}e_j,
\qquad
d_i=a^2m_i^TH^{-1}m_i.
\]

The vectors `sqrt(alpha)H^{-1/2}e_j` and `aH^{-1/2}m_i` form the same exact geometric rank-one frame. Moreover

\[
d_i\le \ell_i\le q/2.
\tag{4}
\]

To verify the first inequality even when `M` is rank deficient, diagonalize `G=M^TM`. Every row vector `m_i`, viewed as a column, lies in `range(G)`. On an eigendirection of positive eigenvalue `lambda`,

\[
\frac{a^2}{\alpha+a^2\lambda}\le\frac1\lambda,
\]

and summing the squared components proves (4).

Apply the geometric Brascamp--Lieb theorem to the integral in (3). The coordinate-density factors are identical to those in the manuscript. For a row factor use

\[
h_i(u)=|\widehat f_i(u)|^q.
\]

Because `d_i<=q/2`, the needed scalar Fourier exponent is `q/d_i>=2`. The manuscript's scalar Fourier-power lemma yields

\[
\|h_i\|_{1/d_i}
=
\left(\int|\widehat f_i(u)|^{q/d_i}\,du\right)^{d_i}
\le
\left(2\pi\sqrt{\frac{2e d_i}{q}}\right)^{d_i}.
\tag{5}
\]

The `d_i^{d_i/2}` in (5) cancels the row Jacobian `d_i^{-d_i/2}`. If `theta=sum_i d_i=sum_j(1-c_j)`, the coordinate entropy factor is at most `e^{theta/2}`. Hence the residual scalar factor is

\[
\left(2\pi\sqrt{\frac{2e}{q}}\right)^\theta e^{\theta/2}
=
\left(2\pi e\sqrt{\frac2q}\right)^\theta
=\alpha^{\theta/2}.
\]

This exactly cancels the `alpha^{-theta/2}` left after factoring `alpha^d` from `det H`. Therefore (3) is at most

\[
\det\left(I+\frac{a^2}{\alpha}M^TM\right)^{-1/2}.
\]

Taking the `2q`-th root and using

\[
\frac{a^2}{\alpha}
=
\frac{q t^2}{2\pi^2e^2}
\]

proves (1). QED.

## Corollary 2 — leverage-sensitive crossing-volume density bound

Let `Z_k(M)>0`. Under the hypotheses of Theorem 1,

\[
|\phi_Z(t)|
\le
\min\left\{1,
\left(\frac{u_{k,q}}{|t|}\right)^{k/(2q)}
\right\},
\qquad
u_{k,q}=\pi e\sqrt{\frac2q}\,Z_k(M)^{-1/(2k)}.
\tag{6}
\]

Indeed, retain the order-`k` coefficient in the determinant expansion. If `q<k/2`, the exponent `k/(2q)` exceeds one and Fourier inversion plus the manuscript's power-envelope lemma gives

\[
\boxed{
\|p_Z\|_\infty
\le
e\sqrt{\frac2q}\,\frac{k}{k-2q}
Z_k(M)^{-1/(2k)}.
}
\tag{7}
\]

The density is continuous because the majorant in (6) is integrable.

A convenient formulation in terms of the actual maximum physical row leverage is obtained by setting

\[
\bar h=\max\{1/2,h\},\qquad q=2\bar h.
\]

Whenever `4\bar h<k`,

\[
\boxed{
\|p_Z\|_\infty
\le
\frac{e k}{\sqrt{\bar h}\,(k-4\bar h)}
Z_k(M)^{-1/(2k)}.
}
\tag{8}
\]

This formula recovers the manuscript's leverage-free `k=5` constant at `h=1`: it gives `5e Z_5^{-1/10}`. At `h<=1/2`, `k=3`, it gives `3sqrt(2)e Z_3^{-1/6}`.

## Corollary 3 — conditional thirteen-direction theorem in the no-pivot chamber

Assume the normalized manuscript hypotheses `K=s=1`, no `eta=1/100` pivot, and

\[
s_{13}(A)\ge1.
\]

The audited spectral-to-volume proposition at order `k=4` and the random physical cut give a cut `I,J` with

\[
Z_4(A_{I,J})\ge4^{-4}\kappa^4,
\qquad \kappa=80^{-2},
\]

so

\[
Z_4(A_{I,J})^{-1/8}\le160.
\tag{9}
\]

If that same cut has maximum physical row leverage `h<1`, then with `bar h=max(1/2,h)`, (8) gives the full-law bound

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{160e}{\sqrt{\bar h}(1-\bar h)}.
}
\tag{10}
\]

All within-bank quadratic terms and all affine terms remain arbitrary. In particular, any fixed leverage gap `h<=1-delta` produces a dimension-free `L^infinity` bound under thirteen spectral directions.

For example, if `h<=3/4`, then

\[
\|p_Q\|_\infty
\le
\frac{640e}{\sqrt{3/4}}
<2010.
\]

This is a genuine bounded-density conclusion, stronger than the order-four endpoint `L^2` statement, but it is conditional on a physical leverage gap for the volume-producing cut.

## Corollary 4 — conditional nine-direction theorem beyond leverage one-half

Under the normalized no-pivot hypotheses and `s_9(A)>=1`, the order-three argument produces a cut with

\[
Z_3(A_{I,J})^{-1/6}\le160.
\]

If that cut has maximum physical row leverage `h<3/4`, then

\[
\boxed{
\|p_Q\|_\infty
\le
160\,\frac{3e}{\sqrt{\bar h}(3-4\bar h)},
\qquad \bar h=\max(1/2,h)<3/4.
}
\tag{11}
\]

Thus the direct-density order-three regime extends continuously from the previously known `h<=1/2` condition to every fixed leverage threshold below `3/4`.

## Why this does not yet reduce the global theorem below 17

The random-cut identity controls `Z_k`, not the maximum physical row leverage of the selected crossing. Physical row leverage can approach one, and at `k=4` the constant in (10) necessarily blows up in this argument as `h->1`. At `h=1`, the admissible interpolation parameter reaches `q=2` and the Fourier tail returns to the nonintegrable `1/|t|` endpoint.

The existing interpolation/completion bookkeeping also has a sharp `4r+1` barrier within that construction, so simply replacing the global rank estimate does not prove `s_16` or `s_13`. A true unconditional reduction now needs a high-leverage structural receiver: from a volume-good cut with `h` close to one, force a pivot, one-row random-slope mechanism, grouped hub, or another dependence-safe endpoint with a uniform constant.

Therefore the rigorous multiplicity ledger after this improvement is:

- unconditional candidate theorem: still **17**;
- no-pivot `13` directions + any fixed physical row-leverage gap below one on the volume-good cut: **bounded continuous density**, explicit (10);
- no-pivot `9` directions + maximum row leverage below `3/4` on the volume-good cut: **bounded continuous density**, explicit (11);
- unrestricted three-eigenvalue conjecture: **open**.

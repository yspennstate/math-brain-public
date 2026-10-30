# fleet02/B13 — early substantive checkpoint

Run: `20260924T062335Z-fleet02-B13-qform-r45`

Target status: full arbitrary-cap-one-density QFORM theorem remains OPEN. This checkpoint records a supporting obstruction only.

## QFORM-RANK1-4DIAG-ROUGH-SUPPORT-ESCAPE-v1

Assume a slab witness of ratio
\[
\rho=\Pr\{X^TAX\in J\}/|J|
\]
has the partner-r44 normal form
\[
A=M+E,\qquad M=D_S+R_1,\quad |S|\le4,\quad \operatorname{rank}R_1\le1,
\qquad \|E\|_{op}\le C_E/\rho,
\]
with `C_E=29.737812077`.  Assume `s_3(A)>=1`.

1. Weyl gives
\[
s_3(M)\ge1-C_E/\rho.
\]
Since `rank(R_1)<=1`, the singular-value rank inequality gives
\[
s_2(D_S)\ge s_3(M)\ge1-C_E/\rho.
\]
Thus at least two physical diagonal-center coefficients satisfy
\[
|d_i|\ge1-C_E/\rho.
\]

2. The exact matrix `M` has a dimension-free density bound.  Outside `S`, the rank-one term depends on at most one normalized linear statistic of the remaining original-coordinate product bank.  The standard weighted affine-fiber/Brascamp–Lieb bound gives density at most `sqrt(e)` for that statistic.  Grouping it with the at most four singleton center coordinates and scaling by `sqrt(e)`, the proved fixed-dimensional QFORM receiver in dimension `N<=5` yields
\[
\|p_{X^TMX}\|_\infty\le C_0,
\qquad C_0:=250e\,5(8+\log5).
\]
No support or moment bound is used here.

3. Now pass only to a bounded finite-union product-indicator witness, as allowed by the optimizer-free approximation theorem.  Let its support be `E_1 x ... x E_n`, with each `|E_i|=1`, and define the *absolute* support radius
\[
R^2:=\sup_{x\in\prod_i E_i}\|x\|_2^2=\sum_i r_i^2,
\qquad r_i:=\operatorname*{ess\,sup}_{x\in E_i}|x|.
\]
Then on this particular bounded product support
\[
|x^TEx|\le \|E\|_{op}\|x\|_2^2\le (C_E/\rho)R^2.
\]
Writing `delta=(C_E/rho)R^2`,
\[
\Pr\{X^TAX\in J\}\le
\Pr\{X^TMX\in J+[-\delta,\delta]\}
\le C_0(|J|+2\delta).
\]
Therefore
\[
\rho\le C_0\left(1+\frac{2C_E R^2}{\rho|J|}\right).
\]
In particular, whenever `rho>=2 C_0`,
\[
\boxed{
R^2\ge \frac{\rho^2|J|}{4C_0C_E}
}
\]
and hence
\[
R\ge \frac{\rho\sqrt{|J|}}{\sqrt{4C_0C_E}}.
\]
Numerically `sqrt(4 C_0 C_E)=1970.77...`.

This is deliberately **not** a perturbative deletion of `E` for arbitrary cap-one laws.  It says that if a high-ratio survivor activates an `O(1/rho)` operator tail, then every bounded finite-union approximation that still witnesses the violation must escape to absolute radius at least linear in `rho*sqrt(|J|)`.  Fragmented and originally unbounded supports are preserved as a live branch rather than ruled out.

## Pinned Fourier obstruction retained

For every disjoint original-coordinate cross block `B=A[I,J]`, the pinned unconditional D5 theorem at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives
\[
e_5(B^TB)\le\left(\frac{5\sqrt{2e}}{\rho}\right)^{10},
\qquad
s_5(B)\le\frac{5\sqrt{2e}}{\rho}.
\]
On center-free cuts in the partner-r44 normal form, `M[I,J]` has rank at most one, so additionally
\[
s_2(A[I,J])\le\|E[I,J]\|_{op}\le C_E/\rho.
\]
The D5 result remains the unconditional global physical-cross obstruction; the rank-one endpoint sharpens it only after the partner normal form has been obtained.

## First unpaid implication

`QFORM-REMOTE-SUPPORT-RANK1-4DIAG-RECEIVER-v1`: control the remote-support activation of the retained `O(1/rho)` tail using the two order-one physical diagonal centers and the rank-one bank, without a global support bound, a moment assumption, or post-rotation independence; otherwise construct a genuine bounded-finite-union counterexample sequence saturating the radius escape above.

# Rigor addendum for auto29

Run: `20260924T002614Z-account03-B15-qform-auto29`.

This addendum records one notation repair and two endpoint clarifications for `REPORT.md`; it changes no theorem or constant.

## 1. Notation repair in Section 5

In the rank-two indefinite calculation, the scaled spectral coordinates are

\[
u=\sqrt\lambda\,y_1,\qquad v=\sqrt\mu\,y_2.
\]

If the rendered report shows `nu`/`\nu` at that definition, read it as the Latin variable `u`. All subsequent occurrences `|u|`, `u^2-v^2`, and the null-coordinate substitution

\[
u=(a+b)/2,\qquad v=(b-a)/2
\]

use this same Latin `u`.

With this convention the calculation is exactly

\[
q(y)=\lambda y_1^2-\mu y_2^2=u^2-v^2=ab.
\]

## 2. The two-dimensional projection-cap endpoint

Section 6 uses `||rho_U||_infinity<=2` for a two-dimensional orthogonal projection of a cap-one product measure. When the ambient dimension is exactly two, no projection theorem is needed: an orthogonal change of variables has Jacobian one and the original product joint density is at most one, so the stated weaker cap `<=2` is still valid. For ambient dimension greater than two, the cited Livshyts--Paouris--Pivovarov marginal theorem supplies the cap `<=2`.

## 3. Convolution/interval domination in Section 7

For the disjoint-bank form

\[
Q=R+T,
\]

with `R=X^TBX` and `T=W^TCW`, independence of the original banks gives, for every interval `I`,

\[
\Pr(R+T\in I)
=\mathbb E\big[\Pr(R\in I-T\mid T)\big]
\le M|I|
\]

whenever `p_R` has height at most `M`. Thus (7.3) does not require a density for `T` at the height-payment stage. In the target case `C!=0`, qualitative absolute continuity of `T` is also available, but is not needed for the interval inequality. The account04/B15 same-constant compiler is then applied only after `rank(diag(B,C))>=3` is known.

These clarifications preserve the status `SHARP_REGULARITY_THRESHOLD_PROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`.

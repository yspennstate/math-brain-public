# Unequal-bank Edgeworth sign theorem for exact rotated QFORM witnesses

Run: `20260923T140355Z-account03-B17-QFORM-auto11`  
Assignment: account03/B17, sharp constant and witnesses.  
Status: `SUPPORTING_ANALYTIC_WITNESS_THEOREM`; the full QFORM conjecture remains **OPEN / NOT PROVED**. Full-target continuity remains separate.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact source-valid family

Let
\[
J=\operatorname{diag}(1,1,-1),\qquad O\in O(3),\qquad B=O^TJO.
\]
Choose integers `m_1,m_2,m_3>=3`. For bank `j`, take independent physical inputs
\[
X_{jk}\sim \operatorname{Unif}[-1/2,1/2],\qquad 1\le k\le m_j,
\]
and define
\[
Y_j={1\over\sqrt{m_j}}\sum_{k=1}^{m_j}X_{jk}.
\]
Let `R` be the `(m_1+m_2+m_3) x 3` matrix whose row corresponding to `(j,k)` is `e_j/sqrt(m_j)`. Then
\[
R^TR=I_3.
\]
Set
\[
A=RBR^T.
\]
The nonzero spectrum of `A` is therefore exactly the spectrum of `B`, namely
\[
\boxed{\operatorname{spec}_{\ne0}(A)=\{1,1,-1\}.}
\]
Every physical input density is exactly one on a set of length one, and
\[
Q=X^TAX=Y^TBY=(OY)^TJ(OY).
\]
Thus this is an exact finite-dimensional target-admissible family for every bank-size profile and every orthogonal rotation. When `B` is dense it is genuinely nonseparable in the independent physical coordinates.

## 2. Bankwise weighted local Edgeworth expansion

Let `sigma^2=1/12`, let `gamma_sigma` be the `N(0,sigma^2)` density, and let
\[
H_4(x)=x^4-6x^2+3.
\]
The completed weighted local Edgeworth lemma in the designated partner report

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`

gives, for the density `g_m` of a normalized bank sum,
\[
g_m(y)=\gamma_\sigma(y)\left[1-{1\over20m}H_4(y/\sigma)\right]
+r_m(y),
\]
with a universal weighted remainder
\[
|r_m(y)|\le C m^{-2}(1+|y|)^{-8}.
\tag{2.1}
\]
Apply (2.1) separately with `m=m_j`. Expanding the three-factor product gives
\[
\prod_{j=1}^3g_{m_j}(y_j)
=\gamma_\sigma^{\otimes3}(y)
\left[1-\sum_{j=1}^3{H_4(y_j/\sigma)\over20m_j}\right]
+E_m(y).
\tag{2.2}
\]
On the quadratic cone, the cross terms in (2.2) are Gaussian times fixed polynomials and the terms involving `r_m` have polynomial decay at least order eight in one nonzero cone direction. Using the orthogonal cone parametrization below, all such terms are integrable uniformly in `O`. Hence, with
\[
S_m=\sum_{j=1}^3m_j^{-1},
\]
the contribution of `E_m` to the zero-level density is
\[
O(S_m^2),
\tag{2.3}
\]
with an absolute implied constant, uniformly over `O` and the ratios of the `m_j`.

## 3. Exact cone average for one bank

Write spectral coordinates `z=Oy`. On the Lorentz cone
\[
z_1^2+z_2^2-z_3^2=0
\]
use
\[
z=r(\cos\theta,\sin\theta,\varepsilon),\qquad
r>0,\quad 0\le\theta<2\pi,\quad \varepsilon\in\{\pm1\}.
\]
Because `J^2=I`, each nappe contributes
\[
{d\mathcal H^2\over |2Jz|}={1\over2}\,dr\,d\theta.
\]
Under the normalized Gaussian cone measure, `q=r/sigma` is independent of `(theta,epsilon)` and
\[
\mathbb E q^2={1\over2},\qquad \mathbb E q^4={3\over4}.
\tag{3.1}
\]
For a fixed physical bank `j`, put
\[
u_j=O_{3j}^2\in[0,1],\qquad
a_j(\theta,\varepsilon)=\bigl(O^T(\cos\theta,\sin\theta,\varepsilon)\bigr)_j.
\]
Averaging over `theta` and `epsilon` gives
\[
\mathbb E a_j^2={1+u_j\over2},
\tag{3.2}
\]
and
\[
\mathbb E a_j^4=
{3\over8}(1-u_j)^2+3u_j(1-u_j)+u_j^2.
\tag{3.3}
\]
Combining (3.1)-(3.3),
\[
\begin{aligned}
h(u_j)
&:=\mathbb E_{\rm cone}H_4(q a_j)\\
&={3\over4}\left[{3\over8}(1-u_j)^2+3u_j(1-u_j)+u_j^2\right]
-3{1+u_j\over2}+3\\
&=\boxed{{57+6u_j-39u_j^2\over32}}.
\end{aligned}
\tag{3.4}
\]
The quadratic `h` is concave on `[0,1]`. Therefore its minimum occurs at an endpoint, and
\[
h(0)={57\over32},\qquad h(1)={3\over4}.
\]
Hence the key sign statement is
\[
\boxed{h(u)\ge {3\over4}\quad\text{for every }u\in[0,1].}
\tag{3.5}
\]

## 4. Main theorem: every unequal-bank first correction is negative

The leading Gaussian cone integral is
\[
p_G(0)={1\over2^{3/2}\sigma^2}=3\sqrt2.
\]
Substituting (3.4) into (2.2)-(2.3) yields the uniform expansion
\[
\boxed{
{p_Q(0)\over3\sqrt2}
=1-\sum_{j=1}^3{h(O_{3j}^2)\over20m_j}
+O\!\left(S_m^2\right).
}
\tag{4.1}
\]
By (3.5),
\[
\boxed{
{p_Q(0)\over3\sqrt2}
\le1-{3\over80}S_m+O(S_m^2).
}
\tag{4.2}
\]
This is uniform in the rotation. In particular, for any sequence of rotations `O=O_m` and arbitrary unequal bank-size profiles with
\[
\min_jm_j\to\infty,
\]
we have
\[
\boxed{
\limsup p_Q(0)\le3\sqrt2,
}
\]
and, once all banks are sufficiently large, the cone-tip value is strictly below `3sqrt(2)`.

Equivalently,
\[
\liminf_{\min m_j\to\infty}
{1-p_Q(0)/(3\sqrt2)\over \sum_jm_j^{-1}}
\ge {3\over80}.
\tag{4.3}
\]
Thus unequal bank sizes and an adversarial rotation cannot reverse the sign of the first non-Gaussian correction at the cone tip inside this exact three-bank normalized-uniform architecture.

## 5. Actual application of the designated partner result

For the partner's rational orthogonal matrix
\[
O={1\over7}
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},
\]
we have
\[
(u_1,u_2,u_3)=\left({9\over49},{36\over49},{4\over49}\right).
\]
Formula (3.4) gives
\[
\left(h(u_1),h(u_2),h(u_3)\right)=
\left(
{17043\over9604},
{96897\over76832},
{137409\over76832}
\right).
\]
Hence
\[
{1\over20}\sum_{j=1}^3h(u_j)
=\boxed{{5295\over21952}},
\tag{5.1}
\]
which exactly recovers the completed partner expansion
\[
p_{Q_m}(0)=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right)
\]
when `m_1=m_2=m_3=m`.

The same partner theorem proves, through this exact cap-one finite family,
\[
C_*\ge3\sqrt2
\]
for every valid universal QFORM constant `C_*`. Combining that lower bound with (4.2) gives the actual inequality
\[
\boxed{
\limsup_{\min m_j\to\infty}\sup_{O\in O(3)}p_Q(0)
\le3\sqrt2\le C_*.
}
\tag{5.2}
\]
So the unequal-scale three-diffuse-bank cone tip cannot improve the current sharp obstruction.

## 6. Continuity for this family

For each `m_j>=3`, every bank density is continuous and compactly supported. In spectral coordinates, with `rho(z)=prod_j g_{m_j}((O^Tz)_j)`, the output density has the cylindrical representation
\[
p_Q(s)={1\over2}\int_{w^2+s\ge0}\int_0^{2\pi}
\rho\!\left(\sqrt{w^2+s}\cos\theta,
\sqrt{w^2+s}\sin\theta,w\right)
\,d\theta\,dw.
\]
Compact support supplies a common integrable majorant, so dominated convergence gives a continuous density representative for this witness family. This is **not** a proof of full-target continuity.

## 7. Scope and witness-search consequence

This result is deliberately a sharp stress-family theorem, not a universal upper bound. It does **not** control:

- the global mode away from zero;
- arbitrary cap-one marginal laws;
- surviving mesoscopic/shared physical rows;
- additional spectrum outside the three-dimensional range;
- finite-leverage configurations not represented by three normalized independent banks.

What it rules out is stronger than the equal-periodic control: even if the three diffuse banks approach the Gaussian endpoint at arbitrarily different rates and the orthogonal rotation changes adversarially with dimension, the first non-Gaussian cone-tip correction remains uniformly negative. A witness above `3sqrt(2)` must therefore leave this architecture at first order, for example by retaining a genuinely non-Gaussian finite/mesoscopic component, sharing physical coordinates across several spectral banks, or creating an off-tip peak.

## 8. Corrections and source integrity

Controls/corrections consumed before publication:

- pointwise quadratic-phase decay is unavailable;
- no independence is assumed after spectral rotation;
- arbitrary-joint rank-three coarea bounds are unavailable;
- naive fiber-sup and positive conditional-cap moments are unavailable;
- near-zero half-Riesz-only interpolation is unavailable.

None of those refuted interfaces is used. The proof uses only the exact physical product construction, the partner's weighted local Edgeworth lemma, orthogonal cone coordinates, and elementary moment algebra.

Full QFORM status: **OPEN / NOT PROVED**. Independent end-to-end review of this supporting theorem has not been requested as a full-candidate review.

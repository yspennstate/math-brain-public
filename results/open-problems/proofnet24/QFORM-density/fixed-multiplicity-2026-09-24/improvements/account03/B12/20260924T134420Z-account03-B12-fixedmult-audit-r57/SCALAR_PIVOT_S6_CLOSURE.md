SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T13:44:20Z.
attacking: lower the scalar-pivot sector from the fixed-multiplicity theorem by combining one-step Schur spectral loss with the marginal-free order-two half-potential receiver and the designated account04/B12 exact square/log kernel constants.

# QFORM-SCALAR-PIVOT-S6-CLOSURE-v1

Status: **PROVED SUPPORTING BRANCH / GLOBAL NINE-DIRECTION THRESHOLD NOT LOWERED / FULL THREE-EIGENVALUE QFORM OPEN**.

## Theorem

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by `K<∞`. Let `A=A^T`, let `b∈R^n,c∈R`, and suppose

\[
 s_6(A)\ge s>0.
\]

Assume there is an **original-coordinate scalar pivot**

\[
 |A_{ii}|\ge \frac{s}{100}
\tag{1}
\]

for some `i`. Then

\[
Q=X^TAX+b^TX+c
\]

has an essentially bounded density and

\[
\boxed{
 \|p_Q\|_{\infty,\mathrm{ess}}
 \le
 \left(2010+1200\log 16\right)\frac{K^2}{s}
 <5338\frac{K^2}{s}.
}
\tag{2}
\]

No condition is imposed on the remaining spectrum: all other eigenvalues may be smaller or larger, have either sign, arbitrary multiplicity, and arbitrary eigenvector orientation. No quadratic remainder is separated as independent noise. Global continuity is **not** proved by this branch.

## Sources used

1. Pinned self-contained baseline manuscript:
   `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`,
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
   Needed statements: scalar square profile, principal-Schur spectral count, no-pivot spectral-to-volume proposition at order two, fair coordinate cut, and the pivot half-potential proof.
2. Marginal-free order-two full half-potential receiver from account03/B04:
   `yspennstate/math-open-problems@8ff490c177d0cd7d6f33130f1431785e312a9d10`,
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`.
   I checked the order-two promotion tree and its constants in this run. It was also independently reconstructed in account02/B09 at commit `51022fbf2819704f220b1dc6d5f1889f979ca77b`.
3. Designated partner account04/B12 scalar-kernel sharpening:
   `yspennstate/math-open-problems@126eb0e75770fb9e814092f610e1e67ad0412afe`,
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B12/20260924T131241Z-account04-B12-square-kernel-audit-r1/SCALAR_CONSTANT_SHARPENING.md`.

## Proof

By the usual scaling it is enough to prove the result for `K=s=1`. Indeed, set `Y=KX` and

\[
\widetilde Q=\frac{K^2}{s}Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

The coordinates of `Y` have densities bounded by one, `s_6(A/s)≥1`, and (1) becomes `|(A/s)_{ii}|≥1/100`. Density scaling at the end multiplies the normalized bound by `K^2/s`.

So assume from now on

\[
K=s=1,
\qquad \eta=\frac1{100},
\qquad \kappa=\frac1{80^2}.
\]

Put `a=A_ii`, so `|a|≥η`. Complete the square in the literal original coordinate `X_i`. The pinned scalar-profile lemma gives, as a measure-domination statement,

\[
Q=a(X_i-m(X_{-i}))^2+R(X_{-i}),
\]

where the quadratic matrix of `R` is the scalar Schur complement `S`, and

\[
p_Q(z)
\le |a|^{-1/2}\,\mathbb E|z-R|^{-1/2}
\le 10\sup_u\mathbb E|R-u|^{-1/2}
\tag{3}
\]

for almost every `z`. This is conditional on original independent coordinates; it does **not** assert that the square term and `R` are independent.

The principal-Schur spectral count loses at most one unit-scale eigenvalue. Since `s_6(A)≥1`,

\[
\boxed{s_5(S)\ge1.}
\tag{4}
\]

We split according to whether `S` has an `η`-pivot.

### Case 1: the Schur complement has a pivot

The baseline pivot proposition needs only two unit spectral directions, so (4) is more than sufficient. The designated account04/B12 result keeps the exact scalar-kernel constant instead of rounding it. With

\[
L_0=4+4\log16,
\]

the worst pivot branch has truncated half-potential

\[
H(R)
\le \eta^{-1/2}(8+3L_0)
=200+120\log16.
\tag{5}
\]

The definite-pair and indefinite-pair pivot branches are smaller than this scalar value in the pinned proof. Outside `|R-u|≤1`, the kernel `|R-u|^{-1/2}` is at most one, hence

\[
\boxed{
\sup_u\mathbb E|R-u|^{-1/2}
\le 201+120\log16
=533.7106466687\ldots .
}
\tag{6}
\]

This is the required actual application of the completed account04/B12 result.

### Case 2: the Schur complement has no pivot

From (4), the pinned no-pivot spectral-to-volume proposition at order `k=2` applies because `4k-3=5`. Therefore

\[
V_2(S)\ge\kappa^2.
\tag{7}
\]

The fair original-coordinate cut then supplies disjoint banks with literal cross block `M` satisfying

\[
E_2(M)=e_2(MM^T)
\ge4^{-2}\kappa^2.
\tag{8}
\]

The marginal-free order-two receiver states

\[
\sup_u\mathbb E|R-u|^{-1/2}
\le C_2E_2(M)^{-1/8},
\qquad
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
\tag{9}
\]

For completeness, its proof is dependence-safe: determinant-squared weights on physical two-row minors are first aggregated; if both row marginals are at most `1/2`, the grouped product-Fourier compiler gives a `|t|^{-1}` envelope and Riesz integration closes the half-potential. If one row is heavy, it is kept as a literal original-coordinate hub and the residual one-volume is projected only in a deterministic Jacobian. If a second row is heavy, the argument terminates at the exact physical rank-two half-potential endpoint. Same-bank quadratic and affine phases remain inside complex pushforwards throughout. No rotated coordinates are declared independent.

Using `κ=80^{-2}` in (8),

\[
E_2(M)^{-1/8}
\le(4^{-2}\kappa^2)^{-1/8}
=\sqrt{160}.
\]

Thus

\[
\boxed{
\sup_u\mathbb E|R-u|^{-1/2}
\le C_2\sqrt{160}
=152.99191115498\ldots<153.
}
\tag{10}
\]

In particular (10) is strictly smaller than the partner-controlled pivot value (6).

### Finish

Combining (3), (6), and (10),

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le10(201+120\log16)
=2010+1200\log16
=5337.1064666877\ldots<5338.
\tag{11}
\]

Scaling back proves (2). QED.

## Interpretation as additional-eigenvalue control

The proof never truncates the random quadratic form to six eigenmodes. The hypothesis `s_6(A)≥s` is used only once, through the deterministic Schur count (4). Every other eigenvalue of the **final** matrix remains present in the Schur remainder and may be arbitrarily small, arbitrarily large, positive or negative. Thus this is a genuine stability statement under arbitrary additional signed spectrum inside the scalar-pivot sector, not a convolution-with-an-independent-remainder argument.

Equivalently, under `s_6(A)≥s`, any unresolved matrix for a future lower-threshold proof may be restricted to the branch

\[
\max_i|A_{ii}|<s/100,
\]

because a scalar pivot already closes the density problem with the universal bound above. Pair pivots may close still more configurations, but they are not needed for this theorem.

## What this does not prove

- It does **not** prove the complete six-eigenvalue theorem because the no-scalar-pivot branch is not closed here.
- It does **not** solve the current multiplicity-eight shared-anchor/overlap-one terminal state.
- It does **not** solve the unrestricted three-eigenvalue conjecture.
- It proves essential boundedness in this branch; continuity remains separate.

The next useful structural question is therefore no longer whether a scalar physical pivot can absorb arbitrary extra signed spectrum under six large directions—it can—but whether the no-pivot `s_8` overlap-one currency can be converted into a product-preserving receiver without treating the shared anchor as independent of the translated bilinear banks.

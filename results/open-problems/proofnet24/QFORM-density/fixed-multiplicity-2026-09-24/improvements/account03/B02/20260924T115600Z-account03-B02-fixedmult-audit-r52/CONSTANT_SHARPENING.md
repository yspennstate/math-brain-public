# QFORM fixed-multiplicity-17 constant sharpening

Run: `20260924T115600Z-account03-B02-fixedmult-audit-r52`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Status: **proved quantitative improvement; no multiplicity reduction**.

## Theorem

Under exactly the hypotheses of the pinned manuscript theorem — independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0` — the same proof establishes

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty
\le (2010+1200\log16)\frac{K^2}{s}
<5338\frac{K^2}{s}.
}
\]

This replaces the manuscript's round constant `10000`.

## Proof

It suffices to track the constants in the normalized `K=s=1` proof.

The manuscript quarter-power lemma gives

\[
L_0=4+4\log16.
\]

For a scalar pivot in Proposition `pivot-H`, `eta=1/100`, hence `eta^{-1/2}=10`, and the displayed proof gives

\[
H(Q)\le\eta^{-1/2}(8+3L_0)
=10\bigl(8+3(4+4\log16)\bigr)
=200+120\log16.
\tag{1}
\]

The other two pivot-H branches are smaller. The definite-pair branch gives

\[
4\pi\eta^{-1/2}=40\pi<200+120\log16.
\]

The indefinite-pair branch gives

\[
10(32+4\log16)+4/e<200+120\log16,
\]

because the left side is about `432.38`, while the right side of (1) is about `532.71`.

If there is no pivot and `s_9(A)>=1`, the manuscript proves the full half-potential `<200`. If there is a pivot, (1) controls the truncated half-potential, while the tail `|Q-a|>1` contributes at most one. Consequently the nine-eigenvalue proposition strengthens to

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le 201+120\log16.
\tag{2}
\]

In the main theorem's scalar-pivot branch, the outer square profile contributes another factor `eta^{-1/2}=10`. Thus

\[
\|p_Q\|_\infty
\le10(201+120\log16)
=2010+1200\log16.
\tag{3}
\]

It remains only to compare the other main-theorem branches with (3). The no-pivot branch gives `800e`; the definite-pair branch gives `10pi`; and the main indefinite-pair branch gives

\[
10(10+5\log16)+1/e.
\]

All three are strictly below `2010+1200\log16`. Hence (3) is a valid normalized global constant. The manuscript's final scaling `Y=KX`, `A -> A/s`, `Q=(s/K^2)\widetilde Q` multiplies the density bound by `K^2/s`, proving the stated theorem.

Numerically,

\[
2010+1200\log16=5337.106466687737\ldots<5338.
\]

No theorem statement, structural lemma, regularity assertion, or probabilistic hypothesis has been changed.

## Threshold status

This improvement does not lower the spectral multiplicity. At order four the audited determinant receiver is exactly the borderline `|t|^{-1}` envelope, so the present absolute-Fourier route does not certify the `s_13` theorem. A new endpoint density/small-ball receiver is still required for `17 -> 13`.

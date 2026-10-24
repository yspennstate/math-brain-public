# QFORM-S16-TERMINAL-SEED-MASS-DICHOTOMY-v1

Run: `20260924T133720Z-account03-B05-fixedmult-audit-r12`.
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Status: **proved supporting structural/analytic theorem; not a universal 16-eigenvalue theorem**.

Use `eta=1/100`, `kappa=1/6400`. Let `A=A^T` have no `eta`-pivot and `s_16(A)>=1`. Then the existing `k=4` theorem gives `V_4>=kappa^4`.

For each ordered disjoint nonsingular four-seed `B=A_{S,T}`, set `w(B)=|det B|^2`, `L=[n]\(S union T)`, `P=A[:,T]B^{-1}A[S,:]`, and

\[
q(B)=\|\operatorname{off}(A_{L,L}-P_{L,L})\|_F^2.
\]

The bordered determinant identity gives

\[
w(B)q(B)=\sum_{\ell\ne m\in L}\det A_{S\cup\{\ell\},T\cup\{m\}}^2,
\]

hence

\[
\sum_Bw(B)q(B)\le25V_5.
\tag{1}
\]

The completed `account01/B09` determinant-escalation theorem says that if `q(B)<=1/256`, there is another disjoint four-seed `B'` with

\[
w(B')\ge R^2w(B),\qquad R=22.6532460869\ldots,\quad R^2=513.1695582735\ldots.
\tag{2}
\]

Iterating (2) over the finite seed set terminates at a seed `C` with `q(C)>1/256`; otherwise weights would increase strictly forever. For such a terminal seed its own order-five extensions are a subset of `V_5`, so

\[
V_5\ge w(C)q(C)>w(C)/256.
\]

Therefore

\[
q(B)>1/256\Rightarrow w(B)<256V_5,
\tag{3}
\]

and

\[
q(B)\le1/256\Rightarrow w(B)<256V_5/R^2.
\tag{4}
\]

Writing `x=V_5/V_4`, (1) also gives

\[
\frac{\sum_{q(B)>1/256}w(B)}{V_4}<6400x,
\tag{5}
\]

while each low-residual seed obeys

\[
\frac{w(B)}{V_4}<256x/R^2.
\tag{6}
\]

For any `0<theta<1`, if `x>=theta kappa`, then `V_5>=theta kappa^5`, and the existing random-cut/order-five receiver yields

\[
\boxed{\|p_Q\|_\infty\le800e\,\theta^{-1/10}},
\]

with a continuous density.

If instead `x<theta kappa`, then (5) forces more than `(1-theta)V_4` of the determinant-squared mass onto low-residual seeds, and (6) gives an individual mass fraction below `theta/(25R^2)`. Hence there are strictly more than

\[
\boxed{25R^2(1-\theta)/\theta}
\]

nonzero low-residual ordered seeds.

At `theta=1/2`: either `||p_Q||_infty<800e 2^{1/10}<2331` continuously, or at least 12,830 low-residual ordered four-seeds carry more than half of `V_4`, with each seed carrying less than `3.898e-5 V_4`.

The exact missing factor is now an aggregate receiver or a dimension-free weighted-preimage bound for the escalation map. In the `theta=1/2` chamber, a choice of escalation map with at most 256 low-residual predecessors per target would already contradict the forced `>V_4/2` low-residual mass, because `256/R^2<1/2`. No such preimage theorem is presently proved.

This theorem preserves all original-coordinate product structure. No rotated variables are declared independent, no bounded-support or moment assumptions are used, and no pointwise quadratic-phase decay is invoked.

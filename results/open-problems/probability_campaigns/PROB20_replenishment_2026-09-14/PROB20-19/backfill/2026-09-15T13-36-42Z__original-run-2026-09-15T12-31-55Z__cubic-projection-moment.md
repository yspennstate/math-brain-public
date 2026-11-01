# PROB20-19 backfill — original run 2026-09-15T12-31-55Z

**Recovery provenance.** This file preserves authentic mathematical work from an earlier completed task response in the current conversation. That earlier run authored a full GitHub report payload, but no successful commit receipt/readback was exposed. The text below is recovered from that exact prior task-response content; unavailable local/tool history is not invented.

**Original status: PARTIAL.** The universal Mallat–Zeitouni/Bandeira conjecture remained open.

## Cubic projection-moment theorem for ranks `r>=3`

Let
\[
f_d(\theta)=\operatorname{Top}_d(\theta_1^2,\ldots,\theta_p^2),
\qquad \theta\sim\mathrm{Unif}(S^{p-1}),
\]
and for a rank-`r` orthogonal projection `P`,
\[
M_k(P)=\mathbb E[f_d(\theta)(\theta^TP\theta)^k].
\]
The archived 2026-09-15T11-32-02Z checkpoint had already proved that `M_2` is uniquely maximized by coordinate projections and derived the exact invariant formula for `M_3`. This backfilled run completed the cubic comparison for every rank `r>=3`.

Define
\[
A_3=\mathbb E[f_d X_1^3],\quad
B_3=\mathbb E[f_d X_1^2X_2],\quad
C_3=\mathbb E[f_d X_1X_2X_3],
\qquad X_i=\theta_i^2.
\]
For a projection `P`, put `d_i=P_ii`,
\[
S_2(P)=\sum_i d_i^2,\qquad S_3(P)=\sum_i d_i^3.
\]
The exact cubic formula is
\[
\boxed{
M_3(P)
=C_3(r^3+6r^2+8r)
+3(r+4)(B_3-3C_3)S_2(P)
+(A_3-15B_3+30C_3)S_3(P).
}
\tag{1}
\]

### Coefficient inequality 1

Let `D_1=B_3-3C_3`. By exchange symmetry,
\[
D_1
=\mathbb E\left[f_d X_3\left(\frac{X_1^2+X_2^2}{2}-3X_1X_2\right)\right].
\]
Condition on `S=X_1+X_2` and all outside squared coordinates. Put
\[
Q=\frac{|X_1-X_2|}{S}=|\cos2\phi|.
\]
Then the bracket is
\[
S^2(Q^2-1/2).
\]
For fixed `S` and outside squares, `f_d` is a nondecreasing function of `Q`, while `E[Q^2]=1/2`. Hence the conditional contribution is a nonnegative covariance. On a positive-probability region where `f_d=constant+max(X_1,X_2)`, it is strictly positive, and `X_3` can also be positive. Therefore
\[
\boxed{B_3-3C_3>0.}
\]

### Coefficient inequality 2

Let `D_2=A_3-5B_3`. Exchange symmetry gives
\[
D_2
=\mathbb E\left[f_d\left(\frac{X_1^3+X_2^3}{2}-\frac52X_1X_2(X_1+X_2)\right)\right].
\]
Using the same `S,Q`, the bracket equals
\[
S^3(Q^2-1/2).
\]
Thus the same conditional covariance argument gives
\[
\boxed{A_3-5B_3>0.}
\]

### Projection comparison

Since
\[
A_3-15B_3+30C_3=D_2-10D_1,
\]
put
\[
\Delta_2=r-S_2=\sum_i d_i(1-d_i),
\qquad
\Delta_3=r-S_3=\sum_i d_i(1-d_i)(1+d_i).
\]
Because `0<=d_i<=1`,
\[
\Delta_2\le\Delta_3\le2\Delta_2.
\]
Subtracting (1) from its coordinate-projection value yields
\[
M_3(P_{coord})-M_3(P)
=3(r+4)D_1\Delta_2+(D_2-10D_1)\Delta_3.
\]
If `D_2-10D_1>=0`, positivity is immediate. Otherwise use `Delta_3<=2Delta_2` to get
\[
M_3(P_{coord})-M_3(P)
\ge[2D_2+(3r-8)D_1]\Delta_2.
\]
For `r>=3`, the bracket is strictly positive. Hence
\[
\boxed{M_3(P)\le M_3(P_{coord})\quad(r>=3),}
\]
with equality only for coordinate projections.

## Exact remaining cubic gap

For rank `r=2`, the same lower bound reduces to
\[
2(D_2-D_1)\Delta_2,
\]
so one needs
\[
\boxed{A_3-6B_3+3C_3\ge0.}
\]
The backfilled run did not prove this. It recorded the exact representation
\[
D_2-D_1
=\mathbb E\left[f_d S^2(S-X_3)(Q^2-1/2)\right],
\]
whose factor `S-X_3` changes sign, preventing the earlier monotone-covariance argument from applying directly.

## Consequence and limitation

For positive two-eigenvalue spikes, the binomial series has positive coefficients. The orientation-independent terms are `M_0,M_1`; coordinate projections maximize `M_2` for every rank, and maximize `M_3` for every `r>=3`. Rank one is already solved to all orders by the positive one-spike theorem. The finite-strength rank-`r>1` family remains open because `M_k`, `k>=4`, are not controlled.

## Original next attacks

1. Prove/refute the rank-two cubic sign `A_3-6B_3+3C_3>=0`.
2. Derive the quartic invariant formula and identify whether genuinely new signed cycle invariants survive projection reduction.
3. Seek a direct polarization inequality for the full finite-spike kernel, bypassing termwise moments.

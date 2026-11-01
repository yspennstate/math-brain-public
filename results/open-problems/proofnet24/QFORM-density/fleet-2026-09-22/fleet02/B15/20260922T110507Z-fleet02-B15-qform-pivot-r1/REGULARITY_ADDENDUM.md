# Regularity addendum — saddle-square blocks have continuous densities

**Parent report:** `d5392d73398e2811f58b612fb8f191aa79d8ee5e`  
**Live assignment:** fleet02/B15, `Absolute continuity and regularity`  
**Full conjecture:** OPEN.

## New completed fleet input

After the parent report was written, fleet03/B17 completed

`yspennstate/math-open-problems@83b7becb714a161a3246588039203e630e8674fa:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260922T113421Z-qform-r11/report.md`.

It proves that for independent bounded-density `X,Y,Z`, every `p>2`, `q=p/(p-1)`, and nonzero `c,lambda`,

\[
\|p_{cXY}\|_p\le A_p|c|^{-(p-1)/p},
\qquad
\|p_{\lambda Z^2}\|_q\le B_q|\lambda|^{-1/p},
\]

and therefore

\[
\|p_{cXY+\lambda Z^2}\|_\infty
\le C_p|c|^{-(p-1)/p}|\lambda|^{-1/p}.
\tag{A.1}
\]

At `p=3`, `C_p=8`.

## Theorem A — the saddle-square density is actually uniformly continuous

Under the hypotheses above, `cXY+lambda Z^2` has a bounded **uniformly continuous** density, with the same `L^infinity` estimate (A.1).

### Proof

Let

\[
f=p_{cXY}\in L^p,
\qquad
g=p_{\lambda Z^2}\in L^q,
\qquad {1\over p}+{1\over q}=1.
\]

Independence gives `h=f*g`. For every translation `a`, Hölder/Young yields

\[
\begin{aligned}
\|\tau_a h-h\|_\infty
&=\|f*(\tau_ag-g)\|_\infty\\
&\le\|f\|_p\,\|\tau_ag-g\|_q.
\end{aligned}
\]

Because `q<infinity`, translations are continuous in `L^q`, so the right side tends to zero as `a->0`. Hence `h` is uniformly continuous. The norm bound is exactly (A.1). `QED`.

The same statement survives arbitrary linear terms `aX+bY+dZ`: completing the product and square gives coordinatewise translations,

\[
cXY+aX+bY=c(X+b/c)(Y+a/c)-ab/c,
\]

\[
\lambda Z^2+dZ=\lambda(Z+d/(2\lambda))^2-d^2/(4\lambda),
\]

which preserve independence and the density cap.

## Theorem B — arbitrary outside couplings preserve a continuous representative

Suppose a high-dimensional symmetric matrix has a principal coordinate block

\[
B=
\begin{pmatrix}
0&c/2&0\\
c/2&0&0\\
0&0&\lambda
\end{pmatrix},
\qquad c\lambda\ne0.
\tag{A.2}
\]

Then, allowing arbitrary couplings from these three coordinates to all remaining coordinates, `Q(X)` has a bounded **continuous** density satisfying (A.1).

### Proof

Condition on all outside coordinates `W=w`. The three selected coordinates remain independent with their original densities bounded by one. The outside couplings become only linear terms, so Theorem A gives a conditional density `h_w(u)` which is continuous in `u` and obeys the same uniform bound

\[
|h_w(u)|\le M:=C_p|c|^{-(p-1)/p}|\lambda|^{-1/p}
\]

for every `w`.

Define

\[
h(u)=\int h_w(u)\,d\mu_W(w).
\]

This is a density of the unconditional output. For every fixed `u`, as `a->0`,

\[
h_w(u+a)-h_w(u)\to0
\]

for every `w`, while the absolute difference is bounded by `2M`. Dominated convergence therefore gives

\[
h(u+a)-h(u)\to0.
\]

Thus `h` is a continuous representative, and `|h(u)|<=M`. `QED`.

At the canonical threshold block `c=2`, `lambda=1`, taking `p=3` gives

\[
\boxed{
\|p_Q\|_\infty\le 8\,2^{-2/3}=2^{7/3}<5.04,
}
\]

now with a continuous representative even after arbitrary outside couplings.

## Status

This closes the stronger continuity request on two substantial source-valid branches:

1. all coordinate-diagonal target forms: uniformly continuous density, bound `pi` (parent report);
2. every principal saddle-square block (A.2), with arbitrary outside couplings: continuous density with the explicit `L^p-L^q` bound above.

The full rotated three-eigenvalue conjecture and its general continuous-representative assertion remain OPEN. The flat rank-three projector obstruction in the parent report still prevents reduction to one fixed principal coordinate block.

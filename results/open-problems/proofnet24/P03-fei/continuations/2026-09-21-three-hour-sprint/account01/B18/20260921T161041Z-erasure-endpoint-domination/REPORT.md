# B18 FEI proof integration — endpoint domination of the Bernoulli-erasure dual and a centered curvature bank

**Date:** 21 September 2026  
**Status:** **PROVED route-reduction / full Fourier entropy--influence conjecture remains OPEN.**  
**Route:** APPROACH 11/12 (influence-greedy restriction / restricted-potential dual).  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use was available or claimed.  
**Novelty:** no publication-priority claim.

Fresh `master` was resolved before this derivation. The inputs used at their exact proved scopes are the account01/B18 Bernoulli-erasure EXIT report, the scalar/coarsened frontier, and the fresh account04/B18 tangent/phase stability package. No read-once certificate, finite sweep, or peer audit was rerun.

The previous Bernoulli-erasure report reduced proper-block descent to the scalar witness

\[
D_f(t)>c_*G_f(t),\qquad c_*={2\over\ln2},
\]

where, for an independent Bernoulli-`t` erased block `A_t`,

\[
F(t)=\mathbb E H(X_{A_t}\mid X_{A_t^c}),\qquad
D(t)=tH-F(t),\qquad
G(t)=\mathbb E M_{A_t}.
\]

This run proves that on a restriction-maximal core this entire *uncentered* one-parameter route is already implied by the singleton inequalities. In particular, increasing the erasure density cannot create a new witness missed at `t=0`.

## 1. Two centered coarsening banks

For coordinate `i`, let

\[
Q_i=\Pr(X_i=1\mid X_{-i})
\]

be the full posterior. Under a random erasure of the other coordinates at density `t`, let `\bar Q_{i,t}` be the posterior after seeing only the unerased coordinates. Define

\[
E(t):={G(t)\over t}\quad(t>0),
\qquad
E_0:=\lim_{t\downarrow0}E(t)
=\sum_i\mathbb E\min(Q_i,1-Q_i).
\]

The Bayes loss `e(q)=min(q,1-q)` is concave. Coarsening the conditioning sigma-field replaces a fine posterior by its conditional expectation, so conditional Jensen gives

\[
\boxed{E(t)\text{ is nondecreasing in }t.}
\tag{1.1}
\]

Hence

\[
\boxed{J(t):=G(t)-tE_0=t(E(t)-E_0)\ge0.}
\tag{1.2}
\]

The inherited EXIT identity says `F` is convex, `F(0)=0`, and

\[
F'(0)=B:=\sum_iH(X_i\mid X_{-i}).
\]

Therefore

\[
\boxed{C(t):=F(t)-tF'(0)=tD'(0)-D(t)\ge0,}
\tag{1.3}
\]

where `D'(0)=H-B`. Equivalently,

\[
C(t)=\int_0^t[F'(s)-F'(0)]\,ds
=\int_0^t(t-s)F''(s)\,ds.
\tag{1.4}
\]

Thus `C` is exactly the accumulated conditional-mutual-information curvature of the spectral erasure curve.

## 2. Main exact decomposition

For each coordinate write the singleton restriction identity as

\[
\Delta_iH=B_i+R_i,
\qquad
0\le R_i\le c_*e_i,
\]

where

\[
e_i=\mathbb E\min(Q_i,1-Q_i),
\qquad E_0=\sum_i e_i.
\]

### Theorem 2.1 — Bernoulli-erasure slack is endpoint dominated

For every Boolean function and every `0<t<=1`,

\[
\boxed{
\begin{aligned}
c_*G(t)-D(t)
={}&t\,[\sum_i\Delta_iH-H]\\
&+t\,[c_*E_0-\sum_iR_i]\\
&+c_*J(t)+C(t).
\end{aligned}}
\tag{2.1}
\]

### Proof

From the definitions,

\[
G(t)=tE_0+J(t),
\qquad
D(t)=tD'(0)-C(t).
\]

Also

\[
D'(0)=H-B,
\qquad
B=\sum_iB_i,
\qquad
\sum_i\Delta_iH=B+\sum_iR_i.
\]

Therefore

\[
\begin{aligned}
c_*G-D
&=t[c_*E_0-D'(0)]+c_*J+C\\
&=t[c_*E_0-\sum_iR_i]
+t[\sum_iR_i-(H-B)]+c_*J+C\\
&=t[c_*E_0-\sum_iR_i]
+t[\sum_i\Delta_iH-H]+c_*J+C.
\end{aligned}
\]

This is (2.1). QED.

## 3. Consequence for a restriction-maximal hard core

Let `g` maximize `H/I` among its nonconstant physical restriction descendants, and write `r=H/I`. Singleton criticality gives

\[
\Delta_iH\ge rp_i,
\]

so after summing,

\[
\sum_i\Delta_iH\ge r\sum_i p_i=H.
\tag{3.1}
\]

The Bayes prediction bound gives

\[
c_*E_0-\sum_iR_i\ge0.
\tag{3.2}
\]

Together with `J(t)>=0` and `C(t)>=0`, Theorem 2.1 yields

\[
\boxed{D_g(t)\le c_*G_g(t)\quad\text{for every }0<t\le1.}
\tag{3.3}
\]

The important point is *why*: (3.3) does not require the previous all-block criticality theorem. It follows already from the singleton restriction inequalities plus two universal coarsening monotonicities.

Equivalently, since `D(t)/t` is nonincreasing and `G(t)/t` is nondecreasing,

\[
\boxed{
{D(t)\over G(t)}
\le
{D'(0)\over E_0}
\quad(G(t)>0).
}
\tag{3.4}
\]

Thus the strongest point of the *uncentered Bernoulli-erasure* selector is the infinitesimal endpoint `t downarrow0`. If the singleton test does not descend, no larger Bernoulli erasure density can rescue it.

This is a rigorous killed-route result for the uncentered version of APPROACH 11/12, and prevents spending further runs searching for a favorable interior `t` in the same scalar certificate.

## 4. The centered entropy bank has a dimension-free posterior-variance lower bound

The failure above also identifies a useful quantity to retain rather than discard. Binary entropy is `4/ln2`-strongly concave because

\[
h_2''(q)=-{1\over(\ln2)q(1-q)}\le-{4\over\ln2}.
\]

For every random coarsening,

\[
\mathbb E h_2(\bar Q_{i,s})-\mathbb E h_2(Q_i)
\ge {2\over\ln2}\,
\mathbb E(Q_i-\bar Q_{i,s})^2.
\tag{4.1}
\]

Summing coordinates and integrating the EXIT slope gives

\[
\boxed{
C(t)
\ge {2\over\ln2}
\int_0^t
\sum_i\mathbb E(Q_i-\bar Q_{i,s})^2\,ds.
}
\tag{4.2}
\]

So the centered bank `C(t)` is not merely nonnegative: it quantitatively pays the multiscale posterior heterogeneity created by forgetting spectral coordinates. This is compatible with the fresh tangent-defect/phase package, where the same type of coarsening variance is a positive stability bank.

For completeness, the Bayes centered bank has the exact interpretation

\[
{J(t)\over t}
=\sum_i\left[
\mathbb E|Q_i-1/2|
-\mathbb E|\bar Q_{i,t}-1/2|
\right]\ge0.
\tag{4.3}
\]

It records the information lost by coarsening for optimal binary prediction.

## 5. What the synthesis changes

The earlier hope was that the all-scale erasure curve might become more favorable than singleton restriction because conditional dependence accumulates at intermediate scales. Equation (2.1) shows the opposite for the uncentered certificate: every such accumulation appears with the *wrong sign* as extra nonnegative slack `C(t)+c_*J(t)`.

Hence the next viable APPROACH 11/12 implication must do at least one of the following:

1. use an **adaptive/non-Bernoulli selector** whose selection law is correlated with influence or phase, so that the endpoint-domination algebra no longer applies; or
2. introduce a **centered restricted potential** that explicitly refunds `C(t)+c_*J(t)` rather than trying to beat it; or
3. couple the fresh signed phase bank to a physical selector, since phase-sensitive signed divergence is not represented by the unsigned Bayes functional `G(t)`.

A concrete next target is therefore to build a physical adaptive block law `A` for which the signed/tangent-defect phase quantity produces a negative selector term before averaging. Reusing Bernoulli blocks and merely optimizing `t` is now provably sterile.

## 6. Ledger

**PROVED in this run:** (1.1)--(1.4), exact four-bank decomposition (2.1), endpoint domination (3.3)--(3.4), and the variance bank (4.2).

**KILLED:** the idea that a restriction-maximal FEI core can be forced to descend by searching for an interior Bernoulli erasure density in the existing scalar witness `D(t)>c_*G(t)` after the singleton endpoint has failed.

**OPEN:** construct a centered or adaptive physical-selector potential that converts the fresh tangent/phase stability into an actual descent, or close FEI by another route. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

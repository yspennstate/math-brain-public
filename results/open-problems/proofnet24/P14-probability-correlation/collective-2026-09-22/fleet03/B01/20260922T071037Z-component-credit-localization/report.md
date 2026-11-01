# FOREST fleet03/B01 — component-credit localization and marked-weight reduction

**Run:** 2026-09-22T07:10Z  
**Status:** ESSENTIAL_STEP_APPLIED; parent FOREST conjecture remains **OPEN**.  
**Brain status:** WITHOUT_VERIFIED_BRAIN.  
**Assignment:** determinant/integral/coupling representation of the actual uniform unrooted forest law, with an explicit unrooting argument.  
**Named partner:** fleet04/B02.

## 1. Inputs actually consumed

1. Campaign lead fleet01/B01 handoff `FOREST-HANDOFF-fleet01-B01-20260922T050946Z.md`, blob `4cee205cb7d254caf785692838111988a0b8a155`, whose current candidate is `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`. Its first unpaid universal implication is the STAR-2 contraction comparison created by conditioning on a triangle edge.
2. Named partner fleet04/B02 handoff `FOREST-HANDOFF-fleet04-B02-20260922T060937Z.md`, blob `0652edeb3af96be8642a68a7e957fe77a5104711`. On a disjoint-edge K5 witness it proves that a Hall/coupling proof preserving the full two-forest edge-multiplicity vector cannot carry all required mass; 106 units must cross at least one multiplicity coordinate.
3. fleet02/B02 handoff `FOREST-HANDOFF-fleet02-B02-20260922T060836Z.md`, blob `a1b5ca5e9886e1f9021fdc68d1bf06f82d1a36a5`, which correctly invalidates the earlier rank-degree homogenization shortcut. I do **not** use that invalid strengthening here.
4. fleet02/B03 handoff `FOREST-HANDOFF-fleet02-B03-20260922T061345Z.md`, blob `4c17f361f23133c2048906f198e84eefc9904b63`, which identifies the STAR-2 law with the uniform forest law on a smaller split graph conditioned on two terminals being disconnected, and notes that the unrestricted conditional statement is parent-hard.

The source literature also confirms that the actual *unrooted* spanning-forest model has a genuine non-Gaussian Grassmann integral representation: Caracciolo–Jacobsen–Saleur–Sokal–Sportiello, *Fermionic field theory for trees and forests* (PRL 93, 080601, 2004; arXiv:cond-mat/0403271), and Caracciolo–Sokal–Sportiello, *Grassmann Integral Representation for Spanning Hyperforests* (J. Phys. A 40, 13799–13835, 2007; arXiv:0706.1509). The relevant point for this run is structural: unrooting is not a plain Gaussian/determinantal root deletion; a bilocal four-fermion interaction is present. No sign theorem is inferred from that representation here.

## 2. Exact marked-weight homogeneity

For a positive weighted forest measure on a simple graph H, write

\[
Z=\sum_{F\text{ forest}}\prod_{a\in F}w_a,
\quad
Z_e=\sum_{F\ni e}\prod_{a\in F}w_a,
\quad
Z_{ef}=\sum_{F\ni e,f}\prod_{a\in F}w_a,
\]

and \(\Delta_{ef}=Z_eZ_f-ZZ_{ef}\).  Fix all weights except \(w_e\).  Since forests use each edge at most once,

\[
Z=A+w_eB,\qquad Z_e=w_eB,
\]
\[
Z_f=A_f+w_eB_f,\qquad Z_{ef}=w_eB_f.
\]

Therefore

\[
\Delta_{ef}=w_e(BA_f-AB_f).
\]

Repeating with \(f\) gives the exact identity

\[
\boxed{\Delta_{ef}(w_e,w_f,\mathbf w_{\rm rest})
      =w_ew_f\,\Delta_{ef}(1,1,\mathbf w_{\rm rest}).}
\]

Thus changing a positive weight on either *marked* edge cannot change the sign of the Rayleigh gap. The attached exact checker verifies this independently on a nontrivial four-vertex graph for several integer marked weights.

## 3. New STAR-2 localization: an unmarked doubled edge is necessary

Let a minimal simple counterexample be conditioned on a triangle edge \(g=uv\), then contract \(g\) and simplify the resulting parallel pairs. The simplified graph H has edge weights in \(\{1,2\}\); weight 2 occurs exactly on the star classes created by common neighbors of \(u,v\).

First reduce to the unique common block containing the two projected marked classes. Weighted forest partition functions factor over edge-biconnected blocks because every cycle is contained in one block. If the marks lie in different blocks then their covariance is exactly zero. If both are in one block B, then

\[
\Delta_H(e,f)=\left(\prod_{C\ne B}Z_C^2\right)\Delta_B(e,f).
\]

Hence doubled classes in other blocks are irrelevant to the sign.

Now suppose every doubled class in B is one of the marked classes themselves. If a mark comes from one member of a doubled preimage pair, conditional on \(g\in F\) the two preimages cannot both occur (they would complete the triangle), so the specific-edge indicator is a positive constant multiple of the simplified class indicator. If the two marks collapse to the same doubled class, they are mutually exclusive and the conditional covariance is already nonpositive. Otherwise they project to distinct classes, and the marked-weight identity above lets us change each marked class weight from 2 to 1 without changing the sign of the gap. We are left with the ordinary unit-weight forest law on the strictly smaller simple block B, which is nonnegative by edge-minimality.

Therefore any genuinely failing STAR-2 contraction stratum in a minimal counterexample must satisfy

\[
\boxed{\text{the common 2-connected marked block contains at least one UNMARKED doubled class}.}
\]

This sharpens the previous fleet02/B03 localization from “some doubled edge in the common block” to “some **unmarked** doubled edge in the common block.” It removes all contraction strata whose only multiplicity defects sit on the queried edges.

### Named-partner application

This conclusion matches fleet04/B02’s independent K5 obstruction in a nontrivial way. In the standard Rayleigh two-forest transport, the total multiplicity of each marked edge is fixed to one on both source and target sides. Thus the partner’s theorem that 106 units must cross *some* edge-multiplicity coordinate cannot be paid by either marked coordinate: the necessary cross-fiber movement is necessarily on an **unmarked** edge. The new STAR-2 localization identifies exactly the same kind of coordinate as the only possible local contraction obstruction. Consequently a viable coupling should be designed around globally moving an unmarked doubled class, not around reweighting the marks.

## 4. Exact unrooting by the u-component

The source-native STAR-2 law can be represented more sharply than a generic global conditioning. Let J be a simple graph and let \(u,v\) be distinct nonadjacent terminals. Condition the *uniform unrooted forest* of J on

\[
D=\{u\not\leftrightarrow v\}.
\]

For a conditional forest F let S be the vertex set of the component containing u. Then there is an exact bijection

\[
F
\longleftrightarrow
\bigl(S,\ T\in\mathcal T(J[S]),\ R\in\mathcal F(J[V\setminus S])\bigr),
\]

where \(u\in S\), \(v\notin S\), T is a spanning tree of the induced graph \(J[S]\), R is an arbitrary forest on the complementary induced graph, and every crossing edge is absent. Conversely every such triple produces a unique forest satisfying D whose u-component is exactly S.

Hence, with \(\tau\) denoting spanning-tree count and \(Z\) ordinary all-forest count,

\[
\boxed{
|\mathcal F(J);D|
=\sum_{S\ni u,\ v\notin S}
  \tau(J[S])\,Z(J[V\setminus S]).
}
\]

The conditional component law is

\[
\boxed{
\pi(S)=
\frac{\tau(J[S])Z(J[V\setminus S])}
     {\sum_{A\ni u,\ v\notin A}\tau(J[A])Z(J[V\setminus A])}.
}
\]

Conditional on S, the two pieces are **independent**: a uniform spanning tree of \(J[S]\) and a uniform unrooted forest of \(J[V\setminus S]\). This is an explicit unrooting representation that preserves every forest size, disconnected forests, and unit edge weights.

## 5. The first missing implication becomes a quantitative component-credit inequality

For marked edges e,f define

\[
m_e(S)=\Pr(e\in F\mid S),\qquad
c_{ef}(S)=\operatorname{Cov}(1_e,1_f\mid S).
\]

The law of total covariance gives the exact identity

\[
\boxed{
\operatorname{Cov}(1_e,1_f\mid D)
=\mathbb E_\pi[c_{ef}(S)]
 +\operatorname{Cov}_\pi(m_e(S),m_f(S)).
}
\]

In the edge-minimal-counterexample setting every stratum has \(c_{ef}(S)\le0\):

- if both marks lie inside S, the stratum is a uniform spanning tree and transfer-current/determinantal negative correlation applies;
- if both lie in the complement, it is the ordinary uniform forest law on a strictly smaller induced simple graph, so minimality applies;
- if the marks lie in opposite factors, the factors are independent;
- if a mark crosses the cut \((S,V\setminus S)\), its indicator is identically zero.

Put \(d_{ef}(S)=-c_{ef}(S)\ge0\). The STAR-2 debt is therefore reduced to the sharp quantitative inequality

\[
\boxed{
\operatorname{Cov}_\pi(m_e,m_f)
\le \mathbb E_\pi[d_{ef}(S)].
}
\]

This is materially narrower than the parent-hard statement “conditioning on \(u\not\leftrightarrow v\) always preserves NC”: it displays the exact negative credit available in every component stratum and the exact positive mixture term that must be paid.

## 6. Source-valid counterexample to the naive mixture-sign shortcut

One cannot hope to prove the last display merely by showing the mixture covariance is always nonpositive.

Take vertices \(\{0,1,2,3\}\), edges

\[
01,02,03,12,
\]

terminals \(u=1,v=3\), and marks \(e=01,f=02\). Note that u and v have common neighbor 0, so adding the missing edge 13 creates the exact triangle geometry relevant to STAR-2.

Condition on \(1\not\leftrightarrow3\). There are exactly 10 forests, with

\[
N_e=3,\quad N_f=4,\quad N_{ef}=1,
\]

so the conditional covariance is

\[
\frac1{10}-\frac3{10}\frac4{10}=-\frac1{50}.
\]

The u-component strata are exactly

| S | mass | m_e(S) | m_f(S) | c_ef(S) |
|---|---:|---:|---:|---:|
| {1} | 4 | 0 | 1/2 | 0 |
| {0,1} | 1 | 1 | 0 | 0 |
| {1,2} | 2 | 0 | 0 | 0 |
| {0,1,2} | 3 | 2/3 | 2/3 | -1/9 |

Therefore

\[
\boxed{\operatorname{Cov}_\pi(m_e,m_f)=\frac1{75}>0,}
\]

while

\[
\mathbb E_\pi[c_{ef}(S)]=-\frac1{30},
\qquad
-\frac1{30}+\frac1{75}=-\frac1{50}.
\]

Thus a correct proof must genuinely compare the positive cross-stratum correlation against the negative UST/smaller-forest credit. The mixture term itself can have the wrong sign even in a four-vertex source-valid STAR-2 geometry.

The attached checker verifies all counts, the component-weight formula, the covariance decomposition, and marked-weight homogeneity exactly using rational arithmetic; it ends `ALL_EXACT_ASSERTIONS_PASSED`.

## 7. What this eliminates and what remains

Eliminated as universal shortcuts:

1. fixing a STAR-2 failure by changing only marked weights;
2. searching for a counterexample whose only doubled classes in the marked block are the marks;
3. proving the component-mixture covariance is always nonpositive;
4. relying on the withdrawn rank-degree homogenization strengthening.

The first surviving universal obligation is now:

> **Component-credit obligation.** In the lead’s edge-minimal triangle-conditioning configuration, with the common marked 2-connected block containing at least one **unmarked** doubled class, prove
> \[
> \operatorname{Cov}_\pi(m_e,m_f)\le\mathbb E_\pi[d_{ef}(S)],
> \]
> or produce a genuine source-valid counterexample.

A coupling proof must be allowed to move an unmarked multiplicity coordinate, exactly as forced by fleet04/B02’s K5 flow audit. The component-set variable S is a natural global coordinate on which such a cross-fiber move can act.

## 8. Classification

`ESSENTIAL_STEP_APPLIED` — the parent Grimmett–Winkler uniform-forest negative-correlation conjecture is **not** claimed solved. This run supplies two exact universal reductions plus a source-valid counterexample to a tempting sign shortcut, and sharpens the next target for the lead.

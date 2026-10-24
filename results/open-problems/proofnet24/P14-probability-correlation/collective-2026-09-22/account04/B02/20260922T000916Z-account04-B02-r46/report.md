# FOREST / account04-B02 — triangle-completion switching identity

Run: `20260922T000916Z-account04-B02-r46`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED (structural elimination only; parent conjecture remains OPEN)**  
Brain status: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact assignment and consumed peer

The active owner control supersedes the former runtime-dependency assignment. The current source-exact target is the Grimmett--Winkler conjecture for the uniform law on **all unrooted forests** of every finite simple graph:

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F)
\]

for every distinct edge pair. Equivalently, with `Z` the number of forests and `Z_e,Z_f,Z_ef` the required-edge counts,

\[
\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.
\]

The exact account04/B02 assignment is to attack the current comparison by a different exchange/coupling construction, retain exact component multiplicities, and compare in formulas with `account01/B03`.

I consumed the complete partner snapshot

`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B03/20260921T234923Z-b03-poprestore-r11/overlap_reconnection_report.md`.

For adjacent distinguished edges `e=ab`, `f=ac`, that report partitions forests of `G-{e,f}` by the terminal partition of `{a,b,c}`. With

- `A=w_{abc}`,
- `B=w_{ac|b}`,
- `C=w_{ab|c}`,
- `Q=w_{a|bc}`,
- `D=w_{a|b|c}`,

it proves the exact formula

\[
\tag{R3}
\Delta_{G}(e,f)=BC-AD+Q(B+C+D+Q).
\]

The partner also showed that trying to force `Cov(X_e,X_f)<=0` at the addability level is false; the overlap reservoir `Q` is essential.

I additionally checked the compatible account03/B02 minimal-counterexample snapshot. It independently derives a deletion/contraction sign-coherence condition for any lexicographically minimal counterexample. The theorem below does not depend on that result, but combines with it in §5.

## 2. New construction: complete the open wedge by one edge

Fix distinct vertices `a,b,c`. Let

\[
e=ab,\qquad f=ac,\qquad h=bc.
\]

Let `K` be any finite graph on the same vertex set with none of `e,f,h` present. Give the edges of `K` arbitrary positive weights. For each forest `H` of `K`, retain its full multiplicative weight and classify it by the connectivity partition induced on `{a,b,c}`. Let `A,B,C,Q,D` be the corresponding **weighted** sums in the five states listed above.

Give `h` weight `z>=0`; the weights of `e,f` may be arbitrary positive values. Because the forest polynomial is multiaffine, the Rayleigh difference for `e,f` is independent of the actual `e,f` weights, so they can be set to one for the calculation.

For a fixed base forest `H`, the allowed subsets of `{e,f,h}` are determined solely by its terminal partition:

- state `A=abc`: contribution `1`;
- state `B=ac|b`: contribution `1+x+z`;
- state `C=ab|c`: contribution `1+y+z`;
- state `Q=a|bc`: contribution `1+x+y`;
- state `D=a|b|c`: contribution `1+x+y+z+xy+xz+yz`.

Thus the exact three-edge forest polynomial is

\[
P(x,y,z)=A+B(1+x+z)+C(1+y+z)+Q(1+x+y)
+D(1+x+y+z+xy+xz+yz).
\]

No rooted, spanning-tree, fixed-size or independence approximation is introduced here; `A,B,C,Q,D` contain the complete outside-graph multiplicities.

## 3. Triangle-completion identity

Differentiate in `x,y` and evaluate `x=y=1`. Direct expansion gives

\[
\Delta_{ef}(z)=P_xP_y-PP_{xy}
\]

and hence

\[
\boxed{
\Delta_{ef}(z)
=BC-AD+Q(B+C+D+Q)+Dz\bigl(D(1+z)+2Q\bigr).
}
\tag{T1}
\]

The first five-state term is exactly the partner's formula (R3). Therefore

\[
\boxed{
\Delta_{ef}(z)-\Delta_{ef}(0)
=Dz\bigl(D(1+z)+2Q\bigr)\ge0.
}
\tag{T2}
\]

Since the empty base forest belongs to the all-separate state, `D>0`. Consequently the increase is **strict for every z>0**.

At unit weight on the closing edge,

\[
\boxed{
\Delta_{K+e+f+h}(e,f)
-
\Delta_{K+e+f}(e,f)
=2D(D+Q)>0.
}
\tag{T3}
\]

This is the requested multiplicity-preserving switch/comparison: adding the closing edge of an adjacent distinguished pair cannot make their Rayleigh gap worse, and at unit weights strictly improves it. The exact surplus is twice the product of the all-separate reservoir with the union of the all-separate and parallel-reconnection reservoirs.

### Proof audit

The only structural input is the quotient of each base forest into its connected components. In the five terminal states, the three potential edges become respectively: three loops; one loop plus two parallel edges; one loop plus two parallel edges; one loop plus two parallel edges; or a triangle on three quotient vertices. The displayed state polynomials are therefore exhaustive and disjoint. Differentiation of their weighted sum proves (T1). All coefficients are nonnegative weighted forest sums, and `D>=1` at unit outside weights because the empty forest is counted, proving strictness in (T2)-(T3).

## 4. Minimal-counterexample consequence

Choose a simple source counterexample lexicographically minimal in `(|V|,|E|)`, and let an adjacent pair `e=ab,f=ac` violate the conjecture:

\[
\Delta_G(e,f)<0.
\]

Then the outer endpoints **cannot be adjacent**.

Indeed, suppose `h=bc` is an edge of `G`. Put `G'=G-h`. This has the same number of vertices and fewer edges, so minimality gives

\[
\Delta_{G'}(e,f)\ge0.
\]

Apply (T3) with `K=G-{e,f,h}`. Then

\[
\Delta_G(e,f)
=
\Delta_{G'}(e,f)+2D(D+Q)
>0,
\]

contradiction.

Therefore:

### `FOREST-MINIMAL-OPEN-WEDGE-20260922`

In a lexicographically minimal simple counterexample, every violating adjacent pair is an **induced open wedge**: if `e=ab` and `f=ac` are positively correlated, then `bc` is absent.

Equivalently, every pair of edges belonging to a triangle has **strictly negative covariance** in a lexicographically minimal counterexample.

This is a true all-orders structural restriction on the unresolved counterexample, not a theorem for a convenient graph family.

## 5. Combination with the other-account sign-cluster result

The current account03/B02 snapshot proves, conditionally on lexicographic minimality, that violating pairs form equivalence classes under `e~f iff Delta(e,f)<0`.

Combining that proved candidate with `FOREST-MINIMAL-OPEN-WEDGE-20260922` yields a sharper necessary condition:

> every nontrivial bad equivalence class meets every triangle in at most one edge; if two class edges share a vertex, their two outer endpoints are nonadjacent.

Thus any future construction of a minimal counterexample has to satisfy both global sign coherence and local triangle exclusion. Conversely, a proof that a surviving 3-connected obstruction forces one bad class to contain two edges of a triangle would close that branch immediately.

No such global forcing statement is proved here.

## 6. Exact positive and negative tests

`triangle_completion_check.py` independently enumerates the source-valid unrooted forest law for every labelled residual graph `K` on `3,4,5` vertices and every choice of three distinct terminals. It separately computes the Rayleigh gaps before and after adding the closing edge and compares them with (R3) and (T3).

Executed result:

- residual/terminal instances: `3939`;
- identity failures: `0`;
- strict-monotonicity failures: `0`;
- minimum unit increment: `2`;
- deliberate negative control, omitting the `D^2` contribution: **rejected**, already on the empty three-terminal base;
- direct recheck of account01/B03's `K4-(2,3)` witness: base terminal tuple `(A,B,C,Q,D)=(0,0,1,0,3)`, gap without `h` = `0`, gap with `h` = `18`, and (T3) predicts exactly `18`.

Checker SHA-256: `02b4e0902c50a626dfc867dc829c74f43d3de795c6caac22c219ad21cd5d982f`.

The finite enumeration is an audit of the exact algebra, not evidence that the universal conjecture is solved.

## 7. Literature/source-status check

A fresh bounded 22 September 2026 search recovered recent special-case work, including Tang--Zhang on sufficiently large complete-graph spanning-subgraph families and Bado on wheel graphs, but no source-matching all-finite-graph uniform-unrooted-forest proof. This is not a worldwide novelty certificate. The parent problem remains labelled OPEN.

## 8. What remains

The partner's universal missing inequality remains

\[
n_{00}n_{11}\le n_{10}n_{01}+Nq.
\]

This run does **not** prove that inequality for arbitrary pairs. It removes one exact local configuration from any lexicographically minimal counterexample and supplies a weighted closure operation for the adjacent-pair case.

The next useful route is not another small-graph census. It is to combine the open-wedge theorem with 3-connectivity: for a violating induced wedge `b-a-c`, use two internally disjoint `b`--`c` reconnection routes in `G-a` and attempt a path-shortening/switching argument that either creates a forbidden triangle inside the bad sign class or pays the partner's overlap reservoir `Q` with controlled multiplicity. That is the first still-unpaid structural step.

## 9. Scope/integrity

No installation work was continued after the current owner control was read. No production state, benchmark data, email, Drive, scheduler setting, permission, paid service, remote workflow, or unrelated private material was touched. The mathematical files contain only source-bound definitions, small exact graph fixtures and repository-relative references. Novelty and target-level closure are not claimed.

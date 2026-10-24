# FOREST / account03-B01 — exact activity coupling for the unrooted forest law

Run: `20260922T003307Z-account03-B01-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED (exact coupling/reduction; parent conjecture remains OPEN)**  
Brain status: **WITHOUT_VERIFIED_BRAIN**

## 1. Source target, role transition, and peer actually consumed

The fresh owner control supersedes this slot's former brain-installer assignment. The effective account03/B01 assignment is now to try a determinant/integral or **coupling representation of the actual uniform unrooted forest law** that supplies the missing sign, with any rooted-forest identity accompanied by an explicit unrooting argument.

The source target is the Grimmett--Winkler pairwise negative-correlation conjecture: for every finite simple graph `G`, with `F` uniform on **all** acyclic edge subsets,

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F),
\]

or, with `Z,Z_e,Z_f,Z_ef` the corresponding integer forest counts,

\[
\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.
\]

I consumed the exact named other-account partner snapshot

`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B02/20260922T000916Z-account04-B02-r46/report.md`

(blob `47f7f2ae8703696df361ce78033b50c51212fa23`). For adjacent `e=ab,f=ac`, it proves the triangle-completion identity

\[
\Delta_{ef}(z)=BC-AD+Q(B+C+D+Q)+Dz(D(1+z)+2Q),
\]

so in a lexicographically minimal counterexample a violating adjacent pair must be an induced open wedge.

I also consumed the team lead snapshot

`account01/B01/20260922T000824Z-account01-B01-forest-11/report.md`

(blob `367d85a8c6ac4ef3f00e1686a28eac60642274e0`), which derives the universal Simpson inequality in a minimal counterexample and proves that the graph of positively correlated edge-pairs is a matching. Finally, I used account01/B03's exact overlap reduction

`account01/B03/20260921T234923Z-b03-poprestore-r11/overlap_reconnection_report.md`

(blob `4dbaa2d764eddbc02026736e5b1fe265ba14f24d`): for `K=G-{e,f}`, if `q` counts forests `H` for which `e` and `f` are individually addable but jointly create a cycle, then

\[
\Delta_G(e,f)=n_{10}n_{01}-n_{00}n_{11}+Nq.
\tag{1.1}
\]

This run attacks that same `q` term from a different representation rather than discarding it.

The three explicit method changes from the standing research rules are: **#1 change category** (forests to activity-weighted spanning trees), **#18 say it in another language** (Crapo activity intervals), and **#25 count the same thing twice** (the overlap reservoir `q` as an exact basis-exchange mass).

## 2. Exact unrooting by internal-activity cubes

It is enough to treat connected `G`. If `e,f` lie in distinct connected components, the forest law factorizes and the covariance is exactly zero. If they lie in one component `G_0`, all other components multiply every relevant count and hence multiply `Delta` by a positive square.

Fix a connected finite simple graph and a total edge order. For a spanning tree `T`, let `IA(T)` be the set of internally active tree edges: `g in T` is internally active when it is the least edge in its fundamental cut. Put

\[
i(T)=|IA(T)|,\qquad w(T)=2^{i(T)}.
\]

The independent sets (forests) have the disjoint activity decomposition

\[
\mathcal F(G)=\bigsqcup_T\{F:T\setminus IA(T)\subseteq F\subseteq T\}.
\tag{2.1}
\]

For completeness, the owner tree of a forest `F` is the lexicographically least spanning tree containing `F`. If `g in T-F` were not internally active, a smaller edge in its fundamental cut would exchange with `g` and give a lexicographically smaller spanning tree still containing `F`, contradiction. Conversely, if `T\setminus IA(T) subseteq F subseteq T` and a lexicographically smaller tree `T'` also contained `F`, the least edge of `T'\T` together with its fundamental cycle in `T` would exhibit a smaller edge in the fundamental cut of some `g in T\T' subseteq T\F`, forcing that omitted `g` to be internally passive, contradiction. Thus the owner is unique and (2.1) follows.

Therefore the **actual uniform unrooted forest law** has the exact two-stage coupling:

1. choose a spanning tree `T` with probability
   \[
   \mu(T)=\frac{2^{i(T)}}{\sum_S2^{i(S)}};
   \]
2. conditional on `T`, keep every internally passive edge of `T`, and independently keep each internally active edge with probability `1/2`.

No root, determinant normalization, fixed number of components, or spanning-tree replacement is being assumed. It is literally a partition of all unrooted forests. In particular

\[
Z=\sum_T w(T).
\tag{2.2}
\]

This supplies the requested explicit unrooting step.

## 3. Put the marked pair first and identify the overlap reservoir

Now fix distinct marked edges `e,f` and choose the total order with

\[
e<f<\text{every other edge}.
\]

Define the exchangeable-tree class

\[
\mathcal A_f(e)=\{T:\ f\in T,\ e\notin T,\ T-f+e\text{ is a spanning tree}\}.
\tag{3.1}
\]

Let `q` be exactly the overlap count in account01/B03: forests `H` of `G-{e,f}` such that `H+e` and `H+f` are forests while `H+e+f` is cyclic.

### Theorem 3.1 — overlap = activity-weighted basis exchange

\[
\boxed{q=\sum_{T\in\mathcal A_f(e)}2^{i(T)}.}
\tag{3.2}
\]

**Proof.** Take an overlap forest `H` and set `F=H+f`. Let `T` be the unique activity-cube owner of `F`.

We have `f in T`. If `e in T`, then `e`, being globally least, is internally active. Since `F` omits `e`, the cube condition gives `F subseteq T-e`. The endpoints of `e` are disconnected in `T-e`, hence also in `F`, contradicting that `F+e=H+e+f` is cyclic. Therefore `e notin T`.

Because `F+e` is cyclic and `F subseteq T`, the whole fundamental `T`-path between the endpoints of `e` is present in `F`. Because `H+e=F-f+e` is acyclic, `f` lies on that path. Equivalently `T-f+e` is a spanning tree, so `T in A_f(e)`.

Conversely let `T in A_f(e)`. The edge `e` crosses the fundamental cut of `f`, so `f` is not internally active. Every other tree edge `g` on the fundamental cycle `C_T(e)` is also internally inactive, because the globally least edge `e` crosses the fundamental cut of `g`. Hence every forest `F` in the activity cube of `T` contains `C_T(e)-e`, including `f`. Put `H=F-f`. Then `H+f=F` is a forest; `H+e` is a forest because deleting `f` broke the unique `T`-path between the endpoints of `e`; and `H+e+f` contains `C_T(e)`. Thus every one of the `2^{i(T)}` cube forests produces an overlap state. Distinct activity cubes are disjoint, so all produced `H` are distinct and (3.2) follows. QED.

This identifies the positive correction in (1.1) with a concrete spanning-tree exchange mass instead of a terminal-state remainder.

## 4. Exchange doubles the activity weight exactly

For `T in A_f(e)`, put `T'=T-f+e`. Then

\[
\boxed{IA(T')=IA(T)\cup\{e\}},\qquad \boxed{w(T')=2w(T)}.
\tag{4.1}
\]

Indeed `e` is internally active in `T'` because it is globally least, while `f` is internally inactive in `T` because `e` crosses its fundamental cut. For a common tree edge `g` on `C_T(e)-{e,f}`, `e` crosses the fundamental cut in `T`, so `g` is inactive there; in `T'`, the edge `f` crosses the corresponding fundamental cut and is smaller than `g`, so `g` remains inactive. For a common edge outside the exchange cycle, `e` and `f` lie within the same component of `T-g`, so the fundamental cut is unchanged by the swap and the activity status of `g` is unchanged. This proves (4.1).

Consequently the activity weight of the reverse exchange class is exactly

\[
\sum_{T':e\in T',f\notin T',\,T'-e+f\text{ tree}}w(T')=2q.
\tag{4.2}
\]

## 5. Exact marked-edge count identities

Write

\[
W=\sum_Tw(T),\quad W_e=\sum_{T:e\in T}w(T),\quad W_f=\sum_{T:f\in T}w(T),\quad W_{ef}=\sum_{T:e,f\in T}w(T).
\]

Then the activity coupling gives

\[
\boxed{W=Z},\qquad
\boxed{W_e=2Z_e},\qquad
\boxed{W_{ef}=4Z_{ef}},\qquad
\boxed{W_f+q=2Z_f}.
\tag{5.1}
\]

The first identity is (2.2). Whenever `e in T`, it is internally active, so exactly half the forests in that cube contain `e`, proving `W_e=2Z_e`. Whenever both `e,f in T`, both are internally active: `e` is globally least, while the only edge below `f` is the different tree edge `e`, which cannot cross the fundamental cut of `f`; hence exactly one quarter of the cube contains both, proving `W_ef=4Z_ef`.

For `f`, the only way it fails to be internally active is precisely `T in A_f(e)`: because the only edge below `f` is `e`, inactivity means `e` crosses `f`'s fundamental cut, equivalently `T-f+e` is a tree. Thus `f` is kept with probability `1/2` in every other `f`-tree cube and with probability `1` on the exchange class. The extra half-cube mass is `q/2` by (3.2), giving `W_f+q=2Z_f`.

Substitution into the original Rayleigh numerator gives the exact reduction

\[
\boxed{
4\Delta_G(e,f)=W_e(W_f+q)-W W_{ef}.
}
\tag{5.2}
\]

Equivalently, under the activity-weighted spanning-tree law `mu(T)=w(T)/W`, the original unrooted-forest inequality for the ordered pair `e<f` is exactly

\[
\boxed{
\Pr_\mu(f\in T\mid e\in T)-\Pr_\mu(f\in T)\le \frac{q}{Z}=\mu(\mathcal A_f(e)).
}
\tag{5.3}
\]

This is not yet a proof of the conjecture. It is a source-exact change of variables in which the overlap payment is itself a basis-exchange probability.

## 6. How it combines with the cross-account structural results

The partner account04/B02 proved that a violating adjacent pair in a lexicographically minimal counterexample is an induced open wedge. The lead account01/B01 proved that any violating pair is the unique positive-correlation partner of each of its two edges, with every external edge negatively correlated to both.

Equation (5.3) adds a complementary global representation: after putting the marked pair first in the activity order, every possible excess of `f` under conditioning on `e` in the activity-weighted spanning-tree law must be paid by the **specific one-edge basis-exchange class** `A_f(e)`. By account01/B03, `q>0` exactly when `e,f` share a cycle, so for a 3-connected minimal-counterexample pair this payment is present but completely localized.

The next unpaid statement is therefore no longer an unspecified rooted/unrooted transfer. It is the precise activity-basis inequality

\[
\Pr_\mu(f\mid e)-\Pr_\mu(f)\le\mu(\mathcal A_f(e)).
\tag{6.1}
\]

A successful injection/coupling on spanning trees proving (6.1), with the activity weights respected, would prove the source inequality. A counterexample to (6.1) is automatically a counterexample to the source inequality because (5.2) is an identity; unlike previous stronger conditioning lemmas, there is no scope gap.

The natural next recipient is the FOREST lead `account01/B01` and the switching workers. The useful object to transport is not only (6.1), but the exact weight-doubling exchange (4.1), which may allow a sign-reversing or mass-transport pairing between `e,f`-containing trees and the one-sided exchange classes.

## 7. Exact finite audit

`activity_unrooting_check.py` is a standard-library exact enumerator. For every connected labelled simple graph on 2 through 5 vertices and every **ordered** distinct present-edge pair, it independently constructs all forests, all spanning trees, internal activities under the order `e<f<others`, the activity cubes, the overlap count `q`, and both exchange classes. It checks:

- the activity cubes are a disjoint exact partition of all forests;
- `sum_T 2^i(T)=Z`;
- `sum_{A_f(e)}2^i(T)=q`;
- the reverse exchange mass is `2q`;
- `IA(T-f+e)=IA(T) union {e}` on every exchange;
- all four identities in (5.1);
- the Rayleigh identity (5.2).

Executed output:

```text
connected_graphs_n2_to_n5=771
ordered_distinguished_pairs=20898
q_positive_pairs=14934
identity_failures=0
ALL_EXACT_CHECKS_PASSED
```

Checker Git blob: `ccfc64f032d9a83026d53cfaf04ff4a8276b606a`.  
Checker SHA-256: `c041fec011e1da7d4b343f99467dcae895746b0c7442bfae87fac8da2fae210f`.  
Output Git blob: `9f394fd3497b3547409f2da0e643e2499f386598`.  
Output SHA-256: `9164571d7329877185cd6930bf2fc8f48486144ddeb5ffe08c3d09398f331e4c`.

The enumeration audits the identities; the proofs above are the universal argument. It is not evidence by itself for the still-open inequality (6.1).

## 8. Status

- Parent Grimmett--Winkler conjecture: **OPEN**.
- New proved step in this run: exact activity-cube coupling of the actual uniform unrooted forest law; exact identification of the overlap reservoir with activity-weighted basis exchanges; exact exchange weight-doubling; exact spanning-tree reformulation (5.2)/(5.3).
- Outcome: **ESSENTIAL_STEP_APPLIED**.
- External novelty/priority of these deductions: **UNVERIFIED**. No priority claim is made.
- Brain use: **WITHOUT_VERIFIED_BRAIN**. The latest owner control explicitly suspended new installation work for B01; repository access is not native brain retrieval.
- Next exact obligation: prove or refute (6.1) using the activity-weighted exchange geometry, preferably combining the partner's induced-open-wedge restriction and the lead's matching/Simpson constraints.

No email, Drive, public release, scheduler mutation, benchmark material, credentials, unrelated private data, or production brain state was used or changed.

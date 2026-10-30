# FOREST / fleet04 B03 — full-support lemma and a local-cone obstruction

Run: `20260922T001033Z-B03-r43`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Target: Grimmett--Winkler pairwise negative correlation for the uniform law on all unrooted forests of every finite simple graph.  
Outcome: **ESSENTIAL_STEP_APPLIED** for the 3-connected full-support lemma below, and **CANDIDATE_REFUTED** for a purely local three-edge-cone closure. The parent conjecture remains **OPEN**.  
Brain status: **WITHOUT_VERIFIED_BRAIN**.

## 1. Control transition and source boundary

Fresh owner control supersedes this slot's older brain-installation assignment. B03 is now a FOREST proof worker; no new installation or benchmark work is part of this run. Existing installation artifacts were left unchanged.

The source-exact target is: for every finite simple graph `G`, if `F` is uniform over all acyclic edge subsets, including the empty forest and disconnected forests of every size, then for every distinct pair of edges `e,f`,

`P(e,f in F) <= P(e in F) P(f in F)`.

At unit weights, writing `Z` for the number of forests, `Z_e` for forests containing `e`, and `Z_ef` for forests containing both,

`Delta_G(e,f) := Z_e Z_f - Z Z_ef >= 0`.

I reread the canonical P0001 claim and the current shared FOREST target before using inherited work. The bounded current-source check in the shared target still treats the general finite-graph conjecture as open; known wheel, complete-graph/fixed-component, cactus and finite-order results are inputs rather than closure.

The assigned partner is `fleet01/B01`. At the bounded observation point I did not locate a finalized current collective report from that exact slot, so under the live missing-peer rule I did not wait. I instead consumed two finalized other-account results that directly constrain this integrator step:

1. `fleet01/B03/.../overlap_reconnection_report.md`: the exact reconnection identity and the universal residual `R4`.
2. `fleet03/B02/.../report.md`: the exact deletion/contraction identity and sign-cluster theorem for a lexicographically minimal counterexample.

No peer PASS label is imported; the formulas are used explicitly below.

## 2. Peer interface A: exact reconnection residual

For distinct `e,f`, put `K=G-{e,f}` and let `H` range over all forests of `K`. Let

`X(H)=1{H+e is a forest}`, `Y(H)=1{H+f is a forest}`,

and let `n_ij` count forests with `(X,Y)=(i,j)`. Put `N=sum n_ij`. Let `q` count forests with `X=Y=1` for which `H+e+f` is cyclic.

The fleet01/B03 identity is

**(R1)**  `Delta_G(e,f) = n10*n01 - n00*n11 + N*q`.

Thus the source target for this pair is exactly

**(R4)**  `n00*n11 <= n10*n01 + N*q`.

The overlap term is essential: fleet01/B03 gave an exact four-vertex witness where `Cov(X,Y)>0` but the positive `q` term still makes the true Rayleigh gap positive.

## 3. Peer interface B: minimal-counterexample sign clustering

Fleet03/B02 proved the exact three-edge identity, for a third edge `g`,

`AB Delta_G(e,f) = B Z D0 + A Z D1 - Delta_G(g,e) Delta_G(g,f)`,

where `D0,D1` are the `e,f` Rayleigh gaps in the deletion and contraction strata for `g`.

In a lexicographically minimal simple counterexample, minor minimality gives `D0,D1>=0`. Hence if `Delta_G(e,f)<0`, then for every third edge `g`,

`Delta_G(g,e) Delta_G(g,f) > 0`.

Therefore bad pairs (`Delta<0`) form equivalence classes, and every edge outside a nontrivial bad class has strictly positive Rayleigh gap to every edge inside it.

The inherited structural reduction also permits a lexicographically minimal counterexample to be taken 3-connected. The new step below uses that 3-connectivity directly at the reconnection interface.

## 4. New theorem: every reconnection reservoir is nonempty in a 3-connected graph

### Theorem `FOREST-3CONN-FULL-SUPPORT-20260922`

Let `G` be a finite simple 3-vertex-connected graph and let `e,f` be distinct edges. For the `n_ij,q` notation above,

`n00 >= 1`, `n10 >= 1`, `n01 >= 1`, `n11-q >= 1`, and `q >= 1`.

Equivalently, all four addability cells occur, the overlap reservoir is nonempty, and the `11` cell contains at least one state that is not an overlap state.

### Proof

Write `e=ab`.

**(i) `n00>=1`.** A 3-vertex-connected graph is 3-edge-connected. Hence deleting the two edges `e,f` leaves `K` connected. Choose any spanning tree `T` of `K`. The endpoints of both `e` and `f` are connected in `T`, so neither edge is addable to `T`; thus `T` has type `00`.

**(ii) `n11-q>=1`.** Take `H` to be the empty forest of `K`. Each of the two distinct simple edges is individually addable. Adding both distinct edges to the empty graph is still acyclic: they are either disjoint or form a two-edge path, since a simple graph has no parallel two-edge cycle. Hence `H` is a safe `11` state and is not counted by `q`.

**(iii) `n01>=1`.** The graph `G-e` is 2-vertex-connected. Indeed, for every vertex `v`, `G-v` is 2-connected, so deleting the additional edge `e` cannot disconnect `G-v`; hence `(G-e)-v` is connected for every `v`.

Therefore `G-e` contains two internally vertex-disjoint `a-b` paths, say `P1,P2`.

- If `f` is adjacent to `e`, let `c` be the endpoint of `f` not equal to the shared endpoint. At most one of `P1,P2` contains `c` internally, so choose a path `P` avoiding `c`. Its edge set avoids `f`, connects the endpoints of `e`, and does not connect the endpoints of `f`.
- If `f=cd` is disjoint from `e`, the two internally disjoint `a-b` paths cannot both contain both `c` and `d`. Choose one, `P`, that does not contain both. Then `P` cannot use the edge `f`; it connects `a,b` but does not connect `c,d`.

In either case, with `H=E(P)`, `H` is a forest contained in `K`; `e` is not addable but `f` is addable. Thus `H` has type `01`.

**(iv) `n10>=1`.** Interchange `e` and `f` in the preceding argument.

**(v) `q>=1`.** A 3-connected graph is 2-connected, and in a 2-connected graph any two edges lie on a common cycle. One proof is to subdivide the two edges and use the standard fact that any two vertices of a 2-connected graph lie on a common cycle. Let `C` be a cycle containing both `e,f`, and set `H=C-{e,f}`. Then `H` is a forest in `K`, each distinguished edge is individually addable, while adding both reconstructs the cycle `C`. Hence `H` contributes to `q`.

This proves all five strict support assertions. `square`

### Boundary check

The proof does not assume `e,f` are disjoint, does not assume `G-{e,f}` is 2-connected, and does not replace the unrooted forest law by a spanning-tree law. Disconnected `H` are allowed throughout. Simplicity is used only for the safe empty `11` state.

A direct exact sanity enumeration over all labelled 3-connected simple graphs on 4 and 5 vertices found no support failure: 1 graph / 15 marked edge pairs at order 4, and 26 graphs / 825 marked edge pairs at order 5. This is only a check of the theorem, not evidence for the universal conjecture.

## 5. Consequence for a minimal violating pair

For a lexicographically minimal 3-connected counterexample and a violating pair `e,f`, (R4) must fail strictly. Since all quantities are integers, the full-support lemma yields

`n00*n11 >= n10*n01 + N*q + 1`.

Using `n10,n01,q >= 1`,

`n00*n11 >= N + 2`.

Also `N=n00+n10+n01+n11 >= n00+n11+2`, hence

`n00*n11 >= n00+n11+4`,

or

`(n00-1)(n11-1) >= 5`.

In particular the abstract four-cell population of a minimal violation must have `N>=9`. This is a necessary integer constraint only; it is not claimed that every feasible tuple is graph-realizable.

This improves the integrator interface by ruling out boundary-support explanations of a putative 3-connected violation: a counterexample must beat the overlap reservoir despite all ordinary switch target cells being nonempty.

## 6. Adversarial test: the local three-edge cone still permits the bad sign pattern

The next tempting closure is to combine:

1. the fleet01 reconnection identity (R1),
2. the new full-support conditions, and
3. the fleet03 deletion/contraction sign-cluster conditions,

inside only the local three-edge graphic-matroid cone for `{e,f,g}`.

That route is **false** without an additional global compatibility constraint.

For each outside-forest state, contracting its components induces a graphic matroid on the three distinguished edges. Consider the following nonnegative integer mixture of valid three-edge graphic matroid types:

- weight 2: `f` is a loop and `e,g` are parallel;
- weight 2: `e` is a loop and `f,g` are parallel;
- weight 3: `g` is a loop and `e,f` are free;
- weight 1: `U_{2,3}`, the triangle matroid.

The resulting exact selected-subset counts are

`w(empty)=8, w(e)=6, w(f)=6, w(g)=5, w(ef)=4, w(eg)=1, w(fg)=1, w(efg)=0`,

so

`Z=31, Z_e=11, Z_f=11, Z_g=7, Z_ef=4, Z_eg=1, Z_fg=1`.

Therefore

`Delta(e,f)=11*11-31*4=-3`,

but

`Delta(e,g)=Delta(f,g)=11*7-31*1=46>0`.

Thus `e,f` have the forbidden positive covariance while the third edge `g` has exactly the strict external sign required by the fleet03 sign-cluster theorem.

The two `g` strata are individually nonnegative for the `e,f` pair:

- `g=0`: `(A,Ae,Af,Aef)=(24,10,10,4)`, so `D0=10*10-24*4=4`;
- `g=1`: `(B,Be,Bf,Bef)=(7,1,1,0)`, so `D1=1`.

The fleet01 reconnection cells for `e,f` are

`(N,n00,n10,n01,n11,q)=(13,4,2,2,5,1)`,

with `n11-q=4`. Hence **every reservoir in the new theorem is strictly positive**, yet

`n10*n01 - n00*n11 + N*q = 4-20+13 = -3`.

The exact arithmetic is independently archived in `local_cone_witness_check.py` and `local_cone_witness_check.out`, which end in `LOCAL_CONE_WITNESS_PASS`.

### What this does and does not refute

This is **not** claimed to be the restriction of one globally realizable finite simple graph, so it is **not a counterexample to Grimmett--Winkler**.

It is a counterexample to the proof strategy that uses only:

- nonnegative membership in the local three-edge graphic-matroid mixture cone,
- the fleet01 reconnection identity/support conditions, and
- the fleet03 minor nonnegativity/sign-cluster inequalities.

Those local constraints are jointly consistent with a source violation. Therefore a successful all-graphs proof must use a genuinely global compatibility relation tying the outside-forest types together inside one graph.

## 7. Compact conditional end-to-end argument after this run

A lexicographically minimal source counterexample may be taken 3-connected. Fix a violating pair `e,f`.

1. Fleet01/B03 reduces the target exactly to (R4).
2. This run proves every ordinary switch cell, the overlap reservoir, and a safe `11` reservoir are nonempty in the 3-connected obstruction.
3. Fleet03/B02 forces every third edge to see `e` and `f` with the same strict Rayleigh sign and partitions all violating pairs into bad equivalence classes.
4. The local-cone witness above proves that steps 1--3 alone cannot contradict a violation.
5. **First remaining essential implication:** derive a graph-global compatibility inequality among the outside-forest three-edge types (equivalently, among terminal connectivity partition weights) that is absent from the abstract local cone and is strong enough to force (R4) in a 3-connected graph.

A useful next formulation is to expose the outside forest `J=H-{g}` and require that all local matroid types arise from the *same* ambient graph as `J` varies. The missing inequality must exploit transitions between such outside states (or a separator/cycle-space conservation law), not merely pointwise matroid type membership.

## 8. Status and handoff

**Parent target:** OPEN.  
**New valid step:** `FOREST-3CONN-FULL-SUPPORT-20260922`.  
**Eliminated route:** local three-edge-cone + sign-cluster + minor nonnegativity alone cannot close the conjecture.  
**Next recipient:** FOREST lead / switching and separator workers. The next proof attempt should target a global consistency constraint on the outside-forest type weights and test it against the exact local witness above before promotion.

No novelty/priority claim is made. No production data, private unrelated material, benchmark answer, email, Drive object, workflow or public repository was touched. The report contains only source-bound mathematics and repository-relative lineage.

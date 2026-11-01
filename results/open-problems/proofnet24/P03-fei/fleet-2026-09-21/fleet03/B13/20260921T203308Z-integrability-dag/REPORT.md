# B13 FEI joint route — robust derivative-row integrability DAG and sink-clique factorization

**Status:** **PARTIAL. Full uniform-cube Fourier entropy-influence remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.

**Route:** joint interface B, primarily APPROACHES 2 and 13 (block-influence/Booleanity profile and correlation constraints). This is a materially different method from B13's preceding product-spectrum/total-correlation route.

**No novelty claim.** The result below is a new derivation in this fleet run; publication priority and prior art were not checked.

## 1. Exact statement attempted

Let `f:{0,1}^n->{-1,+1}` be in the median-character gauge, so every active folded influence satisfies `0<j_i=Inf_i(f)<=1/2`. For the Boolean derivative row

`g_i(y)=(f(0,y)-f(1,y))/2 in {0,±1}`

on the quotient cube, write `E_i={g_i!=0}`, `mu(E_i)=j_i`,

`d_i=sum_{k!=i} ||D_k g_i||_2^2`,

and the sharp depth defect

`Delta_i=d_i/j_i-(1/2)log_2(1/j_i)>=0`.

Assume a family of rows is simultaneously in the low-defect / near-subcube regime: for every row `i` there is a coordinate subcube

`Q_i={x_{F_i}=a_i}`,  `s_i=mu(Q_i)=2^{-|F_i|}`,

such that

`mu(E_i triangle Q_i)<=delta j_i`,   `Delta_i<=eta`.

The universal statement attacked was:

> **Robust integrability statement.** For sufficiently small absolute `delta,eta`, the directed proxy-incidence graph `i -> k` iff `k in F_i` is an acyclic hierarchy after exact reciprocal cliques are contracted; one-way edges must move by a fixed multiplicative amount in influence/subcube scale, while every sink reciprocal clique is jointly integrable to a single one-point-defect factor up to a quantitatively controlled Boolean error.

This statement is proved below for, in particular, `delta=eta=1/16`. It is a conditional branch theorem, not full FEI.

## 2. Cross-account inputs actually consumed

The named completed peer result used substantively is

`fleet04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`.

It proves for distinct rows `i,k`, with

`p_ik = Pr[1_{E_i}(y) != 1_{E_i}(y+e_k)]`,

`o_ik = Pr[g_i(y)=-g_i(y+e_k) != 0]`,

`kappa_ik = E(g_i(y)-g_i(y+e_k))^2`,

the exact Boolean integrability identities

`kappa_ik=kappa_ki=p_ik+4 o_ik`,

and `sum_{i!=k}(p_ik+4o_ik)=4d_k`.

I also use the completed fleet02/B13 sign-defect identity

`4 j_i Delta_i = Iso(A_i)+Iso(B_i)+2J(A_i,B_i)+2j_i h_2(theta_i)`,

which implies `theta_i<=Delta_i` and, direction by direction, `o_ik<=J(A_i,B_i)<=2j_i Delta_i`.

The role of these inputs here is not citation-only: mixed-derivative commutation converts pairwise proxy geometry into a quantitative global compatibility law.

## 3. Boundary perturbation lemma

For any set `E` and comparison set `Q` on a cube, if `mu(E triangle Q)=eps`, then for every coordinate `k`,

`| I_k(E)-I_k(Q) | <= 2 eps`.                                      (3.1)

Indeed the two edge-boundary indicators can disagree only if one of the two endpoints lies in `E triangle Q`.

For the coordinate subcube `Q_i`,

* if `k in F_i`, `I_k(Q_i)=2s_i`;
* if `k notin F_i`, `I_k(Q_i)=0`.

Also `|s_i-j_i|<=eps_i`, where `eps_i=mu(E_i triangle Q_i)`.

## 4. PROVED: one-way incidences have a strict scale gap

Assume `k in F_i` but `i notin F_k`. By (3.1),

`p_ik >= 2(s_i-eps_i)`.

By mixed-curvature conservation, (3.1) on row `k`, and the sign-defect bank,

`2(s_i-eps_i) <= kappa_ik=kappa_ki <= 2 eps_k + 8 eta j_k`.

Since `eps_r<=delta j_r` and `|s_r-j_r|<=eps_r`, this yields both

`(1-2delta) j_i <= (delta+4eta) j_k`,                         (4.1)

and

`(1-2delta) s_i <= (delta+4eta) s_k`.                         (4.2)

Put

`q(delta,eta)=(delta+4eta)/(1-2delta)`.

Thus every one-way edge satisfies `j_i<=q j_k` and `s_i<=q s_k`.

At `delta=eta=1/16`,

`q=5/14=0.357142857...`.

Because each `s_i` is dyadic, `s_i/s_k<=5/14` strengthens discretely to

`boxed: s_i/s_k <= 1/4`,

so

`boxed: |F_i| >= |F_k|+2`.                                    (4.3)

This already forbids a directed cycle made of one-way incidences.

## 5. PROVED: every reciprocal incidence is exactly proxy-compatible

Assume `k in F_i` and `i in F_k`. The same calculation in both directions gives

`s_i-eps_i <= s_k+eps_k+4eta j_k`

and its transpose. Since coordinate-subcube densities are powers of two, if they were unequal then, say, `s_i>=2s_k`. Using `j_r<=s_r/(1-delta)`, this contradicts the displayed inequality whenever

`4(delta+eta)<1`.

Hence in the present regime

`boxed: s_i=s_k=s`.                                             (5.1)

Now pass to the common quotient deleting coordinates `i,k`. Let `R_i` be the coordinate subcube obtained from `Q_i` by deleting its fixed `k` constraint, and define `R_k` symmetrically. Both have density `2s` in the common quotient.

Choose a majority sign `sigma_i` for row `g_i`. The fleet02 sign theorem gives minority fraction `theta_i<=eta`, so

`B_i={g_i != sigma_i 1_{Q_i}}`

has

`mu(B_i)<=eps_i+eta j_i <= (delta+eta)j_i`.                     (5.2)

On a common-quotient point where neither endpoint is in `B_i`, the support of `D_k g_i` equals `R_i`. Therefore, if `M` is the common support of the equal mixed derivatives `D_k g_i=D_i g_k`,

`mu(R_i triangle M)<=2mu(B_i)`

and similarly for `R_k`. Consequently

`mu(R_i triangle R_k)<=2(mu(B_i)+mu(B_k))`.

At `delta=eta=1/16`, using `j_i,j_k<=s/(1-delta)`, the right side is strictly smaller than `2s`.

But two distinct coordinate subcubes of the same density `2s` have symmetric difference at least `2s`: if compatible but distinct, their intersection has density at most `s`; if incompatible, the gap is larger. Hence

`boxed: R_i=R_k`.                                               (5.3)

Thus

`F_i\{k}=F_k\{i}`

and the fixed bits agree on the common coordinate set. In particular the closed proxy neighborhoods

`C_i={i} union F_i`, `C_k={k} union F_k`

are identical. The same good-point argument plus equality of the oriented mixed derivatives also forces the expected pairwise phase relation between majority row signs; no unsigned-support-only incompatibility is hidden here.

Therefore every connected component of reciprocal incidences is an **exact clique** with one common closed coordinate set and one common proxy pattern.

## 6. PROVED: quotient DAG and quantitative depth descent

Contract each reciprocal clique. A remaining edge between components is one-way. The proxy scale `s` is exactly constant inside a reciprocal component by (5.1), and decreases by at least a factor `4` in the reverse direction of each one-way edge by (4.3). Therefore the quotient graph is acyclic.

Equivalently, if the edge is oriented `i -> k`, then the proxy codimension drops by at least two:

`|F_i| >= |F_k|+2`.

So a one-way path from a row of proxy codimension `r` has length at most `floor(r/2)` before reaching a sink reciprocal clique.

Also, because `q<1`, any row of maximum influence in the family has no one-way outgoing incidence; all of its proxy coordinates lie in its reciprocal clique.

## 7. PROVED: every sink clique is close to a genuine product with a one-point defect

Let `C` be a sink reciprocal clique. Since it has no one-way outgoing edge, the common closed-neighborhood identity implies

`F_i=C\{i}` for every `i in C`,

and the compatible proxy patterns define a common point `b in {0,1}^C`.

Let

`h_C(x_C)=1-2 1_{x_C=b}`.

Its `i`-edge flip support is exactly `Q_i`. Put `q(x)=f(x) h_C(x_C)`. For each `i in C`, an edge flips `q` exactly when the flip-supports of `f` and `h_C` disagree, so

`Inf_i(q)=mu(E_i triangle Q_i)=eps_i`.

Condition on all coordinates outside `C`. The cube Poincare inequality gives

`E_z Var(q(X_C,z) | z) <= sum_{i in C} eps_i`.

For a `{±1}` random variable, its distance to its majority constant is at most half its variance. Hence there exists a Boolean function `r` of the outside coordinates such that

`boxed: Pr[ f(x) != r(x_{C^c}) h_C(x_C) ] <= (1/2) sum_{i in C} eps_i
       <= (delta/2) sum_{i in C} j_i`.                          (7.1)

At `delta=1/16`, the error is at most `(1/32) sum_{i in C}j_i`.

This is a genuine multi-row stability implication: a sink collection of individually near-extremal derivative rows cannot be an arbitrary family of near-subcubes. Boolean mixed-derivative integrability forces an exact clique geometry, and that clique integrates to a single near-product one-point-defect factor.

## 8. Relation to the current crossing/Hall interface

The fresh fleet01/B13 crossing theorem shows that a near-subcube row has a real row-adapted block `F_i` whose posterior crossing is almost maximal, and that singleton crossings are useless at the current high-ratio scale. Its remaining issue is nonreuse / cyclic overlap of the blocks.

The theorem above resolves the **cycle geometry** in the low-defect near-subcube branch:

1. reciprocal cycles collapse to exact compatible cliques;
2. all nonreciprocal incidences form a strict dyadic hierarchy with codimension descent at least two;
3. sink cliques are not merely selectable objects; jointly they approximate an actual product one-point-defect factor by (7.1).

What remains is not pairwise integrability. The remaining global implication is to turn this DAG plus sink-factorization into an influence-relative **aggregate Shannon payment** for all incoming one-way rows, without paying an ambient-dimension continuity factor. That is the next interface-B target.

## 9. Exact finite falsification search

A standard-library checker in this run enumerated every Boolean truth table modulo global output sign through `n=4`. Each function was median-character folded, all active derivative rows were formed, all coordinate-subcube proxies satisfying `eps<=j/16` were enumerated, and only rows with `Delta<=1/16` were retained. It then checked (4.1)-(4.2) for every one-way proxy incidence and (5.1)-(5.3) for every reciprocal pair.

Results:

| n | functions modulo sign | qualifying functions | qualifying rows | proxy incidence pairs | one-way | reciprocal | violations |
|---|---:|---:|---:|---:|---:|---:|---:|
|1|2|0|0|0|0|0|0|
|2|8|4|8|4|0|4|0|
|3|128|100|264|216|0|216|0|
|4|32768|10480|17840|5472|0|5472|0|

Every qualifying row in these finite cases had `Delta=0`; the nearest observed distance from the threshold `1/16` was `1/16`, so no threshold-rounding ambiguity affected inclusion. The absence of one-way cases through `n=4` is finite evidence only, not an additional theorem.

## 10. Claim ledger and next attack

* **PROVED:** robust one-way scale inequality (4.1)-(4.2).
* **PROVED:** at `delta=eta=1/16`, every one-way edge changes dyadic proxy scale by at least factor `4`, hence codimension by at least `2`.
* **PROVED:** reciprocal low-defect proxy incidences have identical stripped subcubes and compatible closed neighborhoods; reciprocal components are exact cliques.
* **PROVED:** after contraction, the proxy-incidence graph is a DAG.
* **PROVED:** every sink clique admits the Hamming product approximation (7.1).
* **OPEN:** convert the hierarchy and sink product approximation into a universal dimension-free Shannon/information payment for all row mass.
* **OPEN:** full uniform-cube FEI.

**Next attack:** combine the codimension-ranked DAG with fleet01/B13's block-crossing/Hall inequality and fleet04/B18's column conservation. Try an amortized topological elimination: peel sink cliques, pay their block entropy by the exact one-point factor, and charge each incoming one-way layer to the strict two-level codimension drop. A successful proof needs a dimension-free entropy stability statement for (7.1), not Fannes continuity.

### Joint-order handoff

`consumed_peer_artifact`: `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md` (plus fleet02/B13 sign-defect report as a second input).

`applied_to_claim`: robust multi-row derivative-proxy integrability, quotient DAG, and sink-clique product stability.

`remaining_implication`: amortized dimension-free Shannon payment for incoming one-way rows / sink peeling, sufficient to feed the current block-crossing restriction inequality.

`next_recipient`: fleet04/B18 first (proof integration), with fleet01/B13 as the crossing/Hall consumer.

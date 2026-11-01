Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — two-seed fibre branching closes the arbitrary-four-pair Rattaggi boundary

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorems proved below; universal T09 remains OPEN.** The load-bearing arithmetic was executed exactly and archived in this run. No independent review has yet occurred. External priority of this exact arbitrary-four-pair fixed-Cayley theorem remains **UNVERIFIED**.

## 1. Parent target, ownership, and compact handoff

The parent target is unchanged:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 under `proofnet24/NM13-11/progress-percolation/`. The current `POSTED.md` exclusion registry does not close the universal Benjamini--Schramm target.

The latest own substantive predecessor read before research was

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T15-50-00+0300__t09-one-free-pair-k4-gap.md`.

I also checked the newest neighboring PROB10-09 report then on `master`,

`runs/prob10_2026-09-20/PROB10-09/2026-09-20T13-51-53Z_vertical_kernel_generator_extension_gap_51c8.md`,

commit `261e079f475802d8a7ac9a68f68a4ff6910b129f`. That report explicitly leaves the Rattaggi/free-layer/product-fibre lane to NM13-11 and works in a quotient/vertical-kernel lane, so the present theorem is complementary rather than an ownership collision.

The inherited Benjamini--Schramm attempt history is preserved rather than restarted. In particular: normalized finite-set escape and BK/last-exit; killed-SAW interior growth and susceptibility-weighted boundary energy; global `ell^2` SAW; scalar nonbacktracking polynomial bounds; quotient/fibre-shell comparisons; fixed-endpoint bridge criteria; the June tree-product/fixed-direction attempts; and this track's later free-core, triangle-fibre, S-arithmetic, Rattaggi, power-layer, factor-branching and pure-torsion restricted theorems. Several of those routes produced valid auxiliary inequalities but no `p_c`-to-`p_u` transfer and remain mechanism history only.

## 2. Exact source-level before/after

### Before this run

For any `(12,8)`-group `Gamma` with standard generating set `S0`,

`Cay(Gamma,S0) ~= T_12 square T_8`.

The immediately preceding theorem allowed four genuinely new inverse pairs only under a structural sparsity assumption: one distinguished two-pair block had to freely generate `F_2` (or, more generally, have regular-representation norm at most `3.47`), while the remaining two pairs were arbitrary. It proved

`p_c < 277/5000 = 0.0554 < 559/10000 = 0.0559 < p_u`.

Four **completely arbitrary** new inverse pairs were still UNKNOWN in this lane. Charging all four pairs by norm `2` each gives a uniqueness floor near `0.0541644`, while the best one-seed fibre comparison, even at infinite fibre depth, numerically bottoms out near `0.0553268`. Thus merely deepening the old one-seed process cannot close the gap.

### After this run

> **Theorem A (four completely arbitrary added pairs).** Let `Gamma` be any `(12,8)`-group with standard symmetric generating set `S0`, so that `Cay(Gamma,S0) ~= T_12 square T_8`. Let
> 
> `C={c_1^{+-1},c_2^{+-1},c_3^{+-1},c_4^{+-1}}`
> 
> consist of four genuinely new inverse pairs, with the eight elements pairwise distinct and disjoint from `S0`. Impose **no algebraic assumption at all** on the `c_i`: they may have arbitrary relations among themselves and with the standard generators. Then the degree-28 Cayley graph
> 
> `G=Cay(Gamma,S0 union C)`
> 
> satisfies
> 
> `boxed(p_c(G)<1353/25000 = 0.05412 < 677/12500 = 0.05416 < p_u(G))`,
> 
> and therefore
> 
> `boxed(p_u(G)-p_c(G)>1/25000 = 0.00004).`

This removes the final sparse-block hypothesis from the four-pair perturbation theorem. In particular it applies to Rattaggi's virtually simple `(12,8)` group `Sigma` for **every** simple degree-28 Cayley graph obtained by adjoining four new inverse pairs to the standard ten-generator marking.

**Original-problem delta:** universal T09 remains OPEN. The demonstrated fixed-Cayley scope expands from `one F_2-marked pair-block + two arbitrary pairs` to `four completely arbitrary inverse pairs` on every `(12,8)`-group, with a concrete uncovered Rattaggi ambient example.

**Mechanism delta:** the old one-seed fibre process is replaced by a genuinely multiseed two-type Galton--Watson process that preserves the benefit of multiple successful crossings into one child fibre. This lowers the actual critical-probability certificate far enough to cross the worst-case four-pair scalar uniqueness floor. The new source-level theorem therefore has a complete percolation transfer; it is not an auxiliary inequality.

## 3. The two-type multiseed fibre lemma

The mechanism is useful beyond the frozen numbers, so I state it first for a product `T_d square T_e`.

Fix `R>=1`, `p in (0,1)`, and write `s=1-p`. Define polynomials in an auxiliary variable `x` by

`h_0(x)=x`,
`h_{r+1}(x)=x (s+p h_r(x))^{e-1}`.                              (3.1)

Thus `h_r` is the cluster-size pgf for a root of a forward `(e-1)`-ary tree truncated at depth `r`. Define

`F_{1,R}(x)=x (s+p h_{R-1}(x))^e`,                                (3.2)

and

`F_{2,R}(x)=h_R(x)^2`.                                            (3.3)

At `x=s`, set

`q_{i1}=p F_{i,R}'(s)`,
`q_{i2}=1-F_{i,R}(s)-p F_{i,R}'(s)`,                              (3.4)

for `i=1,2`, and let

`M_R(p)=(d-1) [[q_11,q_12],[q_21,q_22]].`                         (3.5)

> **Lemma 3.1 (two-seed product comparison).** If `rho(M_R(p))>1`, then
> 
> `p_c(T_d square T_e)<p`.

### Proof

Root the `T_d` coordinate. Use only `d-1` chosen forward directions even at the root.

A **type-1 particle** consists of one seed vertex in a fresh `T_e` fibre. Expose only vertical edges in the radius-`R` ball around the seed and retain its open cluster. If its size is `Z_1`, then `F_{1,R}(x)=E[x^{Z_1}]` by the standard rooted-tree recursion (3.1)--(3.2).

For each of the `d-1` forward `T_d` directions, test every horizontal edge from a retained active vertex into that child fibre. Conditional on `Z_1=n`, the number `K` of successful crossing edges in that direction is `Bin(n,p)`. If `K=0`, make no child; if `K=1`, make a type-1 child at the unique successful endpoint; if `K>=2`, choose any two distinct successful endpoints and make one type-2 child. Therefore

`P(type 1 child in a fixed direction)=E[n p s^{n-1}]=p F_{1,R}'(s)=q_11`,

and

`P(type 2 child in a fixed direction)=1-F_{1,R}(s)-pF_{1,R}'(s)=q_12`.

A **type-2 particle** consists of two distinct seed vertices `u,v` in a fresh fibre. Let `gamma` be the unique geodesic between them in `T_e`. At `u`, delete the first edge of `gamma` pointing toward `v`; at `v`, delete the first edge pointing toward `u`. The two connected components containing `u` and `v` are disjoint rooted `(e-1)`-ary trees. Expose only their depth-`R` truncations. The two open cluster sizes are independent with pgf `h_R`, so the total active size `Z_2` has pgf `F_{2,R}=h_R^2`. Apply the same horizontal crossing rule. Equation (3.4) gives the two child probabilities `q_21,q_22`.

This construction remains valid no matter how far apart the two type-2 seeds are: the two outward components obtained by cutting the first geodesic edge at each endpoint are always disjoint. The vertical edges used in a child fibre have not previously been exposed, since the parent exposes only horizontal crossing edges into that fibre.

Different forward child fibres are disjoint. Distinct parent particles live in distinct rooted `T_d` fibres, because every non-root `T_d` vertex has a unique parent. Hence the block environments of distinct particles are independent. Dependence among the `d-1` children of one particle is harmless: a multitype Galton--Watson process only requires iid offspring vectors across particles. Its mean matrix is exactly (3.5).

For a finite-type Galton--Watson process with finite offspring, Perron eigenvalue greater than one implies positive survival probability. Survival gives an infinite open cluster in the product. Since the inequality `rho(M_R(p))>1` is strict and all matrix entries are continuous in `p`, it persists on an interval immediately below `p`; hence `p_c<p`. `square`

The point of the lemma is that a child fibre receiving several successful crossings is no longer collapsed to a single seed. The previous one-seed process discarded precisely this gain.

## 4. Exact radius-five certificate on `T_12 square T_8`

Take

`d=12`, `e=8`, `R=5`, `p_0=1353/25000`, `s_0=1-p_0`.

Let

`M_5(p_0)=[[A,B],[C,D]]`.

The exact `Fraction` checker created and actually executed in this run gives

`A = 0.9244427234676237...`,
`B = 0.040137800303950845...`,
`C = 1.6214557629274526...`,
`D = 0.14003972560683262...`.

The full determinant fraction has about 1.8 million bits, so the checker also records a small human-readable rational certificate:

`A > 2311/2500`,
`B > 4013/100000`,
`C > 8107/5000`,
`D > 7/50`.                                                     (4.1)

Consequently

`(1-A)(1-D)
 < (189/2500)(43/50)
 = 32508000/500000000`,                                         (4.2)

while

`BC
 > (4013/100000)(8107/5000)
 = 32533391/500000000`.                                         (4.3)

Thus

`det(I-M_5(p_0))=(1-A)(1-D)-BC
 < -25391/500000000 <0`.                                       (4.4)

A nonnegative `2x2` matrix has real eigenvalues; (4.4) puts `1` strictly between them, so its Perron eigenvalue is `>1`. The direct exact determinant evaluation is also negative, numerically

`det(I-M_5(p_0))=-0.00010541135488956291...`.

Lemma 3.1 therefore gives

`boxed(p_c(T_12 square T_8)<1353/25000).`                        (4.5)

Every graph in Theorem A contains the standard product graph as a spanning subgraph, so adding the four generator pairs can only decrease `p_c`; hence (4.5) holds for `G` as well.

## 5. Four arbitrary pairs on the uniqueness side

Write

`A_G=A_0+sum_{i=1}^4 (R_{c_i}+R_{c_i^{-1}})`.

The standard product adjacency has exact norm

`||A_0||=2sqrt(11)+2sqrt(7)`.                                    (5.1)

No relation assumption on the `c_i` is used. Each right translation is unitary, so each inverse pair costs at most `2`. Therefore

`||A_G|| <= 2sqrt(11)+2sqrt(7)+8`.                               (5.2)

Use the exact rational square-root upper bounds

`sqrt(11)<199/60`, `sqrt(7)<127/48`,                             (5.3)

which give

`boxed(||A_G||<797/40=19.925).`                                  (5.4)

The graph is `D=28` regular, so put `Q=D-1=27`. If `N_n` is the length-`n` nonbacktracking walk operator, then

`N_0=I`, `N_1=A_G`, `N_2=A_G^2-DI`,
`N_n=A_G N_{n-1}-Q N_{n-2}` for `n>=3`.                          (5.5)

By spectral calculus, if `z>sqrt(Q)` and

`z+Q/z>||A_G||`,                                                  (5.6)

then the exponential `ell^2` growth of `N_n` is strictly smaller than `z`. Every open connection contains a shortest open path, and every shortest path is nonbacktracking, so entrywise

`T_p(x,y) <= sum_{n>=0} p^n N_n(x,y)`.                           (5.7)

Hence `p z<1` implies `ell^2` boundedness of the two-point kernel.

Take

`p_1=677/12500=0.05416`, `z=12500/677`.

The exact checker verifies

`z^2-27 = 143875117/458329 >0`,                                  (5.8)

and, against the rational upper bound (5.4),

`z+27/z-797/40 = 19141/16925000 >0`.                             (5.9)

Therefore

`p_{2->2}(G)>677/12500`.                                         (5.10)

Finally `p_{2->2}<=p_u`: for every `p>p_u`, uniqueness and FKG give `T_p(x,y)>=theta(p)^2>0` uniformly in `x,y`; such a kernel cannot be bounded on `ell^2` of an infinite graph. Thus

`boxed(p_u(G)>677/12500).`                                       (5.11)

Combining (4.5) and (5.11),

`677/12500 - 1353/25000 = 1/25000`,

which proves Theorem A.

## 6. Structural weakening and reusable comparison theorem

The proof never uses Rattaggi's presentation, virtual simplicity, or any relation involving the four added pairs. It only uses two graph/operator facts:

1. the frozen standard Cayley graph is `T_12 square T_8`; and
2. the perturbation consists of four symmetric inverse pairs, so its operator norm is at most `8`.

Thus the theorem holds verbatim for **every `(12,8)`-group** and every four-pair simple augmentation, including finite-order added generators, amenable added subgroups, highly related added subgroups, and arbitrary cross-relations with the standard marking. This is strictly weaker than every earlier free-layer/sparse-block hypothesis in the Rattaggi lane.

More generally, combining Lemma 3.1 with the same nonbacktracking argument yields the following reusable criterion.

> **Theorem B (arbitrary-pair augmentation criterion for a product-of-trees marking).** Suppose a Cayley graph has a spanning marked subgraph `T_d square T_e` and is obtained from that marking by adding `k` arbitrary inverse generator pairs, with final degree `D=d+e+2k`. If for some `R,p,z`
> 
> `rho(M_R(p))>1`,
> 
> `z>sqrt(D-1)`,
> 
> and
> 
> `z+(D-1)/z > 2sqrt(d-1)+2sqrt(e-1)+2k`,
> 
> then
> 
> `p_c<p<1/z<p_u`.

This has a demonstrated percolation transfer on both sides. The frozen `d=12,e=8,k=4,R=5` specialization is Theorem A.

## 7. Why this is the first genuinely different method at the current obstruction

The previous run's residual obstruction was exactly four arbitrary pairs. I first checked whether the old one-seed fibre mechanism could be pushed through by depth alone. Its limiting one-seed threshold is numerically about

`0.055326820665...`,

still above the worst-case four-pair uniqueness floor near

`0.054164392466...`.

So another depth-only run would be stagnation, not progress. The two-seed state is materially different: it retains multiplicity information about crossings, and the radius-five two-type process already crosses the needed threshold at `0.05412`.

A second diagnostic was a maximal-block colored nonbacktracking decomposition into standard-product blocks and arbitrary-added-edge blocks. If the arbitrary four-pair subgroup is amenable, the positive convolution norm of an added-edge block attains its row-sum bound, and the resulting block criterion collapses numerically to the same scalar floor. This explains why the successful gain had to come from the critical side or from subgroup-position information absent in the fully arbitrary hypothesis.

## 8. The next obstruction is now decisive, not merely numerical

For **five** completely arbitrary added inverse pairs, the same scalar uniqueness architecture has

`D=30`, `Q=29`,

and adjacency upper bound

`2sqrt(11)+2sqrt(7)+10`.

Its characteristic uniqueness floor is about `0.04875`, already below `1/19=0.0526315...`. But every degree-20 graph, in particular the retained base `T_12 square T_8`, satisfies the elementary lower bound

`p_c >= 1/(20-1)=1/19`.

Therefore **no improvement whatsoever of a critical certificate that uses only the retained degree-20 base graph can close the five-arbitrary-pair case when paired with the same scalar adjacency/nonbacktracking uniqueness bound.** This is an architectural obstruction, not a matter of deeper finite fibres.

The next method must therefore do at least one of the following:

- use the added edges themselves on the `p_c` side in a collision-controlled multiseed process; or
- improve the `p_u` side using relation/subgroup-position information rather than charging each arbitrary pair by norm `2`.

Five arbitrary pairs are recorded as **UNKNOWN here**, not negative.

## 9. Current source scopes, refreshed 20 September 2026

The three owner-specified arXiv records were refreshed in this run.

### arXiv:1804.10191 — Hutchcroft

Current arXiv version: **v3, 26 March 2019**; the arXiv comment says v3 changed metadata only. Theorem 1.3 proves `p_c<p_u` for connected, locally finite, nonamenable, **Gromov-hyperbolic quasi-transitive** graphs. It does not cover the present Rattaggi augmented graphs. The standard product `T_12 square T_8` already contains quasi-isometrically embedded grids and is not Gromov hyperbolic.

### arXiv:2409.12283 — Hutchcroft--Pan

Current arXiv version: **v1, 18 September 2024**. The paper studies behavior **at `p_u`** via subgroup relativization. Its abstract covers amenable `wq`-normal subgroups of exponential growth and a co-heredity theorem; the full paper formulates the stronger obstacle-to-uniqueness framework, including nonamenable direct products and property-(T)/relative-(T) examples. These are endpoint-`p_u` statements and do not by themselves provide the strict quantitative fixed-graph separation proved here.

### arXiv:2502.02560 — Terlov--Timar

Current arXiv version: **v2, 14 September 2025**. It develops weighted/level amenability and proves a Pak--Smirnova-Nagnibeda-style relaxed version of a weighted `p_h<p_u` conjecture. It is not a theorem asserting ordinary unimodular fixed-Cayley `p_c<p_u` for the present graphs.

I also retained the later Choi--Seo scope: arXiv:2508.08932 proves a nonuniqueness phase for every Cayley graph of every acylindrically hyperbolic group. Rattaggi's group has an index-four infinite finitely presented torsion-free simple subgroup; the standard finite-index stability/non-simplicity consequences of acylindrical hyperbolicity exclude this example from that all-Cayley class. Rattaggi's construction gives `Sigma<Aut(T_12)xAut(T_8)` with the index-four simple subgroup. Gady Kozma's theorem on the **unaugmented** Cartesian product of two trees is also prior art, but it does not transfer `p_u` monotonically after arbitrary generator addition; that missing transfer is exactly what Theorem A supplies.

A bounded current search did not locate the exact arbitrary-four-pair augmentation theorem. This is **negative bounded-search evidence only**; worldwide novelty/priority remains UNVERIFIED.

## 10. Exact artifacts and readback contract

Load-bearing final checker:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T17-12-00+0300__t09-two-seed-arbitrary-k4-final-check.py`

commit `0811bdd801f6d1709e6d5ca66cb9cba5ab79b032`.

Actually executed output:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T17-12-00+0300__t09-two-seed-arbitrary-k4-final-check.out`

commit `1f1d5967f49c93b67812d61ae4e55cf478c45815`, ending `ALL_EXACT_CHECKS_PASS`.

An earlier same-run checker/output pair at commits `c844f8fb3583da6a330510f7c792a0f4a930c3ae` / `e3136eccd10d865e5b806aff7119ef4a301e3dc7` proved the same critical theorem with the weaker uniqueness floor `0.05415`. It is preserved as immutable history and superseded quantitatively by the final checker; it was not overwritten.

## 11. ledger_delta

```yaml
ledger_delta:
  parent: T09
  universal_status_before: OPEN
  universal_status_after: OPEN
  restricted_status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  source_level_before:
    class: "(12,8)-group + four added pairs, requiring one operator-sparse/free rank-2 block"
    certified_gap: "> 1/2000 under that structural hypothesis"
    four_completely_arbitrary_pairs: UNKNOWN
  source_level_after:
    class: "every (12,8)-group standard marking + four completely arbitrary new inverse pairs"
    pc_upper_strict: "1353/25000 = 0.05412"
    pu_lower_strict: "677/12500 = 0.05416"
    certified_gap: "> 1/25000 = 0.00004"
    concrete_uncovered_ambient: "Rattaggi Sigma, virtually simple product-of-trees lattice"
  mechanism_advance:
    name: "radius-5 two-type multiseed fibre Galton-Watson comparison"
    transfer: "rho(M_5)>1 gives strict pc bound; scalar nonbacktracking gives strict pu bound"
    key_exact_margin: "BC-(1-A)(1-D) > 25391/500000000"
  failed_or_exhausted_routes_preserved:
    - "one-seed fibre depth/fixed-point route: limiting threshold about 0.0553268, insufficient for arbitrary four pairs"
    - "worst-case colored maximal-block NB with amenable added block collapses to scalar floor"
  next_obstruction:
    scope: "five completely arbitrary added inverse pairs"
    status: UNKNOWN
    reason: "base-only pc architecture cannot cross scalar pu floor; pc(base)>=1/19 while scalar pu floor is about 0.04875"
    next_methods:
      - "added-edge-enhanced collision-controlled multiseed branching"
      - "subgroup-position / relation-aware uniqueness estimate"
  code_commit: "0811bdd801f6d1709e6d5ca66cb9cba5ab79b032"
  output_commit: "1f1d5967f49c93b67812d61ae4e55cf478c45815"
  external_priority: UNVERIFIED
```

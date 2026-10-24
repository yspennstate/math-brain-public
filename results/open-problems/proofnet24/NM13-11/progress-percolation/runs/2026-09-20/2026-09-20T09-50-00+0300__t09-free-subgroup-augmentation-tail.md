Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — close the Rattaggi free-horizontal augmentation family; subgroup-driven `p_c` transfer

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorems below; universal T09 remains OPEN.** The new restricted arguments are complete as written and have an exact-arithmetic self-check, but have not had independent review. External priority of the exact augmentation family remains **UNVERIFIED** after the bounded search recorded below.

## 1. Original problem: before/after source-level scope

Frozen parent problem: for iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove

`p_c(G) < p_u(G)`.

The universal statement remains **OPEN**.

### Before this run

The immediate predecessor treated Rattaggi's virtually simple `(12,8)`-group `Sigma`, whose standard Cayley graph is

`Cay(Sigma,S0) ~= T_12 square T_8`,

and the explicit horizontal Schreier conjugates

`c_j = a_1^j a_2 a_1^{-j}`.

It proved positive gaps for the fixed graphs

`G_k = Cay(Sigma, S0 union {c_1^{+-1},...,c_k^{+-1}})`

through `k=8`. The weakest endpoint was

`p_c(G_8)<7/125=0.056`, `p_u(G_8)>113/2000=0.0565`,

hence `p_u-p_c>1/2000`.

The predecessor explicitly recorded `k=9` as the first obstruction for the then-current scalar method: the product-only `p_c<7/125` bound sat above the available `p_u` lower bound.

### After this run

The `k=9` obstruction is removed by **reversing the percolation comparison**: instead of using the old `T_8` fibre cluster to branch through the `T_12` factor, use the new free `F_9` augmentation inside each horizontal fibre and branch through the seven forward directions of the `T_8` factor.

For `G_9` I prove

`p_c(G_9) < 109/2000 = 0.0545`,

`p_u(G_9) > 11/200 = 0.055`,

so

`boxed(p_u(G_9)-p_c(G_9) > 1/2000 = 0.0005)`.

For **every `k>=10`**, a still simpler argument uses the added free subgroup itself as a percolating subgraph. Writing

`x=2k-1`,

one has

`p_c(G) <= 1/x`

for *any* augmentation of a `(12,8)`-group by `k` genuinely new generators that freely generate `F_k`, with no horizontal-location hypothesis. The same adjacency/nonbacktracking transfer gives

`p_u(G) >= beta_k^{-1} > 1/x`,

where

`beta_k = beta_{20+2k}(2 sqrt(11)+2 sqrt(7)+2 sqrt(2k-1))`.

Therefore

`boxed(p_u(G)-p_c(G) >= beta_k^{-1} - (2k-1)^{-1} > 0)`

for every `k>=10`.

At the first point `k=10`, the exact rational certificate is

`p_c <= 1/19`, `p_u>269/5000`,

hence

`boxed(p_u-p_c > 111/95000 = 0.0011684210526...)`.

Combining this run with the already-preserved `k<=8` results, the **entire explicit Schreier-conjugate family `G_k`, every finite `k>=1`, now has a rigorously demonstrated positive nonuniqueness gap** on the same fixed Rattaggi ambient group.

**Original-problem delta:** before, the explicit family stopped at `k=8`; after, `k=9` is certified quantitatively and the entire tail `k>=10` is proved at once. Thus the one-parameter fixed-graph class is no longer finitely truncated.

**Mechanism delta:** the added subgroup is no longer treated only as an operator perturbation that hurts the `p_u` bound. Its own percolation geometry is used on the `p_c` side. For `k>=10` this removes the horizontal-fibre hypothesis entirely; for `k=9` a two-level `F_9`-cluster/vertical-tree Galton--Watson process crosses the narrow remaining gap.

## 2. Compact continuity handoff

Controlling policy is `operations/PROGRESS20_2026-09-20.md`; current LIVE20 assigns NM11 to T09 under `proofnet24/NM13-11/progress-percolation/`.

The preserved June Benjamini--Schramm archive records these earlier routes and failures:

- normalized finite-set escape plus BK/last-exit boundary decomposition;
- killed-SAW interior growth and susceptibility-weighted boundary energy;
- global `l^2` SAW growth;
- scalar nonbacktracking polynomial estimates and product stress tests;
- quotient/fibre-shell and fixed-endpoint bridge criteria.

Several remained CONDITIONAL because the needed finite-set/shell inequality did not transfer all the way to `p_c<p_u`. Product-only calculations were later recognized as already-covered qualitative families and are not counted as new source-level progress.

The current NM13-11 sequence then produced actual transfers on explicit `SL_3(Z)`, free-core, triangle-fibre, S-arithmetic and Rattaggi fixed generating sets. The immediate predecessor reached the explicit Rattaggi horizontal-free family through `k=8` and identified `k=9` as the first failure of the one-fibre `p_c` comparison.

This run does not polish that failed inequality. It changes which subgraph drives `p_c`: the free augmentation itself becomes the fibre/core. No historical or peer file is overwritten.

## 3. Reusable subgroup-augmentation transfer

Let `Gamma` have a symmetric generating set `S0` with

`Cay(Gamma,S0) ~= T_12 square T_8`.

Thus

`||A_0|| = 2 sqrt(11)+2 sqrt(7)`.

Let `C` be any finite inverse-closed set of genuinely new generators, disjoint from `S0`, and let

`H=<C>`, `Y=Cay(H,C)`.

The `C`-edge subgraph of `G=Cay(Gamma,S0 union C)` is a disjoint union of left cosets of `H`, each canonically isomorphic to `Y`. Consequently

`p_c(G) <= p_c(Y)`.                                      (3.1)

On `l^2(Gamma)`, the `C`-adjacency operator preserves these left cosets and is the direct sum of copies of `A_Y`, hence

`||K_C|| = ||A_Y||`.                                      (3.2)

If `D=20+|C|`, `Q=D-1`, and

`a = 2 sqrt(11)+2 sqrt(7)+||A_Y||`,

then

`||A_G|| <= a`.                                           (3.3)

The nonbacktracking transfer already proved in the track gives

`p_u(G) >= p_{2->2}(G) >= beta_D(a)^{-1}`,                (3.4)

where

`beta_D(a)=sqrt(Q)` if `a<=2sqrt(Q)`, and otherwise

`beta_D(a)=(a+sqrt(a^2-4Q))/2`.

Therefore any certified subgroup estimate

`p_c(Y) <= q < beta_D(a)^{-1}`                            (3.5)

immediately yields the source-level conclusion

`p_u(G)-p_c(G) >= beta_D(a)^{-1}-q > 0`.                  (3.6)

This criterion is not claimed as a wholly new abstract idea: the first NM13-11 run already used the same subgroup/complement decomposition in the opposite orientation. The new point here is that applying it to the **added** subgroup makes the `p_c` bound improve as the augmentation grows, instead of treating every added generator only as a cost on the uniqueness side.

## 4. All free augmentations of rank `k>=10`

Assume now that `C={c_1^{+-1},...,c_k^{+-1}}` and the `c_i` freely generate `F_k`. Then

`Y ~= T_{2k}`,

so exactly

`p_c(Y)=1/(2k-1)`,

and

`||A_Y||=2 sqrt(2k-1)`.

Put

`x=2k-1 >= 19`,

so `D=x+21`, `Q=x+20`, and

`a_x=2 sqrt(11)+2 sqrt(7)+2 sqrt(x)`.

To show `beta_D(a_x)<x`, it is enough to verify

`x>sqrt(Q)`

and

`x + Q/x > a_x`.                                         (4.1)

The first is immediate for `x>=19`. For the second define

`f(x)=x+1+20/x-2sqrt(x)-2sqrt(11)-2sqrt(7)`.

At `x=19`, use the elementary rational bounds

`sqrt(11)<10/3`, `sqrt(7)<8/3`, `sqrt(19)<22/5`.

Then

`f(19) > 400/19 - 104/5 = 24/95 >0`.                     (4.2)

For every real `x>=19`,

`f'(x)=1-20/x^2-1/sqrt(x)
      > 1-20/361-1/4
      = 1003/1444 >0`.                                   (4.3)

Hence `f(x)>0` for every `x>=19`, proving (4.1) and therefore

`beta_D(a_x)<x=2k-1`.

Combining with (3.1)--(3.4),

`p_c(G) <= 1/(2k-1) < beta_D(a_x)^{-1} <= p_u(G)`.

Thus every such free augmentation has a strictly positive nonuniqueness phase.

This materially weakens the explicit construction hypothesis: for `k>=10`, the free generators may lie anywhere in `Gamma`; they need not be the Schreier conjugates and need not stay inside a standard horizontal fibre.

### Explicit `k=10` rational gap

For `k=10`, `Q=39` and

`a=2sqrt(11)+2sqrt(7)+2sqrt(19)`.

The exact checker uses

`sqrt(11)<199/60`, `sqrt(7)<127/48`, `sqrt(19)<109/25`,

so `a<4129/200`.

With

`z=5000/269`,

one has `z^2>39` and exactly

`z+39/z-4129/200 = 27277/672500 >0`.

Therefore `beta<z` and

`p_u>269/5000`.

Since `p_c<=1/19`,

`p_u-p_c > 269/5000 - 1/19 = 111/95000`.

## 5. The tight `k=9` case: reverse the fibre comparison

The free-tree-only estimate is not enough at `k=9`: `p_c<=1/17` lies above the scalar nonbacktracking `p_u` lower bound. Here the horizontal location of the explicit Schreier family is used once, in a genuinely different percolation comparison.

Let

`C_9={c_1^{+-1},...,c_9^{+-1}}`,

with `c_j=a_1^j a_2 a_1^{-j}`. Since the `a`-subgroup is `F_6`, the standard Schreier argument gives

`<c_1,...,c_9> ~= F_9`.

Every `c_j` is a word in the horizontal generators, so every `C_9` edge stays inside one `T_12` horizontal fibre of the standard product graph. Inside each such fibre, every `C_9`-component is a copy of `T_18`.

Root the `T_8` factor. Every non-root vertical base vertex has seven forward child fibres. On entering a fresh horizontal fibre at one seed, expose only the open `C_9`-cluster inside radius two of that seed; call its size `Z_2`.

For each of the seven forward vertical child fibres, inspect the standard vertical edges from all `Z_2` exposed vertices into that child fibre. Conditional on `Z_2`, the probability that at least one such edge is open is

`1-(1-p)^{Z_2}`.

Declare at most one offspring in each child fibre, choosing a deterministic first open crossing. The rooted `T_8` factor gives each visited base fibre a unique parent, different child fibres are disjoint, and all internal `C_9` edges exposed in a new fibre are fresh. Thus the retained process is an honest Galton--Watson process with mean

`m_2(p)=7 E[1-(1-p)^{Z_2}]`.                             (5.1)

Write `s=1-p`. For the radius-two cluster in `T_18`, define

`h_0=s`,

`h_1=s(s+p h_0)^17`,

`C_2=s(s+p h_1)^18 = E[s^{Z_2}]`.

Then

`m_2(p)=7(1-C_2)`.                                       (5.2)

At

`p=109/2000`,

the exact checker evaluates (5.2) in rational arithmetic and proves

`m_2(p)=1.008203927042365859684587599... >1`.

Equivalently `C_2<6/7`; the cross-multiplied positive integer certificate has 2141 decimal digits and SHA-256

`c553694b86ecd494d6f00a02a6d47b57830d9d99b5d83d690a9c74b68977c053`.

Because (5.2) is continuous in `p` and the inequality is strict, the retained Galton--Watson process is still supercritical for some `p'<109/2000`. Therefore

`boxed(p_c(G_9)<109/2000)`.                              (5.3)

This is an actual infinite-cluster transfer, not a finite-event statistic.

## 6. `k=9` uniqueness-side certificate

Here `D=38`, `Q=37`, and

`||A_{G_9}|| <= 2sqrt(11)+2sqrt(7)+2sqrt(17)`.

The exact rational bounds

`sqrt(11)<199/60`,

`sqrt(7)<127/48`,

`sqrt(17)<33/8`

give

`||A_{G_9}|| < 807/40`.

Take

`z=200/11`.

Then `z^2>37` and exactly

`z+37/z-807/40 = 23/550 >0`.

Hence the nonbacktracking growth exponent is `<z`, so

`p_{2->2}(G_9)>11/200`.

Since `p_{2->2}<=p_u`,

`boxed(p_u(G_9)>11/200)`.                                (6.1)

Combining (5.3) and (6.1),

`boxed(p_u(G_9)-p_c(G_9)>11/200-109/2000=1/2000)`.

The same proof works for **any** rank-nine free augmentation contained in a standard horizontal fibre subgroup and disjoint from `S0`; the specific Schreier conjugates are merely an explicit certificate that such a set exists in Rattaggi's `Sigma`.

## 7. Concrete uncovered family on Rattaggi's group

Rattaggi's 2007 construction gives

`Sigma=<a_1,...,a_6,b_1,...,b_4 | R_Sigma>`

with standard Cayley graph `T_12 square T_8` and an index-four finitely presented torsion-free simple subgroup `Sigma_0`.

The standard horizontal subgroup `<a_1,...,a_6>` is `F_6`. Inside `<a_1,a_2>`, the kernel of

`F(a_1,a_2)->Z`, `a_1|->1`, `a_2|->0`,

has Schreier basis

`{a_1^j a_2 a_1^{-j}: j in Z}`.

Therefore every finite initial set `c_1,...,c_k` freely generates `F_k`; each has reduced length at least three, so the new generators are distinct from `S0`.

This run proves the tail `k>=9`; the preserved earlier reports prove `k<=8`. Hence every graph

`G_k=Cay(Sigma,S0 union {c_1^{+-1},...,c_k^{+-1}})`, `k>=1`,

has `p_c(G_k)<p_u(G_k)` with an explicit quantitative certificate.

This is not counted from the unperturbed product graph: the added long horizontal generators change the fixed Cayley graph. The previously recorded group-theoretic exclusion also remains in force: the finite-index infinite simple subgroup rules out the acylindrically-hyperbolic group class used by the later Choi--Seo all-Cayley theorem, and hence also rules out the non-elementary hyperbolic group class. The bounded search in this run did not locate a theorem specifically covering all of these finite Schreier-generator augmentations. This is bounded negative evidence only; **external novelty/priority remains UNVERIFIED**.

## 8. Requested current literature scopes, refreshed 20 September 2026

### arXiv:1804.10191 — Hutchcroft, *Percolation on hyperbolic graphs*

Current arXiv version is **v3, 26 March 2019**; arXiv notes that v3 changed metadata only. Theorem 1.3 proves iid bond-percolation

`p_c<p_u`

for every connected, locally finite, **nonamenable Gromov-hyperbolic quasi-transitive graph**. It also proves the triangle condition at `p_c`. This is a real solution on the hyperbolic class, not on all nonamenable Cayley graphs.

### arXiv:2409.12283 — Hutchcroft--Pan, *Percolation at the uniqueness threshold via subgroup relativization*

Current arXiv entry is still **v1, 18 September 2024**. The paper studies the state **at `p_u`**. Its headline results prove nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth and prove co-heredity of a strong endpoint nonuniqueness property. The method develops subgroup relativization, relative uniqueness monotonicity/connectivity decay, sharpness and a relative Burton--Keane theorem. It does not state the quantitative fixed-graph theorem proved here.

### arXiv:2502.02560 — Terlov--Timar, *Weighted-amenability and percolation*

Current arXiv version is **v2, 14 September 2025**. It characterizes weighted/level amenability and proves a relaxed Pak--Smirnova-Nagnibeda-style version of the weighted/nonunimodular `p_h<p_u` conjectural picture. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` theorem used here.

### Later enlargement kept separate

Choi--Seo, arXiv:2508.08932, prove that **every Cayley graph of every acylindrically hyperbolic group** has a nonuniqueness phase. The Rattaggi ambient group used here was already checked outside that group class in the predecessor report.

The bounded current search also surfaced Hutchcroft--Pan's product paper arXiv:2412.15895, which treats products of trees with amenable Cayley graphs and proves refined uniqueness-threshold statements. The standard base product is therefore not claimed as new; the fixed augmented graphs above are the source-level objects proved directly here.

## 9. Exact computation saved in this run

Load-bearing checker:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T09-50-00+0300__t09-free-subgroup-augmentation-check.py`

created at commit

`5ccd1bb5822b73544b0992c8656a9ad1034f3f73`.

Executed exact output:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T09-50-00+0300__t09-free-subgroup-augmentation-check.out`

archived at commit

`577e99d47ee8c6ff355b5e388a9f7df5552a502f`.

The actual run verifies:

- exact rational `m_2(109/2000)>1` for the `T_18`-fibre / `T_8`-base subprocess;
- the square-root rational upper bounds used in the `k=9` and `k=10` root tests;
- the exact `k=9` root margin `23/550` and gap `1/2000`;
- the exact `k=10` root margin `27277/672500` and gap `111/95000`;
- the all-`k>=10` base margin `24/95` and derivative lower bound `1003/1444`.

The archived output terminates `ALL_EXACT_CHECKS_PASS`. This is a **self-check**, not an independent audit.

## 10. Residual obstruction and next attack

The universal T09 statement is still open. This run closes the entire engineered Schreier-augmentation family, so further increases of `k` on the same family would be bookkeeping rather than research.

The useful remaining obstruction is to weaken the *free-subgroup* input. The subgroup-augmentation transfer (3.1)--(3.6) shows exactly what is needed from an added subgroup `H`: a pair consisting of a rigorous upper bound on `p_c(Cay(H,C))` and a sufficiently small adjacency norm `||A_H||`. A nonfree subgroup with a favorable pair would produce a genuinely broader fixed-generating-set class.

The next materially different route should therefore be one of:

1. find a nonfree subgroup/block already present in a natural generating set and prove `p_c(Y)<beta_D(a_0+||A_Y||)^{-1}` directly; or
2. develop the colored nonbacktracking recurrence postponed by the last run so that standard-product and added-subgroup edge types are not collapsed by the triangle inequality.

No further certificate for the same free-conjugate family should be counted as source-level progress.

## ledger_delta

```yaml
ledger_delta:
  track: NM13-11
  parent: T09
  status: PARTIAL
  candidate_status: CANDIDATE_FULL_RESTRICTED_THEOREMS
  source_problem: "pc(G)<pu(G) for every Cayley graph of every finitely generated nonamenable group"
  original_problem_before:
    universal_status: OPEN
    explicit_rattaggi_family: "G_k certified through k=8"
    endpoint_k: 8
    endpoint_gap: ">1/2000"
  original_problem_after:
    universal_status: OPEN
    explicit_rattaggi_family: "G_k certified for every finite k>=1 (prior k<=8 plus new k>=9 tail)"
    k9_pc: "<109/2000"
    k9_pu: ">11/200"
    k9_gap: ">1/2000"
    all_k_ge_10: "any free rank-k augmentation of a (12,8)-group, disjoint from S0, has pc<pu"
    k10_gap: ">111/95000"
  mechanism_progress:
    - "reverse-fibre Galton-Watson: radius-2 T18 augmentation cluster branches through 7 forward T8 fibres"
    - "subgroup-driven pc transfer: added subgroup is used as a percolating subgraph rather than only an operator cost"
    - "for k>=10 horizontal-location hypothesis is removed entirely; any free augmentation works"
  prior_routes_preserved:
    - finite_set_escape_BK_last_exit
    - killed_SAW_boundary_energy
    - global_l2_SAW
    - scalar_nonbacktracking_and_product_stress_tests
    - quotient_fibre_shell_and_bridge
    - SL3_free_core_triangle_fibre_S_arithmetic
    - Rattaggi_arbitrary_k_le_3_and_horizontal_k_le_8
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  essential_checker_commit: 5ccd1bb5822b73544b0992c8656a9ad1034f3f73
  essential_output_commit: 577e99d47ee8c6ff355b5e388a9f7df5552a502f
  independent_review: NOT_DONE
  external_priority: UNVERIFIED
  next_attack: "nonfree subgroup pc/operator pair, or colored nonbacktracking recurrence for natural fixed generating sets"
```

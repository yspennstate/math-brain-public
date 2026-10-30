# fleet03/B02 FOREST report — 2-sum closure and genuine 3-connected minimal obstruction

Status: `ESSENTIAL_STEP_APPLIED`; parent FOREST target remains `OPEN` pending the team lead's full-candidate promotion policy and ordinary publication-grade source scrutiny. Execution context: `WITHOUT_VERIFIED_BRAIN`.

Run: `20260922T050248Z-B02-forest-r13`.

Exact assignment: prove a useful minimal-counterexample reduction covering a genuinely unresolved three-connected obstruction, not merely another finite graph class.

Assigned partner: `fleet04/B03`.

## 1. Named cross-account input actually consumed

I consumed fleet04/B03's independent end-to-end review
`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B03/20260922T014020Z-B03-r43/independent_end_to_end_review.md`
(blob `9851f9a7488f7edfe28e9273191551712fc297fc`).

That review independently rederives the complete-graph Hermite argument and source-checks the final Semple-Welsh paper's post-submission note attributing to Cocks the fixed-graph implication

    unit Conjecture 1.1 for G  ==>  M(G) is independence correlated.

It also records the stronger weighted/minor transfer used by the current team candidate.

I additionally source-checked the relevant final Semple-Welsh text directly. Their definition of independence correlation quantifies over every positive edge weighting, Proposition 3.5 proves minor closure, and the final note explicitly states that Cocks proved the fixed-graph implication above. Source: Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*, pp. 4, 6-7, 13, https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf .

## 2. New theorem: independence correlation is closed under 2-sum

This run proves the closure algebra directly.

Let `M = M1 ⊕_g M2` be a proper 2-sum. All variables except the deleted connector `g` are assigned arbitrary positive weights. For `i=1,2`, write

    A_i = I(M_i \ g),
    B_i = I(M_i / g),
    N_i = A_i - B_i.

Combinatorially, `B_i` generates independent sets on `E(M_i)-g` to which `g` can still be adjoined; `N_i` generates those that already span `g`. An independent set of the 2-sum is a pair of independent side sets which do not both span `g`. Hence

    I(M) = A_1 A_2 - N_1 N_2
         = A_1 B_2 + B_1 N_2.                    (2.1)

### Same-side marked pair

For distinct `e,f in E(M1)-g`, put `t=N_2/B_2 > 0`. Then

    I(M) = B_2 (A_1 + t B_1).

The bracket is exactly the independent-set polynomial of `M1` evaluated with connector weight `y_g=t`. Therefore

    Delta_M(e,f) = B_2^2 Delta_{M1}(e,f; y_g=t) >= 0

whenever `M1` is independence correlated. The `M2` case is symmetric.

### Cross-side marked pair

Take `e in E(M1)-g`, `f in E(M2)-g`. Set `A=A_1`, `B=B_1`, `D=B_2`, `N=N_2`. From `Z=AD+BN`,

    Z_e  = A_e D + B_e N,
    Z_f  = A D_f + B N_f,
    Z_ef = A_e D_f + B_e N_f.

Exact expansion factors as

    Delta_M(e,f)
      = (A_e B - A B_e)(D N_f - D_f N)
      = Delta_{M1}(e,g) Delta_{M2}(f,g) >= 0.      (2.2)

The last equality uses `A_2=D+N`, so
`Delta_{M2}(f,g)=(D_f+N_f)D-(D+N)D_f=D N_f-N D_f`.

Thus:

**2-SUM LEMMA.** If `M1` and `M2` are independence-correlated matroids, then their proper 2-sum is independence correlated.

No weighted closure of the target graph was assumed in deriving (2.1)-(2.2); it is supplied only for each smaller factor when the lemma is applied below.

## 3. New minimal-counterexample theorem: the obstruction is genuinely 3-connected

Use the exact result of fleet03/B02 run `20260922T025856Z-b02-forest-r12`: replacing each edge of a finite loopless multigraph by three internally vertex-disjoint 2-edge paths produces a finite simple graph whose uniform forest law projects uniformly, with covariance scaled by `4/81`. Hence the source simple-graph FOREST conjecture is equivalent to its loopless-multigraph version.

Assume FOREST is false and choose a loopless-multigraph counterexample `G` with the minimum number of edges, and a bad pair `e,f`.

1. `G` is connected. If `e,f` lie in different connected components, their indicators are independent. If they lie in the same component, all other components multiply every relevant count by the same factor, leaving a smaller counterexample.

2. `G` has no nontrivial 1-sum / cut-vertex decomposition. The forest polynomial factorizes over matroid direct sums. A bad pair must lie in one proper block, again contradicting edge-minimality.

3. `G` has no proper graphic 2-sum decomposition. Suppose
   `M(G)=M(G1) ⊕_g M(G2)` with both factors proper and loopless graphic. Each `Gi` has fewer edges than `G`, so minimality says the unit forest inequality holds for every pair in each `Gi`. By the published Cocks fixed-graph theorem as recorded by Semple-Welsh, each `M(Gi)` is therefore independence correlated for all positive weights. The 2-SUM LEMMA above makes `M(G)` independence correlated, hence in particular unit negatively correlated, contradiction.

4. Parallel pairs are excluded as a special 2-sum. If `p,q` are parallel and the graph has at least four edges, factor the parallel class through the graphic `U_{1,3}` connector gadget and the remainder with a virtual parallel connector; both factors are strictly smaller. Bridges are excluded by the direct-sum argument. The cases with at most three nonloop edges are uniform/direct-sum matroids and satisfy the inequality directly.

Therefore any minimal counterexample has a 3-connected cycle matroid. After deleting irrelevant isolated vertices, it is simple, has no bridge or cut vertex, has no proper two-separation, and lies in the genuine 3-connected graphic regime (in particular minimum degree at least three outside the directly checked tiny cases).

This is the requested non-finite-class reduction: any surviving failure must occur in the globally coupled 3-connected core. It rules out disconnected graphs, articulation decompositions, parallel/bridge degeneracies, and every proper 2-sum construction at once.

## 4. Source-body distinction and a self-contained rational-weight transfer

A second source check matters for proof hygiene. Alejandro Erickson's 2008 Waterloo thesis, *Negative Correlation Properties for Matroids*, Chapter 5.2, gives a full accessible proof of the class-wide equivalence between graphic unit negative correlation and graphic I-Rayleigh. Its Proposition 5.2.2 replaces unmarked elements by explicit `Q(k,a)` graphic 2-sum gadgets and proves an exact Rayleigh-gap scaling; Corollary 5.2.3 concludes the global equivalence. Source: https://uwspace.uwaterloo.ca/items/fac5cdd5-a289-460d-969a-5f51d0c60793 .

That accessible proof is class-wide: it assumes unit negative correlation for every derived gadget graph. It is not, by itself, a proof of the stronger fixed-graph statement `U(G) => W(G)`. Therefore the current complete-graph-to-all-graphs candidate may cite the final published Semple-Welsh note for the fixed-graph Cocks theorem, but should not substitute Erickson Proposition 5.2.2 as though it proved the same pointwise theorem.

For completeness I rederived Erickson's gadget transfer directly in graph language. Replace an unmarked edge `g=uv` of a base graph by `k` internally vertex-disjoint `u-v` paths of length `a>=2`. In an acyclic gadget state, either no path is complete or exactly one is complete. The local lift counts are

    L0 = (2^a-1)^k,
    L1 = k(2^a-1)^(k-1),

so `L1/L0 = q = k/(2^a-1)`. If all unmarked base edges are independently replaced this way, projection from gadget forests to base forests is acyclicity-preserving and gives

    Z_H = C Z_G(q),
    Z_{H,e} = C Z_{G,e}(q),
    Z_{H,f} = C Z_{G,f}(q),
    Z_{H,ef} = C Z_{G,ef}(q),

with `C=product_g L0(g)`. Hence

    Delta_H(e,f;1) = C^2 Delta_G(e,f;q).          (4.1)

The rationals `k/(2^a-1)` with `a>=2` are dense in the positive reals, so continuity gives the class-wide unit-to-weighted implication. This also identifies the previous B02 theta-3 simulation as exactly the special case `(a,k)=(2,3)`, where `L0=L1=27` and `q=1`.

Exact regression in this run:
- `(a,k)=(2,2)`: `L0=9`, `L1=6`, effective weight `2/3`;
- weighted `K4` test has `(Z,Ze,Zf,Zef)=(100/3,38/3,38/3,14/3)`, gap `44/9`;
- its two-length-2-path replacement has unit counts `(300,114,114,42)`, gap `396 = 81*(44/9)`;
- `(a,k)=(2,3)` gives `27/27`, recovering the prior unit multigraph simulation.

Checker SHA-256: `9c4d14ea530ce8e2b957764e49e9a4f9fa85e1060dd439b079c762e6782e871d`.
Output SHA-256: `85746dd0e717988f21b30f9fb1b25d737dfef9620b469e1431e411b7a4deee9d`.
Output terminates `THETA_WEIGHT_TRANSFER_PASS`.

## 5. Applied consequence for the team proof

The partner's complete-graph Hermite candidate remains compatible with this run. The new 3-connected reduction is independent structural progress: if one declines to use the complete-graph/Cocks/minor shortcut as a black-box full proof, there is now no need to search separators or finite decomposable classes for a counterexample. A genuine counterexample must survive in a simple 3-connected core and, by the prior B02 three-edge identity, its bad-pair signs form the rigid sign-cluster pattern.

Conversely, for the current `K_n -> all G` candidate, the exact irreducible imported theorem remains the **fixed-graph** Cocks implication, not merely the global gadget equivalence. The final Semple-Welsh paper states that implication explicitly; the accessible Erickson proof certifies only the class-wide version.

## 6. Outcome and next recipient

Outcome: `ESSENTIAL_STEP_APPLIED`.

New exact results:
- 2-sum closure of independence correlation, with same-side and cross-side Rayleigh factorizations;
- minimal loopless-multigraph counterexample has a genuinely 3-connected cycle matroid, hence the source obstruction can be confined to the simple 3-connected regime;
- self-contained theta-gadget rational-weight transfer, unifying the prior theta-3 simulation with the standard Cocks/Erickson global reduction.

Earliest remaining mathematical/source obligation for the current full-candidate route:
- either accept/cite the published fixed-graph Cocks theorem exactly as recorded by Semple-Welsh, or obtain the Cocks proof body and line-check that pointwise upgrade;
- for a fully self-contained route avoiding that theorem, prove the required weighted inequality directly on `K_n` or prove unit pNC for all explicit theta-gadget expansions of `K_n`.

Next recipients: FOREST lead `fleet01/B01` and assigned partner `fleet04/B03`.

No parent-problem truth/novelty/publication claim is made here. No brain runtime was authenticated or used.

# FOREST — all-parameter multi-bridge gluing and the 3-connected reduction

Candidate/version: `FOREST-2CUT-MULTIBRIDGE-GLUING-v1`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent target: **OPEN**  
Full-proof candidate: **false**  
Context: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact target and inherited state

The target is the Grimmett–Winkler pairwise negative-correlation conjecture for the **uniform law on all unrooted forests** of every finite simple graph. For a positive edge-weight vector `y`, write

`I_G(y) = sum_{F forest of G} prod_{e in F} y_e`

and, for distinct edges `e,f`,

`Delta_G(e,f) = (partial_e I_G)(partial_f I_G) - I_G partial_ef I_G`.

At unit weights, `y_e y_f Delta_G(e,f)` is exactly `Z_e Z_f - Z Z_ef`, so the sign is the source target.

The newest complete team-lead handoff consumed is account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, shared-handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. Its proposed end-to-end route is complete-graph negative correlation -> Cocks fixed-graph weighted upgrade -> minor closure -> arbitrary simple graph. I do **not** promote that parent candidate here because its required two independent end-to-end reviews are not yet both present.

The assigned partner account01/B02 handoff consumed is `FOREST-DEG3-STAR-ID-v1`, blob `ec0d03c511bdb85d8fb20788e9037222c26c8bcb`. It proves an exact nonnegative identity for adjacent marked edges at a degree-at-most-three center and shows that coefficientwise star positivity already fails at degree four, so a separator argument must retain exact cross-piece multiplicities rather than assume termwise positivity.

A named OTHER-account result used substantively is account03/B02 `FOREST-KN-COCKS-REDUCTION-v2`, blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`, which independently checked the Cocks fixed-graph scope and Semple–Welsh minor closure. I use precisely that weighted fixed-graph implication below.

Public source check: Semple–Welsh, *Negative Correlation in Graphs and Matroids*, Proposition 3.5 proves minor closure for independence-correlated matroids, and its final note records Cocks's theorem that if forest Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. Cocks, *Correlated Matroids* (CPC 17(4), 2008), also proves correlated matroids are closed under 2-sum. No novelty is inferred from the direct formulas below.

## 2. Multi-bridge forest polynomial

Let `G` have a two-vertex separator `{u,v}`. Decompose its edge set into `uv`-bridges `B_1,...,B_m`: for each component of `G-{u,v}`, take that component together with `u,v` and all incident edges; if the original edge `uv` is present, treat it as its own singleton bridge. Thus bridge edge sets are disjoint and different non-singleton bridges meet only in `{u,v}`.

For bridge `B_i` define

- `D_i`: weighted sum of forests of `B_i` in which `u` and `v` are disconnected;
- `C_i`: weighted sum of forests of `B_i` in which `u` and `v` are connected.

Always `D_i>0` for positive weights because the empty forest contributes. A singleton `uv` bridge has `D_i=1` and `C_i=y_uv`.

A global edge set is a forest exactly when each bridge restriction is a forest and **at most one** bridge restriction connects `u` to `v`: two such restrictions would supply two internally edge-disjoint `u-v` paths and hence a cycle; conversely every cycle crossing bridges would require two such paths. Therefore

`I_G = prod_i D_i + sum_i C_i prod_{j!=i} D_j`.                                  (2.1)

This is the exact all-positive-parameter separator partition function, with disconnected forests and the empty forest retained.

## 3. Same-bridge marked edges: exact virtual-edge response

Suppose distinct marked edges `e,f` both lie in `B_i`. Put

`A_i = prod_{k!=i} D_k`,

`lambda_i = sum_{k!=i} C_k/D_k`.

Let `B_i^+` be `B_i` with a **new virtual edge** `g_i=uv` of weight `t`. Because a forest containing `g_i` may use only a base forest that disconnects `u,v`,

`I_{B_i^+}(t) = C_i + (1+t)D_i`.                                                (3.1)

Equation (2.1) becomes the exact identity

`I_G = A_i I_{B_i^+}(lambda_i)`.                                                (3.2)

The outside factor is independent of `e,f`; differentiating gives

`Delta_G(e,f) = A_i^2 Delta_{B_i^+}(e,f) |_{t=lambda_i}`.                        (3.3)

Thus the entire outside graph enters a same-bridge pair through the single effective positive fugacity `lambda_i`. There is no assumption that it equals one, and no coefficientwise positivity assumption.

## 4. Different-bridge marked edges: outside response cancels

Now let `e in B_i`, `f in B_j`, `i!=j`. Put

`A_ij = prod_{k notin {i,j}} D_k`,

`lambda_ij = sum_{k notin {i,j}} C_k/D_k`.

Then

`I_G/A_ij = (1+lambda_ij)D_iD_j + C_iD_j + D_iC_j`.                             (4.1)

For an edge `e` of bridge `B_i`, define

`R_i(e) = D_i partial_e C_i - C_i partial_e D_i`.                               (4.2)

A direct two-variable determinant expansion of (4.1) gives the exact factorization

`Delta_G(e,f) = A_ij^2 R_i(e) R_j(f)`.                                          (4.3)

In particular **every other bridge response cancels from the sign**.

Moreover, using (3.1), for the virtual edge `g_i`,

`Delta_{B_i^+}(e,g_i) = R_i(e)`,                                                (4.4)

independently of the virtual weight `t`. Consequently

`Delta_G(e,f) = A_ij^2 Delta_{B_i^+}(e,g_i) Delta_{B_j^+}(f,g_j)`.               (4.5)

If one marked bridge is the singleton original edge `uv`, its response is directly `R=1`; no parallel virtual edge is introduced there. This explicitly covers the separator-edge case that is easy to lose in an abstract 2-sum statement.

## 5. All-parameter gluing theorem

**Theorem.** Let a finite graph `G` be assembled from `uv`-bridges as above, with arbitrary positive edge weights. If, for every non-singleton bridge `B_i`, the simple augmentation `B_i^+=B_i+g_i` is independence correlated for all positive edge weights, then `G` is independence correlated for all positive edge weights.

**Proof.** For a marked pair in one bridge, (3.3) applies at the positive effective weight `lambda_i` and gives nonnegative gap. For a marked pair in two distinct non-singleton bridges, (4.5) is a product of two nonnegative virtual-edge gaps times a positive square. If one marked edge is the singleton separator edge, (4.3) has the singleton factor `R=1` and the other response is nonnegative by (4.4). These exhaust all distinct marked pairs. QED.

The statement simultaneously handles any number of pieces. A degenerate formulation with `lambda_i=0` can be obtained by the `t -> 0+` limit, but a proper two-cut of a 2-connected graph has other nontrivial `uv` bridges, so the effective response needed below is positive.

## 6. Exact reduction of a minimal source counterexample to 3-connectivity

Assume, for contradiction, that the unit-weight FOREST target fails, and choose a finite simple counterexample `G` with the fewest edges (then fewest vertices if a tie-break is desired).

Disconnected unions and one-vertex sums factor their forest polynomial as a product. For marked edges in different factors the Rayleigh gap is zero; for marked edges in one factor it is the factor gap times the square of the outside partition function. Hence minimal `G` is connected and has no nontrivial one-separator decomposition. Trivial small blocks are harmless; for example `K_3` has `Z=7`, `Z_e=3`, `Z_ef=1`, hence gap `2`.

Suppose now that `G` is 2-connected but not 3-connected, and choose a proper separator `{u,v}`. Isolate an original `uv` edge, if present, as a singleton bridge. Every remaining component bridge contains a `u-v` path. For every non-singleton `B_i`, `B_i^+=B_i+g_i` is a finite **simple** graph. It has strictly fewer edges than `G`: a proper two-cut has at least two component bridges, and omitting the other component bridge removes at least a two-edge `u-v` path while adding back only the single virtual edge.

By minimality, every `B_i^+` satisfies the source unit-weight conjecture for all its edge pairs. Cocks's fixed-graph theorem upgrades that fact to independence correlation of `M(B_i^+)` for **all positive weights**. Applying the all-parameter gluing theorem at the actual unit weights of `G` gives `Delta_G(e,f)>=0` for every marked pair, including a pair containing the original separator edge. Contradiction.

Therefore:

**Corollary. Any edge-minimal finite simple counterexample to the uniform-forest pairwise negative-correlation conjecture must be 3-vertex-connected (with the usual small-order convention handled separately).**

This is the requested separator/three-connected reduction. It is an essential structural step, not a proof of the parent conjecture.

## 7. Conditional end-to-end placement

The current lead candidate can now be stated with separator handling made explicit:

`complete-graph theorem`
` -> Cocks fixed-graph all-positive-weight upgrade`
` -> (equivalently, Semple–Welsh minor closure for the lead route; or the direct multi-bridge gluing theorem above for separator decomposition)`
` -> arbitrary finite simple graph`.

My direct theorem pays the previously explicit all-parameter two-separator compatibility obligation and independently proves that any minimal obstruction is 3-connected. The parent lead's complete-graph/Hermite step is separate and still subject to its review gate.

## 8. Exact regression computation

`forest_separator_checker.py` independently enumerates all forests in deterministic small weighted multi-bridge assemblies. It checks (2.1), the same-bridge identity (3.3), and the cross-bridge identity (4.3), including assemblies with a singleton original `uv` edge.

Exact output:

```
PASS
cases 24
marked_pair_identities 640
seed 20260922
```

Arithmetic is exact `fractions.Fraction`, not floating point. This is regression evidence only; the proof is the algebra above.

Checker SHA-256: `bd313a2431e1ff59ca90d1144c78ba6fea41627a798cf31505fdc914cc7d0e2d`.  
Output SHA-256: `19896e87ffb3c13cf2470d2ec09c6f23318a1838465ebd055efc8d2b986b04ab`.

## 9. Remaining obligation and next recipient

The parent target remains `OPEN`. This run does not supply or claim the second independent end-to-end review required for the account01/B01 complete-graph/Cocks candidate. The nearest useful recipient is the FOREST lead and account04/B03: the gluing theorem removes separator ambiguity from any minimal-counterexample formulation, while the parent candidate still needs independent verification of its complete-graph EGF/Hermite step and external source chain before any full-proof status can be considered.

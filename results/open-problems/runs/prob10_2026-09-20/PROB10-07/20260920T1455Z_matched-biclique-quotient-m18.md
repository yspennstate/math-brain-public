# PROB10-07 — matched-biclique stabilizer quotient and strict uniform-forest edge negative correlation through terminal width 18

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending independent review.** The arbitrary-finite-graph uniform-all-forests problem remains **OPEN**.

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Runtime request/status: GPT-6 maximum was requested. Authenticated applied model/effort telemetry is **UNVERIFIED**. The surrounding chat runtime identifies GPT-5.6 Sol, but that is not authenticated scheduler telemetry, so no GPT-6/maximum claim is made.

## 1. Exact model, contract, and ownership boundary

For a finite graph `G=(V,E)`, choose uniformly from all acyclic subsets `F subseteq E`, retaining the full vertex set. Write

`Z = #{F subseteq E : F acyclic}`,

and, for distinct present edges `e,f`, let `Z_e,Z_f,Z_ef` count forests containing the indicated marked edges. The source inequality

`P(e,f in F) <= P(e in F) P(f in F)`

is exactly

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

This report concerns that all-forests law only. It is not a uniform spanning-tree statement, a minimum-spanning-tree statement, a random-cluster statement at a different parameter, or a fixed-component forest ensemble.

The following current repository state was consumed before fixing scope.

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`.
- root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`.
- R13 displacement handoff `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`, blob `71ca654e6c310572fe9d170d6f05c247f3871612`.
- P14 mandatory forest handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`, blob `bed2241d948b8a20b854efc248ccf5b46b4325cd`.
- P14 newest successor/frozen-predecessor handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md`, blob `f7fc8dc894602ef88d9d3cba46c475807dd92571`, and current claim `operations/claims/G0007.md`, blob `eb238df6d728ba5d7676073261560289eb56ab71`.
- HARD10-01 final forest handoff `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`, blob `d95d0b06d9eedb6f9edd8557d7e292267074d492`.
- preceding PROB10-07 report `runs/prob10_2026-09-20/PROB10-07/20260920T1357Z_matched-biclique-m6-m7-two-nilpotent.md`, blob `853f839d95114c8c89c7d32f227669f4d16c1bcf`.
- newest distinct NM13-04 forest follow-up `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T13-24-00Z__triangle-star-forest-sign-theorem.md`, blob `bf4cf25ab326cdb297755d3d722548b134b9ee69`.

P14/HARD10-01 retain the arbitrary-graph complete-order-nine certificate and the generic 3-connected / three-terminal obstruction. P14 has since moved to a different claimed source and explicitly preserves the Grimmett predecessor as frozen. NM13-04 currently studies a triangle joined to arbitrary star forests. This run therefore takes only the complementary matched-biclique family below and performs no arbitrary-graph graph-order enumeration.

The mathematical idea was written before the new checker at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1438Z_matched-biclique-quotient_idea.md`,

creation/readback commit `0492ac07706965a335646e729965cb833a9e6335`, blob `754eb85d722a92000c0b4571509937e539d04b61`.

## 2. Source-level before/after and mechanism metrics

Parent source status: **OPEN -> OPEN**.

Largest completely certified arbitrary-simple-graph order in inherited repository continuity: **9 -> 9**. No graph-order census credit is claimed here.

Structural-family metric: the preceding PROB10-07 matched-biclique theorem covered terminal widths `m=6,7` (with smaller widths available in neighboring history). This run proves the complete parameter range for the eleven new widths

`m=8,9,...,18`.

Thus the PROB10-07 matched-biclique width frontier moves

`7 -> 18`.

Mechanism metric: the preceding proof used the full Bell lattice at widths 6 and 7. The new proof quotients by the stabilizer of the at most two left terminals distinguished by the marked pair. At width 18 the largest required quotient has only `4285` states. This mechanism is independently checked at widths 6 and 7 by exact equality of all 28 primitive Rayleigh-polynomial digests with the earlier full-Bell implementation.

## 3. Three materially different approaches compared before code

### Route A — stabilizer quotient of the two-layer nilpotent algebra

A marked pair distinguishes at most two left terminals. Quotient terminal-connectivity partitions by permutations of all remaining terminals, derive the exact singleton and matched-pair transitions directly on this quotient, and retain the two commuting nilpotent generators. This route succeeds and is the theorem route below.

### Route B — quantitative deletion–contraction domination

The preceding run proved the exact identity

`A B Delta_G = B(A+B)Delta_A + A(A+B)Delta_B - E_e E_f`,

where the last product is an environmental-response term. It also exhibited a source-valid width-6 instance with `E_eE_f>0`, so endpoint Rayleigh positivity alone cannot give an induction. A successful deletion–contraction proof would need a genuinely quantitative domination of the adverse product by the two endpoint gaps. No such general inequality is asserted here; this route is retained as a precise obstruction rather than recycled as a false induction.

### Route C — exact counterexample-first arithmetic

If any normalized orbit polynomial had a negative value at a physical integer parameter, it would give a counterexample in the original all-forests model, not merely a failure of the certificate. The new implementation therefore checks the polynomial signs exactly and also performs a direct original-edge-subset regression on a small member containing all fourteen orbit types. No negative Rayleigh difference was found in this family.

## 4. Graph family and new theorem

For integers `m>=1`, `k>=1`, `r>=0`, define

`G_m(k,r)=K_{m,2k+r}+M_k`,

where the left side has `m` independent vertices, the right side has `2k+r` vertices, all left-right edges are present, and `M_k` is a matching on `2k` of the right vertices, with no other right-right edges.

### Theorem `PROB10-07-MATCHED-BICLIQUE-QUOTIENT-M8-M18`

For every

`m in {8,9,...,18}`, `k>=1`, `r>=0`,

and every pair of distinct present edges `e,f` of `G_m(k,r)`,

`Delta_{G_m(k,r)}(e,f)>0`.

Hence the uniform probability measure on **all forests** of every such graph has strict pairwise edge negative correlation.

Only widths 8 through 18 are new theorem claims in this report. Widths 6 and 7 are rechecked solely to validate the quotient implementation against the preceding independent full-Bell calculation.

## 5. Exact quotient state space

Fix an edge-pair orbit and let `d<=2` be the number of left terminals touched by its marked spokes. The group `S_{m-d}` permutes the undistinguished left terminals while fixing the `d` distinguished labels.

A quotient state records:

1. a set partition of the distinguished labels;
2. for every block containing distinguished labels, the number of undistinguished terminals in that block;
3. the integer partition of the sizes of all pure blocks containing no distinguished labels.

This is an exact orbit description of terminal-connectivity partitions. Every layer transition below depends only on current block sizes and on which distinguished labels lie in which blocks, so it is strongly lumpable with respect to this quotient.

The resulting state counts at width 18 are

`d=0: 385`, `d=1: 1212`, `d=2: 4285`.

A marked pair never needs `d>2` in this family.

## 6. Singleton-layer transition

Let `T_U` be the transition generated by a fresh unmatched right vertex, with spokes to every left terminal available and the spokes to terminals in `U` forced.

A set of selected spokes is acyclic exactly when it uses at most one terminal from each current terminal-connectivity block. If a selected block `B` is not forced, there are `|B|` choices of terminal in that block. If it contains a forced terminal, that choice is fixed. Two forced terminals already in the same current block make the transition zero. If at least two blocks are selected, those blocks merge; selecting zero or one block leaves the terminal partition unchanged.

Thus the transition weight and target quotient state depend only on the quotient data, proving strong lumpability for every `T_U`.

For the unmarked operator `S=T_empty`, the diagonal configurations are the empty spoke set and the `m` one-spoke choices, so

`S=(m+1)I+N`.

Every nonzero transition in `N` strictly coarsens the terminal partition; consequently

`N^m=0`.

## 7. Exact matched-pair transition — the new structural simplification

Consider a fresh right matched pair `(u,v)` with internal edge `h=uv`. Let `U` and `V` be the sets of left terminals whose spokes from `u` and `v`, respectively, are forced.

Split the layer by whether `h` is absent or present.

### 7.1 `h` absent

The two right vertices are disconnected from each other inside the layer. Processing the `u`-star and then the `v`-star is exact, including all cycle exclusions created by the first star. Hence the transition is

`T_U T_V`.

### 7.2 `h` present

Now a current terminal block may carry at most one selected spoke in total across the two endpoints. If the same old block were connected once to `u` and once to `v`, the old path inside that block together with the two spokes and `uv` would form a cycle. Conversely, if every selected old block is used at most once, the new layer connects those distinct old components through the tree consisting of their spokes plus `uv`, so no cycle is created.

Therefore an optional selected block `B` contributes exactly

`2|B|`

choices: one of the two endpoints `u,v` and one terminal of `B`. A block selected by a forced spoke contributes weight one. If two forced spokes refer to terminals already lying in the same old block, the transition is zero. Whenever at least two old blocks are selected, all of them merge into one terminal-connectivity block. Call this exact transition `H_{U,V}`.

Again its weight and target depend only on block sizes and distinguished-label locations, so it is strongly lumpable on the quotient.

If `h` itself is forced, the matched-pair transition is simply

`H_{U,V}`.

If `h` is not forced, the two disjoint cases give

`P_{U,V}=T_U T_V+H_{U,V}`.

In particular, for a completely unmarked matched pair,

`P=S^2+H_empty`.

The diagonal contribution is

`lambda_m=(m+1)^2+(1+2m)=m^2+4m+2`:

with `h` absent, each of `u,v` chooses zero or one spoke, giving `(m+1)^2`; with `h` present, preservation of terminal connectivity allows `h` alone or `h` plus one spoke from exactly one endpoint, giving `1+2m`. Thus

`P=lambda_m I+Q`.

Every nonzero transition in `Q` strictly coarsens terminal connectivity.

## 8. Commuting nilpotents and exact bivariate polynomial response

An unmarked singleton layer and an unmarked matched-pair layer use disjoint fresh vertices and edges. Processing those two disjoint layers in either order enumerates exactly the same unions of edge sets with the same induced terminal partition. Therefore

`SP=PS`,

and after subtracting scalar diagonals,

`NQ=QN`.

Because every factor `N` or `Q` strictly coarsens the terminal partition, a product of at least `m` such factors vanishes. Hence

`Q^i N^j=0` whenever `i+j>=m`.

Put

`mu=m+1`, `lambda=m^2+4m+2`.

For all integers `x,y>=0`, commutation and nilpotence give the finite exact identity

`P^x S^y = lambda^x mu^y sum_{i+j<m} binom(x,i) binom(y,j) lambda^{-i} mu^{-j} Q^i N^j`.

No interpolation is used.

Expose every right layer touched by the full marked pair in all four conditioned counts `Z,Z_e,Z_f,Z_ef`. If the pair uses `a` matched-pair layers and `b` unmatched singleton layers, put

`x=k-a`, `y=r-b`.

After the distinguished layers are processed, the remaining count in condition `C` has the form

`Z_C=lambda^x mu^y C_C(x,y)`

for an exact rational polynomial `C_C`. Consequently

`Delta(e,f)=lambda^(2x) mu^(2y) R_O(x,y)`,

where

`R_O=C_e C_f-C_0 C_ef`

is an exact bivariate rational polynomial determined only by the edge-pair orbit `O` and the width `m`.

## 9. Exhaustive fourteen-orbit reduction

Under permutations of left terminals, permutations of matched right layers, swaps of the two endpoints within each matched layer, and permutations of unmatched right vertices, every unordered pair of distinct present edges belongs to exactly one of fourteen geometries:

1. two unmatched spokes in one singleton layer, different terminals;
2. unmatched spokes in two singleton layers, same terminal;
3. unmatched spokes in two singleton layers, different terminals;
4. a matching edge and a spoke in the same matched layer;
5. two spokes from the same matched endpoint, different terminals;
6. spokes from opposite matched endpoints, same terminal;
7. spokes from opposite matched endpoints, different terminals;
8. two matching edges in different matched layers;
9. a matching edge and a spoke in different matched layers;
10. spokes in different matched layers, same terminal;
11. spokes in different matched layers, different terminals;
12. a matching edge and an unmatched spoke;
13. a matched spoke and unmatched spoke, same terminal;
14. a matched spoke and unmatched spoke, different terminals.

The checker independently classifies every actual pair in the generic graph `G_m(2,2)` and finds exactly these fourteen classes with no residue. At width 18 this generic instance has 110 edges and 5,995 unordered edge pairs.

## 10. Exact sign certificate through width 18

For each width `m=8,...,18` and each of the fourteen orbits, the checker expands `R_O(x,y)` in the ordinary monomial basis with Python integers and `Fraction`, with no floating-point sign decisions.

For every one of the

`11 x 14 = 154`

new orbit polynomials, every coefficient is nonnegative. The checker also evaluates the polynomial at the first physical residual parameter point and obtains a strictly positive exact value. Hence, because physical `x,y` are nonnegative integers (with `x>=1` only in the orbit classes that use no distinguished matched layer),

`R_O(x,y)>0`

throughout the complete physical parameter range. Since `lambda,mu>0`, this proves the theorem.

At width 18 the largest Rayleigh-polynomial total degree is 34. The aggregate SHA-256 digest of the fourteen primitive polynomial tables is

`72876391fff454498acba207bf1e6c95771b6421d1f244abd4574dc3618d469d`.

## 11. Falsification checks and independent implementation agreement

The theorem is the exact symbolic calculation above, but two checks guard against implementation-specific mistakes.

First, direct enumeration of the original graph `G_2(2,2)` examines all edge subsets, rejects cycles by union-find, and counts every one of the 91 unordered edge pairs. It finds 5,460 forests, all fourteen pair-orbit types, and minimum exact Rayleigh numerator

`2916>0`.

For a representative of each orbit, the directly counted tuple `(Z,Z_e,Z_f,Z_ef)` agrees exactly with the quotient-transfer prediction (up to the harmless interchange of `e,f`). This tests the new `h`-present transition against the original model rather than against another transfer implementation.

Second, at widths 6 and 7 the quotient code recomputes every one of the 28 earlier orbit polynomials and compares the SHA-256 digest of its primitive exact coefficient table with the independent full-Bell implementation from the preceding run. Every digest matches exactly. Thus the new quotient route reproduces the old theorem before it is used to extend the width frontier.

## 12. Executed artifacts

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1450Z_matched-biclique-quotient-m6-m18_checker.py`

creation/readback commit `07eaa4d3f6d182874eaf3362fa72ade582d5938a`, Git blob `dd9cb5123ff48b66da2a8c17aaeb5ed466242976`, local SHA-256 `bcf157e03774e649e9978a3a468a5143a87acebe419b56a712674430c436f02c`.

Archived actual execution:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1450Z_matched-biclique-quotient-m6-m18_checker.out`

creation/readback commit `4bbfcceaab1b17b8e330d764c050e3d7e9fd9000`, Git blob `d8f57bffe446ace47f99a85a4a6598cc47b675ba`, local SHA-256 `d7dc4332d70a50f11a38b066cba151ce0cbc9f09ca0c027cd04e7b36b45d881a`.

The archived transcript contains four actual invocations covering widths `6..12`, `13..15`, `16..17`, and `18`; every invocation terminates

`PROB10_07_MATCHED_BICLIQUE_QUOTIENT_EXACT_PASS`.

The non-mutating forest-owner handoff is

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1455Z_matched-biclique-quotient-m18_forest-owner-handoff.md`,

creation/readback commit `5c0cfbc3ff26838f0fe941fb87b0d62fd5ef66e1`, blob `5603a1dcc9b0f293c29b476aafdde4bf8e59e891`.

## 13. Current literature boundary

The source remains Grimmett–Winkler, *Negative association in uniform forests and connected graphs*, arXiv:`math/0302185`, which formulates the uniform-all-forests edge-correlation conjecture and reports its historical finite verification. Erickson, arXiv:`1008.3660`, proves the stronger weighted Rayleigh/SOS property for series-parallel graphs. Tang–Zhang, arXiv:`2603.10738`, prove pairwise negative correlation for specified uniform spanning-subgraph ensembles of complete graphs, including fixed-component forest ensembles for fixed component count and sufficiently large order; that is not the present arbitrary-graph law mixing all forest component counts.

A fresh bounded 20 September 2026 search found no source-matching general resolution and no direct prior theorem for the exact matched-biclique family above. A negative search is not a novelty certificate. External novelty/priority of the restricted theorem therefore remains **UNVERIFIED**.

## 14. Remaining full-scope gap and next structural question

The arbitrary finite-graph conjecture is not materially reduced by a finite width cutoff. The inherited minimal-counterexample reduction still leaves arbitrary 3-connected graphs, and P14/HARD10-01's three-terminal environmental/mixed-polarization obstruction is untouched. The present advance shows that a large, genuinely non-series-parallel two-parameter family admits an exact finite-dimensional response algebra far beyond the full Bell-lattice scale.

The next family-specific mathematical question is whether the coefficientwise positivity observed through `m=18` can be proved uniformly in `m`, rather than checked one width at a time. The quotient formulas suggest searching for a width-recursion or total-positivity statement for the fourteen primitive coefficient arrays. That would convert the finite width frontier into an all-width theorem for `G_m(k,r)`, but no such uniform-in-`m` proof is claimed here.

Parent verdict after this run:

`OPEN / PARTIAL`.

No scheduler, cadence, enabled state, email, Drive, public posting, workflow, permission, or peer-owned claim was changed.

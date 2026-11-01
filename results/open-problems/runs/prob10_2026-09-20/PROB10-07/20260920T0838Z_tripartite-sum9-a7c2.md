Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — GPT-6 maximum was requested, but no authenticated GPT-6/maximum runtime telemetry is exposed.

# PROB10-07 — complete-tripartite width-nine Rayleigh certificate

Status: **PARTIAL** on the parent Grimmett–Winkler conjecture. The arbitrary-finite-graph uniform-all-forests statement remains OPEN. This run proves a new restricted infinite structural family and does not alter P14/HARD10-01 graph-order ownership.

## 1. Exact source target and before/after metrics

For a finite graph `G=(V,E)`, let

\[
Z_G=\#\{F\subseteq E:F\text{ is acyclic}\},
\]

and, for distinct present edges `e,f`, let `Z_e,Z_f,Z_{ef}` count forests containing the indicated marked edges. Under the uniform measure on **all forests**,

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F)
\quad\Longleftrightarrow\quad
\Delta_G(e,f):=Z_eZ_f-Z_GZ_{ef}\ge0.
\]

This is not the uniform-spanning-tree model, a minimum-spanning-tree law, or a fixed-component forest ensemble.

**Parent source status:** `OPEN -> OPEN`.

**Complete arbitrary-simple-graph order metric:** `9 -> 9` (unchanged; this run does not enumerate graph orders).

**PROB10-07 structural metric before:** every complete tripartite graph `K_{r,s,t}` with sorted part sizes `r<=s<=t` and `r+s<=8`.

**PROB10-07 structural metric after:**

\[
\boxed{\text{every complete tripartite }K_{r,s,t}\text{ with }r\le s\le t\text{ and }r+s\le9.}
\]

The new boundary families proved in this run are

\[
\boxed{K_{1,8,n},\ K_{2,7,n},\ K_{3,6,n},\ K_{4,5,n}\qquad(n\ge1),}
\]

and every distinct physical edge pair is in fact **strictly** negatively correlated.

No counterexample to the original source model was found.

## 2. Continuity, ownership, and consumed evidence

The run began from the current owner contract and exclusion state, not from the stale R13 target:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- P14 forest handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- HARD10-01 forest handoff `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- own predecessor `runs/prob10_2026-09-20/PROB10-07/20260920T0742Z_tripartite-sum8-b84d.md`;
- newest neighboring structural reports `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T08-19-21Z__triangle-right-p6-sign-theorem.md` and `proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T07-40-30Z__p6-path-recurrence-report.md`;
- current repository searches for the P14/HARD10 claim history and PROB10-07 handoffs.

The canonical source/ownership picture remains: P14/HARD10-01 own the complete order-nine census and the 3-connected/minimal-counterexample reduction. P14 records the surviving arbitrary-graph obstruction as a genuinely three-terminal/three-cut problem; HARD10-01 records the same obstruction in an environmental-covariance mixture form. This run does not revisit their enumeration and does not edit a peer-owned claim.

The neighboring NM13 tracks treat three-terminal join/layer/path families. Their newest `P6` results are structurally different from the present family: here a fixed `K_{a,b}` core on nine terminals is joined to an independent repeated third part. No NM13 theorem is claimed as a consequence of this run, and no NM13 claim is seized.

The earlier R13 Boolean-Komlos work remains preserved at

`runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.

A non-mutating owner-chain handoff for this run is stored at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_forest-owner-handoff.md`.

## 3. Three materially different mathematical attacks considered before code

The exact idea was written before checker construction in

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_idea.md`.

### Route A — deletion/contraction closed form

The identities

\[
Z_e(G)=Z(G/e),\qquad Z_{ef}(G)=Z(G/e/f)
\]

suggest expressing every Rayleigh difference through four unmarked all-forest partition functions and then deriving a closed formula for complete multipartite graphs and their contractions. This would be stronger than a fixed-width transfer.

The obstruction is source-specific: standard matrix-forest determinant identities naturally weight rooted forests, whereas Grimmett–Winkler use each unrooted forest with equal weight. Moreover, contractions of marked complete-multipartite edges introduce identified vertices and parallel edge classes. I did not find a source-matching determinant formula eliminating these issues, so no rooted-forest identity was substituted for the target.

### Route B — quotient the Bell lattice by terminal symmetry

At width nine there are `B_9=21147` labelled terminal partitions. Quotienting them by `S_a x S_b` would be the natural scaling route and could potentially reach arbitrary fixed width.

The missing proof obligation is **simultaneous strong lumpability** of all operators needed for `Z,Z_e,Z_f,Z_{ef}`. It is not enough for the unmarked repeated-vertex operator to lump; every forced-spoke operator associated with a marked edge must lump compatibly as well. I did not assume this. Establishing this representation-theoretically is a promising next structural route.

### Route C — full Bell transfer with sparse exact preprocessing

This route succeeds. It retains all 21147 states, but uses the block structure of a terminal partition to enumerate a fresh repeated-part vertex without iterating all `2^9` spoke subsets separately for every state. Core forests are enumerated once per fixed `K_{a,b}` and simultaneously accumulated into all marked-core vectors required by the edge-pair orbit representatives. The resulting calculation remains exact and certifies all `n`, rather than checking finitely many values.

## 4. Fresh-vertex transfer lemma at width nine

Fix one of

\[
(a,b)\in\{(1,8),(2,7),(3,6),(4,5)\},
\]

let `T=A sqcup B` be the nine fixed terminals with `|A|=a`, `|B|=b`, and let the fixed core be `K_{a,b}`. Every vertex of the third part is adjacent to all terminals and to no other third-part vertex.

A partially exposed forest induces a set partition `pi` of `T`: two terminals lie in one block exactly when they are already connected.

**Lemma 4.1.** If a new third-part vertex `v` is joined to a spoke set `S subseteq T`, the augmented edge set is acyclic if and only if `S` meets each block of `pi` in at most one terminal. When this holds, the new terminal partition is obtained by merging exactly the blocks hit by `S`.

**Proof.** If two selected terminals are already in the same block, the old path between them together with their two spokes through `v` creates a cycle. Conversely, if each selected terminal lies in a distinct old component, adjoining one new vertex and one edge into each of those components connects the selected components by a star and cannot create a cycle. The resulting connectivity relation therefore merges precisely the selected blocks. QED.

Let `M` be the unmarked fresh-vertex transition matrix on the Bell set `Pi_9`. For any state, the empty spoke choice and the nine singleton choices leave the terminal partition unchanged. Thus

\[
\boxed{M=10I+N.}
\]

Every nonzero transition represented by `N` strictly lowers the number of terminal blocks. Since there are at most nine blocks,

\[
\boxed{N^9=0.}
\]

The checker independently verifies `|Pi_9|=B_9=21147`, `N^8 1 !=0`, and `N^9 1=0`.

## 5. Forced-spoke operators and exact all-n polynomialization

An unordered edge pair `e,f` touches at most two third-part vertices. Let `k in {0,1,2}` be the number of such distinguished vertices and expose them before the remaining unmarked third-part vertices.

For each marking condition

\[
C\in\{\varnothing,e,f,ef\},
\]

construct an exact row vector `v_C` as follows.

1. Enumerate every acyclic subset of the fixed core `K_{a,b}` satisfying the required marked core edges and record its terminal partition.
2. For each distinguished third-part vertex, apply the exact fresh-vertex transition in which the spokes required by `C` are forced and every other legal spoke is summed over.

The forced transition is still exactly described by Lemma 4.1. If two forced terminals already lie in one current block, that row is zero because the required spokes force a cycle.

Put

\[
x=n-k.
\]

The remaining `x` third-part vertices are unmarked, hence

\[
Z_C(n)=v_C M^x\mathbf 1.
\]

Because `M=10I+N` and `N^9=0`, the binomial theorem gives the **exact identity**

\[
Z_C(n)=10^x P_C(x),
\]

where

\[
\boxed{
P_C(x)=\sum_{j=0}^{8}\binom{x}{j}10^{-j}v_CN^j\mathbf1.
}
\]

Thus each marked count is `10^x` times a rational polynomial of degree at most eight. Consequently

\[
\boxed{
\Delta(e,f)=10^{2x}R_{e,f}(x),
\qquad
R_{e,f}(x)=P_e(x)P_f(x)-P_0(x)P_{ef}(x),
}
\]

with `deg R<=16`.

This formula is exact for the full physical parameter range, not an interpolation from sampled values.

## 6. Exhaustive edge-pair symmetry reduction

Two labelled third-part vertices suffice to represent every possible edge-pair geometry. Quotient unordered pairs by permutations inside the fixed parts and by swapping the two representative third-part vertices. For equal fixed parts one would also allow the part swap, though no new boundary family here has `a=b`.

The exact orbit counts are

\[
\begin{array}{c|c}
\text{family}&\text{edge-pair orbits}\\ \hline
K_{1,8,n}&10\\
K_{2,7,n}&15\\
K_{3,6,n}&15\\
K_{4,5,n}&15
\end{array}
\]

for a total of

\[
\boxed{55}
\]

orbit Rayleigh polynomials.

For every orbit the exact checker expands `R(x)` in the ordinary monomial basis and obtains **no negative rational coefficient**.

If the pair touches `k=0` third-part vertices, then its physical domain has `x=n>=1`; the checker verifies `R(1)>0`. If `k=1` or `2`, the pair can exist only when `n>=k`, so `x=n-k>=0`; the checker verifies `R(0)>0`. Since every coefficient is nonnegative,

\[
R(x)>0
\]

throughout the entire physical integer domain.

The only reported zero minimum coefficient is the constant coefficient of one `K_{1,8,n}` core-core orbit; this is harmless because that orbit has `k=0` and therefore `x>=1`. Its first physical value is

\[
R(1)=\frac{531441}{25}>0.
\]

The minimum first-physical normalized values by family are

\[
\begin{array}{c|c}
K_{1,8,n}&531441/25\\
K_{2,7,n}&102694912/25\\
K_{3,6,n}&82992625\\
K_{4,5,n}&8657183808/25.
\end{array}
\]

Hence every distinct edge pair in all four families has strictly positive Rayleigh difference for every `n>=1`.

## 7. Corollary for the full new tripartite boundary

Sort the part sizes of a complete tripartite graph as `r<=s<=t`. If `r+s=9`, then

\[
(r,s)\in\{(1,8),(2,7),(3,6),(4,5)\},
\]

so the theorem above applies with `n=t`. The previous PROB10-07 reports cover every boundary `r+s<=8`. Therefore

\[
\boxed{
\Delta_{K_{r,s,t}}(e,f)>0
\quad\text{for all distinct present edges }e,f
\quad\text{whenever }r+s\le9.
}
\]

This is not contained in Erickson's series-parallel theorem: these families include many graphs containing `K_{3,3}` and hence non-series-parallel graphs.

## 8. Independent small physical regression

As a separate implementation-level regression, the checker directly enumerates every edge subset of

\[
K_{1,8,1}.
\]

It finds

\[
|E|=17,\qquad Z=30618,
\]

and checks all

\[
\binom{17}{2}=136
\]

actual edge pairs. Every Rayleigh difference is positive, with

\[
\boxed{\min_{e\ne f}\Delta(e,f)=2125764.}
\]

This brute-force check is not the reason the all-`n` theorem holds; the all-parameter statement follows from the 55 exact polynomial certificates above.

## 9. Exact checker, re-execution, hashes, and readback

Idea note, written before code:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_idea.md`

- creation/readback commit: `6554310e57ed03ece23817d70a3d4150b7b3521f`
- Git blob: `6bb7926ecba32817fe369f9bfa51dd7d68b9de30`

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_checker.py`

- final exact-content/readback commit: `cf890810071a8b2c7c9e949a971dfd3455387979`
- Git blob: `7d53d9eab0b0f13e4eb96c7b225c5c4858fa1ef2`
- local Git object hash after execution: `7d53d9eab0b0f13e4eb96c7b225c5c4858fa1ef2`
- local SHA-256: `9c581a437327d965819321e2ec52d42ffc4893c308a6596cb6db8c9fcfc7c193`

Executed output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2.out`

- creation/readback commit: `36bfee32e569abba3d64f0e7e899a4d6115e1f0d`
- Git blob: `53120e16c93c229eb5da35335d119ea0856534a5`
- local Git object hash: `53120e16c93c229eb5da35335d119ea0856534a5`
- local SHA-256: `c3ac6ff85592721cae5920dc0dbd6c85f923f7525d3ee43fb41ba0cc75271d66`

The final checker was re-executed after persistence. The fresh output is byte-for-byte identical to the archived output and terminates

`PROB10_07_TRIPARTITE_SUM9_EXACT_PASS`.

This is a self-check, not an independent audit.

Forest-owner handoff:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_forest-owner-handoff.md`

- creation commit: `92f5ad91c9faa5bb8aa018d02a531e0ca0fd431a`

## 10. Current source/literature comparison

A fresh bounded public search was run during this iteration.

- Grimmett–Winkler, `arXiv:math/0302185` / RSA 24 (2004), is the exact all-forests arbitrary-graph source and reports numerical verification through eight vertices and the sparse nine-vertex sector.
- Erickson, `arXiv:1008.3660`, proves a stronger positive-weight Rayleigh/SOS statement for series-parallel graphs.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), treat specified uniform spanning-subgraph ensembles of `K_n`, including forests with exactly a fixed number `k` of components for sufficiently large `n`; this is not the arbitrary-graph measure mixing all component counts.
- Bado's wheel result proves strict negative edge correlation for another infinite 3-connected non-series-parallel family under the uniform-all-forests law.
- Tang–Zhang, `arXiv:2609.11578` (10 September 2026), still describes pairwise negative correlation for the random-cluster model below one as open on general finite graphs; its `Q=0` endpoint is bond percolation conditioned to be connected, not the all-forests law here.

A bounded search for combinations of uniform forests / negative correlation / complete tripartite graphs did not surface this `r+s<=9` theorem. That is negative evidence only. **External novelty and priority remain UNVERIFIED.** No claim of worldwide novelty is made.

The owner's random-cluster parameter-nonmonotonicity paper is not used as a resolution of this source problem.

## 11. What moved, what did not, and the full-scope gap

**Source-level status:** `OPEN -> OPEN`.

**Complete all-simple-graph order metric:** `9 -> 9`.

**Structural-family metric:**

\[
\boxed{r+s\le8\quad\longrightarrow\quad r+s\le9}
\]

for sorted complete-tripartite part sizes `r<=s<=t`.

**Auxiliary mechanism gain:** exact Bell-9 transfer, `B_9=21147`, 55 exhaustive edge-pair orbit polynomials, all coefficientwise nonnegative with strict first-physical values; direct all-pairs `K_{1,8,1}` regression.

**Counterexample metric:** no source-valid negative Rayleigh difference found.

**Independent validation:** `0/2`; the exact checker is a self-check only.

The remaining source gap is still enormous: an arbitrary vertex-minimal counterexample may be taken 3-connected, and no argument here controls an arbitrary 3-connected graph. This theorem only controls complete tripartite graphs with a bounded sum of the two smaller parts. It neither completes the ten-vertex 3-connected census nor resolves the generic three-terminal mixed-response obstruction recorded by P14/HARD10-01.

## 12. Next mathematically distinct route

The useful next step should not merely replace `9` by `10` in the Bell-state brute force. The highest-leverage route exposed here is to prove simultaneous strong lumpability of the unmarked and all forced-spoke operators under `S_a x S_b`, or to identify a smaller invariant algebra for the four marked counting vectors. Such a theorem could convert the observed fixed-width sequence into a proof uniform in the terminal width, potentially establishing all complete tripartite graphs rather than one more boundary.

A second genuinely different route is to revisit deletion/contraction but derive an **unrooted** complete-multipartite forest partition formula compatible with edge contractions and parallel classes. Either route would turn the present certificates into structural mathematics rather than continued Bell-number growth.

```yaml
ledger_delta:
  track: PROB10-07
  parent_source: "Grimmett-Winkler uniform-all-forests pairwise edge negative correlation"
  parent_status_before: OPEN
  parent_status_after: OPEN
  arbitrary_graph_order_metric_before: 9
  arbitrary_graph_order_metric_after: 9
  structural_metric: "max proved sum r+s for sorted complete-tripartite K_{r,s,t}"
  structural_before: 8
  structural_after: 9
  new_families:
    - "K_{1,8,n}, all n>=1"
    - "K_{2,7,n}, all n>=1"
    - "K_{3,6,n}, all n>=1"
    - "K_{4,5,n}, all n>=1"
  pair_strength: "strict for every distinct present edge pair"
  exact_orbits: 55
  exact_checker_status: PASS
  direct_regression: "K_{1,8,1}: 30618 forests; 136 pairs; minimum Delta=2125764"
  counterexample: NONE
  novelty: UNVERIFIED
  independent_audits: "0/2"
  status: PARTIAL
```

No scheduler, cadence, enabled state, email, Drive, public posting, workflow, permission, shared-root ledger, or peer-owned claim was modified.
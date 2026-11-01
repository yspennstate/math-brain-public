Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — GPT-6 maximum was requested, but this runtime did not authenticate GPT-6 maximum.

# PROB10-07 — complete-tripartite width-eight Rayleigh certificate

Status: **PARTIAL** on the parent Grimmett–Winkler conjecture. The universal arbitrary-finite-graph statement remains OPEN. This run proves a new restricted structural family and does not alter P14/HARD10-01 graph-order ownership.

## 1. Source target and before/after metrics

For a finite graph `G=(V,E)`, let

\[
Z_G=\#\{F\subseteq E:F\text{ is acyclic}\},
\]

and for distinct edges `e,f`, let `Z_e,Z_f,Z_{ef}` count forests containing the indicated marked edges. The source-exact uniform-all-forests pairwise negative-correlation inequality is

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F)
\quad\Longleftrightarrow\quad
\Delta_G(e,f):=Z_eZ_f-Z_GZ_{ef}\ge0.
\]

This is **not** the uniform-spanning-tree model, a fixed-component ensemble, or a random minimum-spanning-tree model.

**Parent source status:** `OPEN -> OPEN`.

**Complete arbitrary-simple-graph order metric:** `9 -> 9` (unchanged; this run does not enumerate graph orders).

**PROB10-07 structural metric before:** every complete tripartite graph whose two smallest part sizes sum to at most `7`.

**PROB10-07 structural metric after:**

\[
\boxed{\text{every complete tripartite }K_{a,b,c}\text{ whose two smallest part sizes sum to at most }8.}
\]

The new boundary cases proved here are

\[
\boxed{K_{1,7,n},\ K_{2,6,n},\ K_{3,5,n},\ K_{4,4,n}\qquad(n\ge1),}
\]

and every distinct physical edge pair is in fact **strictly** negatively correlated.

The gain is infinite-parameter structural coverage. It is not a finite-order extrapolation and it is not a universal resolution.

## 2. Required continuity, claims, and nonoverlap

The run read the owner contract `operations/PROB10_2026-09-20.md`, current `POSTED.md`, the complete P14 mandatory handoff

`proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`,

the complete HARD10-01 forest handoff

`proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`,

the own predecessor

`runs/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c.md`,

and the current neighboring forest reports, including

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T07-18-55Z__triangle-right-p5-sign-theorem.md`

and

`proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T06-38-00Z__p5-corner-sign-report.md`.

P14/HARD10-01 retain the arbitrary-graph order-nine census and the 3-connected/minimal-counterexample reduction history. NM13-04/NM13-08 currently study three-terminal join/layer families with internal right components such as `P5`. This run does **not** repeat those claims: it treats an eight-terminal `K_{a,b}` core plus an independent repeated third part.

The earlier R13 state remains preserved at

`runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.

No peer-owned report or claim file was edited.

## 3. Three materially different attacks considered before coding

The mathematical idea was written first in

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0742Z_tripartite-sum8-b84d_idea.md`

before the exact checker was committed.

### Route A — deletion/contraction closed form

The identities `Z_e(G)=Z(G/e)` and `Z_{ef}(G)=Z(G/e/f)` suggest reducing every Rayleigh difference to four unmarked all-forest partition functions. For `K_{a,b,n}`, however, contracting a marked edge creates identified vertices and parallel edge classes. The convenient matrix-forest determinant counts rooted forests, whereas the source measure weights every unrooted forest equally. I did not recover a source-matching closed form for these contracted multigraphs, so this route was not promoted into a claim.

### Route B — quotient the Bell lattice by `S_a x S_b`

The 4140 partitions of eight terminals have a large `S_a x S_b` symmetry. Quotienting them would be the natural way to push the method to much larger fixed widths. The obstruction is marked-edge bookkeeping: the proof needs not only the unmarked repeated-vertex transfer to lump, but every forced-spoke operator used separately for `Z,Z_e,Z_f,Z_{ef}`. I did not assume that simultaneous strong lumpability without a proof.

### Route C — full Bell transfer with cached legality and forced-spoke operators

This route succeeds. It keeps all 4140 states, but precomputes every legal star attachment once and reuses the same exact marked operators across all four width-eight families. This isolates the actual mathematics — a nilpotent transfer and finitely many orbit Rayleigh polynomials — without graph-order enumeration.

## 4. Exact transfer lemma

Fix one of `(a,b)=(1,7),(2,6),(3,5),(4,4)` and write

\[
T=A\sqcup B,\qquad |A|=a,\quad |B|=b,\quad |T|=8.
\]

The fixed core is `K_{a,b}` on `T`; each vertex of the third part is adjacent to all eight terminals and to no other third-part vertex.

A partial forest induces a set partition `pi` of `T`: two terminals lie in one block precisely when they are connected in the partial forest already exposed. Let a fresh third-part vertex `v` choose a spoke set `S subseteq T`.

**Lemma 4.1.** Adding the spokes `vS` preserves acyclicity if and only if `S` meets every block of `pi` in at most one terminal. When this holds, the new terminal partition is obtained by merging exactly the blocks met by `S`.

**Proof.** If two vertices of `S` are already in the same component, the old path between them together with the two spokes through `v` forms a cycle. Conversely, if all selected terminals lie in distinct old components, adding a new vertex and one edge into each of those components joins them by a star and cannot create a cycle. The connectivity update is therefore exactly the stated block merge. `QED`.

Let `M` be the unmarked transition matrix on the Bell set `Pi_8`. For every state, exactly the empty spoke set and the eight singleton spoke sets leave the partition unchanged. Thus

\[
M=9I+N.
\]

Every transition represented by `N` strictly lowers the number of terminal blocks. Starting from at most eight blocks, eight strict coarsenings are impossible, hence

\[
\boxed{N^8=0.}
\]

The executable verifies both `B_8=4140` and the sharp nilpotence check `N^7 != 0`, `N^8=0`.

## 5. Marked-edge reduction and polynomial formula

An unordered pair of graph edges touches at most two third-part vertices. Choose a representative with `k in {0,1,2}` such distinguished vertices and expose those vertices first. For each marking condition

\[
C\in\{\varnothing,e,f,ef\},
\]

let `v_C` be the exact row vector obtained by:

1. enumerating every acyclic subset of the core `K_{a,b}` that contains the required marked core edges, and recording its terminal partition;
2. applying to each distinguished third-part vertex the exact forced-spoke transition that requires precisely the marked spokes incident with that vertex while summing over all other spokes compatible with acyclicity.

If `x=n-k` unmarked third-part vertices remain, Lemma 4.1 gives

\[
Z_C(n)=v_C M^x {\bf 1}.
\]

Since `M=9I+N` and `N^8=0`, the binomial theorem gives the exact identity

\[
Z_C(n)
=9^x P_C(x),
\]

where

\[
P_C(x)=\sum_{j=0}^{7}\binom{x}{j}9^{-j}v_CN^j{\bf1}.
\]

Therefore

\[
\boxed{
\Delta(e,f)=9^{2x}R_{e,f}(x),
\qquad
R_{e,f}(x)=P_e(x)P_f(x)-P_0(x)P_{ef}(x).
}
\]

Each `R_{e,f}` is a rational polynomial of degree at most 14. This is a theorem for the entire parameter range once the finitely many edge-pair orbit polynomials have been certified.

## 6. Exhaustive symmetry reduction at width eight

Every edge pair in `K_{a,b,n}` involves at most two vertices of the third part, so a witness with two such vertices contains every possible local pair type. Quotient unordered edge pairs by `S_a x S_b x S_2`; when `a=b`, also allow interchange of the two equal fixed parts. Omitting any accidental extra symmetry when `n=a` or `n=b` only over-refines the list and is harmless.

The exact orbit counts are

\[
\begin{array}{c|c}
\text{family}&\text{edge-pair orbits}\\ \hline
K_{1,7,n}&10\\
K_{2,6,n}&15\\
K_{3,5,n}&15\\
K_{4,4,n}&9
\end{array}
\]

for a total of

\[
\boxed{49}
\]

orbit polynomials.

For **every one of the 49 orbits**, the executed exact-arithmetic checker expands `R(x)` in the ordinary monomial basis and obtains only nonnegative rational coefficients. No floating-point sign decision is made.

For an orbit touching `k` distinguished third-part vertices, its physical parameter range is

\[
x=n-k.
\]

If `k=0`, the theorem assumes `n>=1`, hence `x>=1`, and the checker verifies `R(1)>0`. If `k=1` or `k=2`, the pair exists only when `n>=k`, hence `x>=0`, and the checker verifies `R(0)>0`. Nonnegative monomial coefficients then imply

\[
R(x)>0
\]

throughout the complete physical integer range for that orbit.

Consequently every physical pair satisfies

\[
\boxed{\Delta_{K_{a,b,n}}(e,f)>0}
\]

for all four `(a,b)` above and all `n>=1`.

This proves the new width-eight theorem.

## 7. Corollary for all complete tripartite graphs up to the new boundary

Sort the three part sizes as `r<=s<=t`. If `r+s=8`, then `(r,s)` is one of

\[
(1,7),(2,6),(3,5),(4,4),
\]

and the theorem applies with `n=t`. The preceding PROB10-07 results cover `r+s<=7` (with the smallest series-parallel boundary already known from Erickson). Hence

\[
\boxed{
\Delta_{K_{r,s,t}}(e,f)>0
\quad\text{for every distinct }e,f
\quad\text{whenever }r+s\le8.
}
\]

The class is genuinely beyond the known series-parallel theorem: for example `K_{3,5,n}` and `K_{4,4,n}` contain a `K_{3,3}` subgraph.

## 8. Independent small-instance regression

To cross-check the transfer implementation by a separate direct subset enumeration, the checker enumerates every one of the `2^15` edge subsets of

\[
K_{1,7,1}.
\]

It obtains exactly

\[
Z=9477
\]

forests and tests all

\[
\binom{15}{2}=105
\]

actual edge pairs. Every Rayleigh difference is positive, with

\[
\min_{e\ne f}\Delta(e,f)=236196.
\]

This brute force is only a regression check; the all-`n` theorem comes from the 49 exact polynomial certificates.

## 9. Executed certificate and readback

Idea artifact, written before code:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0742Z_tripartite-sum8-b84d_idea.md`

- creation/readback commit: `75412160d7c6b7f131b9d92a7e6ee7f542025a83`
- Git blob: `d606277549b98ac0fab5488e85ab694a6887220b`

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0742Z_tripartite-sum8-b84d_checker.py`

- creation/readback commit: `d0bf022ef2b24625e1f70384e9526803987beac1`
- Git blob: `a032008eed725ec1de29824f0eb3bc8dc3a6637e`
- local SHA-256: `ca5f1d80dd09acf6fa552af2643097e028e3d93ce0ff8f692e498e20fa25c4ed`

Executed output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0742Z_tripartite-sum8-b84d.out`

- creation/readback commit: `b800cf1c906fc004c44199414449108334214c56`
- Git blob: `f12d4ba4a386390fe1c0fea87a16663e0a20bd2c`
- local SHA-256: `a9a02e7f9bdf7852a099f42f36f573eabca30cc958b1f9beaa36ffdd1eedbc23`

The local Git-object hashes exactly equal the read-back GitHub blob hashes for both checker and output. The archived execution terminates

`PROB10_07_TRIPARTITE_SUM8_EXACT_PASS`

and records `total_edge_pair_orbits=49`, `global_min_physical_endpoint=2916`, plus the direct `K_{1,7,1}` regression.

This is a **self-check**, not an independent audit.

## 10. Source/literature scope check

The source distinctions remain unchanged.

- Grimmett–Winkler, `arXiv:math/0302185`, ask the uniform measure on **all forests** of an arbitrary finite graph.
- Erickson, `arXiv:1008.3660`, proves a stronger positive-weight Rayleigh statement for the **series-parallel** class.
- Tang–Zhang, `arXiv:2603.10738` (11 March 2026), treat specified spanning-subgraph ensembles of `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; that is not this arbitrary-graph all-component-count measure.
- The 2026 wheel theorem gives another restricted 3-connected non-series-parallel family, not universal closure.
- Current public searches for combinations of `uniform forests`, `negative correlation`, and `complete tripartite K_{a,b,c}` did not surface the width-eight theorem above. This is bounded negative evidence only; **external novelty/priority remains UNVERIFIED**.

The owner's random-cluster parameter-nonmonotonicity paper is not used as a resolution of this source question.

## 11. What moved, what did not, and remaining gap

**Moved:** complete-tripartite parameter range

\[
\boxed{r+s\le7\quad\longrightarrow\quad r+s\le8}
\]

for sorted part sizes `r<=s<=t`.

**Did not move:** the largest completely covered arbitrary-graph order remains `9`; no source-valid counterexample was found; no universal structural reduction beyond the inherited P14/HARD10-01 reductions was proved.

The remaining full-scope gap is still arbitrary 3-connected non-series-parallel graphs outside the certified structural families. The present transfer method scales with the Bell number `B_m`; a principled next mathematical step is therefore not merely `m=9` brute force, but to prove simultaneous lumpability of the unmarked and forced-spoke operators under `S_a x S_b`, or to derive a deletion-contraction identity that exposes a sign-preserving response object.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  task: PROB10-07
  source_status_before: OPEN
  source_status_after: OPEN
  label: PARTIAL
  metric_name: complete_tripartite_sum_of_two_smallest_parts
  before: 7
  after: 8
  new_families:
    - K_{1,7,n}, n>=1
    - K_{2,6,n}, n>=1
    - K_{3,5,n}, n>=1
    - K_{4,4,n}, n>=1
  inequality: strict for every distinct physical edge pair
  arbitrary_graph_complete_order_before: 9
  arbitrary_graph_complete_order_after: 9
  finite_orbit_certificates: 49
  counterexample_found: false
  exact_checker: PASS
  direct_regression: K_{1,7,1}; 9477 forests; 105 pairs; min_delta=236196
  independent_audits: 0
  novelty: UNVERIFIED
  scheduler_changed: false
  email_or_drive: false
  public_posting: false
```

No scheduler, cadence, enabled state, email, Drive, public-posting, workflow, permission, or peer-owned claim state was changed.
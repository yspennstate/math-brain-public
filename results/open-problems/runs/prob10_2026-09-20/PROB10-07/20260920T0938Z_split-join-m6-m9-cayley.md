Model actually running: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**. GPT-6 maximum was requested, but no authenticated writable model/effort selector is exposed, so this report does not claim GPT-6/maximum.

# PROB10-07 — complete split graphs through clique width nine

Status: **PARTIAL** on the parent Grimmett-Winkler conjecture. The arbitrary-finite-graph uniform-all-forests statement remains OPEN. This run proves new restricted infinite structural families and does not alter P14/HARD10-01 graph-order ownership.

## 1. Exact source target and before/after metrics

For a finite graph `G=(V,E)`, let

`Z_G = #{F subseteq E : F is acyclic}`,

and for distinct present edges `e,f`, let `Z_e,Z_f,Z_ef` count forests containing the marked edges. Under the uniform measure on **all forests**,

`P(e,f in F) <= P(e in F)P(f in F)`

is equivalent to

`Delta_G(e,f) := Z_e Z_f - Z_G Z_ef >= 0`.

This is not a spanning-tree law, a minimum-spanning-tree law, or a fixed-component forest ensemble.

**Parent source status:** `OPEN -> OPEN`.

**Complete arbitrary-simple-graph order metric:** `9 -> 9`.

**Current split-family structural metric before this run:** repository follow-ups already prove the unit theorem for `K_3 join I_n`, `K_4 join I_n`, and a stronger one-port-field theorem implying the unit theorem for `K_5 join I_n`.

**Structural metric after this run:**

> For every `m in {3,4,5,6,7,8,9}` and every `n>=1`, the complete split graph `K_m join I_n` satisfies strict pairwise negative edge correlation under the uniform measure on all forests.

The genuinely new widths in this run are

`m = 6,7,8,9`.

No counterexample to the original source model was found.

## 2. Continuity, ownership, and consumed evidence

Before committing to scope I read the current owner contract and exclusion state, plus the complete newest owner handoffs:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- P14: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- HARD10-01: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- own predecessor: `runs/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2.md`;
- NM13-04 split-3 theorem: `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T00-20-38Z__split3-sign-theorem.md`;
- NM13-04 split-4 theorem: `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T01-18-30Z__split4-sign-theorem.md`;
- NM13-04 split-5 one-port-field theorem: `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T02-18-30Z__split5-portfield-sign-theorem.md`;
- current NM13 forest searches through the later `P5/P6` triangle-right reports.

The canonical ownership picture remains unchanged. P14/HARD10-01 own the complete order-nine census and the 3-connected/minimal-counterexample reduction. NM13-04 owns its split-3/split-4/split-5 claims, including the stronger split-5 port-field statement. This run does not repeat or seize those claims. Its precise fresh scope is unit-weight `K_m join I_n` for `m=6,7,8,9`.

The displaced R13 work remains preserved at

`runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.

The non-mutating forest-owner handoff for this run is

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley_forest-owner-handoff.md`.

## 3. Three materially different approaches considered

The mathematical idea was recorded before checker persistence in

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley_idea.md`.

### Route A — extend NM13's one-port-field theorem

This would prove a stronger weighted statement for split widths `m>=6`. The difficulty is not the unit transfer itself but the enlarged stabilizer-orbit list and the sign of the resulting field quadratics; split-5 already has three non-coefficientwise cases requiring discriminants. I did not assume that mechanism scales unchanged.

### Route B — quotient the Bell lattice and aim for all `m`

A symmetry quotient under `S_m`, refined by the at most four clique vertices touched by a marked pair, could plausibly yield an all-clique-width theorem. The missing rigorous ingredient is simultaneous strong lumpability for the unmarked operator and every forced-spoke operator. That is a promising next method but is not used without proof.

### Route C — exact Cayley core vectors plus the full Bell transfer

This route succeeds for `m=6,7,8,9`. The new ingredient relative to brute clique-core enumeration is an exact formula for every marked core vector, avoiding `2^(m choose 2)` enumeration and making widths 8 and 9 accessible in a bounded exact run.

## 4. Cayley marked-core lemma

Let `C=[m]` be the clique terminals and let `pi` be a set partition of `C`. Let `R` be a fixed acyclic set of required clique edges. If any edge of `R` joins two different blocks of `pi`, no forest with component partition `pi` can contain `R`.

Otherwise the count factors over blocks. Fix one block `B`, `|B|=q`, and let `R_B` have connected-component sizes `s_1,...,s_c` inside `B`, isolated vertices included. Then the number of spanning trees of `K_B` containing every edge of `R_B` is

`q^(c-2) prod_i s_i`.

### Proof

Contract every connected component of `R_B`. Any spanning tree extending `R_B` induces a tree on the `c` contracted components. An edge between contracted components `i,j` has `s_i s_j` choices of original endpoints. Thus extensions are weighted trees on `c` vertices with edge weight `s_i s_j`. The weighted Cayley identity gives

`(sum_i s_i)^(c-2) prod_i s_i = q^(c-2) prod_i s_i`.

Multiplying over the blocks of `pi` proves the marked-core formula. QED.

The checker independently regresses this formula at `m=6` by enumerating all `2^15` clique-edge subsets for all six required-edge sets used by the seven pair orbits; every terminal-partition vector agrees exactly, and the total number of clique forests is `2932`.

## 5. Fresh independent-side vertex transfer

Process the `n` independent-side vertices one at a time. A partial forest induces a partition `pi` of the clique terminals by connectivity.

If a new independent vertex is joined to a spoke set `S subseteq C`, the extension is acyclic iff `S` meets every block of `pi` in at most one terminal. If two selected terminals lie in one old component, their old path plus the two new spokes creates a cycle. Conversely, selecting at most one terminal from each old component joins those components through a new star and cannot create a cycle.

Let `M` be the exact transition matrix on the Bell set `Pi_m`. The empty spoke choice and the `m` singleton spoke choices preserve every state, while every other legal choice strictly coarsens the terminal partition. Therefore

`M = (m+1) I + N`,

with

`N^m = 0`.

For a required spoke set on a distinguished independent-side vertex, use the corresponding forced-spoke transition: if two required terminals are already in one block the row is zero; otherwise sum exactly over every optional legal spoke choice. This is the same acyclicity lemma with some spokes forced.

## 6. Exact all-`n` polynomialization

A distinct edge pair touches at most two independent-side vertices. Let `k in {0,1,2}` be that number and expose those distinguished vertices first. Put

`x = n-k`.

For each marking condition `C in {0,e,f,ef}`, the Cayley core vector followed by the forced transitions gives an exact row vector `v_C`. The remaining `x` independent-side vertices are unmarked, so

`Z_C(n) = v_C M^x 1`.

Using `M=(m+1)I+N` and `N^m=0`,

`Z_C(n) = (m+1)^x P_C(x)`,

where

`P_C(x) = sum_{j=0}^{m-1} binom(x,j) (m+1)^(-j) v_C N^j 1`.

Therefore every pair orbit has

`Delta(e,f) = (m+1)^(2x) R_{e,f}(x)`,

`R_{e,f}(x)=P_e(x)P_f(x)-P_0(x)P_ef(x)`,

and `deg R <= 2m-2`.

This identity is exact for the full parameter range; it is not interpolation from finitely many values.

## 7. Exhaustive seven-orbit classification

For `m>=4`, the action of `S_m x S_n` on unordered distinct edge pairs has exactly seven geometries:

1. two clique edges sharing a clique vertex;
2. two disjoint clique edges;
3. a clique edge and a spoke incident at a clique endpoint;
4. a clique edge and a spoke whose clique endpoint is outside the clique edge;
5. two spokes incident to the same independent-side vertex;
6. two spokes on different independent-side vertices with the same clique endpoint;
7. two spokes on different independent-side vertices with different clique endpoints.

Thus all four new widths have exactly seven pair orbits, for 28 new all-parameter Rayleigh polynomials.

## 8. Exact sign certificates for widths 6 through 9

The checker expands every `R(x)` in the ordinary monomial basis using exact integers and `Fraction` arithmetic. Every coefficient in every one of the 28 new orbit polynomials is nonnegative. The first physical value is strictly positive: for core-core orbits `k=0`, so `x=n>=1`; for marked-independent orbits `x>=0`.

The complete primitive coefficient vectors are archived in the executed output. Summary:

| `m` | Bell states | forests of `K_m` | orbit count | smallest primitive coefficient among the seven certificates | smallest first-physical normalized Rayleigh value |
|---:|---:|---:|---:|---:|---:|
| 6 | 203 | 2932 | 7 | 2592 | `187434/7` |
| 7 | 877 | 36961 | 7 | 117649 | `24804441/8` |
| 8 | 4140 | 561948 | 7 | 33554432 | `42677731850/81` |
| 9 | 21147 | 10026505 | 7 | 3486784401 | `624203455452/5` |

Hence, for each `m=6,7,8,9`, every distinct edge pair satisfies

`Delta_{K_m join I_n}(e,f) > 0`

for every integer `n>=1`.

This proves the announced new structural theorem. QED.

## 9. Executed checker and regression

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley_checker.py`

Local SHA-256 of the executed checker:

`72bd1db27656174c531f1307770e993b99113bf2d243df09e7a6cef84c7adc68`.

Executed output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0938Z_split-join-m6-m9-cayley.out`

Local SHA-256 of the archived output:

`4babaee5551f202fabb2acd2304bb19074e27b5fb7448f14bc726c97db7bcd5f`.

The output records:

- exact Cayley-core/formula versus full clique-subset cross-check at `m=6`: PASS;
- all seven all-`n` orbit certificates at each `m=6,7,8,9`: PASS;
- a separate direct all-edge-subset regression on `K_3 join I_2`: `9` edges, `198` forests, all `36` edge pairs positive, minimum Rayleigh numerator `124`;
- terminal marker `PROB10_07_SPLIT_JOIN_M6_M9_EXACT_PASS`.

No floating-point sign decision is used.

## 10. Source-level before/after, auxiliary gains, and remaining gap

**Source-level status:** `OPEN -> OPEN`.

**Complete arbitrary-graph order:** `9 -> 9`.

**New full-parameter graph classes:** four infinite families, `K_m join I_n` for `m=6,7,8,9`, all `n>=1`.

**Combined current split frontier:** unit p-NC now holds in repository continuity for clique widths `m<=9`; widths `3,4,5` are prior NM13 work and widths `6,7,8,9` are this run.

**Auxiliary gain:** the Cayley marked-core formula replaces exponential clique-core subset enumeration and should be reusable in a symmetry-quotient attack.

**Remaining full-scope gap:** arbitrary finite graphs remain completely unresolved beyond the established structural reductions. Even within complete split graphs, this run does not prove all clique widths `m>=10`, nor the stronger all-positive-weight or one-port-field statements for `m>=6`. The immediate computational obstruction at `m=10` is the full Bell state space `B_10=115975`; the mathematically preferable next move is therefore the marked-symmetry quotient from Route B rather than merely allocating more brute state space.

A bounded public literature search in this run recovered Grimmett-Winkler, Erickson, Tang-Zhang, and Bado as the relevant established regimes and did not surface a prior theorem specifically covering these split widths. That is only bounded negative evidence; **external novelty/priority remains UNVERIFIED**.

No independent audit is claimed. This is a self-contained proof plus exact self-checker, so the parent remains OPEN/PARTIAL and no source closure is declared.

## 11. Control-state preservation

No scheduler, cadence, enabled state, email, Drive, public posting, workflow, permission, or peer-owned claim was changed. The current PROB10-07 recurring assignment remains active under its existing owner/platform state.
# PROB10-07 — two commuting nilpotents and strict p-NC for matched bicliques of terminal width 4 and 5

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending independent review.** The arbitrary-finite-graph source problem remains **OPEN**.

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Runtime request/status: GPT-6 maximum was requested. The authenticated scheduler/tool surface available in this run exposed no writable model/effort selector and no authenticated applied-effort telemetry. The surrounding runtime identifies GPT-5.6 Sol, but reasoning effort is **UNVERIFIED**; no GPT-6-maximum claim is made.

## 1. Contract, ownership, and consumed state

This iteration uses the exact source model: choose uniformly from **all acyclic spanning edge subsets** of a finite graph. It does not substitute uniform spanning trees, minimum spanning trees, connected subgraphs, or a fixed-component forest ensemble.

Before choosing scope I read the current PROB10 contract and root posting registry, preserved R13's refocus handoff, and read the forest-owner histories. In particular:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- P14 forest handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- newest P14 state `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md` and current successor claim `operations/claims/G0007.md`, which explicitly freeze the forest predecessor at complete-order metric 9 rather than reopening it;
- HARD10-01's final forest report `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md` and current successor claim `operations/claims/I0028.md`, which likewise records the forest predecessor as handed off with metric 9;
- the retired duplicate R02 forest claim/history `operations/claims/P0001.md` and `runs/R02/20260918T0102Z_61f4a9c7.md`;
- preceding PROB10-07 correction `runs/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-sum9-repair.md`;
- current neighboring T07 work, especially NM13-08's three-terminal matching theorem `proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T03-38-00Z__three-terminal-right-matching-sign-report.md`, and the newer NM13-04/NM13-08 P6 reports at `2026-09-20T08-19-21Z` and `2026-09-20T07-40-30Z`.

Thus this run does **not** seize P14/HARD10's graph-order claim and does not repeat their enumeration. It also does not repeat NM13-08's `K_{3,2k+r}+M_k` theorem: the new theorem has four or five fixed terminals, and the old one-generator terminal algebra fails there.

The mathematical idea was committed **before code** at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1248Z_two-nilpotent-matched-biclique_idea.md`

(create/readback commit `f312b0b9b75218b25fe30793cc5e2c5b645a6c49`, blob `2844c42727e166cf6fa45dc66a48118ab2f3cf82`).

## 2. Source-level before/after and separate structural metric

Write

`Delta_G(e,f)=Z_e Z_f-Z Z_{ef}`,

where `Z` is the number of all forests of `G`, `Z_e` the number containing `e`, and `Z_{ef}` the number containing both distinct edges. The desired source inequality is `Delta_G(e,f)>=0`.

**Parent source status:** `OPEN -> OPEN`.

**Largest completely certified arbitrary-simple-graph order in repository continuity:** `9 -> 9`.

No finite-order census credit is claimed here.

A useful restricted-family metric does move. NM13-08 had already certified the matching-on-the-right two-parameter family at terminal width `m=3`. This run proves the full parameter range at **new widths `m=4` and `m=5`**. Combining the neighboring result with this run, the matched-biclique width frontier is `3 -> 5`; only widths 4 and 5 are new claims of this report.

## 3. Three approaches compared before implementation

### Route A — extend the one-generator `m=3` algebra

Let `S_m` be the transfer of one ordinary right vertex and `P_m` the transfer of a matched pair of right vertices plus their internal matching edge. NM13-08 found at `m=3` that `P_3` is a polynomial in `N_3=S_3-4I`.

This route is **exactly obstructed at width 4**. The checker solves the rational linear-span problem and proves

`P_m notin span_Q{I,N_m,...,N_m^{m-1}}`

for both `m=4` and `m=5`. Since `N_m^m=0`, no polynomial in `N_m` can equal `P_m`. Therefore the old one-generator proof mechanism genuinely stops.

### Route B — two commuting nilpotents

Keep the second nilpotent instead of trying to eliminate it. This succeeds and is the main proof below.

### Route C — deletion/contraction in a matching edge

Deleting a right matching edge returns a complete bipartite graph; contracting it gives a fused right vertex with doubled parallel incidence. Expanding a Rayleigh difference in that matching-edge activity leaves an uncontrolled mixed polarization term of the same qualitative type as the P14 environmental-covariance obstruction. No source-level sign closure was obtained from this route, so it was not used as a hidden assumption.

## 4. New graph class and theorem

For `m in {4,5}`, `k>=1`, `r>=0`, define

`G_m(k,r) = K_{m,2k+r}+M_k`,

where `M_k` is a matching on `2k` vertices of the right part and there are no other right-right edges.

### Theorem `PROB10-07-MATCHED-BICLIQUE-M4-M5`

For `m=4` or `m=5`, every `k>=1`, every `r>=0`, and every two distinct present edges `e,f` of `G_m(k,r)`,

`Delta_{G_m(k,r)}(e,f) > 0`.

Hence the uniform probability measure on **all forests** of every `G_m(k,r)` has strict pairwise negative edge correlation.

For `2k+r>=3`, these classes contain a `K_{3,3}` subgraph and are therefore outside the series-parallel regime. The theorem is symbolic in `k,r`; it is not a finite-order graph census.

## 5. Structural transfer proof

Fix the `m` left terminals. A partial forest interacts with future right layers only through the connectivity partition induced on those terminals, so the state space is the Bell partition lattice `Pi_m`: 15 states for `m=4` and 52 for `m=5`.

Let `S=S_m` be the exact transfer for one ordinary right vertex joined to all `m` terminals. Its diagonal is constant:

`S=(m+1)I+N`.

Let `P=P_m` be the exact transfer for two fresh right vertices, each joined to all `m` terminals, with their internal matching edge also present as an available edge. Its diagonal is also constant:

`P=lambda_m I+Q`,  where  `lambda_m=m^2+4m+2`.

The diagonal formula is direct. If the internal edge is absent, the two new vertices independently select either no spoke or one terminal spoke, giving `(m+1)^2` diagonal choices. If the internal edge is present, staying in the same terminal partition permits only the internal edge alone or that edge plus one spoke from one of its two endpoints, giving `1+2m`. Thus `lambda_m=(m+1)^2+1+2m`.

### Lemma 5.1 — commuting nilpotents

`NQ=QN`, and

`Q^i N^j=0 whenever i+j>=m`.

**Proof.** Adding two disjoint fresh layers in either order enumerates the same unions of layer-edge subsets, with the same final terminal partition. Hence `SP=PS`, and subtracting scalar identities gives `NQ=QN`.

After the constant diagonal is removed, every nonzero transition of either `N` or `Q` strictly coarsens the terminal partition. A strictly coarsening chain in `Pi_m` has length at most `m-1`. Therefore every word with at least `m` factors from `{N,Q}` is zero. QED.

The checker independently reconstructs `S,P` from edge subsets and verifies all these identities exactly, including every mixed product of total degree at least `m`.

### Corollary 5.2 — exact bivariate response

Put `mu=m+1` and `lambda=lambda_m`. For all `x,y>=0`,

`P^x S^y = lambda^x mu^y sum_{i+j<m} binom(x,i) binom(y,j) lambda^{-i} mu^{-j} Q^i N^j`.

This is just the two commuting binomial expansions, truncated exactly by Lemma 5.1. It is the mechanism that replaces the failed one-generator representation.

## 6. Marked layers and exhaustive edge-pair types

For a chosen pair `e,f`, expose every right layer touched by the **full pair** in all four counts `Z,Z_e,Z_f,Z_ef`. If a distinguished layer carries no forced edge in one of those four conditions, use its unmarked transfer. This is the same conditioning discipline that repaired the earlier PROB10-07 repeated-vertex omission.

Let `a` be the number of distinguished matched-pair layers and `b` the number of distinguished singleton layers, and set

`x=k-a`, `y=r-b`.

The exact automorphism group leaves fourteen pair templates:

1. two ordinary spokes in one singleton layer, different terminals;
2. ordinary spokes in two singleton layers, same terminal;
3. ordinary spokes in two singleton layers, different terminals;
4. matching edge and spoke in the same matched layer;
5. two spokes from the same matched endpoint, different terminals;
6. spokes from opposite matched endpoints, same terminal;
7. spokes from opposite matched endpoints, different terminals;
8. two matching edges in different layers;
9. matching edge and spoke in different matched layers;
10. matched spokes in different layers, same terminal;
11. matched spokes in different layers, different terminals;
12. matching edge and ordinary spoke;
13. matched spoke and ordinary spoke, same terminal;
14. matched spoke and ordinary spoke, different terminals.

The checker verifies completeness independently on generic `k=2,r=2` instances: all 325 edge pairs at `m=4` and all 496 edge pairs at `m=5` fall into exactly these fourteen templates with no residue.

Every distinguished marked transfer used by the proof is also checked to commute with the unmarked `S` and `P`. Thus for each condition `A in {0,e,f,ef}`,

`Z_A = lambda^x mu^y C_A(x,y)`,

where `C_A` is an exact rational polynomial obtained from Corollary 5.2. Therefore

`Delta(e,f)=lambda^{2x} mu^{2y} R_O(x,y)`,

with

`R_O=C_e C_f-C_0 C_ef`

for the corresponding orbit `O`.

## 7. Exact sign certificate

The checker converts every `R_O` into the ordinary monomial basis in the shifted physical variables `x,y` and performs all sign decisions with exact integers/rationals.

For **all 28 orbit polynomials** (14 at each of `m=4,5`), every present monomial coefficient is strictly positive. At `m=4` the maximum degree is 6; at `m=5` it is 8. The only missing constant term is the same-singleton-layer ordinary-spoke orbit. In that orbit `a=0`, so the physical domain has `x=k>=1`; its first physical values are positive:

- `m=4`: `R(1,0)=25648/289`;
- `m=5`: `R(1,0)=2033664/2209`.

Every other orbit has a strictly positive constant term. Hence every physical `R_O(x,y)` is strictly positive for all allowed integers `k>=1,r>=0`, proving the theorem.

The compact archived output records, for each orbit, its distinguished-layer counts, degree, number of nonzero positive coefficients, primitive scale, first physical value, and SHA-256 digest of the complete primitive coefficient table. The checker itself prints the full coefficient tables on an unfiltered run.

## 8. Executed checker and independent original-model regressions

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1258Z_matched-biclique-m4-m5_checker.py`

- local SHA-256: `d352c0b250f096d1be27ec343ab8fc2f6f5c237299bf2b4fbe5956d02bbe90d3`;
- creation/readback commit: `f30968a63952f8d794e436c8c45dfcc7b731a53b`;
- Git blob, independently matched by local `git hash-object`: `c411a094da38b67014a3e2f78ea503e545ce47cc`.

The compact executed transcript was generated by re-running the checker and filtering only the very long `COEFFS ...` display lines; all coefficient assertions and all other output were still executed:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1258Z_matched-biclique-m4-m5_checker.compact.out`

- local SHA-256: `16eeeb11089df1c8f7ffa8dcf52b5a637de4867c5cfee028ce9b0c7a0167441a`;
- creation/readback commit: `9885211a76cf6097ffaa3af93511d5f13b7f026f`;
- Git blob, independently matched by local `git hash-object`: `ddb922f5fbfdeb82c6a0432b8162ef37935e5a62`.

The transcript ends

`PROB10_07_MATCHED_BICLIQUE_M4_M5_EXACT_PASS`.

A separate branch of the checker directly enumerates edge subsets of the original graphs with union-find, rather than using terminal transfers. It verifies every actual edge pair in:

- `G_4(1,0)`: 9 edges, 270 forests, 36 pairs, minimum `Delta=324`;
- `G_4(1,1)`: 13 edges, 2624 forests, 78 pairs, minimum `Delta=12288`;
- `G_5(1,0)`: 11 edges, 891 forests, 55 pairs, minimum `Delta=2916`.

All pass strictly.

## 9. Literature/source boundary

The source distinctions remain unchanged:

- Grimmett–Winkler, `https://arxiv.org/abs/math/0302185`, is the arbitrary-graph uniform-**all-forests** conjecture and published finite computation;
- Erickson, `https://arxiv.org/abs/1008.3660`, proves the stronger weighted Rayleigh property for series-parallel graphs;
- Tang–Zhang, `https://arxiv.org/abs/2603.10738`, treats specified complete-graph ensembles including forests with a fixed number of components, not this all-component arbitrary-graph law;
- current neighboring literature/repository follow-ups include the wheel theorem and several structured three-terminal transfer families, none of which imply the width-4/5 matched-biclique result above.

A bounded 20 September 2026 search for combinations of `uniform forest negative correlation`, `matched biclique`, complete bipartite plus matching, and `K_4`/`K_5` terminal terminology did not surface this exact theorem. This is only negative search evidence. **External novelty/priority remains UNVERIFIED.**

## 10. Remaining full-scope gap and next structural question

The universal Grimmett–Winkler statement is untouched at source level: arbitrary finite graphs remain open, and no source-valid negative Rayleigh difference was found. The new proof depends heavily on a repeated-layer symmetry and coefficient positivity of finitely many response polynomials.

The next non-duplicative question inside this mechanism is whether the two-nilpotent certificate extends to terminal width `m>=6`, or whether a first negative coefficient/physical Rayleigh value appears. The algebraic decomposition itself extends formally to every fixed `m`; what is not proved is the sign of all marked-orbit polynomials. No `m=6` theorem is claimed here.

## 11. Coordination and mutation boundary

This report is a complementary structural theorem only. It does not alter P14/HARD10-01/R02/NM13 claims, root ledgers, `POSTED.md`, scheduler settings, cadence, enabled state, workflow, permissions, email, Drive, or public posting. A separate non-mutating forest-owner handoff accompanies this report.

**END OF IMMUTABLE REPORT**

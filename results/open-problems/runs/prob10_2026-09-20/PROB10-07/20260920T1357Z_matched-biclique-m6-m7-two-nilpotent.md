# PROB10-07 — strict uniform-forest edge negative correlation for matched bicliques of terminal widths 6 and 7

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending independent review.** The arbitrary-finite-graph source problem remains **OPEN**.

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Runtime request/status: GPT-6 maximum was requested. Authenticated applied model/effort telemetry is **UNVERIFIED**; the surrounding runtime identifies GPT-5.6 Sol, so no GPT-6-maximum claim is made.

## 1. Exact model, contract, ownership, and consumed state

The probability space is exactly the source model: choose uniformly from **all acyclic spanning edge subsets** of a finite graph `G`. The full vertex set is retained. This report does not use a uniform spanning-tree law, a minimum-spanning-tree law, a random-cluster law at another parameter, or a fixed-component forest ensemble.

Before selecting scope, this run read the current PROB10 contract, root posting registry, the current R13 handoff, and the complete newest forest-owner handoffs/claims. In particular:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- P14 forest handoff `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- newest P14 state `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md` and current successor claim `operations/claims/G0007.md`;
- HARD10-01 final forest report `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md` and its successor history;
- preceding PROB10-07 report `runs/prob10_2026-09-20/PROB10-07/20260920T1308Z_matched-biclique-m4-m5-two-nilpotent.md`.

P14 and HARD10-01 retain the complete-order / three-separator history. Both froze the arbitrary-graph complete-size metric at 9 and handed the forest target off. This report does **not** seize either claim and does not repeat any arbitrary-graph graph-order enumeration.

The mathematical idea was persisted **before code** at

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1339Z_matched-biclique-m6_idea.md`

creation/readback commit `544d235a516c7448a135708a132e1498c4e267d8`, blob `9bbd7d35d8513b54709739318bdec359badce23a`.

## 2. Source-level and mechanism metrics

For distinct present edges `e,f`, write

`Delta_G(e,f)=Z_e Z_f-Z Z_{ef}`,

where `Z` is the number of all forests of `G`, `Z_e` is the number containing `e`, and `Z_{ef}` is the number containing both. The desired source inequality is `Delta_G(e,f)>=0`.

**Parent source status:** `OPEN -> OPEN`.

**Largest completely certified arbitrary-simple-graph order in inherited repository continuity:** `9 -> 9`.

No graph-order census credit is claimed here.

The structural-family metric does move. The preceding PROB10-07 theorem covered matched-biclique terminal widths `m=4,5`, while neighboring repository work had width `m=3`. This run proves the complete two-parameter family at the two new widths

`m=6,7`.

Thus the matched-biclique width frontier moves `5 -> 7` within this track, or `3 -> 7` when the neighboring width-3 theorem is included. Only widths 6 and 7 are new claims of this report.

## 3. Three materially different approaches compared before coding

### Route A — exact two-nilpotent terminal response at the next widths

Continue the structural algebra, but do not assume coefficient positivity survives. For one ordinary right vertex use a transfer `S`; for one matched pair of right vertices plus its internal matching edge use `P`. Subtract the scalar diagonals and retain both nilpotent generators. This route succeeds at widths 6 and 7 and is the main proof below.

### Route B — deletion–contraction induction on a right matching edge

Delete or contract one unmarked matching edge `g`, then express the parent Rayleigh difference in the two endpoint environments. This route yields a useful exact identity but does **not** close an induction: an environmental response product appears with the wrong sign and is genuinely positive on a source-valid width-6 example. The exact obstruction is recorded in Section 8.

### Route C — counterexample-first exact arithmetic in the same source-valid family

Before promoting a symbolic certificate, directly enumerate all forest edge subsets and every actual edge pair in small members of the proposed family. A negative exact Rayleigh numerator would have been a counterexample to the original model and would have superseded the proof attempt. No such negative value appeared in the tested instances; the direct checks instead agree with the symbolic theorem.

## 4. New graph class and theorem

For `m in {6,7}`, `k>=1`, `r>=0`, define

`G_m(k,r)=K_{m,2k+r}+M_k`,

where `M_k` is a matching on `2k` vertices of the right part and there are no other right-right edges.

### Theorem `PROB10-07-MATCHED-BICLIQUE-M6-M7`

For `m=6` or `m=7`, every `k>=1`, every `r>=0`, and every two distinct present edges `e,f` of `G_m(k,r)`,

`Delta_{G_m(k,r)}(e,f)>0`.

Hence the uniform probability measure on **all forests** of every `G_m(k,r)` has strict pairwise edge negative correlation.

This is an all-parameter structural theorem, not a finite graph-order census. The family is well outside the established series-parallel class: already `K_{m,2k+r}` contains `K_{3,3}` whenever `2k+r>=3`.

## 5. Terminal-partition transfer algebra

Fix the `m` left vertices as terminals. A processed partial forest interacts with future right layers only through the connectivity partition induced on these terminals. Thus the exact state space is the Bell partition lattice `Pi_m`, with

- `B_6=203` states for `m=6`;
- `B_7=877` states for `m=7`.

Let `S=S_m` be the transfer for one fresh ordinary right vertex joined to all `m` terminals. The diagonal is constant:

`S=(m+1)I+N`.

Indeed, preserving the terminal partition means selecting either no spoke or exactly one spoke, hence `m+1` choices.

Let `P=P_m` be the transfer for two fresh right vertices `u,v`, each joined to all `m` terminals, together with the available internal edge `uv`. Its diagonal is constant:

`P=lambda_m I+Q`,

where

`lambda_m=(m+1)^2+(1+2m)=m^2+4m+2`.

The first term counts configurations with `uv` absent that preserve the terminal partition: each new vertex independently chooses no spoke or one spoke. With `uv` present, preservation permits the internal edge alone or it plus one spoke from exactly one endpoint, giving `1+2m` choices. Hence

- at `m=6`: `S=7I+N`, `P=62I+Q`;
- at `m=7`: `S=8I+N`, `P=79I+Q`.

### Lemma 5.1 — commuting nilpotents and exact truncation

For each `m in {6,7}`,

`NQ=QN`,

and

`Q^i N^j=0` whenever `i+j>=m`.

**Proof.** The unmarked singleton layer and unmarked matched-pair layer use disjoint fresh vertices and edges. Processing them in either order enumerates exactly the same unions of edge subsets with the same induced terminal partition, so `SP=PS`. Subtracting scalar multiples of the identity gives `NQ=QN`.

After the scalar diagonal is removed, every nonzero transition under `N` or `Q` strictly coarsens the terminal partition. A partition of `m` terminals can be strictly coarsened at most `m-1` times. Therefore any product containing at least `m` factors from `{N,Q}` is zero. This proves the claimed mixed nilpotence. QED.

The exact checker independently reconstructs `S` and `P` from admissible layer edge subsets and verifies both identities entrywise with integer arithmetic.

### Corollary 5.2 — exact bivariate finite response

Set `mu=m+1` and `lambda=lambda_m`. For all integers `x,y>=0`,

`P^x S^y = lambda^x mu^y sum_{i+j<m} binom(x,i) binom(y,j) lambda^{-i} mu^{-j} Q^i N^j`.

This is the commuting binomial expansion, truncated exactly by Lemma 5.1. Consequently every marked count after finitely many distinguished layers is a scalar exponential `lambda^x mu^y` times an exact polynomial in `x,y` of bounded degree.

## 6. Exhaustive marked edge-pair orbit reduction

Expose in all four counts `Z,Z_e,Z_f,Z_{ef}` every right layer touched by the full marked pair. If a distinguished layer has no forced marked edge in one of the four conditions, use its ordinary unmarked transfer; never omit the layer.

Let `a` be the number of distinguished matched-pair layers and `b` the number of distinguished ordinary singleton layers. Put

`x=k-a`, `y=r-b`.

The automorphism group leaves exactly fourteen pair templates:

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

The checker independently classifies every actual pair in generic `G_m(2,2)` instances and finds no residue:

- `m=6`: 38 edges, 703 unordered edge pairs, exactly 14 orbit types;
- `m=7`: 44 edges, 946 unordered edge pairs, exactly 14 orbit types.

For each orbit `O` and condition `A in {0,e,f,ef}`, Corollary 5.2 gives

`Z_A=lambda^x mu^y C_A(x,y)`

with `C_A` an exact rational polynomial. Therefore

`Delta(e,f)=lambda^(2x) mu^(2y) R_O(x,y)`,

where

`R_O=C_e C_f-C_0 C_{ef}`.

## 7. Exact sign certificate on the full physical parameter range

The checker expands each `R_O` in the ordinary monomial basis in the shifted physical variables `x,y` and performs all sign decisions with exact rational arithmetic.

For all 14 orbits at `m=6` and all 14 orbits at `m=7`, every nonzero monomial coefficient of `R_O` is **strictly positive**. Thus all 28 orbit polynomials are coefficientwise nonnegative.

For the orbit consisting of two distinct terminal spokes in the same ordinary singleton layer, there is no distinguished matched-pair layer, so its physical domain has `x=k>=1`; its first physical values are

- `m=6`: `R(1,0)=9871360/961>0`;
- `m=7`: `R(1,0)=753664000/6241>0`.

For every other orbit the first allowed physical value is also strictly positive. Hence every physical integer point satisfies `R_O(x,y)>0`. Since `lambda,mu>0`, this proves

`Delta_{G_m(k,r)}(e,f)>0`

for every allowed `m,k,r,e,f`, completing the theorem.

The archived transcript stores the degree, number of positive coefficients, first physical value, and SHA-256 digest of the primitive coefficient table for each orbit. Maximum Rayleigh-polynomial degrees are 10 at width 6 and 12 at width 7.

## 8. Auxiliary gain: exact deletion–contraction Rayleigh identity and a sharp obstruction

Route B gives a useful general identity that should be preserved separately from the restricted theorem.

Fix an edge `g` distinct from marked `e,f`. Split all forests according to whether `g` is absent or present. Write

- `A,A_e,A_f,A_{ef}` for the `g`-absent counts;
- `B,B_e,B_f,B_{ef}` for the `g`-present counts.

Equivalently `A` is the deletion environment and `B` is the contraction environment after the usual bijection for forests containing `g`. Define

`Delta_A=A_e A_f-A A_{ef}`,

`Delta_B=B_e B_f-B B_{ef}`,

and the environmental response numerators

`E_e=B A_e-A B_e`,

`E_f=B A_f-A B_f`.

Then direct expansion gives the exact identity

`A B Delta_G(e,f)=B(A+B)Delta_A+A(A+B)Delta_B-E_e E_f`.      (8.1)

**Proof.** Expand the right-hand side. The coefficients of `A_eA_f` and `B_eB_f` each reduce to `AB`, the two cross products each appear with coefficient `AB`, and the `A_{ef},B_{ef}` terms equal `-AB(A+B)(A_{ef}+B_{ef})`. Factoring `AB` yields exactly

`(A_e+B_e)(A_f+B_f)-(A+B)(A_{ef}+B_{ef})=Delta_G(e,f)`.

QED.

Identity (8.1) pinpoints why endpoint Rayleigh positivity alone does not make deletion–contraction an induction: if `E_eE_f>0`, the environmental term has the adverse sign.

The checker supplies an exact source-valid witness inside `G_6(1,1)`. Take `g=M0`, `e=L0-R0`, `f=L0-R1`. It obtains

`A=51712`, `B=16384`,

`Delta_A=92078080`, `Delta_B=21233664`,

`E_e=E_f=59506688`,

so

`E_eE_f=3541045916729344>0`,

while the complete graph still has

`Delta_G(e,f)=205324288>0`.

Thus the naive deletion–contraction induction is exactly obstructed even inside a positive family: a successful general recursion would need a quantitative domination of `E_eE_f` by the two endpoint gaps, not merely their nonnegativity.

## 9. Executed exact checker and original-model regressions

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1346Z_matched-biclique-m6-m7_checker.py`

- local executed SHA-256: `e648ee6722f2c8772728b8e612dddd1fd60bf474ef9e25df646b99aa4e8f0d73`;
- create/readback commit: `d990735568e4ef02baf82c3d256ef09ef1bf538d`.

Archived execution:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1346Z_matched-biclique-m6-m7_checker.out`

- local SHA-256: `d3ab855d1b411be62ce9f60d94c7934cda4f17d56461c992c47ac7f4d318da6c`;
- create/readback commit: `76e2b82a26578b6378cdb4b1d2c97c3716bd5399`;
- Git blob: `30f583468df30996fdf7ea83cb99de21b3a39528`.

The checker was re-executed after archiving. The regenerated output has the same SHA-256 `d3ab855d1b411be62ce9f60d94c7934cda4f17d56461c992c47ac7f4d318da6c` and is byte-for-byte identical to the archived transcript. The transcript ends

`PROB10_07_MATCHED_BICLIQUE_M6_M7_EXACT_PASS`.

Separate direct edge-subset enumeration in the **original all-forests model** verifies every actual edge pair in:

- `G_6(1,0)`: 13 edges, 2916 forests, 78 pairs, minimum `Delta=26244`;
- `G_7(1,0)`: 15 edges, 9477 forests, 105 pairs, minimum `Delta=236196`;
- `G_6(1,1)`: 19 edges, 68096 forests, 171 pairs, minimum `Delta=6553600`.

These regressions do not prove the infinite families by themselves; they independently test the transfer construction against the source definition on small members.

## 10. Source and prior-art boundary

The source distinctions remain essential.

- Grimmett–Winkler pose the arbitrary-graph uniform-**all-forests** negative-correlation conjecture and report finite computational verification only in bounded orders.
- Erickson proves a stronger weighted Rayleigh statement for series-parallel graphs, a different structural class.
- Tang–Zhang's 2026 work treats specified spanning-subgraph ensembles of complete graphs, including fixed-component forest regimes, not the arbitrary-graph all-component law here.
- The recent wheel theorem is another restricted non-series-parallel positive family, not a universal resolution.

A bounded current search did not surface the exact all-parameter matched-biclique theorem above. This is only negative search evidence. **External novelty and priority remain UNVERIFIED.** The owner's separate random-cluster parameter-nonmonotonicity paper is not counted as a resolution or antecedent of this theorem.

## 11. Consumed evidence and source-level before/after

Consumed repository evidence is listed in Section 1. The proof depends only on the exact combinatorial transfer construction and the executed exact checker; it does not use P14/HARD10-01's graph-order enumeration as a proof ingredient.

Before this run, the matched-biclique two-nilpotent theorem in this track stopped at widths 4 and 5. After this run, widths 6 and 7 are also completely certified for every `k>=1,r>=0` and every edge pair.

The deletion–contraction route also improves from a qualitative warning about environmental covariance to the exact identity (8.1) plus a concrete positive-response obstruction witness.

## 12. Remaining full-scope gap

Nothing in this report controls an arbitrary finite graph. The proof relies on repeated matched/singleton right layers and the finite terminal-partition algebra. It gives neither a universal structural decomposition nor a source-valid negative Rayleigh counterexample.

The parent Grimmett–Winkler conjecture therefore remains **OPEN/PARTIAL**. The arbitrary-graph complete-order metric remains 9. Independent validation of the restricted theorem is still required before any stronger status label.

A useful next question within this route is whether coefficientwise positivity persists at width 8 or whether an exact orbit polynomial first develops mixed signs. A more ambitious route is to use (8.1) to seek a provable inequality bounding `E_eE_f` by the endpoint Rayleigh gaps on a substantially broader decomposition class.

## 13. Integrity / state-change record

This run created only the idea checkpoint, exact checker/output, this immutable report, and a non-mutating forest-owner handoff. It did **not** alter any scheduler, cadence, enabled state, email, Drive, public posting, workflow, permission, peer claim, shared claim ledger, or P14/HARD10-01 file.

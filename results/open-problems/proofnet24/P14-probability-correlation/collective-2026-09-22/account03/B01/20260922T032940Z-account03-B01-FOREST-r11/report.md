# FOREST / account03 B01 — exact activity unrooting + rooted-determinant mixture no-go

**Run:** `20260922T032940Z-account03-B01-FOREST-r11`  
**Candidate version:** `FOREST-ACTIVITY-TWO-CHANNEL-v1` plus refutation of `FOREST-ROOTED-DETERMINANT-MIXTURE-v1`  
**Outcome:** **ESSENTIAL_STEP_APPLIED** with subsidiary **CANDIDATE_REFUTED**.  
**Parent team state inherited from the lead:** internal `FULL_PROOF_CANDIDATE`; no public/established-theorem promotion.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and exact assignment

For every finite simple graph `G=(V,E)`, choose uniformly from **all** acyclic edge subsets, including the empty forest, disconnected forests and every forest size. For every distinct pair `e,f`, the target is

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

The account03/B01 assignment is to try a determinant/integral or coupling representation of the **actual unrooted law**, with an explicit unrooting argument whenever rooted-forest identities are used. This run does both: it derives a genuine exact unrooted coupling through Tutte/Crapo activities, and proves that the most direct random-root-weight determinant mixture cannot possibly perform the needed unrooting even on `K_4`.

## 2. Exact peer inputs consumed and applied

### Campaign lead

Consumed the current lead handoff `FOREST-KN-COCKS-RECONCILED-v3`,

`scheduled_tasks/work/shared/collective-open-problems-2026-09-22/handoffs/FOREST/account01-B01-20260922T030948Z-v3.md`, blob `e02a4281a67d992d06d7c2c70586efa656353cab`,

and its full scientific report

`proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T030948Z-b01-forest-auto11/report.md`, blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`.

The lead candidate has no currently identified unpaid implication: it proves every complete graph by an exact labelled-forest/Hermite argument, then uses the Cocks fixed-graph weighted upgrade and Semple--Welsh minor closure to reach every finite simple graph. I do not restart or weaken that chain here.

### Required named OTHER-account partner

Consumed account04/B02's current handoff

`scheduled_tasks/work/shared/collective-open-problems-2026-09-22/handoffs/FOREST/account04-B02-20260922T030824Z.md`, blob `c5776f4ffec3033953ce460620bbf7f2e170aaad`.

That result gives exact overlap-reservoir formulas on `K_n` and, crucially, a disjoint-edge `K_5` witness showing that a **q-only** defect-routing coupling is impossible: its cells are `(n00,n10,n01,n11,q)=(49,21,21,43,14)` and the q-only capacity is insufficient, while the ordinary switch channel restores the positive Rayleigh gap `210`.

I apply that result explicitly in Section 4: the activity representation derived here produces `Q=14` on the same `K_5` marked pair and an exact two-channel decomposition in which the Q-channel alone again cannot pay the defect; the ordinary cross channel is indispensable.

## 3. Exact unrooting by basis activity

Fix **any** total edge order with the marked pair first:

`e < f < every other edge`.

Let `M(G)` be the graphic matroid. Its bases are maximal spanning forests (one spanning tree in every nontrivial connected component of `G`; isolated vertices cause no difficulty). For a basis `B`, let `IA(B)` be its set of internally active edges and `i(B)=|IA(B)|`.

The standard Crapo activity partition of the Boolean lattice says every spanning subgraph lies in one unique interval

`[ B \ IA(B), B union EA(B) ]`

indexed by a basis `B`. In the graphic setting this is also stated as: every spanning subgraph is obtained uniquely from one spanning forest by deleting internally active edges and adding externally active edges. A convenient source is Dedndreaj--Tittmann, *On the Activities and Partitions of the Vertex Subsets of Graphs*, arXiv:2008.02006, whose abstract states this exact graphic-matroid consequence of Crapo's partition.

For an **acyclic** subset, no externally active edge can occur. Indeed, if `x` is externally active for `B`, then `x` is the least edge of its fundamental circuit `C(B,x)`. Every `b in C(B,x)-{x}` can be replaced by the smaller edge `x`, hence such `b` is not internally active. Therefore every edge of `C(B,x)-{x}` lies in the lower endpoint `B\IA(B)`. Any interval member that also contains `x` contains the entire circuit and is dependent. Thus every forest has the unique form

`F = B \ D,  D subseteq IA(B)`.

Conversely every such deletion is a forest. Therefore

**`Z = sum_B 2^{i(B)}`**,

and the **uniform unrooted forest law** is sampled exactly by

1. choose a basis `B` with probability `mu(B)=2^{i(B)}/Z`;
2. independently delete every edge of `IA(B)` with probability `1/2`;
3. keep all non-internally-active basis edges.

This is an exact coupling representation of the actual unrooted law, not a rooted-forest proxy and not a fixed-size measure.

## 4. Marked-pair formulas and the two-channel identity

Because `e` is globally least, if `e in B` then `e` is internally active. If both `e,f in B`, then `f` is internally active as well: the only smaller edge is `e`, which is already in the basis, and every possible replacement edge is later than `f`.

If `e notin B` and `f in B`, then `f` is internally inactive **exactly when** `B-f+e` is again a basis, since `e` is the only smaller element outside `B` that could replace `f`.

Define the exchange class

`A_f(e)={B basis : f in B, e notin B, and B-f+e is a basis}`

and the activity-weighted totals

`W_ab = sum_{B: 1_{e in B}=a, 1_{f in B}=b} 2^{i(B)}`,

`Q = sum_{B in A_f(e)} 2^{i(B)}`.

The exact forest counts are then

`Z = W00+W10+W01+W11`,

`Z_e = (W10+W11)/2`,

`Z_f = (W01+W11+Q)/2`,

`Z_ef = W11/4`.

The only asymmetry is the correction `Q`: in an `01` basis from the exchange class, `f` is **not** internally active, so it is never deleted; outside that class it is internally active and survives with probability `1/2`.

Hence the target Rayleigh difference has the exact identity

**`4 Delta_G(e,f) = W10 W01 - W00 W11 + Q (W10+W11)`**.      (A)

Equivalently, under the basis law `mu(B) proportional 2^{i(B)}`,

**`P_mu(f | e) - P_mu(f) <= mu(A_f(e))`**                  (B)

is exactly equivalent to the original uniform-unrooted forest inequality.

This is a genuine all-graphs coupling reduction: it preserves disconnected graphs, every forest size, and unit weights. It does **not** by itself prove the sign in (A); it isolates the exact two channels that a direct coupling must exploit.

### Applying account04/B02's K5 obstruction

For `K_5` with disjoint marked edges first in the order, the exact activity checker gives

`(W00,W10,W01,W11,Q)=(49,70,56,116,14)`.

The same marked-pair forest counts are `(Z,Z_e,Z_f,Z_ef)=(291,93,93,29)`. Thus

`4 Delta = 70*56 - 49*116 + 14*(70+116)`

`        = 3920 - 5684 + 2604`

`        = 840`,

so `Delta=210`, exactly the lead/partner value. Most importantly, **the Q-channel alone contributes only `2604 < 5684`**, so it cannot pay the negative defect term. The cross channel `W10 W01=3920` is essential. This is the activity-coupling version of account04/B02's independently found q-only no-go, and the activity reservoir evaluates to the same `14` on that exact witness.

Therefore a viable direct proof cannot be a one-reservoir argument. It must exploit both the ordinary `10 x 01` exchange mass and the overlap/exchange reservoir, or use the lead's analytic route.

## 5. A determinant/integral unrooting route is impossible in its canonical form

A standard matrix-forest identity for a weighted graph with Laplacian `L(y)` and vertex root weights `x=(x_v)` is

`det(L(y)+diag(x))`

` = sum_{F forest} y^F product_{C component of F} (sum_{v in C} x_v)`.      (C)

This follows directly by expanding the determinant in the diagonal variables and applying the all-minors matrix-tree theorem; at `x_v=1` it is the usual rooted-forest determinant. Chebotarev--Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575, is a standard rooted-forest source.

A natural hoped-for unrooting is to average (C) over a random root-weight vector `x`, perhaps even with a signed measure, so that every unrooted forest coefficient becomes the same constant. The following exact obstruction rules this out.

### No-go theorem

For every `n>=4`, there is **no** finite linear mixture (positive or signed, assuming the needed coefficient moments exist) of standard kernels

`det(L_{K_n}(y)+diag(x))`

whose edge-monomial coefficients are all one, i.e. whose result is the uniform unrooted forest polynomial of `K_n`. An overall nonzero scalar does not help.

**Proof.** If such a mixture existed, average its root-weight measure over all vertex permutations. Since both `K_n` and the desired unrooted polynomial are permutation invariant, this symmetrization preserves the alleged representation. Let

`m_k = E[x_1 ... x_k]`

for any `k` distinct coordinates under the symmetrized measure. A fixed forest whose component-size partition is `(s_1,...,s_k)` has, by (C), averaged coefficient

`(s_1 ... s_k) m_k`,

because expanding the product of component root sums chooses one vertex from each component, and all squarefree `k`-coordinate moments agree after symmetrization.

Uniform unrooting requires this value to be the same nonzero constant for **every** partition of `n` into `k` positive component sizes. Already for `k=2`, compare component sizes

`1+(n-1)` and `2+(n-2)`.

Their coefficients would be `(n-1)m_2` and `2(n-2)m_2`, respectively. For `n>=4` these multipliers differ, so they cannot both equal the same nonzero constant. Contradiction.

For `K_4` the contradiction is especially transparent. A forest with component sizes `1+3` has root factor whose symmetrized expectation is `3m_2`, while a `2+2` forest has coefficient `4m_2`; uniform unrooting would require

`3m_2 = 1 = 4m_2`.

Thus even signed randomization of vertex killing/root weights cannot flatten the rooted determinant into the uniform unrooted law. Any successful determinant/integral route must contain additional component-shape-dependent or nonlocal structure; randomizing ordinary diagonal root weights alone is structurally insufficient. **QED.**

This is a counterexample to a proposed universal representation mechanism, **not** a counterexample to the FOREST conjecture.

## 6. Exact computational audits

Two independent exact checkers accompany this report.

### Activity unrooting checker

A standard-library exhaustive checker enumerated **all 1,074 simple graphs on 2--5 labelled vertices having at least two edges**, including disconnected graphs, and all **11,766 unordered marked-edge pairs**. For each pair it put the marks first in the total order, enumerated maximal graphic bases and internal activities, and independently enumerated every forest. It verified

`Z=sum W`,

`2 Z_e=W10+W11`,

`2 Z_f=W01+W11+Q`,

`4 Z_ef=W11`,

and identity (A) exactly, with zero failures.

Output:

```text
ACTIVITY_UNROOTING_EXHAUSTIVE_PASS
graphs_n2_to_n5_with_at_least_two_edges = 1074
marked_pairs_checked = 11766
K5_disjoint: Z,Ze,Zf,Zef = (291, 93, 93, 29)
K5_disjoint: W00,W10,W01,W11,Q = (49, 70, 56, 116, 14)
K5_disjoint: 4*Delta = 840 Delta = 210
ACTIVITY_TWO_CHANNEL_IDENTITY_PASS
```

Checker SHA-256: `2414d57e875770329d23aedcf81b17be938153b479ae51c99cca5f083422727f`.  
Output SHA-256: `24a77ebc454ddacf26199575903ae60fc5d133c1d2023c93c9d3e3f07ecc13df`.

### Determinant coefficient checker

An exact SymPy 1.14.0 calculation expanded `det(L_{K4}(y)+diag(x))` and extracted two forest coefficients:

```text
K4_ROOTED_DETERMINANT_COEFFICIENT_CHECK
partition 1+3: x1*(x2 + x3 + x4)
partition 2+2: (x1 + x2)*(x3 + x4)
after permutation symmetrization:
  E[1+3 coefficient] = 3*m2
  E[2+2 coefficient] = 4*m2
uniform unrooted coefficient c>0 would require 3*m2=c=4*m2
hence m2=0 and c=0, contradiction
DETERMINANT_MIXTURE_UNROOTING_NO_GO_PASS
```

Checker SHA-256: `8b7f999d6e9470bf2091cb10f42cc71287e8623565e0cd6cd35e41adc246662f`.  
Output SHA-256: `8183753761e0ed905243bbc618449eff1da85c3a61244339b253d20368ce96eb`.

The no-go theorem is symbolic; the computation is only an independent audit of the `K_4` coefficient extraction.

## 7. Status and next useful recipient

**New exact contribution:** the actual uniform unrooted law has the activity-basis coupling (Sections 3--4) and exact two-channel Rayleigh identity (A). The canonical random-root-weight determinant-mixture route is rigorously impossible already on `K_4` (Section 5). The named account04/B02 q-only obstruction is reproduced inside the activity representation on its exact `K_5` witness.

**Parent status:** I do not demote the lead's `FOREST-KN-COCKS-RECONCILED-v3`; that candidate remains internally complete with two prior independent end-to-end reviews. This run is an independent structural contribution/route elimination, not a new public solution claim.

**Next recipient:** FOREST lead `account01/B01`, and the direct-coupling workers `account01/B02` / `account01/B03`. If they pursue a direct all-graphs coupling despite the already-complete analytic candidate, the exact remaining coupling obligation is now sharply stated as proving

`W10 W01 + Q(W10+W11) >= W00 W11`

for the activity-weighted basis cells, with neither channel discarded. A determinant route must go beyond mixtures of ordinary diagonal-root matrix-forest kernels and encode component-shape dependence explicitly.

No brain installation/benchmark work, scheduler mutation, email, Drive, public posting, paid model/API/Codex, remote workflow, or cross-account native action was performed.

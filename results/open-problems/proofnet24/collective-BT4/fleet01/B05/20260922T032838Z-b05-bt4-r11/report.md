# BT4 B05 report — double-sink support splice

Run: `20260922T032838Z-b05-bt4-r11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z / BT4`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `BT4-G1-DOUBLE-SINK-SPLICE-v1`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and role

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Digons count. This report works only inside the team's inherited oriented exact-outdegree-seven minimum-counterexample normal form and does not claim the target theorem.

B05 role: construct an exchange which turns the inherited three-cycle packing into four cycles and account for all affected vertices.

## Exact inherited inputs used

1. Campaign lead fleet02/B04 controlling correction, shared blob `efc49c4d0177e30caf791b471ff9a9becb2c060b`: in the no-cross branch every cycle-supported heavy witness has a heavy-cycle inport. Its earlier unsupported TCEX use in the `A not->z` branch is not used.
2. Assigned OTHER-account partner fleet02/B06, `BT4-3SLOT-SYNC-v1`, shared blob `80d995a193feaf7d0e90f1a7e894689f395e2a0f`: same-pair fresh-witness regeneration can cycle, coalesced exits cannot be assumed distinct, and the live missing ingredient is a genuine cross-pair synchronization/exchange.
3. fleet03/B06 `BT4-G1-PORT-SPACING-v1`, shared blob `2c82f2baa29017affdc5e8684af25830d9c49a00`: for two same-heavy support witnesses the heavy-target return segments obey an exact one-sided cyclic corridor.
4. fleet04/B04 `BT4-G1-PREDECESSOR-FORK-v1`, shared blob `332c9d67222424c8ebe0c25a7cf195dd2c2bd1af`: in G1-S a support five-witness `z in B`, heavy on `A`, has at least `m>=3` remainder predecessors; its unique remainder exit either avoids that predecessor region or any return is long/neutral. For two same-heavy witnesses, the predecessor cycles intersect; disjoint inport sets force a common remainder predecessor with an additional residual outarc.

The partner's coalescence warning is applied directly below: no distinct-exit or disjoint-path assumption is made without explicitly requiring the corresponding paths.

## Conditional end-to-end location

Take the inherited globally minimum three-cycle packing `(A,B,C)` with acyclic remainder `R`, in the global no-six, no-cross G1-S branch. Let `z1,z2 in B` be two cycle-supported five-witnesses heavy on the same cycle `A`. In the fixed pair-residual graph `Gamma=D-(A union C)=D[B union R]`, each `zi` has exactly its support successor plus one remainder exit `ei`. The G1-S invariant and no-six give

`d_Gamma^+(r) >= 3` for every `r in R`.

The first missing global step is to turn the two support witnesses plus their remainder routing into two disjoint replacement cycles, allowing `A,C` to remain untouched. The following two lemmas do exactly this whenever the remainder does not coalesce too strongly.

## Lemma 1 — sink-fan collar

Let `z in B` be any G1-S support five-witness with unique remainder exit `e`. Let

`P : e = v0 -> v1 -> ... -> v_L = s`

be a shortest directed path in `R` from `e` to an `R`-sink `s`; thus `L=dist_R(e,s)`. Such an `s` exists because `R` is finite and acyclic. Put `n=|B|` and

`T_s = N_D^+(s) intersect B`, `k=|T_s|`.

Then:

1. `k>=3`;
2. for every `b in T_s`,

   `L + d_B(b,z) + 2 >= n`,

   where `d_B(b,z)` is the forward distance on the directed cycle `B` from `b` to `z`, with the trivial distance zero allowed when `b=z`;
3. consequently

   `L >= k-2 >= 1`;

4. if `L < n-2`, then

   `T_s subset (z, z^{+(L+2)}]_B`.

### Proof

Since `s` is an `R`-sink, it has no outneighbor in `R`. Hence all of its `Gamma`-outneighbors lie on `B`. The G1-S/no-six residual-degree bound gives `k=d_Gamma^+(s)>=3`.

For each `b in T_s`, form

`K_b = z -> e -> P -> s -> b -> B[b,z]`.

This is a genuine directed cycle disjoint from `A` and `C`. Replacing `B` by `K_b` leaves a legal three-cycle packing `(A,K_b,C)`. Global minimum of `(A,B,C)` therefore implies `|K_b|>=|B|`. Counting edges (equivalently vertices) gives

`|K_b| = L + d_B(b,z) + 2`,

which proves (2).

If `L>=n-2`, then because `k<=n`, already `L>=k-2`. Otherwise `L<n-2`. Then `b=z` is impossible by (2), and (2) is equivalent to `d_B(z,b)<=L+2` for every `b in T_s`; hence all `k` distinct fan targets lie among the first `L+2` strict successors of `z`. Thus `k<=L+2`, so again `L>=k-2`. Since `k>=3`, `L>=1`. The same argument gives (4). QED.

### Immediate consequence

The unique remainder exit of a G1-S support five-witness is never itself an `R`-sink. More generally every exit-to-sink route pays at least `d_B^+(s)-2` remainder edges. In the short-return regime it also forces the entire sink fan into a bounded forward window on `B`.

This is a second, independent corridor axis: fleet03/B06 confines the heavy fan on `A`; this lemma confines the terminal sink fan on the support cycle `B`.

## Lemma 2 — double-sink support splice

Let `z1,z2 in B` be distinct support witnesses with exits `e1,e2`. Suppose there are vertex-disjoint directed paths in `R`

`P_i : e_i -> ... -> s_i`,  `i=1,2`,

where each `s_i` is an `R`-sink. Choose any `b_i in N^+(s_i) intersect B`. If the two directed support segments

`B[b1,z1]` and `B[b2,z2]`

are vertex-disjoint, then `D` contains four vertex-disjoint directed cycles.

### Proof and complete vertex accounting

Define

`L_i = z_i -> e_i -> P_i -> s_i -> b_i -> B[b_i,z_i]`.

Each `L_i` is directed in the original digraph. The two `R`-parts are disjoint by hypothesis; `R` is disjoint from `B`; the two `B`-segments are disjoint by hypothesis; hence `L_1,L_2` are vertex-disjoint. Both are disjoint from `A,C`. Therefore

`A, C, L_1, L_2`

are four vertex-disjoint directed cycles.

Affected vertices are explicit: the old cycle `B` is discarded as one packing member; its vertices on the two disjoint segments are consumed by `L_1,L_2`, while all remaining vertices of `B` become uncovered. The two chosen `R` paths are consumed by the new cycles; every other old remainder vertex stays uncovered. `A` and `C` are unchanged. No hidden edge-disjoint-to-vertex-disjoint substitution is used. QED.

## Corollary — a second exact cyclic corridor

Continue in a counterexample and assume the two disjoint exit-to-sink paths above exist. Let

`T_i=N^+(s_i) intersect B`, `k_i=|T_i|>=3`, `L_i=|E(P_i)|`.

Then every segment `B[b1,z1]`, `b1 in T1`, intersects every segment `B[b2,z2]`, `b2 in T2`; otherwise Lemma 2 gives four cycles.

If additionally `L_i<n-2` for both `i`, Lemma 1 implies `z_i notin T_i`. Applying the elementary directed-cycle interval argument used in the fleet03/B06 corridor theorem, all-crossing is equivalent to

`T1 subset (z1,z2]_B`  OR  `T2 subset (z2,z1]_B`.

Indeed, if neither inclusion holds, choose

`b1 in T1 intersect (z2,z1)_B`,
`b2 in T2 intersect (z1,z2)_B`;

then `B[b1,z1] subset (z2,z1]_B` and `B[b2,z2] subset (z1,z2]_B`, so the two segments are disjoint, contradiction.

Consequently

`d_B(z1,z2) >= k1`  OR  `d_B(z2,z1) >= k2`,

and each `k_i>=3`.

Thus, whenever the remainder supplies two disjoint exit-to-sink routes, a genuine counterexample must pay a second support-cycle port-spacing constraint in addition to the already proved heavy-cycle fan corridor.

## What this closes and what remains

This closes the entire subcase in which two same-heavy G1-S witnesses have vertex-disjoint exit-to-sink routes and their terminal sink fans admit opposite support choices. No assumption that the exits are distinct is made; if they coalesce, the lemma simply does not claim disjointness, exactly respecting fleet02/B06's counterexample mechanism.

The surviving obstruction is now precise:

- either the two exit-to-sink path systems are forced to coalesce/intersect in `R`;
- or disjoint routes exist, but every pair of terminal sink fans obeys the support corridor above;
- simultaneously the same two witnesses obey fleet03/B06's heavy-target corridor on `A` and fleet04/B04's intersecting predecessor-cycle / common-remainder-predecessor fork.

Call the first unpaid implication `BT4-G1-TWO-AXIS-CLOSURE-v1`:

> In a no-six, no-cross G1-S state, show that the simultaneous heavy-target corridor on `A`, terminal-sink corridor on `B`, and predecessor-cycle intersection/common-R-fork cannot persist in a globally minimum packing without producing a cross-packed transition, a six-fan, a strict smaller three-packing, an exchanged-remainder directed cycle, or two disjoint replacement cycles.

The most concrete next attack is the coalesced branch, because the new lemma disposes of the genuinely disjoint routing geometry. One should use the common remainder predecessor with its third residual outarc against the common downstream bottleneck of the two exit systems.

## Status

`ESSENTIAL_STEP_APPLIED`. This is not a proof of BT4. Exact-six, G1-R and other global branches remain open. No source-valid target counterexample was found or claimed. No computation was needed for the two new lemmas.

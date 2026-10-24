Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = 3 -> 3`. Methods actually tried: #1, #4, #15.**

# NM13-04 / P0457 — full sharp diameter in the new logarithmic connectivity band

Run UTC: 2026-09-18T02:16:28Z  
Track: `NM13-04 Graph Counterexamples`, CLOSABLE OUTSIDE.  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`.  
Canonical near-logarithmic source target after this run: **PROVED-CANDIDATE / closure AUDIT-PENDING**.  
Frozen metric after this run: **`S_exact = 3` (unchanged)**.

## 1. Continuity, ownership, required reads, and runtime controls

This is the sixth NM13-04 research run on the already admitted P0457 target. Intake was **not** reopened and no second claim was created.

Canonical identity remains:

- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025;
- source target frozen in `operations/claims/P0457.md`: characterize the diameter of `LK(n,k)` in the additional **near-logarithmic** range where the 2026 paper's Theorem 6 proves connectivity;
- dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- SHA256 residue modulo 13: `3`, matching NM13-04's exclusive shard;
- exclusive owner: NM13-04.

Before new mathematics I reread/recovered the controlling/current state required by the owner: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the P0457 claim and exact catalog/attempt history; the newest own report `2026-09-18T01-27-56Z__p0457-bulk-distance-sandwich.md`; newest neighboring NM13-03 report `2026-09-18T02-10-29Z__admission-screen-6.md`; and newest neighboring NM13-05 report `2026-09-18T01-23-13Z__d0004-symmetric-ternary-threshold.md`. NM13-03 remains admission-pending. NM13-05 continues D0004 and has not audited P0457. No release, competing owner, handoff, retirement, posted settlement, or source-specific correction affecting P0457 was recovered.

Large aggregate files can be connector-truncated. I used exact-path/exact-ID/dedup/claim/report reads in addition to the visible roots and do not infer inaccessible, deleted, non-master, or truncated history is empty.

The exposed task-control surface still has prompt/title, timing/schedule and enabled-state fields but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-effort telemetry**. The requested `GPT-6 / maximum` therefore remains prompt text only. This invocation actually runs GPT-5.6 Sol; reasoning is `UNVERIFIED`. The historical P26 `You cannot modify this task` response remains authorization/context-specific; repository state records later successful modification from another authorized context. A future refusal must be handled from the owning/authorized account/workspace/product/admin/API surface, not by cloning the task or bypassing permissions. No support escalation is claimed here.

## 2. Source and literature check — 2026-09-18 UTC

The 2026 source still explicitly says that, after improving connectivity, “another open problem is characterizing the diameter for the additional range of `k(n)` from Theorem 6 where connectivity holds.” Theorem 6's connected side is

`k >= log n + t0 sqrt(log n) log log n`, with fixed `t0>1/2`.

The source places this question in the near-connectivity regime. The 2015 predecessor of La and Kabkab, *A New Random Graph Model with Self-Optimizing Nodes: Connectivity and Diameter*, Internet Mathematics 11 (2015), Theorem 5.3, proves

`D(LK(n,k))/(log n/log log n) -> 1`

only for `k=Theta(log n)` with `liminf k/log n > beta_*`, `beta_* ~= 2.4626`; its proof uses a connected Erdos–Renyi graph embedded in `LK`.

Fresh bounded searches on 2026-09-18 used the exact 2026 title/authors plus `diameter`, `bilateral preference random graph diameter`, `LK(n,k) diameter`, and the 2015 predecessor title. They recovered the 2026 source, the 2015 predecessor, and classical Erdos–Renyi diameter literature, but no later source-matching resolution. This is **bounded negative evidence only**, not a proof of worldwide openness and not a novelty certificate.

A key published ingredient used below is Chung and Lu, *The diameter of sparse random graphs*, Advances in Applied Mathematics 26 (2001), which proves in particular that when `np -> infinity` (using diameter as the maximum finite component diameter),

`diam(G(n,p)) = (1+o_P(1)) log n / log(np)`.

Riordan and Wormald (Combinatorics, Probability and Computing 19 (2010), 835–926) later obtain much sharper concentration over the full sparse range. I use only the first-order consequence above. The new leave-one-out block-core attachment argument below is not claimed known; publication novelty is **UNVERIFIED**.

## 3. Frozen metric: no movement

The canonical claim freezes

`S_exact = largest s for which this track has a complete deterministic diameter classification for the exact source family LK(n,n-1-s), uniformly over the stated feasible n.`

Earlier runs proved `S_exact=3`. The asymptotic theorem below does not extend that deterministic co-degree classifier, so I do not replace or silently renormalize the metric.

- before: `S_exact=3`;
- after: `S_exact=3`;
- frozen-metric movement: **none**;
- consecutive unchanged runs since the last frozen-metric movement: **3**;
- stuck recoveries used: **0**.

Thus, under the owner's literal three-unchanged-run rule, the **next** NM13-04 invocation must be a Section-I thinking-only stuck-recovery run with no new mathematical claim, even though this run makes source-level progress.

---

## 4. Main theorem

Work in the equivalent exponential-value representation: every edge of `K_n` has an iid `Exp(1)` score, each vertex proposes its `k` largest incident scores, and an edge is present in `LK(n,k)` iff both endpoints propose it.

### Theorem P0457-SHARP-LOGBAND-DIAMETER

Fix constants `t0>1/2` and `T>1`. Let `k=k(n)` be any integer sequence satisfying, for all sufficiently large `n`,

`log n + t0 sqrt(log n) log log n <= k <= T log n`.

Then

`D(LK(n,k)) / (log n / log log n) -> 1`

in probability.

In particular, this extends the La–Kabkab sharp diameter law from the old `liminf k/log n > beta_* ~=2.4626` regime all the way down to every fixed positive distance above the connected side of the 2026 source window. This is exactly the canonical P0457 near-logarithmic gap.

I prove the theorem below. No finite computation enters the proof.

---

## 5. Method #1 — CHANGE THE CATEGORY: worst-vertex distance becomes a leave-one-out rank problem

The immediately preceding run found the obstruction to a direct connected-ER sandwich: the definite lower threshold graph has polynomially many isolates near `k~log n`. The mistake is to demand that this lower graph itself span every source vertex.

Instead, remove the source vertex from the object against which it is tested. For distinct `v,w`, let

`T_w^(-v)`

be the `k`th largest score among the `n-2` edges incident to `w` other than `vw`. This variable is measurable from edges **not incident to `v`**. Therefore, conditional on every non-`v` edge, all scores `(V_vw)_{w!=v}` remain iid `Exp(1)`.

For any threshold `q`,

`T_w^(-v) <= q < V_vw`

implies that `w` proposes `vw`. If in addition `v` itself proposes `vw`, the edge is in `LK(n,k)`.

This changes the exceptional-vertex question from a dependent BFS problem into an order-statistic statement with fresh iid incident scores, provided the target core is also chosen without using any edge incident to `v`.

---

## 6. Recovered robust definite-edge sandwich

The preceding run proved, uniformly for `log n <= k <= T log n`, that with probability `1-o(1)` every vertex `i` has kth-largest incident score `U_{i,k}` in

`L_- <= U_{i,k} <= L_+`,

where

`L_+ = log((n-1)/k)+2`,
`L_- = log((n-1)/k)-3/2`.

For completeness, this follows directly from binomial Chernoff bounds: `U_{i,k}>L_+` means at least `k` of `n-1` iid exponentials exceed `L_+`, whose mean count is `e^-2 k`; `U_{i,k}<L_-` means fewer than `k` exceed `L_-`, whose mean is `e^(3/2)k`. Both one-vertex tails have exponent strictly larger than `log n` when `k>=log n`, so a union bound over all vertices is `o(1)`.

Define threshold graphs from the same raw edge scores:

`G_+ = {ij: V_ij>L_+}`,  `p_+=e^-2 k/(n-1)`,
`G_- = {ij: V_ij>L_-}`,  `p_-=e^(3/2) k/(n-1)`.

On the robust event,

`G_+ subset LK(n,k) subset G_-`.  (6.1)

Both satisfy `np_±=Theta(log n)`, hence the classical ER diameter theorem gives

`diam(G_+) = (1+o_P(1)) s_n`,
`diam(G_-) = (1+o_P(1)) s_n`,

where

`s_n := log n/log log n`.  (6.2)

The only missing ingredient for a full source upper bound is to show that any two source vertices can reach the **same** connected component of `G_+` in one additional source edge each.

---

## 7. Method #15 — BREAK THE SYMMETRY ON PURPOSE: pair-specific block-deleted cores

The independence problem disappears if the core deliberately excludes the endpoint blocks.

Put

`h_n := sqrt(log n) log log n`,
`theta := t0/8`,
`delta_n := theta h_n/k`,
`m_n := ceil(1/delta_n)`.

Then `delta_n ->0`, `m_n->infinity`, and `1/m_n <= delta_n`.

Deterministically partition `[n]` into `m_n` balanced blocks

`B_1,...,B_m`,

so every block has size at most `n/m+1`.

For each unordered pair of block indices `i,j` (allowing `i=j`), let

`W_ij := [n] \ (B_i union B_j)`

(with only one copy removed when `i=j`), and let `H_ij` be the graph on `W_ij` containing exactly edges with raw score greater than `L_+`. Thus

`H_ij ~ G(N_ij,p_+)`,

and, crucially, if `v in B_i`, then `H_ij` is measurable without any edge incident to `v`.

Let `C_ij` be a largest connected component of `H_ij` (ties broken deterministically).

### Lemma 7.1 — every block-deleted core loses only `o(n/k)` vertices

With probability `1-o(1)`, simultaneously for every `i,j`,

`|C_ij| >= N_ij - n/k^3`.  (7.1)

#### Proof

For every pair,

`N_ij >= n(1-2 delta_n)-2`,

and with `lambda_ij=N_ij p_+`, for all large `n`,

`c0 log n <= lambda_ij <= C0 log n`

for fixed positive constants `c0,C0` depending only on `T` (one may take `c0=e^-2/3`).

Fix one such `H~G(N,p_+)`. If a given `r`-set is a connected component, it contains one of `r^(r-2)` spanning trees and has no cut edge. Hence

`P(exists an r-component)`
` <= C(N,r) r^(r-2) p_+^(r-1) (1-p_+)^(r(N-r))`.  (7.2)

Choose a fixed integer `R>12/c0`. For `R<=r<=N/2`, using `C(N,r)<=(eN/r)^r` and `lambda=Np_+`, (7.2) is at most

`N/(lambda r^2) [ e lambda exp(-lambda/2) ]^r`.

For large `n`, `e lambda <= exp(lambda/6)`, so the bracket is at most `exp(-lambda/3)<=n^(-c0/3)`. Summing `r>=R` gives probability `O(n^-3)` that any component has size between `R` and `N/2` (increase fixed `R` if needed).

Let `Z_<R` be the number of vertices in components of size `<R`. Multiplying (7.2) by `r` and summing the finitely many `r<R` gives

`E Z_<R <= n^(1-c0/3)`

for all large `n` (polylogarithmic factors from `lambda^(r-1)` are absorbed). Thus

`P(Z_<R > n/k^3) <= k^3 n^(-c0/3)=o(1)`.

On the complement of those two bad events, there must be one component larger than `N/2`, and every vertex outside it belongs to a component of size `<R`; therefore the largest component has at least `N-n/k^3` vertices.

There are only `O(m^2)=polylog(n)` block pairs, while the displayed failure bounds are polynomially small in `n`. A union bound proves (7.1).  QED.

The point of the artificial blocks is not combinatorial efficiency; it is exact conditional independence. For a pair `u in B_i`, `v in B_j`, both can be tested against the same core `C_ij`, and that core was built using no edge incident to either endpoint block.

---

## 8. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: one-edge attachment to every relevant core

The weaker structural statement needed for the diameter is the following.

### Lemma 8.1 — uniform one-edge core attachment

With probability `1-o(1)`, for every block index `i`, every vertex `v in B_i`, and every `j in {1,...,m}`, vertex `v` has an `LK(n,k)` neighbor in `C_ij`.

#### Proof

Set

`q_n := log((n-1)/k)+delta_n`,
`p_0 := P(Exp(1)>q_n)=e^(-delta_n) k/(n-1)`.

First control endpoints whose leave-one-out threshold is too high. Define the global set

`B := { w : at least k incident edge scores at w exceed q_n }`.

For each `w`, its count is `Bin(n-1,p_0)` with mean

`mu=e^(-delta_n)k`.

The Chernoff bound at level `k` is

`P(w in B) <= exp[-k I(delta_n)]`,

where

`I(x)=x-1+e^-x >= x^2/3`

for all sufficiently small positive `x`. Since `k<=T log n`,

`delta_n^2 k = theta^2 h_n^2/k >= (theta^2/T)(log log n)^2`.

Therefore, with

`b_n := exp[-theta^2 (log log n)^2/(6T)]`,

Markov's inequality gives

`P(|B|>n b_n) <= b_n ->0`.  (8.1)

Also `k b_n->0` and `b_n=o(delta_n)`.

For a fixed vertex `v`, define the **leave-one-out** bad set

`B_v := {w!=v : T_w^(-v)>q_n}`.

If `w in B_v`, then at least `k` edges incident to `w` other than `vw` exceed `q_n`, so `w in B`. Hence pointwise

`B_v subset B`.  (8.2)

Now fix `v in B_i` and an index `j`. Conditional on all edges not incident to `v`, both `C_ij` and `B_v` are fixed. On the core-size event (7.1) and whenever `|B_v|<=n b_n`, put

`A := C_ij \ B_v`.

Then

`|A|/(n-1) >= 1 - 2 delta_n - b_n - k^-3 - o(delta_n)`
`                = 1 - 2 delta_n - o(delta_n)`.  (8.3)

The incident scores `(V_vw)_{w!=v}` are still iid exponentials. Let

`R_v={w:V_vw>q_n}`

and let `S_v` be the labels of the `k` largest incident scores, i.e. the vertices proposed by `v`.

If `|R_v|<=k`, then every edge in `R_v` is proposed by `v`. Thus any `w in A intersect R_v` is proposed by `v`, and since `T_w^(-v)<=q_n<V_vw`, it is also proposed by `w`; hence `vw` is an `LK` edge.

If `|R_v|>k`, then all vertices in `S_v` have score greater than `q_n`. Thus any `w in A intersect S_v` again yields an `LK` edge.

Consequently, conditional on the non-`v` edges,

`P(v has no LK neighbor in A)`
` <= P(A intersect R_v = empty) + P(A intersect S_v = empty)`
` = (1-p_0)^|A| + C(n-1-|A|,k)/C(n-1,k)`
` <= exp(-p_0|A|) + (1-|A|/(n-1))^k`.  (8.4)

By `e^-delta >=1-delta` and (8.3),

`p_0|A| >= k(1-delta_n)(1-2delta_n-o(delta_n))`
`          >= k - 3 delta_n k - o(h_n)`
`          = k - 3 theta h_n - o(h_n)`
`          >= log n + (t0-3theta)h_n - o(h_n)`.

Since `theta=t0/8`,

`p_0|A| >= log n + (5t0/8-o(1))h_n`.  (8.5)

The second term of (8.4) is at most `(3 delta_n)^k` for all large `n`.

There are at most `n m` vertex/core attachment requirements. Therefore (8.4)-(8.5) give

`n m [ exp(-p_0|A|) + (3delta_n)^k ]`
` <= m exp[-(5t0/8-o(1))h_n] + n m(3delta_n)^k`
` -> 0`.  (8.6)

One conditioning subtlety is worth recording. Event (8.1) involves incident edges, so I do **not** condition on it. Instead, (8.2) implies that if `|B|<=nb_n`, then every `|B_v|<=nb_n`; for each fixed `v`, the event `|B_v|<=nb_n` is non-`v` measurable and the conditional calculation above applies. Thus

`P(any attachment fails)`
` <= P(|B|>nb_n) + P(any attachment fails while its |B_v|<=nb_n and its core is large) + P(any core is small)`,

and the three terms tend to zero by (8.1), (8.6), and Lemma 7.1.

This proves the lemma.  QED.

This is the step the direct lower-sandwich proof lacked: the definite ER graph may have many isolates, but every **source** vertex can still use one extra bilateral edge to reach a pair-specific large definite-edge component.

---

## 9. Proof of Theorem P0457-SHARP-LOGBAND-DIAMETER

Intersect the following events, each of probability `1-o(1)`:

1. the robust threshold sandwich (6.1);
2. all block cores are large (Lemma 7.1);
3. every relevant vertex-to-core attachment exists (Lemma 8.1);
4. the two ER diameter asymptotics (6.2).

Take arbitrary source vertices `u in B_i` and `v in B_j`. Lemma 8.1 gives an LK edge from `u` to some `a in C_ij` and an LK edge from `v` to some `b in C_ij`. Since `C_ij` is connected inside `H_ij subset G_+`, and `G_+ subset LK`, both `a,b` lie in the same `G_+` component. Therefore

`d_LK(u,v) <= 1 + d_G+(a,b) + 1 <= diam(G_+) + 2`.

This holds for every pair `u,v`, so it also proves connectivity on the event and yields

`diam(LK) <= diam(G_+) + 2`.  (9.1)

On the same event, `LK subset G_-`. Since `LK` is connected, its supergraph `G_-` is connected as well, and for every pair

`d_LK(u,v) >= d_G-(u,v)`.

Hence

`diam(G_-) <= diam(LK)`.  (9.2)

Combining (9.1)-(9.2),

`diam(G_-) <= diam(LK(n,k)) <= diam(G_+) + 2`.  (9.3)

Finally,

`(n-1)p_+ = e^-2 k`,
`(n-1)p_- = e^(3/2) k`,

and `k=Theta(log n)`. Thus

`log((n-1)p_±)=log log n+O(1)`,

so the classical ER diameter theorem gives

`diam(G_±) = (1+o_P(1)) log n/log log n`.

Divide (9.3) by `s_n=log n/log log n`; the additive `2/s_n` vanishes. Therefore

`diam(LK(n,k))/s_n ->1`

in probability.  QED.

---

## 10. What this resolves, and what it does not

The canonical P0457 claim was deliberately scoped to the source's **additional near-logarithmic connectivity range**. The theorem above gives the same sharp diameter law as La–Kabkab all the way from

`log n + t0 sqrt(log n) log log n`, `t0>1/2`,

through every fixed logarithmic multiple `T log n`. Thus, in the canonical P0457 scope, there is now a full proof on the page of the source-requested characterization:

`D(LK(n,k)) = (1+o_P(1)) log n/log log n`.

I therefore label the canonical mathematical target **PROVED-CANDIDATE / AUDIT-PENDING**, not repository-closed. The owner closure standard still requires independent end-to-end audits by **P26** and **NM13-05**; neither is presumed or counted as passed. No paper folder is created before those audits.

I do **not** claim a theorem for arbitrary superlogarithmic `k` up to order `n`; that broader literal reading is outside the claim's frozen near-logarithmic scope and the proof uses `k<=T log n`. I also do not claim publication novelty from the bounded literature search.

No exact-arithmetic artifact was created because the new result has no finite computational core. Its substantive core is the analytic leave-one-out attachment proof above; manufacturing a checker would not validate that argument.

## 11. Section-B method accounting

The three genuinely new methods actually used on P0457 in this run were:

- **#1 CHANGE THE CATEGORY.** Recast exceptional-vertex metric control as a leave-one-out order-statistic acceptance problem with fresh iid incident scores. **Outcome: succeeded;** it isolates the dependency that had blocked the lower ER core.
- **#15 BREAK THE SYMMETRY ON PURPOSE.** Deterministically partition vertices and delete the endpoint blocks when defining each core. **Outcome: succeeded;** pair-specific block-deleted ER cores are independent of both endpoint incident-score families.
- **#4 PROVE SOMETHING WEAKER, COMPLETELY.** First prove the one-edge attachment lemma to every relevant block core rather than attack diameter directly. **Outcome: succeeded;** combined with the existing ER sandwich it immediately squeezes the full diameter.

These methods were not used in the immediately preceding run and were not previously counted on P0457.

Because the frozen metric has now been unchanged for three consecutive runs, I reserve no new claim-producing triple for the next invocation: the next invocation is required to execute Section I's thinking-only stuck protocol first.

## 12. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  source_id: P0457
  claim_id: P0457
  source_target: diameter_near_the_newly_established_bilateral_connectivity_threshold
  status: PROVED_CANDIDATE_AUDIT_PENDING
  exact_scope:
    model: LK(n,k) bilateral preference graph from iid continuous edge scores
    parameters: "fixed t0>1/2 and T>1; log n + t0*sqrt(log n)*log log n <= k <= T*log n"
    conclusion: "diam(LK(n,k))/(log n/log log n) -> 1 in probability"
    broader_superlogarithmic_scope: NOT_CLAIMED
  metric:
    name: S_exact
    before: 3
    after: 3
    movement: false
  source_level_progress:
    sharp_logarithmic_band_diameter: PROVED_ON_PAGE
    prior_La_Kabkab_threshold: "liminf k/log n > beta_* ~= 2.4626"
    new_lower_endpoint: "Theorem-6 connected side, any fixed t0>1/2"
  section_B_methods:
    attempted: [1, 4, 15]
    outcomes:
      1: "leave-one-out rank reformulation succeeded"
      4: "uniform one-edge block-core attachment lemma proved"
      15: "block deletion broke endpoint/core dependence and succeeded"
  finite_artifact: NONE_ANALYTIC_THEOREM_NO_FINITE_CORE
  literature_check:
    date_utc: 2026-09-18
    original_source: RECHECKED_OPEN_PROBLEM_WORDING
    predecessor_2015: RECHECKED_BETA_STAR_DIAMETER_SCOPE
    ER_diameter_prior_art: CHUNG_LU_2001_AND_RIORDAN_WORMALD_2010
    later_source_matching_resolution_found: false
    negative_search_scope: BOUNDED_NOT_NOVELTY_CERTIFICATE
  audits:
    P26: NOT_YET_PASSED
    NM13-05: NOT_YET_PASSED
  unchanged_runs_since_metric_movement: 3
  stuck_recoveries_used: 0
  next_run_protocol: SECTION_I_THINKING_ONLY_NO_NEW_CLAIMS
  shared_root_edits: NONE
  peer_track_edits: NONE
```

No email/Gmail, Drive, public posting, paid compute, permission change, external workflow execution, peer-track edit, shared-root edit, or schedule creation/modification was performed.

**End of immutable run report.**
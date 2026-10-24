Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = 3 -> 3`. Methods actually tried: #3, #12, #27.**

# NM13-04 / P0457 — sharp bulk-pair distance in the new connectivity range

Run UTC: 2026-09-18T01:27:56Z  
Track: `NM13-04 Graph Counterexamples`, CLOSABLE OUTSIDE.  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`.  
Parent source status after this run: **OPEN / PARTIAL**.  
Frozen metric after this run: **`S_exact = 3` (unchanged)**.

## 1. Continuity, ownership, required reads, and runtime controls

This is the fifth NM13-04 research run on the already admitted P0457 target. I did **not** reopen intake, create a second ownership claim, or edit a shared root ledger.

Canonical identity remains:

- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025;
- source target: the paper's explicit open problem of characterizing the diameter of `LK(n,k)` in the additional near-threshold range where its Theorem 6 proves connectivity;
- canonical dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue modulo 13: `3`, matching NM13-04's exclusive shard;
- exclusive owner: NM13-04 under `operations/claims/P0457.md`.

Before new mathematics I reread/recovered `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, the later owner-authorized NM13 deployment amendment, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the P0457 claim, the newest own report `2026-09-18T00-16-18Z__p0457-logband-expansion-diameter.md`, and the newest recovered neighboring reports from NM13-03 and NM13-05. NM13-03 remains admission-pending; NM13-05 is working D0004 and has not audited P0457. No release, competing owner, handoff, retirement, posted closure, or source-specific correction affecting P0457 was recovered.

The previous run used methods `#9/#11/#28` and established a robust all-vertex order-statistic sandwich plus an `O(log n)` diameter bound throughout the source's newly connected logarithmic band. It explicitly nominated `#3/#12/#27` as the next unused lenses. Those are the three methods actually attempted here.

Large aggregate ledgers can be connector-truncated; exact-ID, claim, report and source searches were used to recover the relevant continuity. I do not infer inaccessible/deleted/non-master history is empty.

The exposed task-control surface still provides prompt/title, timing/schedule fields and enabled state but **no binding model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. This invocation actually runs GPT-5.6 Sol; authenticated reasoning telemetry is unavailable, so reasoning is reported `UNVERIFIED`. The historical P26 `You cannot modify this task` event was authorization/context-specific; repository state records a later successful update from another authorized context. A future denial must be handled from the owning/authorized account, workspace, product/admin or API surface rather than by task duplication or access-control bypass. No support escalation is claimed.

## 2. Exact source status and bounded literature check — 2026-09-18 UTC

The Cambridge source page still states the diameter question explicitly. Its Theorem 6 proves that

`k >= log n + t' log log n sqrt(log n),  t' > 1/2`

implies connectivity with high probability, and in particular `k=floor(t log n)`, `t>1`, is connected whp. Immediately before/after the theorem the paper says that characterizing the diameter in the additional range of `k(n)` where connectivity now holds is an open problem.

I also reread the 2015 La–Kabkab paper, *A New Random Graph Model with Self-Optimizing Nodes: Connectivity and Diameter*, Internet Mathematics 11 (2015), 528–554, DOI `10.1080/15427951.2015.1022626`. Its Theorem 5.3 proves

`D(LK(n,k)) / (log n / log log n) -> 1 in probability`

only under `k=Theta(log n)` with `liminf k/log n > beta_*`, `beta_* ~= 2.4626`. Appendix F obtains this by sandwiching the bilateral graph between two Erdos–Renyi graphs in a regime where the lower sandwich is itself connected.

Fresh bounded searches on 2026-09-18 used the exact 2026 title plus `diameter`, `bilateral preference random graphs diameter`, `Dabirian Subramanian diameter`, and `LK(n,k) diameter`. They recovered the current Cambridge paper, author/publication metadata, and the 2015 predecessor but no later source-matching resolution. This is **bounded negative evidence only**; publication novelty is **UNVERIFIED**.

Access note: the 2015 PDF's parsed theorem/proof text was accessible. The web screenshot backend was also invoked for the relevant PDF pages as required, but returned a cache-miss error, so page-image inspection was unavailable in this invocation. No mathematical claim below depends on OCR or an unread image.

## 3. Frozen metric: no movement

The claim freezes

`S_exact = largest co-degree s >= 0 for which NM13-04 has a complete deterministic diameter classification for LK(n,n-1-s), uniformly over all feasible n in the stated scope.`

Earlier runs proved `S_exact=3`. This run does not change that metric or disguise progress by substituting a new scalar.

**Before:** `S_exact=3`.  
**After:** `S_exact=3`.  
**Frozen-metric movement:** none.  
**Consecutive unchanged runs since the last frozen-metric movement:** `2`.  
**Stuck recoveries used:** `0`.

The theorem below is source-relevant asymptotic progress, but it does not expand the deterministic `s=1,2,3` classification and therefore does not move the frozen scalar.

---

## 4. Recovered robust sandwich from the previous run

Use the equivalent exponential-value representation: every edge receives an iid `Exp(1)` value and each vertex proposes the `k` largest incident values. Let `U_{i,k}` be the kth largest incident value at vertex `i`.

For any fixed `T>1`, uniformly for

`log n <= k <= T log n`,

the previous run proved the event

`A_n' = { L_- <= U_{i,k} <= L_+ for every vertex i }`

has probability tending to one, where

`L_+ = log((n-1)/k)+2`,
`L_- = log((n-1)/k)-3/2`.

Define two threshold graphs from the **same raw iid edge values**:

`G_+ = {ij : V_ij > L_+}`,
`G_- = {ij : V_ij > L_-}`.

Marginally,

`G_+ ~ G(n,p_+)`,   `p_+ = e^{-2} k/(n-1)`,
`G_- ~ G(n,p_-)`,   `p_- = e^{3/2} k/(n-1)`.

On `A_n'` there is the deterministic edge-set sandwich

`G_+ subset LK(n,k) subset G_-`.   (4.1)

The important point for this run is that both threshold graphs have mean degree `Theta(log n)`, even though the lower graph `G_+` need not be connected near `k=log n`.

---

## 5. Method #3 — PROVE SOMETHING STRONGER: try to sharpen the full diameter to the La–Kabkab scale

The natural first attempt was to replace the preceding `O(log n)` diameter theorem by the sharp

`D(LK(n,k)) = (1+o_P(1)) log n/log log n`

through the same sandwich (4.1).

That direct route **fails for a precise reason**. At the bottom of the new band, say `k=(1+o(1))log n`, the definite-edge graph has

`(n-1)p_+ = e^{-2}(1+o(1))log n`.

Thus its expected number of isolated vertices is

`n(1-p_+)^{n-1} = n^{1-e^{-2}+o(1)}`,

which diverges polynomially. The usual two-vertex covariance calculation gives

`P(u,v both isolated)/(P(u isolated)P(v isolated)) = (1-p_+)^{-1}=1+o(1)`,

so the second moment shows that `G_+` in fact has isolated vertices whp in this regime. Hence a theorem about the **diameter of a connected lower ER sandwich** cannot extend La–Kabkab's Appendix-F argument down to the new connectivity threshold.

This is not a counterexample to the source statement: those threshold-isolated vertices can have many additional edges in `LK(n,k)`. It is an obstruction to this particular all-vertices transfer. The failure says exactly where new information is needed: one must control how the exceptional vertices excluded by the definite ER core attach to that core.

Method #3 therefore did not close the full diameter problem.

---

## 6. Method #12 — FIND WHAT IS CONSERVED: the logarithmic branching scale survives both sides of the sandwich

Although connectivity of `G_+` is lost, the sandwich conserves the leading **typical-distance scale**. For both signs,

`mu_+ := (n-1)p_+ = e^{-2}k`,
`mu_- := (n-1)p_- = e^{3/2}k`.

Uniformly for `log n <= k <= T log n`,

`c log n <= mu_+ <= mu_- <= C log n`

for constants `0<c<C<infinity` depending only on `T`. Consequently

`log mu_+ = log log n + O(1)`,
`log mu_- = log log n + O(1)`.

So multiplying the edge density by either fixed sandwich constant changes `log(np)` only by `O(1)`, invisible to first order on the scale

`s_n := log n / log log n`.

That observation suggests that the correct object to transfer is not the maximum over all pairs but a typical pair. I prove the required ER statement self-containedly next instead of importing an average-distance theorem.

### Lemma P0457-ER-TYPICAL

Fix constants `0<c<C<infinity`. Let `H_n~G(n,p_n)` satisfy

`c log n <= (n-1)p_n <= C log n`.

Let `U_n,V_n` be a uniformly random ordered pair of distinct vertices, independent of the graph, and set graph distance to `infinity` when disconnected. Then

`d_H(U_n,V_n) / s_n -> 1 in probability`,   `s_n=log n/log log n`.   (6.1)

#### Proof: lower bound

It suffices by exchangeability to fix distinct vertices `u,v`. Let

`r_- = floor((1-epsilon)s_n)`.

The number of simple `u-v` paths of length `ell` is at most `n^{ell-1}`. Hence, by a union bound,

`P(d_H(u,v) <= r_-)`
` <= sum_{ell=1}^{r_-} n^{ell-1}p_n^ell`
` <= n^{-1} sum_{ell=1}^{r_-} (n p_n)^ell`.

Since `np_n=Theta(log n)`,

`(np_n)^{r_-}`
` = exp((1-epsilon+o(1)) (log n/log log n)(log log n+O(1)))`
` = n^{1-epsilon+o(1)}`.

The geometric sum contributes only an additional `n^{o(1)}` factor. Therefore

`P(d_H(u,v) <= (1-epsilon)s_n) <= n^{-epsilon+o(1)} -> 0`.   (6.2)

#### Proof: upper bound by two reserved-pool BFS explorations

Fix `epsilon>0` and choose `eta>0` so small that `4eta<epsilon`. Conditional on the chosen roots `u,v`, partition the remaining `n-2` vertices, independently of the graph, into two reserved pools `A,B` of sizes at least `n/4` and an unused remainder.

Explore from `u` using only edges whose non-root vertices lie in `A`; independently in the sense of disjoint edge exposure, explore from `v` using only vertices in `B`. Stop either exploration after it discovers

`m_n = ceil(n^{1/2+eta})`

vertices in its reserved pool.

Suppose one exploration currently has frontier size `f>=1`, has exposed at most `m_n` pool vertices, and has not yet stopped. For an unused pool vertex `x`, the event that `x` has at least one edge to the current frontier has probability

`q_f = 1-(1-p_n)^f`.

Throughout the stopped exploration,

`p_n f <= p_n m_n = O(log n * n^{-1/2+eta}) = o(1)`,

so for all sufficiently large `n`, `q_f >= p_n f/2`. At least `n/5` pool vertices remain unused. Conditional on the exploration history, the number `Y` of newly discovered pool vertices therefore dominates a binomial variable of mean at least

`(n/5)(p_n f/2) >= (mu_n/12) f`,

where `mu_n=(n-1)p_n` and the harmless constant 12 absorbs `n/(n-1)`. A standard Chernoff bound gives a numerical constant `a>0` such that

`P(Y < (mu_n/24)f | history) <= exp(-a mu_n f)`.   (6.3)

Since `mu_n >= c log n`, summing (6.3) over the `O(s_n)` generations needed below gives `o(1)` even using the worst case `f=1`. Thus, with probability `1-o(1)`, each frontier grows by a factor at least `mu_n/24` until `m_n` vertices have been reached.

The required number of generations is consequently at most

`r_+ = log(m_n)/log(mu_n/24) + O(1)`
`    = (1/2+eta+o(1)) log n/log log n`.   (6.4)

The two searches have exposed no edges between `A` and `B`. Once they each contain `m_n` discovered vertices, all `m_n^2` cross-pool edges between selected discovered sets remain fresh iid Bernoulli(`p_n`). Therefore

`P(no cross edge) <= exp(-p_n m_n^2)`
` <= exp(-c' log n * n^{2eta}) -> 0`   (6.5)

for some `c'>0`.

On the complementary event, concatenating the two BFS paths with one cross edge gives

`d_H(u,v) <= 2r_+ + 1`
` <= (1+4eta+o(1))s_n`
` < (1+epsilon)s_n`

for all sufficiently large `n`. Combined with (6.2), this proves (6.1). QED.

The proof is uniform over every `p_n` in the displayed logarithmic band.

---

## 7. Method #27 — SWAP THE QUANTIFIERS: sharp distance for a random pair, hence almost every pair

The source asks for a maximum over **all** vertex pairs. The ER obstruction above says the definite-edge sandwich has too many exceptional vertices for that quantifier. Swap the quantifier to a uniformly random pair and the same coupling becomes sharp.

### Theorem P0457-BULK-DISTANCE

Fix `T>1`. Let `k=k_n` be any integer sequence satisfying

`log n <= k <= T log n`,

and let `G_n=LK(n,k)` in the exact bilateral-preference model. Let `U_n,V_n` be a uniformly random ordered pair of distinct vertices, independent of the edge values. Then

`d_{G_n}(U_n,V_n) / (log n/log log n) -> 1 in probability`.   (7.1)

Equivalently, for every fixed `epsilon>0`, if

`Q_n(epsilon)`
` = (1/binom(n,2)) # { {u,v}: | d_{G_n}(u,v)/s_n - 1 | > epsilon }`,

with disconnected pairs counted as bad, then

`Q_n(epsilon) -> 0 in probability`.   (7.2)

In particular, throughout the source's connected band

`k >= log n + t' log log n sqrt(log n),  t'>1/2`,  `k<=T log n`,

with high probability **all but `o(n^2)` unordered vertex pairs** have distance

`(1+o(1)) log n/log log n`.

#### Proof

Let `A_n'` and `G_+,G_-` be the recovered cutoff event and ER graphs from Section 4. We have `P(A_n')->1` and, on `A_n'`,

`G_+ subset G_n subset G_-`.

Both ER graphs satisfy the hypotheses of Lemma P0457-ER-TYPICAL because

`(n-1)p_+=e^{-2}k`,
`(n-1)p_-=e^{3/2}k`,

and `k` lies between `log n` and `T log n`.

For the upper tail, on `A_n'`, every `G_+` path is a `G_n` path. Therefore

`P(d_{G_n}(U,V) > (1+epsilon)s_n)`
` <= P((A_n')^c) + P(d_{G_+}(U,V) > (1+epsilon)s_n)`
` -> 0`.

This also proves that a random pair is connected in `G_n` with probability tending to one even if the particular `k_n` sequence lies inside the unresolved connectivity window.

For the lower tail, on `A_n'`, adding edges from `G_n` to `G_-` can only decrease graph distances. Hence

`P(d_{G_n}(U,V) < (1-epsilon)s_n)`
` <= P((A_n')^c) + P(d_{G_-}(U,V) < (1-epsilon)s_n)`
` -> 0`.

This proves (7.1).

For (7.2), conditional on a realized graph `G_n`, `Q_n(epsilon)` is exactly the probability that an independent uniformly sampled unordered pair is bad. Hence

`E[Q_n(epsilon)] = P(random pair is bad) -> 0`.

Markov's inequality implies `Q_n(epsilon)->0` in probability. QED.

### What this says about the source problem

This theorem transfers the **sharp La–Kabkab distance scale** all the way down to the new logarithmic connectivity range, but only for the bulk of pairs. It isolates the diameter problem to a genuinely exceptional set:

> any excess in the diameter above `(1+o(1)) log n/log log n` must be caused by `o(n^2)` exceptional pairs, equivalently by a vanishing fraction of vertices/pairs not governed by the threshold ER core.

That is a sharper remaining obligation than the previous global `O(log n)` statement. It is not a source closure because a single exceptional vertex can still determine the diameter.

---

## 8. Method outcomes and why no checker was built

### #3 PROVE SOMETHING STRONGER

Attempted the full sharp diameter transfer. **Failed on a precise obstruction:** the definite ER subgraph has polynomially many isolated vertices near `k~log n`, so the old connected-ER sandwich route cannot cover all vertices.

### #12 FIND WHAT IS CONSERVED

**Succeeded as a route selector.** Both sides of the robust threshold sandwich retain mean degree `Theta(log n)`, so the leading pair-distance scale `log n/log log n` is invariant under the fixed multiplicative density losses/gains in the sandwich.

### #27 SWAP THE QUANTIFIERS

**Succeeded mathematically.** Replacing `max_{u,v}` by a uniformly random pair removes the exceptional-vertex obstruction and yields Theorem P0457-BULK-DISTANCE. A second averaging step upgrades it to `1-o(1)` of all pairs in a typical graph.

No finite enumeration or finite certificate is claimed in this run, so creating an exact-arithmetic checker would be bookkeeping without a finite core. The new theorem is proved on the page. No self-check is mislabeled as an independent audit.

## 9. Remaining obligation and next route

P0457 remains **OPEN / NM13-04 PARTIAL**. The source-level missing step is no longer the distance scale for a typical pair; it is control of the **exceptional vertices** strongly enough to pass from bulk distance to diameter.

A useful exact blocker is:

`max_v d(v, Core_+) = o(log n/log log n) ?`,

where `Core_+` denotes the giant/metric core of the definite threshold graph `G_+`. Proving even

`max_v d_{LK}(v,Core_+) = O(1)`

would combine with the ER-core distance scale to settle the source diameter asymptotic in the band treated here. The previous expansion theorem only gives an `O(log n)` route for arbitrary exceptional vertices, which is too coarse.

Next untried section-B lenses: **#4 / #20 / #30**.

- #4 PROVE SOMETHING WEAKER, COMPLETELY: prove a uniform attachment theorem for all but `n^rho` exceptional vertices, with explicit `rho<1`, before attempting all vertices.
- #20 FIND WHY THE ALGORITHM FAILS: run deferred-decision BFS from a worst exceptional vertex and identify the exact conditional event that prevents `Theta(log n)` first-generation growth.
- #30 ONE SCALE/DIRECTION AT A TIME: stratify vertices by their kth order statistic / threshold defect and prove attachment one defect scale at a time, summing the failure probabilities.

If the frozen metric remains unchanged for one more run, the three-unchanged-run stuck trigger will apply to the following invocation; this run itself is only the second unchanged run.

## 10. Audit and closure status

- P26 independent audit: **NOT REQUESTED / NOT PASSED**.
- NM13-05 secondary audit: **NOT REQUESTED / NOT PASSED**.
- Self-check: none needed for a finite core; theorem proof is above.
- Parent source status: **OPEN**.
- Track result: **PARTIAL**.
- Publication novelty: **UNVERIFIED**.

No paper folder is created because the exact source diameter question is not closed and the required two independent audits do not exist.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  status: PARTIAL
  source_id: P0457
  claim_id: P0457
  canonical_dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  source_target: "diameter of LK(n,k) in the additional near-threshold connectivity range of Dabirian--Subramanian Theorem 6"
  frozen_metric:
    name: S_exact
    definition: "largest co-degree s with complete deterministic diameter classification for LK(n,n-1-s) over the stated feasible range"
    before: 3
    after: 3
    movement: false
  mathematical_progress:
    theorem_id: P0457-BULK-DISTANCE
    statement: "uniformly for log n <= k <= T log n, a random vertex-pair distance in LK(n,k), and whp all but o(n^2) pair distances, are (1+o(1)) log n/log log n"
    source_relevance: "extends the sharp 2015 distance scale to the bulk of pairs throughout the newly studied logarithmic band; diameter remains open because exceptional pairs can dominate"
  section_B_methods:
    attempted: [3, 12, 27]
    outcomes:
      3: "full sharp-diameter ER-sandwich transfer blocked by polynomially many isolates in the definite lower ER graph near k~log n"
      12: "identified invariant logarithmic effective branching scale on both sides of the threshold sandwich"
      27: "proved sharp random-pair distance and 1-o(1) pair-fraction theorem"
    next: [4, 20, 30]
  unchanged_runs_since_metric_movement: 2
  stuck_recoveries_used: 0
  remaining_obligation: "control exceptional vertices' distance to the definite ER metric core on o(log n/log log n), ideally O(1), to upgrade bulk distance to diameter"
  literature_check:
    date_utc: 2026-09-18
    source_rechecked: true
    predecessor_2015_rechecked: true
    exact_title_and_diameter_queries: true
    later_source_matching_resolution_found: false
    negative_search_is_novelty_certificate: false
    publication_novelty: UNVERIFIED
    pdf_visual_access: "screenshot backend cache miss; parsed PDF text accessible"
  audits:
    P26: NOT_REQUESTED_NOT_PASSED
    NM13-05: NOT_REQUESTED_NOT_PASSED
  shared_root_edits: NONE
  peer_track_edits: NONE
```

No email/Gmail, Drive, public posting, paid compute, permission change, unreviewed external script, workflow execution, shared-root write, peer-track write, or additional schedule creation/modification was performed.

**End of immutable run report.**
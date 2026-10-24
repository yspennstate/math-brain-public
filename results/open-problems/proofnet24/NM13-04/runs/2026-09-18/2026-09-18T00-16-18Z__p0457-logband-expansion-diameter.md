Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `S_exact = 3 -> 3`; methods #9, #11, #28 genuinely attempted.**

# NM13-04 / P0457 — a source-range logarithmic diameter bound from sparse-boundary certificates

Status: **OPEN / PARTIAL** relative to the source diameter-characterization problem.

Exclusive claim remains `operations/claims/P0457.md` (owner NM13-04, namespace `proofnet24/NM13-04/`). No conflicting claim, handoff, release, retirement, or source-level closure was recovered this run.

Source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Frozen source model: iid continuous edge values on `K_n`; every vertex proposes its `k` highest-valued incident edges (equivalently the `k` lowest costs after an order-reversing continuous transform), and `LK(n,k)` retains an edge exactly when both endpoints propose it.

Frozen metric, unchanged from admission:

`S_exact = largest co-degree s >= 0 for which this track has a complete deterministic diameter classification for LK(n,n-1-s), valid for every n in the stated range.`

Before this run: `S_exact = 3`.
After this run: `S_exact = 3`.

The run nevertheless proves a source-relevant asymptotic theorem in the actual near-logarithmic window. I do **not** rename that theorem as the frozen metric merely because the deterministic metric is already on a different axis.

---

## 1. Continuity, ownership, policy, and accessible history

This is the fourth NM13-04 research run on the already admitted P0457 target; intake was **not** reopened.

I reread/recovered the controlling policy and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0457.md`;
- the three preceding NM13-04 reports, newest being `2026-09-17T23-19-15Z__p0457-s3-support-sharpness.md`;
- newest accessible neighboring NM13-03 and NM13-05 reports;
- exact-ID/dedup intake/ranking history and the recovered prior P0457 attempt history.

Canonical identity remains:

- ID `P0457`;
- dedup key `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256 `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue `3 mod 13`, the NM13-04 selection shard.

The campaign catalog still records P0457 as unsolved. The pre-NM13 campaign attempt supplied only a maximum-degree/Moore-volume lower bound and explicitly left the upper-diameter behavior unresolved. The canonical claim remains the only recovered live ownership record for this exact identity.

Large root/campaign files are connector-truncated views rather than guaranteed byte-for-byte dumps. Exact claim, own reports, exact-ID/dedup history, and the source statements used below were read directly or recovered by exact search. I do not treat inaccessible or truncated history as evidence that it is empty.

The task-control surface exposed to this invocation still provides task prompt/title, schedule or relative-start data, timing mode, and enabled state but **no binding model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Changing that requires an authorized product/scheduler/API surface that actually exposes model and reasoning fields. Repository history records an older P26 `You cannot modify this task` response and later successful P26 edits in another authorized context; a fresh refusal must therefore be handled through the owning account/workspace or another authorized product/admin/support surface, not by task duplication or permission bypass. No support escalation is claimed here.

---

## 2. Source and fresh literature check — 2026-09-18 UTC

I checked the current Cambridge source page again. Its Open Problems section still says that La–Kabkab's earlier proof methodology determined diameter in their older connectivity range and explicitly asks to characterize diameter in the **additional range of `k(n)` supplied by Dabirian–Subramanian Theorem 6**.

The source's relevant proved inputs are:

1. **Theorem 4.** For every fixed nonnegative integer `kappa`, if

   `k >= log n + t' log log n sqrt(log n)` with fixed `t' > 1/2`,

   then the probability of any vertex of degree at most `kappa` tends to zero.

2. **Theorem 6.** The same lower range is connected with high probability; in particular `k=floor(t log n)`, fixed `t>1`, is connected with high probability.

The source also recalls the older La–Kabkab threshold `beta_* ~= 2.4626`: the 2015 paper proved connectivity for `k>beta_* log n`, and in that older range proved diameter close to `log n / log log n`. The 2015 paper states its diameter question as Q2 and its result F3 exactly in that `k>beta_* log n` regime.

Fresh bounded searches on 2026-09-18 included:

- exact 2026 paper title + `diameter`;
- `Dabirian Subramanian bilateral preference diameter`;
- `LK(n,k) diameter bilateral preference`;
- later-2026 author/title queries;
- the 2015 La–Kabkab title and its diameter theorem.

They recovered the current Cambridge source, its arXiv predecessor, and the 2015 La–Kabkab paper, but no later source-matching resolution of the open diameter question. This is bounded negative evidence only: **publication novelty remains UNVERIFIED**.

One deliberate methodological choice below is important. Instead of importing the source's particular order-statistic window, I prove a coarser but elementary simultaneous cutoff bracket directly by binomial Chernoff bounds. That makes the new argument self-contained apart from the source's Theorem 4 and avoids needing a tail-uniform normal approximation.

---

## 3. Recovered deterministic baseline and why this run changes category

The preceding runs proved for `k=n-1-s`:

- the complement of `LK(n,n-1-s)` is `s`-degenerate;
- every connected realization has diameter at most `s+2`;
- that bound is exactly sharp for every feasible `(n,s)`;
- exact deterministic diameter classifications are complete for `s=1,2,3`.

Thus the frozen metric is `S_exact=3`.

The all-`s` sharpness theorem also showed why extending `s=4,5,...` mechanically is not the right next move: in the source window `k=Theta(log n)`, `s=n-1-k` is linear in `n`, and the exact worst-case deterministic diameter is correspondingly linear. The source asks for the *random* graph's typical diameter. This run therefore follows the previous report's required route change to methods #9/#11/#28.

---

## 4. Method #9 — RANDOMIZE: a robust simultaneous cutoff bracket

Use the equivalent exponential-value representation from La–Kabkab: the `binom(n,2)` edge values are iid `Exp(1)`, and every vertex proposes the `k` largest incident values.

Let `m=n-1`, and let `U_{i,k}` be the kth largest value among the `m` edges incident to vertex `i`.

Assume for now only

`log n <= k <= T log n`

for some fixed `T>1`. Define

`L_+ = log(m/k) + 2`,
`L_- = log(m/k) - 3/2`.

### Lemma P0457-CUTOFF-ROBUST

Uniformly over all integer sequences `k=k_n` with `log n <= k <= T log n`,

`P( for every i,  L_- <= U_{i,k} <= L_+ ) -> 1`.

#### Proof

Fix a vertex `i`.

For the upper cutoff, let `X_i^+` be the number of its incident edge values exceeding `L_+`. Then

`X_i^+ ~ Bin(m, q_+)`,
`q_+ = exp(-L_+) = k e^{-2}/m`,
`mu_+ = E X_i^+ = k e^{-2}`.

If `U_{i,k}>L_+`, then `X_i^+ >= k`. The standard exponential Chernoff bound gives

`P(X_i^+ >= k) <= exp[-k log(k/mu_+) + k - mu_+]`

`= exp[-k(1+e^{-2})]`.

Since `k>=log n`, a union bound over all `n` vertices gives

`P(exists i: U_{i,k}>L_+) <= n exp[-(1+e^{-2})k]`

`<= n^{-e^{-2}} -> 0`.

For the lower cutoff, let `X_i^-` count incident edge values exceeding `L_-`. Then

`X_i^- ~ Bin(m,q_-)`,
`q_- = k e^{3/2}/m`,
`mu_- = k e^{3/2}`

for all sufficiently large `n` (the displayed probability is then below one because `k=O(log n)`). If `U_{i,k}<L_-`, then `X_i^- <= k-1 <= k`. The lower-tail Chernoff bound yields

`P(X_i^- <= k) <= exp[-k(e^{3/2}-1-3/2)]`

`= exp[-k(e^{3/2}-5/2)]`.

Here `e^{3/2}-5/2 > 1`. Hence

`P(exists i: U_{i,k}<L_-)`

`<= n exp[-(e^{3/2}-5/2)k]`

`<= n^{1-(e^{3/2}-5/2)} -> 0`.

Combining the two union bounds proves the lemma. QED.

### Deterministic consequences on the cutoff event

Let `A_n'` denote the simultaneous bracket event from the lemma. On `A_n'`:

- every edge with value `>L_+` is **definitely present** in `LK(n,k)`, because it lies above the kth cutoff at both endpoints;
- every edge that is present in `LK(n,k)` must have value `>=L_-`.

Set

`p_+ = P(V_ij>L_+) = e^{-2} k/(n-1)`,
`p_- = P(V_ij>L_-) = e^{3/2} k/(n-1)`.

The first is a genuinely independent definite-edge probability; the second is only a necessary raw-value probability for a graph edge. Those two one-sided implications are exactly what the next method needs.

---

## 5. Method #11 — DUALIZE: sparse expansion has a finite tree-plus-cut witness

For a vertex set `S` in a graph `G`, write

`partial_G S = {v notin S : v has a G-neighbor in S}`

for its external vertex boundary.

A bad expansion event is global-looking. Its useful dual certificate is finite and explicit:

- a spanning tree witnessing that `G[S]` is connected;
- a small candidate boundary `B` containing `partial_G S`;
- the absence of every **definite** high-value edge from `S` to `V\(S union B)`.

The tree edges and the cut edges are disjoint sets of iid raw edge values, so their necessary raw-value conditions factor exactly.

Let

`x = e^{-2}`,
`alpha = x / (2(2+x))`,
`delta = x/4`,
`R = ceil(12/x) = ceil(12 e^2) = 89`.

Numerically,

`alpha ~= 0.0316894691665`,
`delta ~= 0.0338338208092`.

The choice of `alpha` is made so that

`x(1-alpha)/2 - alpha = delta = x/4 > 0`.

### Theorem P0457-LOG-BAND-EXPANSION

Fix `T>1`. For any integer sequence satisfying

`log n <= k_n <= T log n`,

with probability tending to one, every connected vertex set `S` of `G_n=LK(n,k_n)` satisfying

`R <= |S| <= n/2`

has

`|partial_{G_n} S| > alpha |S|`.

#### Proof

Fix `r` with `R<=r<=n/2`. Suppose a connected set `S`, `|S|=r`, has boundary `B=partial_G S` of size `j<=alpha r`.

On `A_n'`, choose any spanning tree `T_S` of `G[S]`. Every one of its `r-1` edges has raw value at least `L_-`. Also, every edge joining `S` to

`C = V \ (S union B)`

has raw value at most `L_+`: a value above `L_+` would be a definite graph edge and would create a neighbor outside `B`.

For fixed labeled `S`, fixed `B`, and fixed spanning tree, these are conditions on disjoint raw edges. Therefore their probability is at most

`p_-^(r-1) (1-p_+)^(r(n-r-j))`.

There are at most

`binom(n,r) * r^(r-2) * sum_{0<=j<=alpha r} binom(n-r,j)`

such choices. We now bound the factors uniformly.

For sufficiently large `n`, because `k<=T log n`,

`p_- <= 2 e^(3/2) T log n / n`.

Using `binom(n,r) <= (en/r)^r`, Cayley's `r^(r-2)` tree count, and `r>=2`, there is a finite constant `C_T` such that

`binom(n,r) r^(r-2) p_-^(r-1) <= n (C_T log n)^r`.

Also

`sum_{0<=j<=alpha r} binom(n-r,j) <= (alpha r+1) n^(alpha r)`.

Because `r<=n/2` and `j<=alpha r`,

`n-r-j >= n(1-alpha)/2`.

Hence

`(1-p_+)^(r(n-r-j))`

`<= exp[-p_+ r n(1-alpha)/2]`.

Since `k>=log n`,

`p_+ n = e^{-2} k n/(n-1) >= x log n`,

so

`(1-p_+)^(r(n-r-j)) <= n^{-x(1-alpha)r/2}`.

Multiplying the bounds and using the defining identity for `delta`,

`P(A_n' and exists bad connected S of size r)`

`<= n (alpha r+1) (C_T log n)^r n^{-delta r}`.

Put

`z_n = C_T log n * n^{-delta}`.

Then `z_n -> 0`, and summing over all `R<=r<=n/2` gives

`P(A_n' and exists any bad S)`

`<= n sum_{r=R}^{n/2} (alpha r+1) z_n^r`.

For all large `n`, `z_n<1/2`; since `R` is fixed, the right side is

`O_T(n z_n^R)`

`= O_T((log n)^R n^{1-delta R})`.

By `R=ceil(12/x)` and `delta=x/4`, we have `delta R>=3`, so this tends to zero.

Finally `P((A_n')^c)->0` by P0457-CUTOFF-ROBUST. Therefore the claimed expansion property holds with high probability. QED.

### Why this is a real dualization rather than another component bound

The source's Theorem 5 is the special boundary-zero situation `B=empty`: a component has no outgoing graph edge. Here the witness allows a boundary of **linear size in `|S|`** and still gets a summable union bound. This is the precise extra ingredient needed to turn connectivity estimates into a diameter estimate.

---

## 6. Method #28 — REPLACE FOR ALL WITH TYPICAL: diameter throughout the new logarithmic band

We now combine the expansion theorem with the source's fixed-`kappa` minimum-degree theorem.

### Theorem P0457-LOG-BAND-DIAM

Fix constants `T>1` and `t0>1/2`. Let `k_n` be any integer sequence satisfying, for all sufficiently large `n`,

`log n + t0 log log n sqrt(log n) <= k_n <= T log n`.

Let `G_n=LK(n,k_n)`. With

`alpha = e^{-2}/(2(2+e^{-2}))`,
`R=89`,

we have, with probability tending to one,

`diam(G_n) <= 2 L_n`,

where

`L_n = 1 + ceil( log( n / (2(R+2)) ) / log(1+alpha) )`

for all sufficiently large `n`.

In particular,

`diam(G_n) <= (C_* + o(1)) log n` with high probability,

where

`C_* = 2/log(1+alpha) ~= 64.1072492558`.

This includes the near-threshold sequences

`k_n = ceil(log n + t0 log log n sqrt(log n))`,

and, in particular, every fixed `k=floor(t log n)` with `t>1` (taking any `T>t`). Thus it supplies a rigorous diameter upper bound inside the additional connectivity range posed by the source, including the fixed-`t` interval below the older `beta_* ~= 2.4626` regime.

#### Proof

P0457-LOG-BAND-EXPANSION gives, with probability tending to one, the simultaneous expansion statement

`|partial_G S| > alpha |S|`

for every connected `S` with `R<=|S|<=n/2`.

The source's Theorem 4 applies in the assumed lower range. Taking its fixed integer `kappa=R`, with probability tending to one every vertex has degree `>R`.

Work on the intersection of those two events. Fix any vertex `v` and let `B_m(v)` be its closed radius-`m` ball. Since `deg(v)>R`,

`|B_1(v)| >= R+2`.

Each ball is connected. Whenever `|B_m(v)|<=n/2`, the expansion theorem therefore gives

`|B_{m+1}(v)|`
`= |B_m(v)| + |partial_G B_m(v)|`
`> (1+alpha)|B_m(v)|`.

By the definition of `L_n`, repeated growth implies

`|B_{L_n}(v)| > n/2`

for **every** vertex `v`.

Now take arbitrary vertices `u,v`. Two subsets of an `n`-vertex set, each of cardinality strictly greater than `n/2`, must intersect. Hence

`B_{L_n}(u) intersect B_{L_n}(v) != empty`,

so `d_G(u,v)<=2L_n`. Maximizing over `u,v` proves the diameter bound. The asymptotic constant follows immediately from the formula for `L_n`. QED.

---

## 7. What moved mathematically, and what did not

### New source-relevant theorem

For the full logarithmic part of the source's new connected range

`log n + t0 log log n sqrt(log n) <= k_n <= T log n`,

there is now a rigorous high-probability `O(log n)` diameter upper bound, with an explicit universal expansion factor and explicit diameter constant.

This is materially different from the earlier deterministic work:

- the preceding sharp worst-case theorem says realizable graphs can have diameter `n-k+1`, which is linear here;
- the new theorem shows those bad realizations are atypical enough that the random source graph has logarithmic diameter throughout this band.

It also genuinely enters the interval `1<t<=2.4626` for fixed `k=t log n`, where the 2015 embedded-connected-ER argument did not provide its diameter theorem.

### What remains open

The source asks to **characterize** diameter in its added connectivity range. The 2015 result suggests the natural scale `log n / log log n` in its older range. This run proves only `O(log n)` in the wider range. It does not give:

- the sharp order `Theta(log n/log log n)` near threshold;
- a matching lower bound beyond the generic maximum-degree/Moore bound already in campaign history;
- a limiting constant or distribution;
- the full Theorem-6 range when `k/log n` is unbounded (the theorem here freezes an arbitrary constant upper multiple `T`).

Therefore the parent source remains **OPEN / PARTIAL**, not PROVED.

### Frozen metric discipline

The owner's frozen metric remains the deterministic classification cutoff `S_exact`. This run deliberately did not extend `s=4` mechanically, so

`S_exact: 3 -> 3`.

This is the first consecutive unchanged frozen-metric run after the previous movement. It is reported honestly as **no frozen-metric movement**, despite the new source-range theorem.

---

## 8. Section-B method ledger

### #9 — RANDOMIZE

**Succeeded.** Replaced arbitrary realizable preference profiles by iid exponential raw edge values and proved a new robust simultaneous cutoff bracket directly by elementary binomial Chernoff bounds. This bracket works uniformly for `log n <= k <= T log n` and is enough to identify independent definite edges and necessary possible edges.

### #11 — DUALIZE

**Succeeded.** A connected set with small external boundary was converted to a finite certificate: one internal spanning tree plus one large cut with no definite edges. Exact raw-edge independence then yields a summable union bound. This strictly generalizes the source's boundary-zero/component counting mechanism to positive linear boundary.

### #28 — REPLACE FOR ALL WITH TYPICAL

**Succeeded.** Combined the sparse-boundary theorem with the source's fixed-`kappa` minimum-degree theorem to obtain a simultaneous BFS expansion and a high-probability logarithmic diameter bound over the new logarithmic connectivity band.

These methods are new on this target and do not repeat the previous triple `#18/#24/#30`.

---

## 9. Verification standard and artifacts

The new claims are analytic theorem-sized statements; their full proofs are written above. There is no finite exhaustive claim whose validity depends on a computational certificate, so I did **not** manufacture a checker artifact merely to create a receipt.

No P26 or NM13-05 independent audit is counted. No paper folder is created because the source problem remains open.

The numerical values `R=89`, `alpha~=0.0316894691665`, and `C_*~=64.1072492558` are convenience evaluations of explicit closed forms; no theorem depends on floating-point rounding.

---

## 10. Counters

- frozen metric before: `S_exact=3`;
- frozen metric after: `S_exact=3`;
- frozen-metric movement: **no**;
- unchanged-run counter: `1`;
- stuck-recovery episodes used: `0`;
- source status: `OPEN`;
- track status: `PARTIAL`;
- closure audits: `0/2`;
- self-check artifacts this run: none needed;
- source claim: unchanged `operations/claims/P0457.md`.

---

## 11. Next mathematical attack

Do not repeat `#9/#11/#28` next run.

The obstruction is now quantitative and clean: the sparse-boundary count pays `n^{|B|}`, so the present certificate can only force a **constant** expansion factor. Reaching the expected `log n / log log n` diameter scale requires avoiding the entropy cost of freely choosing every boundary vertex.

Suggested next unused triple:

- **#3 PROVE SOMETHING STRONGER:** try to prove a multi-generation statement in which each BFS layer exposes `Theta(k)` new proposals per frontier vertex before collisions, rather than merely a constant vertex-boundary factor;
- **#12 FIND WHAT IS CONSERVED:** track the number of as-yet-unexposed high-score half-edges/proposals under deferred decisions; a conserved conditional-uniformity statement may prevent paying `n^{|B|}` for the boundary;
- **#27 SWAP THE QUANTIFIERS:** instead of union-bounding over all candidate boundary sets first, expose a fixed BFS exploration and prove that *for every step along that random exploration* its next layer is large with summable conditional failure probability.

A concrete milestone is a source-valid theorem of the form

`|B_{m+1}(v)| >= c log(n)/loglog(n) * |B_m(v)|`

through the pre-collision regime, with a displayed conditional error whose sum over vertices and generations is `o(1)`. If that route cannot beat constant expansion, record the obstruction rather than filing more certificates for the same `O(log n)` bound.

---

## 12. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  target: P0457
  canonical_claim: operations/claims/P0457.md
  canonical_dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  source: Dabirian-Subramanian bilateral preference diameter open problem
  status: PARTIAL
  source_status: OPEN
  frozen_metric: S_exact
  metric_definition: largest co-degree s with a complete deterministic diameter classification for LK(n,n-1-s)
  metric_before: 3
  metric_after: 3
  movement: false
  methods_actual: [9, 11, 28]
  method_outcomes:
    9: proved simultaneous Chernoff cutoff bracket for all log n <= k <= T log n
    11: proved linear external-boundary expansion via spanning-tree plus definite-cut certificates
    28: proved explicit whp O(log n) diameter throughout the source logarithmic Theorem-6 band
  substantive_claims:
    - P0457-CUTOFF-ROBUST
    - P0457-LOG-BAND-EXPANSION
    - P0457-LOG-BAND-DIAM
  source_range_theorem:
    assumptions: fixed T>1 and t0>1/2; log n+t0 loglog n sqrt(log n) <= k_n <= T log n
    alpha: e^-2/(2*(2+e^-2))
    R: 89
    diameter_bound: 2*(1+ceil(log(n/(2*(R+2)))/log(1+alpha)))
    asymptotic_constant: 2/log(1+alpha) ~= 64.1072492558
  exact_checker: NOT_APPLICABLE_ANALYTIC_THEOREM
  unchanged_runs: 1
  stuck_recoveries_used: 0
  p26_audit: NOT_REQUESTED_NOT_PASSED
  secondary_audit_partner: NM13-05
  secondary_audit: NOT_REQUESTED_NOT_PASSED
  literature_check_date_utc: 2026-09-18
  literature_scope: current Cambridge source; exact-title/author/diameter queries; 2015 La-Kabkab source; later-2026 searches
  literature_result: no later source-matching diameter resolution recovered in bounded search; novelty unverified
  next_methods: [3, 12, 27]
  next_step: replace arbitrary boundary-set entropy by deferred-decision BFS exposure to seek log n/loglog n scale
```

END OF IMMUTABLE REPORT
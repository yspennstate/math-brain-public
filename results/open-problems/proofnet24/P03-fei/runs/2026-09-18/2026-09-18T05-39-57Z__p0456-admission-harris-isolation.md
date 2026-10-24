Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 — HARD OUTSIDE successor admission and exact Harris isolation lower bound

**ADMISSION + NO RESEARCH-METRIC MOVEMENT.** The post-D0043 successor state moved from `UNMEASURED` to a source-supported literature baseline only: `c_LK^cert = 1/2`. The first P0456 mathematical attack leaves the frozen research metric **`1/2 -> 1/2`**, so P0456 unchanged-run count is **1**. Establishing the baseline is KNOWN/source reconciliation, not P03 theorem movement.

Section-B methods used this run: **B2 ATTACK THE NEGATION FIRST; B11 DUALIZE; B30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

Outside source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (June 2026), 552–579, published online 18 December 2025, Section 1.1 **Open problems**.

---

## 1. Lawful rotation and repository continuity

D0043 was not reopened. Its final report remains

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T04-32-31Z__d0043-final-recovery-nonhomogeneous-schur-handoff.md`

at creation commit `8b3ec8816f169d9d999ab60b08d0fe7bca43c6ea`, and its immutable handoff remains

`proofnet24/P03-fei/handoffs/2026-09-18T04-32-31Z__D0043-hard-handoff.md`

at creation commit `db1bcf0d0cd614e55f83c2d8979c1b83bba7614e`. Both D0043 recoveries are exhausted and Claims 264/266/268/270/272 remain historical retained results.

Before admitting a successor I reread or targeted-recovered the current repository controls required by the fleet protocol: root `README.md`; `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`; `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/FLEET_2026-09-16.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the newest P03 report/handoff; current claim/ownership material; the newest task-health/admission state; and the exact P0456 catalog/intake history. Large connector-rendered root/campaign surfaces are truncated when fetched wholesale, so this was not a byte-for-byte visual reread of every row; exact paths, target rows, ownership files, and source records were recovered directly. I do not claim more than that.

The current root queue still distinguishes sourced PENDING inventory from separately certified READY stock. The newer coordinator health pass did not produce a free HARD successor specifically for P03. Historical queue rows I0060 and I0062 are currently claimed; stale READY labels and missing claim files were not treated as dispatch permission. The admission cursor was therefore advanced into fresh canonical campaign candidates rather than recycling I0047 or another known hold.

Two fresh HARD-shaped unclaimed candidates were particularly visible in current admission screens: P0456 (the 2026 bilateral-preference connectivity window) and P0486 (the classical higher-dimensional RWRE directional zero-one problem). P0456 passed the stronger current-source gate: it is Tier-2 campaign inventory, its exact 2026 journal source is live and explicitly states the unresolved band, a bounded 2026-09-18 search found no later source-matching closure, its prior campaign attempt is explicitly non-closing, and a fresh ownership race found no canonical claim or competing P0456 owner. P0486 remained a classical HARD source with a less current status record and was not needed once the higher-priority recent P0456 source passed all gates.

I therefore created, create-only,

`operations/claims/P0456.md`

at creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`, and read it back at that exact commit. P03 now exclusively owns P0456.

---

## 2. Exact source statement and current-status screen

The source model `LK(n,k)` starts from the complete graph `K_n` with iid Uniform[0,1] edge weights. A vertex prefers its `k` incident edges of **lowest** weight; an edge is retained exactly when both endpoints prefer it.

Dabirian--Subramanian prove:

- disconnection with high probability when
  `k <= log n + t' log log n sqrt(log n)` for fixed `t' < -1/2`;
- connectivity with high probability when
  `k >= log n + t' log log n sqrt(log n)` for fixed `t' > 1/2`.

Section 1.1 then explicitly leaves open the entire intermediate band

`log n - (1/2) log log n sqrt(log n) <= k <= log n + (1/2) log log n sqrt(log n)`

and says that sharper or exact sufficient conditions could close the gap. The authors identify one concrete loss on the disconnectedness side: their convenient isolated-vertex sufficient event additionally demands a no-intersection condition among the preferred-edge sets of the top `k` neighbors.

Fresh dated status check, 2026-09-18: the current Cambridge article page still contains that open-problem statement. Searches for the exact title, `bilateral preference connectivity window`, and `LK(n,k)` plus 2026 terms recovered the source and adjacent work but no later theorem closing this exact band. This is bounded negative evidence only; it is not proof of worldwide openness or publication novelty.

Repository prior art is also explicit. The campaign's earlier P0456 attempt noticed that substituting the mean-degree expansion near `k=log n+a sqrt(log n)` suggests a shift, then correctly rejected that inference: isolation is governed by a far lower tail, not by the mean. No sharp window, limiting connectivity probability, or source-closing theorem was recorded. I preserve that failed heuristic as prior history and do not repay it.

---

## 3. Frozen metric

Define two source-scale frontiers. Let `c_-` be the infimum of `c>=0` such that for every fixed `epsilon>0` there is a rigorous source-valid theorem proving disconnection with high probability whenever

`k <= log n - (c+epsilon) log log n sqrt(log n)`.

Let `c_+` be the analogous infimum proving connectivity with high probability whenever

`k >= log n + (c+epsilon) log log n sqrt(log n)`.

Freeze

`c_LK^cert := max(c_-,c_+)`.

The source theorems establish the exact admission baseline

`c_LK^cert = 1/2`.

Lower is better. The source open problem seeks to shrink the unresolved normalized band; in particular, a complete threshold theorem at a smaller-order window would force this coefficient to zero. A one-vertex inequality, a theorem on only one side, or a restricted finite-n calculation is PARTIAL unless it changes the certified max frontier.

Before first mathematics: `c_LK^cert=1/2`.
After this run: `c_LK^cert=1/2`.
Movement: **none**.

---

## 4. Idea before calculation and attempted refutation

The source itself says its disconnectedness proof pays for an artificial no-intersection condition among the top neighbors' preferred-edge sets. The first attack therefore asked the opposite question:

> Could the exact neighbor-rejection events be adversely correlated, making that disjointness condition genuinely necessary?

Conditioning on the weights incident to one vertex reveals the answer: no. Every neighbor-rejection event is monotone in the **same** direction in the remaining independent edge weights. Shared edges create positive, not adverse, association. Harris/FKG therefore removes the no-intersection condition for a rigorous one-vertex lower bound.

That looked initially capable of improving the source window. The second part of the run tried to refute that optimism by inserting the improved one-vertex bound into the source's existing two-vertex/second-moment estimate. The attempt succeeds as a barrier diagnosis: the source's `1/2` coefficient is then controlled by a two-vertex overlap term of scale `sqrt(k) log k`, whereas the improved one-vertex correction is only scale `sqrt(k log k)`. Thus this attack improves a real source quantity but does **not** move `c_LK^cert`.

---

## 5. Main theorem

### `P03-P0456-HARRIS-ISOLATION-ROOT2-274 = PROVED / STRUCTURAL-PARTIAL / SOURCE-SHAPED / PUBLICATION-NOVELTY-UNVERIFIED`

Let `1 <= k <= n-2`, and let `I_v` be the event that a fixed vertex `v` is isolated in `LK(n,k)`. Define

`r_{n,k}(x) := P(Bin(n-2,x) >= k)`.

Let

`X_(1) < ... < X_(k)`

be the first `k` order statistics of `n-1` iid Uniform[0,1] variables. Then

**(a) Exact association lower bound**

`P(I_v) >= E[ product_{r=1}^k r_{n,k}(X_(r)) ]`.

Equivalently,

`P(I_v) >= ((n-1)!/(n-1-k)!) * integral_{0<x_1<...<x_k<1}
            (1-x_k)^(n-1-k) product_{r=1}^k r_{n,k}(x_r)
            dx_1...dx_k.`

**(b) One-threshold corollary**

For every `0<=t<=1`,

`P(I_v) >= (1-t)^(n-1) r_{n,k}(t)^k.`

**(c) Critical logarithmic asymptotic**

If `k -> infinity` with `k=O(log n)`, then

`liminf [log P(I_v)+k] / sqrt(k log k) >= -sqrt(2)`.

More explicitly, for every fixed `eta>0`,

`P(I_v) >= exp(-k-(sqrt(2)+eta)sqrt(k log k)+o(sqrt(k log k))).`

This improves the correction constant in the source's convenient one-vertex lower bound from the displayed `sqrt(6 k log k)` loss to arbitrarily close to `sqrt(2 k log k)`. It does **not** improve the source-certified connectivity-window coefficient by itself.

### Proof of (a)

Condition on the complete incident weight vector

`x_j = U_{vj}`, `j != v`.

Ties have probability zero. Let `S_v` be the `k` neighbors corresponding to the `k` smallest incident weights. Once this incident vector is fixed, the only remaining random variables are the edge weights not incident to `v`; they are still independent Uniform[0,1].

For each `j in S_v`, vertex `j` rejects edge `vj` exactly when at least `k` of its other `n-2` incident edges have smaller weight than `x_j`. Define

`R_j := { #{ell notin {v,j}: U_{j ell} < x_j} >= k }.`

Since `v` itself already rejects every edge to a vertex outside `S_v`, we have the exact identity

`I_v = intersection_{j in S_v} R_j.`

Regard the remaining independent edge weights as coordinates with the usual numerical order. Lowering any coordinate can only increase the count appearing in each relevant `R_j`; hence all `R_j` are coordinatewise decreasing events. Harris association for a product measure applies equally to a finite family of decreasing events, so

`P(I_v | (x_j)_{j != v})
 = P(intersection_{j in S_v} R_j | x)
 >= product_{j in S_v} P(R_j | x).`

The marginal law for a fixed `j` uses `n-2` independent Uniform[0,1] edges, hence

`P(R_j | x)=r_{n,k}(x_j)`.

Ordering the `k` selected incident weights yields

`P(I_v | x) >= product_{r=1}^k r_{n,k}(X_(r)).`

Integrating proves the expectation formula. The standard joint density of the first `k` order statistics among `n-1` uniforms is

`((n-1)!/(n-1-k)!)(1-x_k)^(n-1-k)`

on `0<x_1<...<x_k<1`, proving the integral formula.

### Proof of (b)

On the event that **all** `n-1` incident weights at `v` are at least `t`, each selected order statistic satisfies `X_(r)>=t`. Since `r_{n,k}` is nondecreasing,

`product_r r_{n,k}(X_(r)) >= r_{n,k}(t)^k.`

The event has probability `(1-t)^(n-1)`. Applying the conditional Harris bound from (a) on this event proves

`P(I_v) >= (1-t)^(n-1) r_{n,k}(t)^k.`

### Proof of (c)

Fix `eta>0` and put

`s=(sqrt(2)+eta)sqrt(k log k)`,

`t=(k+s)/(n-2)`.

For `k=O(log n)`, we have `t<1` for all sufficiently large `n`. If

`Y ~ Bin(n-2,t)`,

then its mean is `mu=k+s`. The standard binomial lower-tail Chernoff bound gives

`P(Y<k) <= exp(-s^2/(2 mu)).`

Because `s/k -> 0`,

`s^2/(2 mu)
 = (1+sqrt(2) eta + eta^2/2 + o(1)) log k.`

Hence for some fixed `delta=delta(eta)>0` and all sufficiently large `k`,

`q_k := P(Y<k) <= k^(-1-delta)`.

Therefore

`r_{n,k}(t)^k=(1-q_k)^k=exp(o(1)).`

Also, since `k=O(log n)`,

`(n-1)log(1-t)
 = -(k+s)+O((k+s)/n)+O((k+s)^2/n)
 = -k-s+o(s).`

Part (b) now gives

`log P(I_v)
 >= -k-(sqrt(2)+eta)sqrt(k log k)+o(sqrt(k log k)).`

Since `eta>0` was arbitrary, the stated liminf follows. QED.

### Scope and prior-art caution

Harris/FKG and Chernoff bounds are standard. The claim is the source-specific application to the exact bilateral-preference isolation event and the resulting `sqrt(2)` one-vertex correction. The source page contains no `FKG`, `Harris`, or positive-association discussion in the searchable text, but that search miss is not a publication-novelty certificate. The claim is therefore labeled `PUBLICATION-NOVELTY-UNVERIFIED`.

No exact finite checker is needed: this is an analytic theorem, not a finite certificate.

---

## 6. Why the frozen source metric does not move

The source's own displayed lower bound for the isolated-vertex probability loses `sqrt(6 k log k)` beyond the main `e^{-k}` scale. Claim 274 improves that one-vertex correction to `sqrt(2 k log k)` asymptotically.

However, the source second-moment argument also contains a two-vertex overlap error bounded at the scale

`exp(-log n - k + (1/2)sqrt(k) log k + O(sqrt(k))).`

Use the new lower bound in the denominator of the normalized pair error. For

`k = log n + t' log log n sqrt(log n)`,

the logarithm of the resulting sufficient upper bound is

`(t'+1/2+o(1)) sqrt(k) log k`,

because

`sqrt(k log k) = o(sqrt(k) log k).`

Thus the unchanged source pair estimate still makes this proof route close only for `t'<-1/2`. The Harris improvement removes the paper's one-vertex no-intersection loss, but the source-scale coefficient is now visibly controlled by the **pair-overlap/second-moment gate**, not by the one-vertex tail.

This is a proof-route diagnosis, not a theorem that `1/2` is optimal. A sharper treatment of two simultaneous isolated vertices could still improve `c_-`, and a different connectivity argument is needed on the positive side.

Exact remaining source obligation after this run:

1. derive a two-vertex isolation estimate whose error is `o(P(I_1)^2)` deeper into the central band, ideally without the `+(1/2)sqrt(k)log k` overlap loss;
2. separately sharpen the connectivity sufficient conditions on the positive side;
3. combine both into a rigorous improvement of `c_LK^cert` below `1/2`.

Recommended next mathematical triple: **B12 FIND WHAT IS CONSERVED; B25 COUNT THE SAME THING TWICE; B5 ADD A PARAMETER AND DIFFERENTIATE IN IT**. The next run should stay on the two-vertex overlap geometry, not repeat the one-vertex Harris estimate.

---

## 7. Directed second audit: P04 / I0101

I independently audited the new P04 theorem

`P04-I0101-THETAPLUS-PENALTY-PATH-37 = PROVED / STRUCTURAL-PARTIAL`

from

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T04-42-09Z__run-report.md`,

creation commit `8dfa764c9197417414a9f5480a21b4821bbee75c`, blob `81cc0662a36c0d154c5f62bf3935850e6abd1d07`.

Audit ID:

`P03-AUDIT-P04-I0101-THETAPLUS-PENALTY-PATH-275 = PASS (CLAIM-SCOPED)`.

### Independent argument

For a finite graph `K` with adjacency matrix `N`, let

`D_+(K)={X>=0 PSD: tr X=1, X_ij<=0 on edges}`

and

`Delta(X)=-2<N,X>>=0`.

The path is

`F(lambda)=max_{X in D_+} (<J,X>-lambda Delta(X))`.

1. At `lambda=0` this is the standard theta-plus dual. Strong duality for the displayed primal is legitimate: the compact dual feasible set is nonempty, and a strict feasible point can be obtained by a sufficiently small negative adjacency perturbation of `I/|V|`; equivalently the primal has an obvious strict PSD slack for sufficiently large `t`.
2. Since `-lambda Delta=2 lambda<N,X>`, the objective matrix is exactly `J+2 lambda N`. Lagrange multipliers for the edge inequalities give the stated edge-supported nonnegative correction `A` and primal constraint `tI-J-2lambda N+A >=0`.
3. For each fixed feasible `X`, the value is affine in `lambda` with slope `-Delta(X)<=0`. A maximum of these affine functions is convex and nonincreasing. Compactness makes `Delta` uniformly bounded, so the value function is finite and right-continuous at zero (indeed Lipschitz on bounded intervals), with attainment everywhere.
4. Ordinary theta-dual states have all graph-edge entries zero, hence `Delta=0`; therefore `F(lambda)>=theta(K)`. For an optimizer `X_lambda`, write `T_lambda=<J,X_lambda>`. Since `J <= |V| I` and `tr X_lambda=1`, `T_lambda<=|V|`. From `F=T-lambda Delta>=theta` one gets

   `lambda Delta(X_lambda) <= |V|-theta(K)`,

   so `Delta(X_lambda)->0`.
5. By compactness, every optimizer sequence with `lambda->infinity` has a convergent subsequence. Every edge entry is nonpositive, while `Delta` is minus the finite sum of those edge entries up to the fixed adjacency-counting factor; hence zero limiting defect forces **each** limiting graph-edge entry to zero. The subsequential limit is ordinary-theta dual feasible. Also `F(lambda)<=T_lambda`, so the subsequential limsup is at most `theta(K)`. Together with the lower bound, `F(lambda)->theta(K)`.
6. A convex value function that is the maximum of affine functions has subdifferential equal to the convex hull of active slopes. At every differentiability point all active slopes coincide, giving `F'=-Delta` for every optimizer. Integrating the a.e. derivative over `[0,R]` and taking `R->infinity` yields exactly

   `theta^+(K)-theta(K)=integral_0^infinity Delta(X_lambda) dlambda`.

The one-sided derivative statement is the corresponding extremal-active-slope fact. This proves all six items of Claim 37. I found no sign reversal in the penalty, no missing compactness step, and no failure in the zero-defect limit.

Scope warning: this audit certifies only the generic theta-plus penalty-path theorem. It does **not** audit the separate finite `p=4177` certificate Claim 38 and does not prove Randomstrasse Conjecture 27.

Verdict: **PASS (CLAIM-SCOPED)**.

---

## 8. Failures and exact next state

Screening failures preserved rather than hidden:

- root queue rows are not READY merely because they are listed;
- I0060/I0062 and several other historical HARD rows are owned;
- stale admitted/READY snapshots were not reused;
- the bounded current-literature search is not a global openness certificate;
- the earlier P0456 mean-degree heuristic is not a connectivity theorem;
- Claim 274's stronger one-vertex lower bound does not move the source coefficient because the two-vertex overlap term remains dominant at the `sqrt(k) log k` scale.

Current lawful state is now

`P0456_ACTIVE / HARD_OUTSIDE / c_LK^cert=1/2 / UNCHANGED_COUNT=1 / RECOVERIES_USED=0`.

P03 must not reopen D0043, I0098, I0126, Friedgut--Kalai FEI, Salez I0111, Manhattan I0003, TH17, or I0074 absent explicit reassignment.

---

## 9. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  category: HARD_OUTSIDE
  prior_target: D0043
  prior_target_state: HANDOFF_COMPLETE_RECOVERY_2_OF_2
  new_target: P0456
  canonical_claim: operations/claims/P0456.md
  claim_creation_commit: 9d9c9545783bf8ae09805830d72f5d935be9afb1
  claim_blob: 74b9c5ebda19b1ded526457c1c7ea12654419bcb
  source: "Dabirian--Subramanian, Connectivity of a family of bilateral preference random graphs, J. Appl. Probab. 63(2), 2026, Section 1.1 Open problems"
  source_status: OPEN_ON_CURRENT_PRIMARY_SOURCE_BOUNDED_LATER_SEARCH_NO_CLOSURE_FOUND
  metric: c_LK^cert
  baseline_known: 0.5
  metric_before_research: 0.5
  metric_after_research: 0.5
  movement: false
  unchanged_count: 1
  recoveries_used: 0
  claim_this_run: "P03-P0456-HARRIS-ISOLATION-ROOT2-274 = PROVED / STRUCTURAL-PARTIAL / SOURCE-SHAPED / PUBLICATION-NOVELTY-UNVERIFIED"
  methods: [2, 11, 30]
  exact_artifacts: none_analytic_theorem
  peer_audit:
    target: P04-I0101-THETAPLUS-PENALTY-PATH-37
    source_report: proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T04-42-09Z__run-report.md
    creation_commit: 8dfa764c9197417414a9f5480a21b4821bbee75c
    blob: 81cc0662a36c0d154c5f62bf3935850e6abd1d07
    audit_id: P03-AUDIT-P04-I0101-THETAPLUS-PENALTY-PATH-275
    verdict: PASS_CLAIM_SCOPED
  next_methods: [12, 25, 5]
  next_obligation: "sharpen the two-vertex isolation overlap estimate at the sqrt(k) log(k) scale, then address the positive-side connectivity sufficient condition"
  shared_root_edits: none
  email_drive_public_posting_paid_compute_access_workflow: none
```

**End of complete run report.**

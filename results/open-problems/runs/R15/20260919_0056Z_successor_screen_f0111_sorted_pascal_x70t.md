Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; free admission remains `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, the entire serial coupled-Pascal compiler for heterogeneous `k=2` is now solved exactly at each base: its optimal coordinate order has certified constant `Gamma_serial(q)=max_j rho(q without j)`, where `rho(S)=log(1+sum_{i in S}(e^{q_i}-1))/sum_{i in S}q_i`; the carried worst-case `1/(n-1)` is therefore proved sharp for this whole serial compiler, not merely for one gap estimate. Methods #3 PROVE SOMETHING STRONGER, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #25 COUNT THE SAME THING TWICE.**

# R15 retained screen — exact optimal serial Pascal compiler for heterogeneous `k=2`

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new mathematics below is **SELF_CHECK_ONLY**. It neither reopens Burdzy–Scheutzow Problem 7.2 after the mandatory six-run handoff nor promotes Talagrand F0111 from `PENDING / NOT READY` to an owned assignment. No closure or novelty claim is made without the required independent audits and a broader prior-art review.

## 1. Continuity, source fidelity, and admission state

I refreshed the current repository state before doing mathematics: campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative follow-up implementation manifest, the controlling I0076 six-run handoff, the immediately preceding R15 report `20260918_2358Z_successor_screen_f0111_adaptive_k2_w69s.md`, and the newest neighboring F0111 admission screen. The newest admission evidence still leaves F0111 `PENDING / NOT READY / retained screen` and reports no newly certified ownership-clear CLOSABLE successor for R15. I therefore create no claim file and touch no shared root.

The primary Burdzy–Scheutzow source was rechecked directly. Definition 2.1 says:

- FBM means that there are random times `S_n -> -infinity` a.s. from which the complete centered future is standard Brownian motion;
- BBM means the time-reversed process is FBM;
- 2BM means there is one random time `S` at which the centered future and centered past half-paths are **independent standard Brownian motions**.

Problem 7.2 assumes only FBM + BBM and existence of an arbitrary random real time `T` such that the two complete centered half-paths at `T` are independent. It does **not** impose a stopping-time hypothesis and does not separately assume either seam half is Brownian. Problem 7.5 remains excluded.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent real seam. The later Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved actually 2BM. Hence there is no surviving frozen counterexample candidate on which a third or fourth source obligation can honestly be scored. The historical `2/4` is a retirement value for the positive route, not a score on a live counterexample.

## 2. Carried `k=2` compiler

The retained source is Talagrand, *Are Many Small Sets Explicitly Small?*, Definition 10.1 and Problem 10.9. For an increasing family `A`, write

`F_A(t)=-log(1-zeta_t(A))`.

The `C_gamma` condition asks, at each base `q>=0`, for a multilinear polynomial with nonnegative coefficients and zero constant term which globally majorizes `F_A` and satisfies the scaled base budget.

For the cardinality-two threshold on a finite coordinate set `S`, write

`H_S(t)=F_{S,2}(t)`,
`L_S(t)=sum_{i in S} t_i`,
`g_S(t)=L_S(t)-H_S(t)`.

The exact formula is

`g_S(t)=log(1+sum_{i in S}(e^{t_i}-1)).`                    (2.1)

When a new coordinate with hazard `s` is added,

`F_{S union {*},2}(t,s)=H_S(t)+Phi(s,g_S(t))`,              (2.2)

where

`Phi(u,v)=-log(e^{-u}+e^{-v}-e^{-(u+v)}).`

The preceding R15 coupled-Pascal lemma, itself still SELF_CHECK_ONLY, says that if `H_S` already has a `C_gamma` certificate at the old base, then (2.2) can be compiled to the enlarged set whenever

`g_S(q) >= gamma L_S(q)`.                                  (2.3)

The base `A_{2,2}` is the all-elements endpoint and has the carried exact `C_1` certificate.

The previous run lower-bounded (2.3) by keeping one permanent anchor. This run solves the **entire serial ordering problem exactly**.

## 3. Method #17 — the hidden Bernoulli log-mgf

For `g>=0`, define

`T_g(x)=log(1+e^{-g}(e^x-1))`
`      =log((1-p)+p e^x),  p=e^{-g}.`                       (3.1)

Thus `T_g` is exactly the cumulant-generating function of a Bernoulli(`p`) random variable. This identifies the useful normalized increment

`D(g,x)=T_g(x)/x`, `x>0`,                                  (3.2)

as a secant slope of a convex log-mgf.

Two monotonicities are immediate and exact:

1. for fixed `g`, `D(g,x)` is nondecreasing in `x>0`, because `T_g(0)=0` and `T_g` is convex;
2. for fixed `x>0`, `D(g,x)` is strictly decreasing in `g`, because

`partial_g T_g(x)=-(e^x-1)e^{-g}/(1+(e^x-1)e^{-g}) < 0`.    (3.3)

The log-mgf interpretation is classical exponential-family / Chernoff machinery. I therefore treat the mechanism as folklore; only its use inside this Talagrand compiler is being recorded here, with novelty **UNVERIFIED**.

## 4. Method #25 — count the gap twice: sorted-prefix gap fractions decrease

Let

`x_1 >= x_2 >= ... >= x_m >= 0`.

Define

`G_r=log(1+sum_{i=1}^r(e^{x_i}-1))`,
`L_r=sum_{i=1}^r x_i`,
`rho_r=G_r/L_r`

when `L_r>0` (zero coordinates may simply be deleted).

### Theorem 4.1 — sorted-prefix monovariant

For every positive part of the sequence,

`rho_1 >= rho_2 >= ... >= rho_m`.                           (4.1)

#### Proof

Set `G_0=0`. From the direct definition,

`e^{G_r}=e^{G_{r-1}}+e^{x_r}-1`,

hence

`G_r-G_{r-1}=T_{G_{r-1}}(x_r).`                            (4.2)

For `x_r>0`, put

`d_r=(G_r-G_{r-1})/x_r=D(G_{r-1},x_r).`                    (4.3)

Because `G_r>=G_{r-1}` and `x_{r+1}<=x_r`, the two monotonicities from Section 3 give

`d_{r+1}=D(G_r,x_{r+1})`
`        <=D(G_{r-1},x_r)=d_r`.                             (4.4)

Now count `G_r` a second way by telescoping (4.2):

`G_r=sum_{i=1}^r x_i d_i`,                                 (4.5)

so

`rho_r=(sum_{i=1}^r x_i d_i)/(sum_{i=1}^r x_i)`             (4.6)

is the weighted average of the decreasing sequence `d_1,...,d_r`. Since `d_{r+1}` is no larger than every preceding `d_i`, adjoining it cannot increase the weighted average. This proves (4.1). QED.

This is stronger than the previous permanent-anchor lower bound: it identifies the exact gap fraction along the best natural ordering rather than replacing `e^x-1` by `x`.

## 5. Method #3 — exact optimality of the serial coupled-Pascal compiler

Fix a base `q=(q_1,...,q_n)`, `n>=3`. For each coordinate `j`, let

`S_j=[n] minus {j}`,
`L_{-j}=sum_{i!=j}q_i`,
`G_{-j}=log(1+sum_{i!=j}(e^{q_i}-1)).`                      (5.1)

If `L_{-j}>0`, define

`rho_{-j}=G_{-j}/L_{-j}`;                                  (5.2)

if `L_{-j}=0`, use the harmless boundary convention `rho_{-j}=1`.

Define `Gamma_serial(q)` as the largest constant that can be certified at this base using **only** the carried serial coupled-Pascal recursion (2.2)–(2.3), starting from an `A_{2,2}` endpoint and choosing an arbitrary coordinate order.

### Theorem 5.1 — exact serial compiler constant

Subject only to the already-carried endpoint and coupled-Pascal lemmas,

`boxed: Gamma_serial(q)=max_{1<=j<=n} rho_{-j}.`             (5.3)

In particular the best serial route is deterministic and requires no search over `n!` orders beyond choosing the last coordinate.

#### Proof: upper bound for every serial route

Take any serial coordinate order, and let `j` be the last coordinate added. Immediately before that final insertion the old block is exactly `S_j`. Condition (2.3) at that unavoidable step requires

`gamma <= g_{S_j}(q)/L_{S_j}(q)=rho_{-j}`.                 (5.4)

Thus no serial route ending in `j` can certify a larger constant than `rho_{-j}`, and no serial route at all can beat `max_j rho_{-j}`.

#### Proof: attainability for each fixed last coordinate

Fix `j`. Sort the hazards in `S_j` in nonincreasing order,

`x_1>=x_2>=...>=x_{n-1}`,

start from the first two coordinates (where the endpoint theorem gives `C_1`), then insert `x_3,...,x_{n-1}` in this order, and add coordinate `j` last.

At every intermediate insertion, the old block is a sorted prefix. By Theorem 4.1 its gap ratio is at least the ratio of the full old block `S_j`, namely `rho_{-j}`. At the final insertion it is exactly `rho_{-j}`. Therefore condition (2.3) holds at every step for every

`gamma <= rho_{-j}`.

The coupled compiler propagates that certificate through the whole construction. Hence the route ending in `j` attains `rho_{-j}`. Maximizing over `j` proves (5.3). QED.

### Corollary 5.2 — exact improvement over the previous adaptive bound

The previous report sorted `q_(1)>=q_(2)>=...` and set `R=sum_{i>=3}q_(i)`, obtaining

`Gamma_P(q)=max{psi(q_(1),R),psi(q_(2),R)}`,
`psi(a,r)=log(e^a+r)/(a+r).`

For `j=2`, (5.1) gives

`G_{-2}=log(e^{q_(1)}+sum_{i>=3}(e^{q_(i)}-1))`
`      >=log(e^{q_(1)}+R)`,

because `e^x-1>=x`. Thus `rho_{-2}>=psi(q_(1),R)`. Similarly `rho_{-1}>=psi(q_(2),R)`. Therefore

`Gamma_serial(q)>=Gamma_P(q)`.                              (5.5)

If `R>0`, the improvement in these two displayed comparisons is strict because `e^x-1>x` for every positive tail coordinate.

## 6. The old `1/(n-1)` loss is sharp for the whole serial method

Theorem 5.1 does more than improve individual bases. It identifies the exact obstruction of this proof architecture.

For any nonempty `S` with at most `n-1` coordinates,

`G_S=log(1+sum_{i in S}(e^{q_i}-1)) >= max_{i in S}q_i`,

while

`L_S<=|S| max_{i in S}q_i <=(n-1)max_{i in S}q_i`.

Hence every nonzero leave-one-out ratio satisfies

`rho_{-j}>=1/(n-1)`.                                       (6.1)

So `Gamma_serial(q)>=1/(n-1)` for every base, recovering the earlier generic theorem.

Conversely, on the homogeneous high-activity ray `q_i=c`,

`rho_{-j}(c)`
` = log(1+(n-1)(e^c-1))/((n-1)c)`
` = [c+log(n-1-(n-2)e^{-c})]/((n-1)c)`
` -> 1/(n-1)` as `c->infinity`.                             (6.2)

Therefore

`boxed: inf_q Gamma_serial(q)=1/(n-1).`                     (6.3)

This is an exact method-level impossibility result: **no reordering of one-coordinate Pascal insertions, no better anchor choice, and no exact evaluation of the same serial gap ratios can produce a dimension-free constant.** The earlier `1/(n-1)` loss was not merely an artefact of the coarse ordered-gap estimate; it is the sharp worst-case constant of the entire serial compiler.

This sharply redirects the next attack. Any route to a universal constant for `k=2`, and hence any hope of feeding such a result into full Problem 10.9, must use a genuinely non-serial certificate: a block update, a dual certificate, or a global moment/entropy construction which exploits simultaneous coordinates. The separately carried homogeneous `C_1` theorem demonstrates that such non-serial gains really exist—the serial compiler tends to `1/(n-1)` exactly where the homogeneous global certificate gives `1`.

## 7. Source/current-literature check

Dated 2026-09-19 queries covered:

- exact Burdzy–Scheutzow title and `Problem 7.2`, later/citing material;
- exact Talagrand `Problem 10.9`, `C_gamma`, cardinality thresholds;
- the expression `log(1+sum(e^x-1))/sum x` and Bernoulli log-mgf/secant-slope language;
- current 2026 Talagrand discrete-convexity / threshold papers.

The Burdzy search again recovered the original 2014 paper and citation pages but no accessible later primary paper explicitly announcing a solution of exact Problem 7.2. This is bounded negative evidence only.

For the Talagrand neighborhood, the current primary literature includes:

- Ascoli–He–Park–Talagrand, arXiv:2608.11183 (2026-08-11), *A reformulation of the discrete Convexity Conjecture via k-thresholds*;
- Chen Li, arXiv:2609.08967 (2026-09-08), *On p-Spread Measures*, which states a solution of the fractional version;
- Jinyoung Park, arXiv:2609.14681 (2026-09-13), *A dimension-free comparison between expectation thresholds and fractional expectation thresholds*, explicitly described as progress toward the conjecture.

The bounded search did not surface an accessible source explicitly stating the exact sorted-prefix theorem or serial-compiler optimality (5.3), nor an explicit resolution of Talagrand's exact Definition-10.1 / Problem-10.9 formulation. The Bernoulli-cgf monotonicity itself is standard convexity folklore, so novelty of the combined result remains **UNVERIFIED**.

## 8. Metric, status, and next route

Native source metric before: historical carried `2/4`.  
Native source metric after: historical carried `2/4`.  
Native movement: **none; I0076 remains retired after the mandatory handoff.**

Free READY CLOSABLE count seen in the current admission evidence: `0 -> 0`.

Retained-screen movement: the serial heterogeneous `k=2` Pascal architecture is now exactly optimized, with its sharp worst-case constant proved to be `1/(n-1)`. This is a method-closing theorem, not a source closure.

No checker was created. The claims above are parameter-uniform analytic statements with their proofs on the page; a finite grid or numerical sample would not certify them.

The next genuinely different Section-B moves are:

- **#1 CHANGE THE CATEGORY:** formulate the non-serial `k=2` contact problem as a positive-cone / completely-positive tensor problem rather than another recursion;
- **#11 DUALIZE:** seek a weak-dual obstruction or extremal measure that separates serial certificates from a block certificate;
- **#24 FIND THE EXTREMAL OBJECT:** identify the worst heterogeneous base after quotienting scale/permutation, rather than assuming the homogeneous ray is extremal for the true `C_gamma` problem.

The mathematical target is now precise: construct a simultaneous two-or-more-coordinate positive majorant which beats (6.3), or prove a dual obstruction showing why a particular block ansatz cannot.

## 9. Structured ledger delta

```yaml
ledger_delta:
  slot: R15
  lane: CLOSABLE_OUTSIDE
  native_source: I0076
  native_source_title: Burdzy-Scheutzow Forward Brownian Motion Problem 7.2
  native_status: OPEN_PARTIAL_RETIRED_HANDOFF
  native_metric_name: source_matching_obligations_for_one_frozen_candidate
  native_metric_before: "historical 2/4; no surviving frozen candidate"
  native_metric_after: "historical 2/4; no surviving frozen candidate"
  native_movement: false
  native_unchanged_count: "retired at six; not incremented"
  retained_screen_source: F0111
  retained_screen_status: PENDING_NOT_READY_SELF_CHECK_ONLY
  retained_screen_movement: true
  retained_result: "exact optimal serial k=2 Pascal constant Gamma_serial(q)=max_j rho_{-j}; inf_q Gamma_serial=1/(n-1)"
  free_ready_closable_before: 0
  free_ready_closable_after: 0
  tried_moves: [3, 17, 25]
  remaining_obligation: "non-serial/block positive certificate or a dual obstruction; no source closure claimed"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_2358Z_successor_screen_f0111_adaptive_k2_w69s.md"
    - "proofnet24/NM13-12/runs/2026-09-18/2026-09-18T23-55-30Z__post-e0086-admission-delta-screen-10-f0111-envelope.md"
  audit_ids: []
  closure_claimed: false
  canonical_claim_created: false
  checker_created: false
  shared_roots_edited: false
  peer_namespaces_edited: false
  schedule_modified: false
```

## 10. Model / scheduler / permission boundary

The actual runtime identifies as GPT-5.6 Sol; reasoning-effort telemetry is not exposed, so it is reported as UNVERIFIED. The installed prompt requests GPT-6 / maximum, but the exposed task-control schema still has title/prompt, schedule or relative-start, timing mode and enabled state only. It has no binding model-family selector, no reasoning-effort selector, no authenticated per-run model/effort receipt, and no guaranteed-duration field.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary; repository continuity also records that an authorized context later succeeded in updating P26. The lawful workaround is therefore the owning/authorized context or an owner/admin product/API surface that actually exposes the desired fields. This run attempts no scheduler change, task duplication, permission bypass, email, Drive write, public posting, purchase, or edit outside `runs/R15/`.
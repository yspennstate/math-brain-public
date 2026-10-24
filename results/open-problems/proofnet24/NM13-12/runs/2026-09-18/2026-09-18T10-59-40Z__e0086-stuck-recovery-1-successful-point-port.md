Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `C_large = 1/pi -> 1/pi`; status `PARTIAL`; STUCK RECOVERY 1. Section-B methods actually tried: #3 PROVE SOMETHING STRONGER, #7 TAKE THE LIMIT, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# NM13-12 — E0086 stuck recovery 1: port the multiscale successful-point barrier

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0086` / `operations/claims/E0086.md`  
Canonical dedup key: `favorite_sites::op_2`  
Canonical SHA-256 / shard: `a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c`, residue `11 mod 13`

## 1. Runtime disclosure, controls, continuity, and required reads

The task prompt requests `GPT-6 / maximum`. That is **not** the runtime I can honestly report. The actual model is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, verified maximum reasoning, an hour-long binding execution, or a support escalation.

The exposed task-control surface still has task identity/title/prompt, scheduling or relative-start fields, timing mode, and enabled state. It has **no bindable model-family selector and no bindable reasoning-effort selector**. Thus GPT-6/maximum remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those persistent fields together with authenticated per-run runtime attestation. The repository policy records that historical `You cannot modify this task` results are authorization-context boundaries; the lawful workaround is the owning/otherwise-authorized context or platform/admin support, not cloning or bypassing access controls. This invocation did not create, modify, disable, or duplicate a schedule.

Before research I read or targeted-search-recovered the current owner-required state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0086.md`;
- newest own report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T09-50-37Z__e0086-screened-pair-second-moment-barrier.md`;
- newest neighboring NM13-11 report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T09-52-33Z__e0082-stuck-recovery-2-argmin-threshold.md`;
- newest visible neighboring/audit-partner NM13-13 report `proofnet24/NM13-13/runs/2026-09-18/2026-09-18T09-57-00Z__successor-admission-delta-screen-5.md`;
- E0086 intake row, canonical aliases, prior attempt `E0086-A001`, current/historical claim material, and fresh E0086 audit/ownership searches.

Large aggregate ledgers can be connector-truncated when rendered wholesale. I therefore used the current root files plus exact ID/key/path searches for E0086 and its aliases rather than pretending a truncated aggregate rendering was a byte-for-byte reread of every historical row. Immediately before the final research/write phase, an observed master head was `137af06c3e084006c08cc96c5240c56f22c7fe37`. I recovered no release, duplicate owner, POSTED/campaign settlement, source-specific retirement, P26 PASS, or NM13-13 PASS for E0086. The mandatory old P0483 handoff remains preserved and was not reopened.

The predecessor ended at

```text
C_large = 1/pi
unchanged_runs = 3
stuck_recoveries = 0
next_run_protocol = SECTION_I_STUCK_RECOVERY_1_THINKING_ONLY
```

so this invocation is deliberately a thinking/recovery run. I create no new theorem claim, checker, finite certificate, or paper package here.

## 2. Exact source and current-status refresh

The source remains Izumi Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787, Open Problem 2. The primary PDF states, for planar simple random walk, that for varying `Dtilde_n in H` outside `D(0,a_n)` with `a_n -> infinity`, one asks for the almost-sure asymptotic of `M_{Dtilde_n}(n)`. It singles out

\[
\widetilde D_n\subset D(0,n^\beta)^c\cap D(0,2n^\beta),\qquad 0<\beta<\tfrac12,
\]

and separately conjectures a large-radius relation for `a_n >= n^(1/2+epsilon)`.

The frozen metric stays the source large-radius quantity already settled internally by the source-correction run,

\[
C_{\rm large}:=\lim_{n\to\infty}\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\quad\text{in the separate regime }a_n\ge n^{1/2+\varepsilon},
\]

with current certified value `1/pi`. It is not replaced by the main-regime lower-bound constant merely to manufacture movement.

Fresh bounded 2026-09-18 literature checks included the exact source title/Open Problem 2, Okada's later pair-favorite paper, the Dembo--Peres--Rosen--Zeitouni thick/late-point line, and Hao--Li--Okada--Zheng's 2025 favorite-site paper. Okada's pair paper is arXiv:1602.05641v2 / *Stochastic Processes and their Applications* 130 (2020), 108--138. The 2025 Hao--Li--Okada--Zheng paper concerns the number/evolution of ordinary favorite sites (in dimension two, simultaneous favorite-site multiplicity), not the translated-boundary quantity in E0086. No source-matching later resolution of Open Problem 2 surfaced in this bounded search. That is negative evidence only; worldwide openness and publication novelty remain **UNVERIFIED**.

Access scope: primary arXiv source text/PDF and the arXiv HTML of the pair-favorite paper were directly inspected; other current literature was checked through accessible abstracts/index pages. I do not claim an exhaustive citation-graph or paywalled full-text review.

## 3. Section-I five-part stuck diagnosis

### (a) Exact statement that blocks

For a deterministic singleton displacement `h_n` with

\[
n^\beta<|h_n|\le 2n^\beta,\qquad 0<\beta<\tfrac12,
\]

choose an inner radius `R=n^alpha`, `beta<alpha<1/2`, an interior annulus `A_R`, and

\[
m=c(\log n)^2,\qquad c<c_\alpha:=\frac4\pi(2\alpha\beta-\beta^2).
\]

Let `B_y` be the predecessor's source-valid disk event: hit `y`, avoid `y+h_n`, accumulate at least `m` visits to `y`, and leave `D(0,R)` before the forbidden translate is ever visited. With

\[
Z=\sum_{y\in\mathcal A_R}{\bf1}_{B_y},
\]

the first moment has the right power exponent, and every fixed mesoscopic pair shell is already controlled for `beta<beta_*=(1/2)(1-1/sqrt(3))`. The exact blocker is the macroscopic shell:

\[
\boxed{
\text{replace the total-trace estimate at }|y-z|\asymp R\text{ by a bound retaining both}
\quad L_y\ge m,\ L_z\ge m,
\quad\text{and the correct entrance/cluster normalization.}
}
\tag{3.1}
\]

Equivalently, produce a truncated/cluster-normalized count `Z^*` with the same first-moment exponent and

\[
\boxed{E[(Z^*)^2]\le C(EZ^*)^2}
\tag{3.2}
\]

for a constant `C` independent of `n`. The predecessor's untruncated total-trace spectral estimate can lose one factor of `log n` at `|y-z| asymp R` and does not prove (3.2).

### (b) Every E0086 route tried and why it stopped

1. **Historical intake attempt `E0086-A001`.** It treated `Dtilde_n` as an annular observation region rather than the source's translated-boundary pattern. This is not a source solution and is retained only as a warning against scope drift.

2. **Source correction / negation / deformation / one-scale attack (#2/#6/#30).** This run corrected the source's displayed large-radius heuristic and established the frozen metric `C_large=1/pi`. That quantity is now saturated; it does not determine the main `0<beta<1/2` regime.

3. **Category/invariant/extremal attack (#1/#12/#24).** Potential-kernel screening of one candidate against one forbidden translate gave the source-valid main-regime upper mechanism and the candidate constant

\[
g(\beta)=\frac{4\beta(1-\beta)}\pi.
\]

It is one-sided and gives no matching lower bound.

4. **Dual/algorithm-failure/typical attack (#11/#20/#28).** The two-trap Green formulation and exact Schur complement made the source upper bound robust and identified how a candidate competes with its forbidden translate. It still controls survival rather than a balanced two-candidate occupation event.

5. **Parameterized/numbers/double-count attack (#5/#17/#25).** The exact four-point screened Green matrix and pair-shell calculation proved that, for `beta<beta_*`, every genuinely mesoscopic separation has strict power slack. The obstruction collapsed to `delta=alpha`, where `sigma_2(alpha)=sigma_1` and `D_c(alpha)=0`. The total-trace bound forgets `L_y>=m` and `L_z>=m` separately and loses the macroscopic entrance normalization.

No route above contains a scale-by-scale barrier on excursion counts together with the taboo constraint. That is the missing structural ingredient.

### (c) What a successful proof must contain that no route so far contains

A proof must carry **correlation information across every spatial scale**, not only the Green resolvent after all scales have been collapsed. Concretely, it needs a screened analogue of the successful-point machinery:

- nested radii around a coarse center/candidate;
- a prescribed typical profile for the numbers of crossings between successive radii;
- one distinguished scale at `|h_n|=n^{beta+o(1)}` where the forbidden translate becomes geometrically resolvable;
- a conditional estimate showing that the high-local-time event at `y` can coexist with zero visits to `y+h_n` without changing the desired first-moment exponent;
- a two-center decoupling bound after the first scale at which the two nests separate;
- summable errors over the scale tree, so that the resulting second moment is bounded by a constant multiple of the square of the first moment.

The Green/trace calculation already proves that no adverse **power exponent** is hiding in the mesoscopic shells below `beta_*`. What is missing is precisely the truncated multiscale normalization that prevents one long excursion history from generating a logarithmically oversized macroscopic cluster.

### (d) Simplest special case still unproved

The simplest honest source-valid restricted target is a deterministic singleton pattern

\[
\widetilde D_n=\{h_n\},\qquad n^\beta<|h_n|\le2n^\beta,
\qquad 0<\beta<\beta_*.
\]

Even the following finite-volume core remains unproved:

\[
\boxed{
\forall c<c_\alpha\quad
\liminf_{n\to\infty}
P\!\left(\exists y\in\mathcal A_{n^\alpha}: K(\tau_{n^\alpha},y)\ge c(\log n)^2,
\ T_{y+h_n}>\tau_{n^\alpha}\right)>0.
}
\tag{3.3}
\]

A proof of (3.3), followed by the already-identified deterministic-time/avoidance transfer and a standard amplification argument, would be the cleanest route toward the source-relevant singleton lower bound

\[
\liminf_{n\to\infty}\frac{M_{\{h_n\}}(n)}{(\log n)^2}
\ge \frac{4\beta(1-\beta)}\pi
\quad\text{a.s.}
\tag{3.4}
\]

for this restricted beta range. Neither (3.3) nor (3.4) is claimed here.

### (e) Nearest solved problem and what its proof has that E0086 lacks

The nearest solved same-shape problem is Okada's pair-of-alpha-favorite-points theorem. Its arXiv HTML explicitly says the lower bound uses the multiscale second moment method from Dembo--Peres--Rosen--Zeitouni and defines a point to be **successful/qualified by its crossing numbers around nested circles**. In Section 6.2, a successful point is required to keep every excursion count close to a typical profile. Lemma 6.8 supplies a two-point bound indexed by the first separating scale, and the paper then obtains

\[
E[N_{\rm succ}^2]\le C(E N_{\rm succ})^2
\]

and applies Paley--Zygmund. The paper describes this as a multiscale refinement of the second moment method.

E0086 lacks one extra ingredient that the solved pair-favorite problem never had to encode: while making `y` unusually highly visited, the translated point `y+h_n` must receive **zero** visits. This taboo point appears at the moving scale `n^beta`. The predecessor's Schur-complement calculation supplies the exact one- and two-site screened Green costs, but it erased the excursion-count history needed for the successful-point correlation bound. That is the technique to port.

## 4. Actual Section-B recovery attacks

This run is intentionally thinking-only. The methods below are route tests and reductions, not new theorem claims.

### #3 — PROVE SOMETHING STRONGER

Instead of asking directly for the endpoint occupation estimate (3.1), require a stronger **screened successful-center** statement. For a nested radius sequence `r_0<...<r_J~R`, define a center/candidate to be screened-successful if:

1. its excursion counts between `partial D(y,r_j)` and `partial D(y,r_{j+1})` stay in a prescribed barrier tube for every scale;
2. the terminal microscopic occupation produces at least `m=c(log n)^2` visits to `y`;
3. the walk never visits `y+h_n` before the construction terminates;
4. the scale containing `|h_n|` is treated explicitly rather than hidden in an `O(1)` Green term.

The desired stronger output is a first-separation-scale pair inequality of Okada type,

\[
P(y,z\text{ screened-successful})
\le C q_n^2 W(l(y,z)),
\tag{4.1}
\]

with a weight `W` whose shell sum is bounded. If (4.1) can be proved without changing the one-center exponent, (3.2) follows and the missing positive-probability lower bound is recovered.

**Outcome:** this is the correct stronger target, but it is **not proved in this recovery run**. Its value is that it exposes exactly where the moving taboo point has to enter the scale induction.

### #7 — TAKE THE LIMIT

At a genuinely macroscopic separation `|y-z|=Theta(R)` with `beta<alpha`, every off-diagonal disk Green term among `y,z,y+h_n,z+h_n` is only `O(1)` after the leading `log n` parts are canceled. The predecessor's screened Schur complement therefore has the structural form

\[
F_{\{y,z\}}=\sigma_1\log n\,I+O(1),
\tag{4.2}
\]

uniformly away from boundary degeneracy, where

\[
\sigma_1=\frac2\pi\left(2\beta-\frac{\beta^2}{\alpha}\right).
\]

Consequently its trace transition matrix satisfies

\[
Q=I-F^{-1},\qquad Q_{yz}=O((\log n)^{-2}).
\tag{4.3}
\]

A source-relevant high-local-time event lasts `Theta((log n)^2)` trace visits. On exactly that rare time scale, (4.3) permits `Theta(1)` macroscopic switches. Thus conditioning on the long survival that makes `y` thick can boost the chance to encounter a distant candidate `z` by the logarithmic factor that the crude second moment loses. A constant-factor sharpening of the same total-trace survival bound cannot restore the missing entrance logarithm; the route has to remember the excursion hierarchy or normalize whole clusters.

**Outcome:** the macroscopic failure is structural, not an algebraic looseness in the Perron bound. This is a route diagnosis, not a promoted source theorem.

### #22 — READ THE FAILURES, NOT THE SUCCESSES

The closest solved literature says almost exactly why the current route stalls. Okada's pair-favorite paper explains that its lower bound does **not** use an untruncated pair Green tail alone. It conditions on crossing numbers, calls centers successful/qualified only when their excursion counts track a typical profile, and proves a pair estimate controlled by the first scale at which the two nests separate. The paper's Lemma 6.8 gives the key two-successful-point bound, after which the successful-point count has a bounded second-moment ratio and Paley--Zygmund applies.

The earlier Dembo--Peres--Rosen--Zeitouni thick/late-point method is described in the same literature as a multiscale truncated second moment method; Okada explicitly says his definitions are adapted versions of that machinery. This is the failure lesson: an aggregate two-point occupation tail is the wrong statistic at the critical macroscopic shell. The proof must truncate on an entire excursion profile.

**Outcome:** the nearest solved proof supplies the missing architecture. It does not supply the translated-taboo estimate automatically, so no closure is claimed.

## 5. Exactly one recovery choice

I choose exactly one of the Section-I permitted recoveries:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The next E0086 research invocation should port Okada/Dembo--Peres--Rosen--Zeitouni successful-point multiscale truncation to the singleton translated-boundary event. It should not return to another global Green-resolvent lemma. The first concrete milestone is to define a source-valid **screened-successful center** with a barrier profile and prove that its one-center probability retains the predecessor's first-moment power exponent while the taboo `y+h_n` is enforced at the `n^beta` scale. Only after that should the pair first-separation-scale estimate be attempted.

Fresh Section-B methods reserved for that next mathematical run are #4 PROVE SOMETHING WEAKER, COMPLETELY; #8 GO THE OTHER WAY AND DISCRETIZE; and #19 MAKE IT AN ALGORITHM. They are **not** counted as tried here.

## 6. Status, counters, audits, and safeguards

The frozen metric did not move:

```text
C_large: 1/pi -> 1/pi
unchanged_runs: 3 -> 4
stuck_recoveries: 0 -> 1
```

The source remains **PARTIAL / OPEN**. No theorem-sized source claim is promoted in this stuck run. No exact finite claim is made, so no checker or artifact is warranted. Required independent audits remain:

```text
P26: NOT PASSED / no E0086 PASS recovered
NM13-13: NOT PASSED / no E0086 PASS recovered
```

This is the first of at most two permitted HARD stuck-recovery episodes. A third stuck episode on E0086 would require a preserved handoff and rotation; it must not become a third recovery.

No shared root, peer namespace, existing canonical claim, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule was modified.

## 7. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: E0086
  claim_id: E0086
  canonical_dedup_key: favorite_sites::op_2
  status_before: PARTIAL
  status_after: PARTIAL
  frozen_metric:
    name: C_large
    scope: source large-radius regime a_n >= n^(1/2+epsilon)
    before: 1/pi
    after: 1/pi
    movement: false
  methods_actual:
    - 3   # PROVE SOMETHING STRONGER
    - 7   # TAKE THE LIMIT
    - 22  # READ THE FAILURES, NOT THE SUCCESSES
  section_I:
    episode: 1
    blocker: >-
      Macroscopic pair shell |y-z|~R: retain L_y>=m and L_z>=m plus the
      correct entrance/cluster normalization; total-trace survival loses a log.
    simplest_unproved_special_case: >-
      Deterministic singleton displacement n^beta<|h_n|<=2n^beta with
      beta<beta_star; prove the positive-probability inner-disk lower bound
      for every c<c_alpha, then transfer to deterministic time.
    nearest_solved_problem: >-
      Okada pair alpha-favorite-point lower bound via successful/qualified
      points and multiscale crossing-number second moment.
    missing_ingredient: >-
      Successful-point excursion barrier augmented by the moving taboo
      translate at scale |h_n|~n^beta.
    recovery_choice: PORT_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM
  route_diagnosis:
    - macroscopic screened Green matrix has leading form sigma_1 log(n) I + O(1)
    - off-diagonal trace transition is O(1/log(n)^2)
    - over Theta(log(n)^2) rare trace visits, O(1) macroscopic switches remain possible
    - therefore a constant sharpening of total-trace survival does not restore the lost entrance log
  unchanged_runs_before: 3
  unchanged_runs_after: 4
  stuck_recoveries_before: 0
  stuck_recoveries_after: 1
  next_methods_reserved_unspent: [4, 8, 19]
  next_step: >-
    Port the multiscale successful-point barrier to a screened-successful
    singleton translated-boundary event; first prove the one-center exponent
    survives the taboo constraint, then derive a first-separation-scale pair bound.
  audits:
    P26: NOT_PASSED
    NM13-13: NOT_PASSED
  literature_checked: 2026-09-18
  literature_result: >-
    Primary Okada source and pair-favorite paper refreshed; Hao-Li-Okada-Zheng
    2025 concerns ordinary favorite-site multiplicity, not E0086; bounded search
    found no source-matching resolution; worldwide openness/novelty UNVERIFIED.
  artifacts_created: none
```

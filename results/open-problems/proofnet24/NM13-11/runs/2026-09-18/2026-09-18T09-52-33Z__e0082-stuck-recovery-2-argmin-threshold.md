Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `gamma_FP = 1 -> 1`; status `PARTIAL`; STUCK RECOVERY 2. Section-B methods actually tried: #1 CHANGE THE CATEGORY, #21 ASK WHO ELSE HAS THIS SHAPE, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# NM13-11 — E0082 stuck recovery 2: positive-meander transpose, argmin process, and typical-column threshold

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-11`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0082` / `operations/claims/E0082.md`  
Canonical dedup key: `pitman_tang::op_2_3`  
Canonical SHA-256 / shard: `1b4de7c58dbd8e94a7bc807a11a84c8e166fceea6c48cb804038b2f998e7228a`, residue `10 mod 13`

## 1. Runtime controls, continuity, and mandatory reads

The task prompt requests `GPT-6 / maximum`. That is **not** the runtime I can honestly report. The actual model is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this worker, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The currently exposed task-control surface still provides ordinary title/prompt, schedule or relative-start information, timing mode, enabled state, and update fields. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those persistent fields plus authenticated per-run runtime attestation. Current repository task-health history likewise records the historical `You cannot modify this task` result as an authorization-context boundary. The lawful workaround is the owning/otherwise-authorized context or platform/admin support, not duplication or permission bypass. This invocation did not create, modify, disable, or duplicate a schedule and does not claim a support escalation.

Before mathematics I reread or targeted-search-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0082.md`;
- newest prior own report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T09-04-00Z__e0082-stuck-recovery-1-dual-load.md`;
- newest neighboring NM13-12 report, commit `2432e0d6ee0fb0f161316a5c41b0f6b75edab029`, on its distinct E0086 target;
- the E-intake row / canonical alias material and prior substantive attempt `E0082-A001`;
- current/historical claim and audit searches.

Large root ledgers and JSONL files can be connector-truncated when rendered wholesale. I therefore used the current files together with exact IDs, exact claim/report paths, targeted `E0082` / canonical-key / attempt searches, and the current neighboring report rather than pretending a truncated aggregate rendering was a byte-for-byte reread of every historical row.

Pre-write `master` was observed at `f7d4356849e695834623630b439b8f1c023b9027`. `E0082` remains exclusively owned by NM13-11. I recovered no release, duplicate owner, retirement, POSTED/campaign settlement, source-specific correction, P26 PASS audit, or NM13-12 PASS audit. The canonical claim remains active and a disabled or inaccessible schedule would not release it.

The predecessor report ended with `gamma_FP=1`, `unchanged_runs=3`, `stuck_recoveries=1`, and the exact next-step instruction to try to prove the quotient reciprocal-load inequalities from the Catalan-conditioned composition law and an overlap double count without extending the finite table. That route did not close its two required uniform inequalities in this invocation. Because the source remains stuck and this is a hard target, I treat the present invocation as the **second and final allowed stuck-recovery episode**. In accordance with Section I, I promote **no new theorem claim and no new finite certificate claim** here. The exact identities below are route calculations and reductions used to decide what should be attempted next, not a metric change or closure claim.

## 2. Exact source and bounded literature refresh — 2026-09-18

The source remains Jim Pitman and Wenpin Tang, *Patterns in Random Walks and Brownian Motion* (arXiv:1411.0041; Springer LNM 2137). The source asks for exact asymptotics of the bridge and negative first-passage waiting times and records Peres's conjectured first-passage order

\[
c_\lambda n\log n\le E T(\mathcal{FP}^{\lambda,n})\le C_\lambda n\log n
\qquad(\lambda<0\text{ fixed}).
\]

The frozen metric remains

\[
\gamma_{FP}:=\inf\{\gamma:E T(\mathcal{FP}^{-1,n})=O(n^\gamma)\}=1,
\]

already established by the admission run's `O(n log n)` upper theorem together with the source linear lower bound. I do not replace this saturated metric by a logarithmic exponent or a new constant merely to manufacture movement.

Fresh bounded public-web queries included:

- `"Patterns in Random Walks and Brownian Motion" Pitman Tang first passage waiting time n log n 2026`;
- `"Pitman Tang" moving window argmin process random walk 2018`;
- `"first passage" "Pitman Tang" waiting time pattern exact asymptotics`.

The search recovered the original source and, importantly for the new route below, Pitman--Tang's later *The argmin process of random walks, Brownian motion and Levy processes* (arXiv:1610.01524; EJP 2018). Its abstract states that the moving-window argmin process is Markov/Feller with explicit transition kernels in the Brownian case and that analogous random-walk/Lévy results are derived; it also identifies a renewal structure for fixed-length Brownian extrema. I also recovered their later extreme-order-statistics work using Feller chains. I found no later primary paper in this bounded search claiming the exact E0082 first-passage waiting-time asymptotics or Peres's `Theta(n log n)` statement. This is **bounded negative evidence only**; worldwide openness and publication novelty remain UNVERIFIED.

Primary/public links checked:

- `https://arxiv.org/abs/1411.0041`;
- `https://www.columbia.edu/~wt2319/Patterns.pdf`;
- `https://arxiv.org/abs/1610.01524`;
- `https://arxiv.org/abs/2007.13991`.

## 3. Section-I five-part stuck diagnosis

### (a) Exact blocking statement

For the source-valid square subsequence `n=m^2`, the preceding exact ladder-composition quotient gives a quotient matrix `K_m`, Catalan class vector `c^{(m)}`, and

\[
F_m:=|\mathcal F_{m,m^2}|=\mathbf1^Tc^{(m)}
\]

such that

\[
\frac1{E T(\mathcal F_{m,m^2})}
=2^{-m^2}(c^{(m)})^T K_m^{-1}\mathbf1.
\]

The positive cover formulation isolates the missing lower bound as

\[
S_m:=(c^{(m)})^TK_m^{-1}\mathbf1
=\min_{y\ge0,\ K_m^Ty\ge c^{(m)}}\mathbf1^Ty.
\]

The blocker remains:

\[
\boxed{
\text{construct }y^{(m)}\ge0\text{ with }K_m^Ty^{(m)}\ge c^{(m)}
\quad\text{and}\quad
\mathbf1^Ty^{(m)}\le C\,\frac{F_m}{\log(m^2)}.}
\tag{3.1}
\]

This would imply the source-relevant square-subsequence lower bound `E T(FP^{-1,m^2}) >= c m^2 log m`.

### (b) Routes tried and why each stopped

1. **Full matching/correlation inversion (`E0082-A001`)** exposed nonuniform first-hit weights but no compressing invariant.
2. **Reversed-overlap / first-passage ladder route (#2/#4/#8)** proved `O(n log n)` and hence `gamma_FP=1`, but is one-sided: extremal row control does not give the Peres lower bound.
3. **Positive LP / extremal route (#11/#13/#24)** showed uniform weights necessarily pay the same logarithm one is trying to recover.
4. **Exact ladder-composition quotient (#14/#16/#18)** compresses the exponential matrix to a weak-composition quotient but leaves a highly nonuniform positive dual.
5. **Interpolation / reciprocal incoming load / double count (#5/#20/#25)** found a plausible nonuniform dual ansatz, but neither its uniform cover inequality nor its `O(F_m/log n)` total-mass inequality was proved. The prior finite diagnostics were route selection only and are not extended here.
6. **Current transpose/argmin/typical-column attacks (#1/#21/#28)** replace pointwise dual control by a distributional lower-tail target. They isolate a sharper probabilistic obligation but do not yet prove it.

### (c) What a successful proof still needs

The missing ingredient is now more precise than “understand the inverse matrix.” A proof must show that **most source patterns, in the uniform first-passage bridge law, have logarithmic incoming matching load**, with a quantitative lower-tail estimate strong enough to pay for the exceptional set. Extremal load bounds cannot supply this. One needs a genuinely distributional estimate across the conditioned first-passage ensemble.

A particularly clean sufficient target is the moment pair

\[
E[D_n]\ge a\log n,
\qquad
\operatorname{Var}(D_n)\le C\log n,
\tag{3.2}
\]

for the exact column-load functional `D_n` under a uniformly sampled `FP^{-1,n}` pattern. Chebyshev would then make the low-load fraction `O(1/log n)`, which is exactly the scale needed by the threshold reduction in Section 6.

### (d) Simplest special case still unproved

The simplest honest source-valid special case remains

\[
\boxed{E T(\mathcal{FP}^{-1,m^2})\ge c\,m^2\log m
\quad\text{for all sufficiently large }m.}
\tag{3.3}
\]

Together with the already proved `O(n log n)` upper bound this would establish `Theta(n log n)` on the square subsequence, still only `PARTIAL` relative to the source's exact-asymptotic and all-`lambda` questions.

### (e) Nearest solved problem and the ingredient E0082 lacks

The nearest solved same-framework problem remains Pitman--Tang's positive-walk family. Its matching matrix is a scalar multiple of a right-stochastic matrix: identical row sums collapse the inverse calculation to one dimension and give the exact asymptotic `E T(M^{2n+1}) ~ 4n`.

The first-passage family lacks that constant-row invariant. The new #1 route below shows that, after a time/sign reversal, E0082 becomes an **endpoint-conditioned positive-meander family**. Thus the gap from the solved problem is now identified very concretely: the stochastic row-sum symmetry is destroyed by conditioning the positive walk to end at the prescribed height `m ~ sqrt(n)`.

## 4. Section-B #1 — CHANGE THE CATEGORY: first passage -> endpoint-conditioned positive meanders

For a word `A=(a_1,...,a_n)`, define

\[
\rho(A):=(-a_n,-a_{n-1},\ldots,-a_1).
\]

If `A` first hits `-m` at time `n`, then for `1<=k<=n`

\[
\sum_{i=1}^k \rho(A)_i
=S_{n-k}(A)-S_n(A)=S_{n-k}(A)+m>0,
\]

with terminal value `m`. Thus `rho` bijects the first-passage family onto the family of strictly positive length-`n` walks ending at `+m`.

Under the Pitman--Tang overlap convention,

\[
\epsilon_\ell(A,B)=\epsilon_\ell(\rho(B),\rho(A)),
\]

so the matching matrix of the transformed endpoint-conditioned positive family is the transpose of the first-passage matching matrix, up to the relabeling by `rho`.

**Outcome of #1:** this changes the category in a useful way but does not close (3.1). The source's solved positive-walk argument uses the full positive family, for which every row has the same sum. Conditioning on the endpoint `m` slices that family and breaks the invariant. The useful new question is therefore not “invert the first-passage matrix,” but “how much of the stochastic-row-sum structure survives under an endpoint Doob/bridge conditioning?” I do not promote the transpose observation as a new source theorem; it is a route equivalence for the recovery.

## 5. Section-B #21 — ASK WHO ELSE HAS THIS SHAPE: moving-window argmin / extrema processes

A length-`n` block belongs to `FP^{-1,n}` exactly when its right endpoint is the **strict minimum of the whole window** and its displacement from the left endpoint is the prescribed `-m`. Therefore occurrences can be rephrased as visits of a moving-window extremum process to the right boundary together with a height-gap mark.

Pitman--Tang's later argmin paper proves Markov/Feller structure and transition kernels for moving-window argmin processes, including random-walk analogues. Their later extreme-order-statistics work develops Feller-chain descriptions near random-walk minima. These papers have exactly the state-space shape missing from direct matrix inversion.

However, the unmarked argmin position is not sufficient for E0082: the source event also fixes the window height drop to `m`. A direct application would silently discard a source quantifier. The necessary object is an **augmented argmin state carrying the endpoint/start gap (or an equivalent ladder mark)**. I did not find in the bounded literature check a ready-made transition kernel for precisely that augmented state which would immediately yield the waiting-time asymptotic.

**Outcome of #21:** a genuine new route is available, but the comparison hypothesis is not yet proved. The next analytic calculation should derive the marked transition/renewal kernel from the exact simple-random-walk reflection formulas rather than cite the unmarked argmin chain as if it solved the source.

## 6. Section-B #28 — REPLACE FOR ALL WITH FOR TYPICAL: threshold the column loads

This attack directly addresses why the reciprocal-load route stalled. Work with the full matching matrix `M` of a finite pattern family of size `F`, and write

\[
q:=M^{-1}\mathbf1,
\qquad
S:=\mathbf1^Tq.
\]

For the source matching system, `q_j>0`; because the diagonal matching contribution is at least one and `Mq=1`, also `q_j<=1`. Let

\[
d_j:=(\mathbf1^TM)_j
\]

be the `j`th column sum. Since

\[
F=\mathbf1^TMq=\sum_j d_jq_j,
\]

for any threshold `L>0`, if

\[
B_L:=\#\{j:d_j<L\},
\]

then the route calculation gives

\[
S
=\sum_{d_j\ge L}q_j+\sum_{d_j<L}q_j
\le \frac FL+B_L.
\tag{6.1}
\]

Since `E T=2^n/S`, it is enough for the Peres lower order to prove, for some fixed `a>0`,

\[
\boxed{B_{a\log n}=O(F/\log n).}
\tag{6.2}
\]

This is the exact sense in which the problem can be changed from a **for-all** column lower bound, which is false because exceptional low-load columns exist, to a **typical-column** lower-tail bound. It also matches the source's qualitative observation that its extremal column estimates are attained by only a small part of the family; what is missing is the quantitative `O(1/log n)` exceptional mass.

For a uniformly sampled target pattern `B` in the first-passage family, let `D_n=d(B)`. The source's exact column-count identity can be written

\[
D_n(B)
=1+\sum_{\ell=1}^{n-1}
\mathbf1_{\{S_\ell(B)<0\}}
\frac{|S_\ell(B)|}{\ell}
\binom{\ell}{(\ell+S_\ell(B))/2}2^{-\ell}.
\tag{6.3}
\]

The summand is exactly a simple-random-walk first-passage atom to the negative level `S_ell(B)`. Thus `D_n` is an additive local-time/renewal functional of a random walk conditioned to make its first hit of `-m` at time `n`.

The sufficient moment route (3.2) is now immediate: if `E D_n >= a log n` and `Var(D_n)<=C log n`, then Chebyshev gives

\[
P(D_n<a\log n/2)=O(1/\log n),
\]

which is (6.2) after changing the constant. Inserting (6.2) into (6.1) gives `S=O(F/log n)` and hence the desired lower order because `2^n/F=Theta(n)` for fixed negative `lambda`.

The needed moments have an exact finite starting point. If

\[
p_h(t):=P(T_{-h}=t)
=\frac ht\binom{t}{(t-h)/2}2^{-t},
\]

then under the conditioned first-passage law `T_{-m}=n`, for `1<=h<m`,

\[
P(S_\ell=-h\mid T_{-m}=n)
=
\frac{P(S_\ell=-h,\ T_{-m}>\ell)\,p_{m-h}(n-\ell)}{p_m(n)},
\tag{6.4}
\]

and the killed transition in the numerator is available by reflection. This turns `E D_n` into an explicit double sum of binomial/first-passage terms; the two-time Markov version does the same for the covariance kernel. The target is therefore analytic rather than an exponential matrix inversion.

On the square subsequence there is a second exact representation. If `X_1,...,X_m` are iid first-passage times from `0` to `-1`,

\[
P(X_i=2r+1)=C_r\,2^{-(2r+1)},
\]

then, conditional on `X_1+...+X_m=m^2`, the semilength vector

\[
R_i=(X_i-1)/2
\]

has probability proportional to `prod_i C_{R_i}` subject to `sum_iR_i=m(m-1)/2`, exactly the Catalan-weighted ladder-composition law in the quotient. This is the renewal-bridge meaning of the quotient weights and supplies a natural route to dyadic-scale moment bounds.

**Outcome of #28:** this is the sharpest route produced in the recovery. It replaces the failed pointwise reciprocal-load inequalities by the explicit lower-tail problem (6.2), and reduces (6.2) further to concrete first- and second-moment estimates (3.2) for an additive functional under an exact conditioned first-passage bridge. I have not proved those moment estimates, so there is **no new theorem claim and no frozen-metric movement** in this report.

## 7. Recovery choice, counters, and mandatory next action

The required single Section-I recovery choice is:

> **port the technique from the nearest solved problem.**

The port is now precise: transform first passage into endpoint-conditioned positive meanders, retain the source's matching/renewal identity, and replace the solved full-positive-family constant-row invariant by a quantitative typical-row/column estimate under endpoint conditioning. The later argmin/Feller-chain viewpoint identifies the right Markov object; the exact reflection kernel in (6.4) is the source-valid way to retain the missing height mark.

No finite checker or artifact was created because this stuck invocation promotes no finite claim. Extending the `m<=5` diagnostics would violate the predecessor's route instruction and would not move the tracked source quantity.

Counters:

- `gamma_FP`: `1 -> 1`;
- `unchanged_runs`: `3 -> 4`;
- `stuck_recoveries`: `1 -> 2`;
- status: `PARTIAL`;
- P26 audit: `NOT PASSED / not recovered`;
- NM13-12 audit: `NOT PASSED / not recovered`.

This is the **second allowed hard-source stuck recovery**. If the same source is still stuck at the next stuck episode, the owner policy requires a preserved handoff and rotation to another eligible unclaimed residue-10 HARD source; a third E0082 recovery is not authorized.

If a genuine source-metric or source-relevant lower-bound breakthrough occurs before that mandatory handoff point, the fresh methods reserved for the mathematical attempt are **#6 DEFORM TO A POINT YOU CAN SOLVE, #22 READ THE FAILURES NOT THE SUCCESSES, #30 ONE SCALE / ONE DIRECTION AT A TIME**. Concretely: derive (6.4)'s dyadic-scale mean and covariance contributions, compare the endpoint-conditioned meander to the solved positive-walk kernel without dropping the endpoint mark, and stop immediately if the `O(log n)` variance / `Omega(log n)` mean pair cannot be closed.

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  source_id: E0082
  claim_path: operations/claims/E0082.md
  canonical_dedup_key: pitman_tang::op_2_3
  shard_residue_mod_13: 10
  category: HARD_OUTSIDE
  status: PARTIAL
  frozen_metric: gamma_FP
  metric_before: 1
  metric_after: 1
  movement: false
  methods_actual:
    1: "Time/sign reversal maps first-passage patterns to endpoint-conditioned positive meanders and transposes the matching matrix; the solved full-positive stochastic-row invariant is lost exactly at endpoint conditioning."
    21: "Pitman--Tang's later moving-window argmin/Feller-chain work supplies a Markov/extrema framework, but the unmarked argmin state omits the source-required height drop; an augmented kernel is still needed."
    28: "Thresholding column loads reduces the Peres lower order to an O(1/log n) lower-tail bound for the exact first-passage column-load functional; sufficient moment target E[D]>=a log n and Var(D)<=C log n isolated."
  recovery_choice: "port the technique from the nearest solved problem"
  unchanged_runs_before: 3
  unchanged_runs_after: 4
  stuck_recoveries_before: 1
  stuck_recoveries_after: 2
  audits:
    P26: NOT_PASSED
    NM13-12: NOT_PASSED
  substantive_artifacts_created: []
  literature_check_date: 2026-09-18
  literature_scope: "original Pitman--Tang source; exact first-passage/waiting-time queries; later Pitman--Tang argmin-process and extreme-order-statistics papers; source-matching resolution search"
  literature_access_limits: "bounded public-web search and repository source history; absence of a hit is not proof of worldwide openness or novelty"
  next_step: "Attempt exact first/second moment bounds for the column-load functional under the conditioned first-passage bridge using reflection/Markov kernels. If the next stuck episode arrives without source movement, preserve full handoff and rotate; no third E0082 stuck recovery."
```

No shared root, peer namespace, canonical claim, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified in this invocation.

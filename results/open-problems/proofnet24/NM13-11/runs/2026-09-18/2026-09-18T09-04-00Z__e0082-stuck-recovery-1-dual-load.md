Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `gamma_FP = 1 -> 1`; status `PARTIAL`; STUCK RECOVERY 1. Section-B methods actually tried: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #20 FIND WHY THE ALGORITHM FAILS, #25 COUNT THE SAME THING TWICE.**

# NM13-11 — E0082 stuck recovery 1: quotient dual-load route

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-11`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0082` / `operations/claims/E0082.md`  
Canonical dedup key: `pitman_tang::op_2_3`  
Canonical SHA-256 / shard: `1b4de7c58dbd8e94a7bc807a11a84c8e166fceea6c48cb804038b2f998e7228a`, residue `10 mod 13`

## 1. Runtime controls, continuity, and mandatory reads

The task prompt requests `GPT-6 / maximum`. That is **not** the runtime I can honestly report. The actual model is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this worker, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The exposed task-control schema still provides ordinary task title/prompt, schedule or relative-start fields, timing mode, enabled state, and task-update fields. It still exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore the `GPT-6 / maximum` line remains a prompt request only. Making it binding would require an owner-authorized product/workspace/API/admin surface that exposes model family and reasoning effort as persistent task fields, together with authenticated per-run runtime attestation. `RESULTS.md` records that the historical P26 `You cannot modify this task` failure was authorization-context-specific and that a later P26 full update succeeded from a different authorized context. The lawful workaround for a task that refuses modification is therefore the owning/otherwise-authorized context or platform/admin support, not cloning the job or bypassing access controls. This invocation did not create, edit, disable, or duplicate a schedule and does not claim a support escalation.

Before the mathematics I reread or targeted-search-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0082.md`;
- newest prior own report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T08-24-00Z__e0082-ladder-composition-quotient.md`;
- newest neighboring NM13-12 report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T08-59-30Z__e0086-two-trap-green-upper-bound.md`;
- the E-series intake/source material and substantive historical attempt `E0082-A001`;
- current/historical claim and audit searches.

Large JSONL/root-ledger renders can be connector-truncated, so I used exact IDs, current root files, the canonical claim, exact report paths, targeted source/attempt/claim searches, and the newest neighboring report rather than pretending a truncated aggregate render was a byte-for-byte reread of every historical row.

Pre-write `master` was observed at `9ce8e439f39ce332c894a02a82558f476b619f54`. `E0082` remains exclusively owned by NM13-11. I recovered no release, duplicate ownership, retirement, POSTED settlement, source-status correction, P26 PASS audit, or NM13-12 PASS audit. A disabled or inaccessible task would not release the source in any event.

## 2. Exact source and bounded literature refresh — 2026-09-18

The source remains Jim Pitman and Wenpin Tang, *Patterns in Random Walks and Brownian Motion* (arXiv:1411.0041; Springer LNM 2137). The accessible source PDF still states, in its Section 2.5 / printed page 65 open-problem box, the two exact-asymptotic questions for bridge and negative first-passage families. Immediately below, it records Yuval Peres's conjecture that for every fixed `lambda<0`,

\[
c_\lambda n\log n
\le E T(\mathcal{FP}^{\lambda,n})
\le C_\lambda n\log n.
\]

The repository locator `Open problem 2.3 / Section 2.5` and the accessible PDF's displayed label `Open Problem 1` are a version/locator convention, not different mathematical targets.

I checked the source PDF directly at:

- `https://www.columbia.edu/~wt2319/Patterns.pdf`
- `https://arxiv.org/abs/1411.0041`

and ran bounded dated queries including:

- `"Patterns in Random Walks and Brownian Motion" Pitman Tang first passage waiting time Peres n log n 2026`;
- `"Pitman Tang" "first passage" "n log n" waiting time pattern`;
- `"Patterns in random walks and Brownian motion" "matching matrix" first passage`.

The searches recovered the original source and general pattern-renewal references but no later primary paper claiming the exact first-passage asymptotics or the Peres `Theta(n log n)` statement. This is bounded negative evidence only: web/citation indexing and full-text coverage are incomplete, so **worldwide openness and publication novelty remain UNVERIFIED**.

The source itself is also the nearest solved comparison relevant to the obstruction below. For the positive-walk family, Pitman--Tang prove that its matching matrix is a scalar multiple of a right-stochastic matrix: every row sum is identical. Its inverse therefore preserves the same one-dimensional stochastic structure, yielding the exact asymptotic `E T(M^{2n+1}) ~ 4n`. The first-passage family lacks that row-sum uniformity; Section 2.5 explicitly identifies the more complicated inverse matching matrix as the obstruction.

## 3. Why the stuck protocol is mandatory now

The frozen metric from the canonical claim is

\[
\gamma_{FP}:=
\inf\{\gamma:E T(\mathcal{FP}^{-1,n})=O(n^\gamma)\}.
\]

The admission research run moved the certified interval from

\[
1\le \gamma_{FP}\le \frac54
\]

to the exact exponent value

\[
\gamma_{FP}=1
\]

by proving an `O(n log n)` upper bound. The next run retained `gamma_FP=1` and showed why a uniform-row LP certificate cannot remove the logarithm. The most recent run again retained `gamma_FP=1` while proving the exact ladder-composition quotient `MP=PK` and reducing the inverse/LP problem to weak compositions. Its ledger delta ended with `unchanged_runs=2`, `stuck_recoveries=0`.

Because the same frozen metric has now stayed unchanged for two consecutive post-movement runs, this invocation is the third unchanged run. Under Section I it must be a thinking/stuck run rather than another lemma. I therefore make **no new theorem claim and no new finite certificate claim in this report**. The work below is route diagnosis plus one chosen recovery experiment.

The metric remains deliberately unchanged even though it is saturated at the power-exponent level: the owner instruction forbids silently replacing it by a logarithmic exponent, constant, or a different quotient statistic merely to manufacture movement.

## 4. Section-I five-part stuck report

### (a) Exact statement that blocks

For the source-relevant square subsequence `n=m^2`, let `K_m` be the exact ladder-composition quotient proved in the preceding report, let `c^{(m)}` be the vector of Catalan class sizes, and let

\[
F_m:=|\mathcal F_{m,m^2}|=\mathbf 1^T c^{(m)}.
\]

The preceding quotient theorem gives

\[
\frac1{E T(\mathcal F_{m,m^2})}
=2^{-m^2}(c^{(m)})^T K_m^{-1}\mathbf1,
\]

and the positive packing/covering formulation gives

\[
S_m:=(c^{(m)})^T K_m^{-1}\mathbf1
=\min_{y\ge0,\ K_m^T y\ge c^{(m)}}\mathbf1^T y.
\]

The simplest source-relevant blocker is therefore the following uniform dual-cover estimate:

\[
\boxed{
\text{construct }y^{(m)}\ge0\text{ such that }
K_m^T y^{(m)}\ge c^{(m)},
\qquad
\mathbf1^T y^{(m)}\le
C\,\frac{F_m}{\log(m^2)}
\text{ for all large }m.}
\tag{4.1}
\]

A proof of (4.1), together with the already established upper bound, would give `Theta(n log n)` on the `lambda=-1`, square subsequence. This is not yet the entire source Open Problem, but it is the cleanest unproved source-valid special case.

### (b) Routes tried and the precise reason each stopped

**Historical full matching/correlation system (`E0082-A001`).** The older attempt correctly reduced exact waiting time to the exponentially large matching/correlation system but ran into nonuniform first-hit weights. It did not identify a compressing invariant or a usable positive inverse certificate. Repeating full inversion is therefore not a new route.

**Reversed-overlap / source-first counterexample route (#2/#4/#8).** Reversing the overlap count and exploiting first-passage structure was enough to prove `E T=O(n log n)`, hence `gamma_FP=1`. The failure is one-sided: column/row upper control supplies an upper waiting-time bound, while the Peres lower bound requires proving that the aggregate inverse mass `S_m` is smaller by a logarithmic factor. Bounding a worst row or column cannot do that.

**Uniform LP/extremal route (#11/#13/#24).** Recasting the problem as a positive packing/covering LP showed exactly where a logarithm could enter. But the sharp row-extremal calculation also showed that the worst matching row itself is logarithmic. Any certificate that treats every row with one common scalar therefore pays exactly the logarithm that must be recovered. The obstruction is heterogeneity, not lack of another row-sum estimate.

**Ladder-composition quotient (#14/#16/#18).** The preceding run made real structural progress: it reduced the full exponential matrix to the exact quotient `MP=PK`, with classes indexed by weak compositions and Catalan weights. However, quotienting does not itself create a low-mass dual cover. The remaining dual is still strongly nonuniform across compositions, so the quotient is a new arena rather than the missing inequality.

**Current interpolation/load ideas (#5/#20/#25).** They identify a plausible probabilistic structure for the dual weights, but I do not have a uniform positivity/hazard theorem or a Catalan-conditioned estimate strong enough to prove (4.1). Details are in Sections 5 and 6 below.

### (c) What a proof must contain that the routes do not yet contain

A successful proof needs a **distribution-sensitive averaging mechanism** that recovers a factor `1/log n` from the nonuniform overlap landscape. Equivalently, it needs either:

- a direct feasible quotient dual cover with total mass `O(F_m/log n)`;
- a monotone interpolation whose integrated logarithmic decay is at least `log log n-O(1)`;
- or a renewal/stable-law identity showing that typical Catalan-weighted compositions see enough cumulative overlap mass even though a small exceptional set has near-minimal load.

Every route so far controls extrema or compresses state space. None yet proves that the high Catalan mass lies where the dual can be cheap.

### (d) Simplest special case still unproved

The simplest honest source-valid target is:

\[
\boxed{
E T(\mathcal{FP}^{-1,m^2})
\ge c\,m^2\log m
\quad\text{for all sufficiently large integers }m.}
\tag{4.2}
\]

Since `log(m^2)=2 log m`, this is the square-subsequence form of the Peres lower order. The already proved `O(n log n)` upper bound would then give `Theta(n log n)` on this subsequence. It would remain `PARTIAL` relative to the full source, which asks exact asymptotics and all fixed negative `lambda`.

### (e) Nearest solved problem and the ingredient it has that E0082 lacks

The nearest solved same-framework problem is Pitman--Tang's **positive-walk waiting time**. There, their Lemma 1 proves that the matching matrix has identical row sums and is a scalar multiple of a right-stochastic matrix. Invertibility then immediately transfers that one-dimensional invariant to the inverse and yields `E T(M^{2n+1})~4n`.

For first-passage patterns, the source itself notes that row/column sums vary from order one to much larger scales and that the exact inverse is not understood. E0082 therefore lacks precisely the stochastic one-dimensional quotient that makes the positive-walk proof close. The ladder-composition quotient recovers a finite-dimensional invariant subspace, but not a constant-row one.

## 5. Three genuinely different Section-B attacks in this thinking run

### #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Write the quotient as

\[
K_m=I+Q_m
\]

and deform it by

\[
K_m(t):=I+tQ_m,\qquad 0\le t\le1.
\]

Define formally

\[
S_m(t):=(c^{(m)})^T K_m(t)^{-1}\mathbf1.
\]

Then wherever the inverse exists,

\[
S_m'(t)
=-(c^{(m)})^T K_m(t)^{-1}Q_mK_m(t)^{-1}\mathbf1.
\tag{5.1}
\]

If one could prove throughout `0<=t<=1` that the relevant left and right inverse vectors stay nonnegative and that

\[
-\frac{d}{dt}\log S_m(t)
\]

has integral at least `log log(m^2)-O(1)`, then

\[
S_m(1)\le C F_m/\log(m^2),
\]

which is exactly the missing dual scale.

**Outcome:** the deformation gives a clean scalar target, but the needed positivity and lower hazard bound are not established. Entrywise positivity of `K_m(t)` is not enough to make its inverse positive. This route stops at a real sign problem, not at a missing algebraic manipulation.

### #20 — FIND WHY THE OBVIOUS DUAL ALGORITHMS FAIL

For a target composition `s`, define the Catalan-weighted incoming quotient load

\[
D_m(s):=
\frac{((c^{(m)})^T K_m)_s}{c^{(m)}_s}.
\tag{5.2}
\]

A uniform dual `y=alpha c` can be feasible only after scaling by the smallest `D_m(s)`. The quotient has boundary compositions with load close to the identity contribution, so this construction cannot visibly produce the required `1/log n` total mass. It is the quotient analogue of the already rejected uniform-row certificate.

A less symmetric candidate is the reciprocal-load ansatz

\[
y_s\propto \frac{c_s}{D_m(s)}.
\tag{5.3}
\]

This at least discounts heavily covered classes. The recovery computation in Section 6 tested whether (5.3) is remotely compatible with dual feasibility before spending another run proving estimates for it.

**Outcome:** small quotient diagnostics do not immediately refute (5.3), but neither the cover inequality nor the asymptotic average `sum_s c_s/D_m(s)=O(F_m/log n)` is proved. The route remains viable only if both can be obtained uniformly.

### #25 — COUNT THE SAME OVERLAPS TWICE

The quotient load (5.2) can be read in two ways: sum first over source composition classes, or sum first over overlap shifts of an individual target first-passage word and then average over its target class. This suggests that the right asymptotic object is not an extremal composition but a **Catalan-weighted random composition**.

The class weights from the already-proved quotient theorem are

\[
c_r=\prod_{j=1}^m C_{r_j},
\qquad \sum_j r_j=N.
\]

Equivalently, after multiplying every class by the same conditioning constant, this is the law of `m` iid variables with

\[
P(X=k)=\frac{C_k}{2\,4^k},
\]

conditioned on `X_1+\cdots+X_m=N`. This is only a change of language for the existing Catalan class-size formula, not a new theorem claim here. The tail is of `k^{-3/2}` type, so stable/renewal methods are a natural candidate for estimating typical incoming load.

A second double count, performed only as scratch route selection in this stuck run, suggests expressing an individual target column load through the target's prefix heights and exact first-passage probabilities. I am **not promoting that scratch identity as a theorem in this no-new-claims run**. If this route is used next, the first obligation is to write and certify that identity cleanly before invoking any asymptotic renewal theorem.

**Outcome:** this is the most promising new language because it attacks the missing average rather than the worst class. Its present gap is a quantitative conditioned-heavy-tail estimate tied to the overlap load, not a finite combinatorial identity.

## 6. Chosen stuck recovery: reduce the obstruction to a finite computation and run it

Section I allows exactly one recovery choice. I choose:

**REDUCE THE OBSTRUCTION TO A FINITE COMPUTATION AND RUN IT.**

Using the exact quotient formula already certified in the preceding run, I evaluated the quotient LP route for square sizes `m=2,3,4,5` as a **non-certified floating-point diagnostic only**. The computation tested the reciprocal-load proposal (5.3), the classwise dual coverage it induces, and the exact quotient optimum numerically.

The diagnostic did **not** produce a source theorem and is not being archived as a certificate. Its only route-selection conclusion is:

- the reciprocal-load cover is not immediately destroyed by the first four square sizes;
- a modest rescaling made it classwise feasible in each tested finite quotient;
- but its total mass at these small sizes is still far too pre-asymptotic to infer a `1/log n` law;
- therefore the next proof attempt must target the two analytic inequalities below, not extend the same finite table.

The route is reduced to proving, uniformly in `m`, some fixed `a>0` and `C<infinity` with

\[
\inf_s
\frac1{c_s}
\sum_r K_m(r,s)\frac{c_r}{D_m(r)}
\ge a,
\tag{6.1}
\]

and

\[
\sum_r\frac{c_r}{D_m(r)}
\le C\frac{F_m}{\log(m^2)}.
\tag{6.2}
\]

If (6.1)--(6.2) hold, then

\[
y_r:=a^{-1}\frac{c_r}{D_m(r)}
\]

is a feasible dual with the source-required logarithmic mass. The computation justifies spending one recovery episode on these inequalities; it does not count as mathematical movement and does not establish either one.

No new checker or output artifact was committed because this is explicitly a thinking-only stuck run with no promoted finite claim. Manufacturing a certificate for a diagnostic would violate the owner instruction's research/checking balance.

## 7. Next step and hard-source recovery counter

The next run should **not** compute more quotient sizes. It should attempt one proof route for (6.1)--(6.2), starting from the conditioned Catalan product law and the shift/first-passage double count. The first target should be an exact formula for the class-averaged incoming load as a functional of the conditioned ladder composition; only then should stable-local-limit or renewal estimates be imported.

If that route fails without moving the source quantity, use a different Section-B triple and the second/final allowed stuck-recovery episode. A third stuck episode on E0082 must leave a complete handoff and rotate to another eligible unclaimed residue-10 hard source. Do not reset the counters merely because the power exponent `gamma_FP=1` is already saturated.

No closure is claimed. The source remains `PARTIAL`; exact asymptotics are unresolved here. P26 and NM13-12 audits are both **NOT PASSED / not recovered**. No paper folder is warranted.

## 8. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-11
  category: HARD OUTSIDE
  source_id: E0082
  claim_path: operations/claims/E0082.md
  canonical_dedup_key: pitman_tang::op_2_3
  source_status_before: PARTIAL
  source_status_after: PARTIAL
  metric_name: gamma_FP
  metric_definition: "inf{gamma : E T(FP^{-1,n}) = O(n^gamma)}"
  metric_before: "1"
  metric_after: "1"
  metric_movement: false
  no_movement: true
  stuck_protocol_triggered: true
  methods_attempted: [5, 20, 25]
  method_outcomes:
    5: "K(t)=I+t(K-I) turns the missing logarithm into an integrated log-derivative target, but inverse-vector positivity and the hazard lower bound are unproved."
    20: "Uniform dual weights structurally cannot recover the logarithm; reciprocal incoming-load weights remain plausible but need two uniform inequalities."
    25: "Double counting redirects the problem to Catalan-weighted conditioned compositions and a first-passage/renewal load functional; no new theorem is promoted in this stuck run."
  recovery_choice: "reduce the obstruction to a finite computation and run it"
  recovery_outcome: "Non-certified quotient diagnostics for m=2..5 did not refute the reciprocal-load dual route; proof obligations isolated as (6.1)-(6.2). No finite result is claimed."
  unchanged_runs_before: 2
  unchanged_runs_after: 3
  stuck_recoveries_before: 0
  stuck_recoveries_after: 1
  hard_recovery_limit: 2
  audits:
    P26: NOT_PASSED
    NM13-12: NOT_PASSED
  literature_check_date: 2026-09-18
  literature_scope: "Original Pitman-Tang source PDF/arXiv plus bounded web queries for first-passage waiting time, Peres n log n, matching matrix, and later resolution."
  literature_outcome: "No source-matching later primary resolution located in bounded search; worldwide openness/publication novelty UNVERIFIED."
  substantive_artifacts_created: []
  next_step: "Try to prove quotient reciprocal-load inequalities (6.1)-(6.2) from the Catalan-conditioned ladder-composition law and an exact overlap double count; do not extend the finite table."
```

## 9. Write discipline

This invocation writes exactly this one immutable report under the NM13-11 namespace. It does not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign roots, a peer namespace, the canonical claim, any workflow, permission, public surface, email/Drive resource, paid-compute resource, or schedule. Readback is to be performed at the creation commit with no receipt-only follow-up commit.

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`; successor-gate unchanged count remains `UNKNOWN`. Methods **#7 TAKE THE LIMIT, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #24 FIND THE EXTREMAL OBJECT**.

# R15 CLOSABLE OUTSIDE — successor admission, Schur extremality and tropical tie strata

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, exact Brownian source, and exclusions

I continued from the newest R15 immutable report

`runs/R15/20260918_0726Z_successor_admission_f0111_homogeneous_k2_h52b.md`.

I also read the newer neighboring F0111 handoff

`runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`

before doing new mathematics. I do not rederive or relabel R20's radial-sublinearity, symmetric-certificate reduction, first-order tropical limit, or unique first-order projective certificate.

The original R15 target remains operationally retired after the mandatory six unchanged runs. I reread both the source and the controlling six-run handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`.

The exact source is Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.2. Definition 2.1 and Problem 7.2 say:

- `X=(X_t)_{t in R}` is an FBM if there are random times `S_n -> -infinity` a.s. such that every shifted future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is a BBM iff the time-reversed process is an FBM;
- `X` is a 2BM iff there is a random time `S` at which the two centered half-paths are **independent standard Brownian motions**;
- Problem 7.2 assumes `X` is both FBM and BBM and that there exists an **arbitrary finite random real time** `T` such that the two complete centered half-path processes

  `(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

  are independent, and asks whether these assumptions force `X` to be 2BM;
- there is no stopping-time or splitting-time assumption on `T`, and neither seam half is separately assumed Brownian;
- Problem 7.5 is a different question and remains excluded.

The source itself emphasizes the distinction: Proposition 6.2 rules out an independent seam with a Brownian future for its own non-2BM example, whereas Problem 7.2 deliberately drops the Brownian-half requirement.

The two concrete R15 counterexample candidates remain eliminated. The source Theorem-6.1 FBM+BBM non-2BM candidate has no source-required independent real seam. The later alternating Brownian-prefix/BES candidate has an independent seam but was proved to be 2BM by finite-intensity excursion-Palm de-biasing. Hence there is **no surviving frozen counterexample candidate** whose obligation count can honestly be advanced. The marked Brownian-cell / sparse copied-continuous-block construction in the six-run handoff is only a future architecture, not a verified candidate. I therefore preserve the historical Brownian metric at `2/4` and do not manufacture movement.

### 2026-09-18 source / later-literature check

I checked the UW-hosted source PDF, including Definition 2.1 and the actual Problem 7.2 page, exact-title / exact-problem searches, later-author pages, and accessible citing-paper results. The current Burdzy open-problems page still lists a related bounded-concatenated-pieces problem, but does not itself state a resolution of exact Problem 7.2. Accessible citation results recover, among other things, Pitman--Tang's Brownian spacetime-shift work, but I found no accessible later source explicitly claiming to settle exact Problem 7.2. This is **bounded negative evidence only**, not a worldwide openness certificate.

The current campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest implementation manifest `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, and the newest coordinator status `operations/task_health/runs/2026-09-18T075300Z/status.md` were also reread. The coordinator still reports no newly certified free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor. I therefore create no ownership claim.

The successor-admission metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

## 2. Successor-screening source retained for mathematics only: Talagrand Problem 10.9

I continued F0111 only as **successor-screening mathematics**, not as an admitted R15 assignment.

Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 asks whether there is a universal `gamma>0` such that every cardinality threshold

`A_{n,k}={X subset [n]: |X|>=k}`

belongs to his class `C_gamma`.

Under `zeta_t`, the coordinates are independent with

`P_t(i in X)=1-exp(-t_i)`.

Write

`F_{n,k}(t)=-log P_t(|X|<k)`.

The `C_gamma` condition requires that for every base point `q>=0` there be a multilinear polynomial with nonnegative coefficients and no constant term,

`P_q(t)=sum_{empty != I subset[n]} beta_I(q) t_I`, `beta_I(q)>=0`,

such that

`F_{n,k}(t)<=P_q(t)` for all `t>=0`

and

`P_q(gamma q)<=gamma F_{n,k}(q)`.

The source proves endpoint cases (including the all-elements class through its two-variable composition machinery) but leaves the general cardinality-threshold problem as Problem 10.9.

A fresh 2026-09-18 exact-title / `Problem 10.9` / `C_gamma` search recovered the source and later threshold/Poisson-binomial/majorization literature, but no accessible theorem explicitly resolving the exact heterogeneous-`q` positive-multilinear-majorant problem. Majorization of symmetric Bernoulli functionals is classical machinery, so the mechanism below should be treated as **potentially folklore / prior-art-risk**, not as a novelty claim. Search failure is not a novelty certificate.

Previous R15 work established the global FKG envelope `F_{n,k}(t)<=e_k(t)`, an exact boundary-lifting lemma, a no-go theorem for the natural exchangeable one-orbit dual counterexample family, and the full homogeneous `k=2` certificate with universal `gamma=1/4`. R20 independently developed gap identities, radial sublinearity for `k=2`, symmetric-certificate reduction, and the first-order tropical limit. This run deliberately attacks a different question: **which inhomogeneous activity vector is extremal when the total hazard is fixed, and what is the exact next-order tropical defect?**

## 3. Exact formula and the small-case reconnaissance — method #16

Put

`y_i=exp(t_i)-1`,

`Z_{k-1}(y)=sum_{r=0}^{k-1} e_r(y)`.

Then

`P_t(|X|<k)=exp(-sum_i t_i) Z_{k-1}(y)`,

so

`F_{n,k}(t)=T-log Z_{k-1}(exp(t_1)-1,...,exp(t_n)-1)`,       (3.1)

where `T=sum_i t_i`.

I first expanded the derivative differences in the smallest nontrivial cases (`n=3,k=2` and `n=4,k=3`) looking for a sign change that would defeat homogeneous extremality. The cancellation was exact and suggested the general identity proved below. These small cases were **reconnaissance only**; no finite enumeration or numerical path sample is being used as verification, so there is no finite checker claim to archive.

## 4. Method #24 — FIND THE EXTREMAL OBJECT: the homogeneous hazard vector is globally worst at fixed total hazard

The clean general identity is stronger than the Jensen bound used in the preceding `k=2` theorem.

### Theorem R15-F0111-SCHUR

Fix `2<=k<=n`. The function

`D_{n,k}(t)=log Z_{k-1}(exp(t_1)-1,...,exp(t_n)-1)`

is Schur-convex on `R_+^n`. Consequently

`F_{n,k}(t)=sum_i t_i-D_{n,k}(t)`

is Schur-concave. In particular, if `T=sum_i t_i`, then

```
F_{n,k}(t)
 <= F_{n,k}((T/n) 1_n)
 = T-log[ sum_{r=0}^{k-1} binom(n,r) (exp(T/n)-1)^r ].       (4.1)
```

Thus among **all** inhomogeneous activity vectors with the same total exponential hazard parameter `sum t_i`, the homogeneous vector maximizes the cardinality-threshold hazard `F_{n,k}`.

#### Proof

Write

`Z(t)=Z_{k-1}(exp(t_1)-1,...,exp(t_n)-1)`.

Fix two indices `i != j`, and let `z` denote the `n-2` variables `y_l=exp(t_l)-1` with `l` different from `i,j`. Set

`A=sum_{r=0}^{k-2} e_r(z)`,

`B=sum_{r=0}^{k-3} e_r(z)`,

with the convention that an empty sum is zero. Since

`partial Z / partial y_i = A+y_j B`,

and `dy_i/dt_i=1+y_i`, we have

`partial_i Z=(1+y_i)(A+y_j B)`,

`partial_j Z=(1+y_j)(A+y_i B)`.

Subtracting gives the exact cancellation

```
partial_i Z-partial_j Z
  =(y_i-y_j)(A-B)
  =(y_i-y_j)e_{k-2}(z).                                   (4.2)
```

Every factor on the right except `y_i-y_j` is nonnegative, and `y_i-y_j` has the same sign as `t_i-t_j`. Therefore

`(t_i-t_j)(partial_i Z-partial_j Z)>=0`.

The standard differential criterion for symmetric `C^1` functions now shows that `Z` is Schur-convex. Because `Z>0` and `log` is increasing,

`D=log Z`

is also Schur-convex; equivalently one can divide (4.2) by `Z` and apply the same criterion directly.

The linear symmetric function `T=sum_i t_i` is constant on every majorization class, hence `F=T-D` is Schur-concave. For fixed total `T`, every `t` majorizes the uniform vector `(T/n)1_n`. Schur-concavity therefore gives

`F(t)<=F((T/n)1_n)`.

Substitution into (3.1) gives the displayed formula (4.1). QED.

### What this changes

This is a genuine structural reduction. The source's difficulty is not caused by a hidden inhomogeneous maximizer of `F` at fixed total hazard: the worst hazard is exactly the homogeneous point. Any failure of Talagrand's positive-polynomial budget must instead come from the **geometry of positive multilinear majorants versus the chosen base point**, not from the raw threshold hazard becoming larger under unequal activities with the same total.

For `k=2`, (4.1) recovers and generalizes the convexity/Jensen lower bound on the logarithmic denominator used in the preceding R15 certificate. For all `k`, it gives the same type of exact radial extremal statement at once.

I do not claim this theorem is new. The derivative criterion and majorization mechanism are classical, and related Schur-convexity/concavity results for Poisson-binomial quantities exist in the literature. The exact `(t_i=-log(1-p_i))` threshold-hazard formulation should be prior-art checked before any publication use.

## 5. Method #7 — TAKE THE LIMIT: exact second-order tropical defect lives on tie strata

R20 proved the first-order projective limit

`F_{n,k}(Lx)/L -> sum_{j=k}^n x_(j)`

when the coordinates are ordered

`x_(1)>=...>=x_(n)>=0`.

The first-order limit deliberately forgets which subsets tie for the leading monomial. Keeping the next term gives a precise correction.

### Theorem R15-F0111-TIE

Fix `2<=k<=n` and `x in R_+^n`, sorted decreasingly, and assume

`a:=x_(k-1)>0`.

Let

`b = #{i: x_i>a}`,

`r = #{i: x_i=a}`.

Then `b<=k-2` and `b+r>=k-1`. Put

`M(x)=binom(r,k-1-b)`.

As `L->infinity`,

```
F_{n,k}(Lx)
 = L sum_{j=k}^n x_(j) - log M(x) + o(1).                  (5.1)
```

Equivalently, the exact `O(1)` tropical defect is the logarithm of the number of maximizing `(k-1)`-subsets.

#### Proof

From (3.1), the only nontrivial term is

`Z_{k-1}(exp(Lx_1)-1,...,exp(Lx_n)-1)`.

Because `x_(k-1)>0`, any monomial with fewer than `k-1` selected positive coordinates has strictly smaller exponential rate than the maximum. Among the degree-`k-1` monomials, the maximal exponential rate is

`S_* = sum_{j=1}^{k-1} x_(j)`.

A maximizing `(k-1)`-subset must contain every coordinate strictly above the boundary value `a` and choose exactly `k-1-b` coordinates from the `r` coordinates tied at `a`. Therefore the number of maximizing monomials is exactly

`M(x)=binom(r,k-1-b)`.

Each maximizing product has leading coefficient one, while every other term has strictly smaller exponential rate. Hence

`Z_{k-1}=exp(L S_*)[M(x)+o(1)]`,

and therefore

`log Z_{k-1}=L S_*+log M(x)+o(1)`.

Substituting into `F=L sum_i x_i-log Z_{k-1}` proves (5.1). QED.

### Consequences

1. **Generic rays have no constant defect.** If no tie crosses the selection boundary between positions `k-1` and `k`, then the maximizing `(k-1)`-subset is unique, `M(x)=1`, and

   `F_{n,k}(Lx)=L sum_{j=k}^n x_(j)+o(1)`.

2. **Tie hyperplanes carry the entire fixed-ray `O(1)` defect.** If a tie crosses the cutoff, then `M(x)>1` and the correction is the explicit negative constant `-log M(x)`.

3. **The homogeneous ray recovers the known constant.** If `x=a 1_n` with `a>0`, then `b=0`, `r=n`, so

   `F_{n,k}(La1_n)=(n-k+1)La-log binom(n,k-1)+o(1)`.

This sharpens the neighboring first-order tropical handoff. The second-order obstruction is not confined to the full projective diagonal: it is supported on the entire finite union of **cutoff-tie strata** where the top `(k-1)`-subset ceases to be unique.

The assumption `x_(k-1)>0` is deliberate. At the zero boundary, lower-degree terms can share the same exponential rate and the multiplicity formula changes; I do not silently extend (5.1) to that case.

## 6. What the three moves say about the next route

The combined picture is now unusually rigid.

- Method #24 shows that the raw hazard itself is maximized by homogenizing `t` at fixed `sum t_i`.
- Method #7 shows that at high activity the first nontrivial projective correction is combinatorial and lives exactly on cutoff-tie strata.
- Method #16 found no small-case sign reversal; instead it exposed the exact derivative cancellation (4.2), which then proved the all-`n,k` theorem.

This points to a more specific remaining Talagrand mechanism: if the full source problem fails, a counterexample is unlikely to come from a generic large homogeneous ray or from merely spreading a fixed total hazard unevenly. The plausible obstruction is a **multiscale heterogeneous base point whose positive-polynomial budget is forced to pay simultaneously on several cutoff-tie strata**. Conversely, a positive proof should try to build mixed-degree coefficients adapted to the finite lattice of tie strata and use Schur-concavity to control the interiors between them.

That is a genuinely different route from R20's rejected gap-by-gap certificate and from R15's previous pure-degree / one-orbit dual attacks.

## 7. Admission, ownership, and rotation disposition

Despite the mathematics above, F0111 is still only a screening lead. It is broad, requires one universal constant over every `n,k,q`, and is not currently certified `READY + CLOSABLE`. Recent fleet screens also treat it as an active pending lead rather than free dispatch inventory. I create no claim and do not overwrite another owner.

The current coordinator status still reports zero newly certified READY reserve items in its bounded screen. Therefore

`E_ready: 0 -> 0`.

The Brownian source remains `OPEN / PARTIAL / RETIRED-HANDOFF` at historical `2/4`; this run does not reopen it and does not alter the six-run retirement count.

If F0111 remains unadmitted after the next R15 successor-screening invocation, that invocation should be a handoff/admission run rather than another chain of lemmas. The next fresh method triple for that decision is **#6 DEFORM TO A POINT YOU CAN SOLVE, #8 DISCRETIZE, #12 FIND WHAT IS CONSERVED**.

No checker was created this run. Both new claims are theorem-sized analytic statements with complete proofs on the page, and no finite enumeration is asserted as evidence. Manufacturing a checker for an unchanged admission metric would violate the 90/10 instruction.

## 8. Model / scheduler / denied-task boundary

The model-control limitation is still true in the interface actually exposed to this worker. The task-management surface offers prompt/title, schedule or relative-start data, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution field**. GPT-6 / maximum therefore remains prompt-only; this run actually identifies itself as GPT-5.6 Sol with reasoning level UNVERIFIED.

Changing this requires an eligible owner/platform/backend control that actually exposes model and reasoning fields and attests that they were honored, or product/platform support. It cannot be fixed honestly by inserting stronger prompt text.

`operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records that one P26 modification attempt (native ID `6aa7b43682948191b697d72fec69d539`) returned `You cannot modify this task` in that authorization context. Later root reconciliation records that a full P26 update succeeded from another authorized context. The lawful workaround is therefore the owning/authorized context, supported owner/admin reassignment, or platform support — **not** creating a duplicate task or bypassing permissions. No scheduler or permission change was attempted in this run.

No Gmail, email, Drive, public posting, purchases, paid compute, permission changes, shared-root edits, peer-track edits, or schedule changes were made.

## 9. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  original_source:
    id: I0076
    citation: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.2"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    frozen_metric: "number of four source-matching obligations for one frozen counterexample candidate"
    before: "2/4"
    after: "2/4"
    surviving_frozen_candidate: false
    retirement_unchanged_count: 6
    problem_7_5_excluded: true
  successor_admission:
    metric: E_ready
    before: 0
    after: 0
    unchanged_count: UNKNOWN
    status: "SUCCESSOR_ADMISSION_REQUIRED"
  screening_lead:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    ownership: "NOT CLAIMED BY R15; ACTIVE PENDING SCREENING LEAD"
    status: "PARTIAL SCREENING MATHEMATICS / NOT READY"
    new_results:
      - "R15-F0111-SCHUR: F_{n,k} is Schur-concave in hazard coordinates t; homogeneous t maximizes F at fixed sum t_i"
      - "R15-F0111-TIE: exact O(1) high-activity correction -log binom(r,k-1-b) on cutoff-tie strata when x_(k-1)>0"
    novelty: "UNVERIFIED; majorization mechanism likely classical/folklore-adjacent"
  tried_moves: [7, 16, 24]
  remaining_obligation: "admit one source-clean/current-open/ownership-clear genuinely CLOSABLE outside successor; for F0111 itself, construct a uniform q-adaptive mixed-degree positive majorant or a source-valid counterexample"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_0726Z_successor_admission_f0111_homogeneous_k2_h52b.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "operations/task_health/runs/2026-09-18T075300Z/status.md"
    - "Burdzy--Scheutzow source PDF, Definition 2.1 and Problem 7.2, checked 2026-09-18"
    - "Talagrand STOC 2010 Problem 10.9 and current exact-title/majorization searches, checked 2026-09-18"
  audit_ids: []
  checker: null
  next_methods: [6, 8, 12]
  scheduler_model_selector: null
  scheduler_reasoning_selector: null
  authenticated_runtime_model_telemetry: false
  guaranteed_duration_control: false
```

Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains RETIRED-HANDOFF at `2/4`, and I0124 remains RETIRED-HANDOFF with `H_288=112`. Methods used: #7 TAKE THE LIMIT, #16 COMPUTE EVERY SMALL CASE, #26 HUNT THE SPORADIC CASE.**

# R15 CLOSABLE OUTSIDE — successor admission, Bradley Question 8 zero-set screen

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I do **not** reopen Burdzy--Scheutzow Problem 7.2. Its exact source-matching handoff remains controlling: I0076 is `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`. The source's random-time hypothesis remains independence of the two complete centered forward/backward half-paths at an arbitrary finite random time; no deterministic-time substitute, no stopping-time strengthening, no Problem 7.5 work, and no numerical path verification is introduced here.

I also do **not** reopen I0124. Its six-run retirement remains controlling with `H_288=112` and the internally proved interval `236 <= c_{7,3} <= 285`.

Before new screening I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the newest own R15 report, `runs/R15/20260917_2008Z_successor_admission_d0039_j39.md`;
- the latest NEW-METHODS implementation/deployment material, including `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- the current D/G intake ledgers and current canonical claims for nearby candidates;
- the latest coordinator status `operations/task_health/runs/2026-09-17T210000Z/status.md`.

The 21:00Z coordinator pass independently establishes **zero currently free `READY + CLOSABLE + UNASSIGNED` successors on its screened front**. The new NM13 deployment also means ownership is changing quickly, so a search miss from an earlier hour is not treated as permission to claim.

## 2. Admission metric

There is still no lawful current source assignment, so I do not invent a theorem metric for a target that R15 does not own.

The admission-only metric remains

`E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run.`

Before: `E_ready = 0`.  
After: `E_ready = 0`.

The prior report did not authoritatively freeze a stagnation count for this admission metric, so the count is preserved as `UNKNOWN/UNMEASURED` rather than inferred.

No claim is created.

## 3. Fresh ownership/current-front reconciliation

Several superficially attractive queue rows are no longer available:

- `G0002` has a canonical R09 claim and prior runs/handoff;
- `D0007`, `D0009`, `D0010`, `D0030`, `D0031`, and `D0041` have canonical owners/current runs;
- `D0035` is already internally settled in the intake corrections and is not a fresh source;
- the G0010--G0013 front is already owned or reserved by other active tracks;
- G0014 is the same threshold-cascade source target as the H0010 alias and is theorem-sized rather than a finite CLOSABLE residual;
- the latest coordinator screen records the old four-row READY reserve as stale: I0035 is owned, I0055 is known/resolved in corrected scope, and I0066/I0068 are owned.

I therefore did not seize an old queue row or treat `PENDING` as `READY`.

## 4. Candidate D0036 — exact source scope

Outside source: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), Question 8 in Section 6.5.

For a complex centered weakly stationary (CCWS) sequence `X=(X_k)_{k in Z}`, Bradley defines the interlaced linear dependence coefficient `r*(n)` by taking a supremum of normalized covariances of finite linear combinations supported on arbitrary nonempty finite disjoint sets `Q,S subset Z` with `dist(Q,S) >= n`; `Q` and `S` may be interlaced.

The literal source question is:

> What condition on a spectral density function is necessary and sufficient for a CCWS random sequence to satisfy `r*(n) -> 0` as `n -> infinity`?

Fresh 2026-09-17 searches for Bradley Question 8, `r*(n)`, interlaced maximal correlation/linear dependence, spectral density, and later citing work recovered the source and Bradley's nearby spectral-density papers, but no later source giving the requested necessary-and-sufficient characterization. This is bounded negative evidence, not a novelty certificate.

The exact nearby source results matter:

1. Bradley Theorem 6.2 / Helson--Sarason: ordinary `r(n)->0` is equivalent to a density of the form
   
   `f(t)=|p(t)|^2 exp(u(t)+\tilde v(t))`,
   
   with `p` a polynomial and `u,v` continuous real functions; equivalently the density lies in the relevant VMO class.

2. Bradley Theorem 6.3: continuity of the spectral density is equivalent to decay of the two weaker interlaced linear coefficients `zeta(n)` and `kappa(n)`.

3. Bradley Theorem 6.5: a **positive continuous** spectral density is equivalent to `r*(1)<1` together with `r*(n)->0` (equivalently a nearby formulation with ordinary `r(1)<1`).

So Question 8 is not asking about the positive-continuous region. Its unresolved content is what happens when a continuous/VMO density is allowed to have zeros.

## 5. Move #26 — HUNT THE SPORADIC CASE: finite polynomial zeros are exactly tractable

The first useful sporadic class is a spectral density whose zero set comes entirely from a finite filter.

### Lemma (finite-filter sufficient class; screening lemma, not claimed novel)

Let `Y=(Y_k)` be CCWS with strictly positive continuous spectral density `g`. Let

`p(z)=sum_{j=a}^b c_j z^j`

be a nonzero finite Laurent polynomial and put `d=b-a`. Define

`X_k = sum_{j=a}^b c_j Y_{k+j}`.

Then `X` has spectral density `f=|p|^2 g` and

`r*_X(n) <= r*_Y(n-d)` for every `n>d`

(with the obvious convention on positive integer arguments). Consequently

`r*_X(n) -> 0`.

### Proof

Take any finite nonempty disjoint `Q,S subset Z` with `dist(Q,S)>=n`, and arbitrary coefficient families `(alpha_q)_{q in Q}`, `(beta_s)_{s in S}`. Write

`U = sum_{q in Q} alpha_q X_q`,
`V = sum_{s in S} beta_s X_s`.

Expanding the filter gives

`U = sum_{q in Q} sum_{j=a}^b alpha_q c_j Y_{q+j}`,
`V = sum_{s in S} sum_{ell=a}^b beta_s c_ell Y_{s+ell}`.

After combining repeated indices, `U` is a finite linear combination of `Y` supported in `Q+[a,b]`, and `V` is supported in `S+[a,b]`. For every `q in Q`, `s in S`, `j,ell in [a,b]`,

`|(q+j)-(s+ell)| >= |q-s|-|j-ell| >= n-d`.

Hence the two expanded supports are separated by at least `n-d`. By the definition of `r*_Y`,

`|Cov(U,V)| / (||U||_2 ||V||_2) <= r*_Y(n-d)`

whenever the denominator is nonzero; the zero-denominator cases are harmless under Bradley's convention. Taking the supremum over `Q,S` and all coefficients proves

`r*_X(n) <= r*_Y(n-d)`.

Bradley Theorem 6.5 gives `r*_Y(m)->0` because `g` is positive continuous, so the right-hand side tends to zero. The spectral-density identity `f=|p|^2 g` is the standard finite-filter covariance/Fourier calculation. QED.

This is a complete analytic check of the route. No numerical path sample and no checker is needed.

## 6. Move #16 — COMPUTE EVERY SMALL CASE: exact finite-difference family

Take white noise `Y` and

`p_m(z)=(1-z)^m`, `m=1,2,...`.

Then `X_k=(1-L)^m Y_k` is an `m`-dependent finite moving-average/difference sequence with spectral density

`f_m(e^{it}) = |1-e^{it}|^{2m}`

(up to a positive multiplicative constant). For two index sets separated by more than `m`, the expanded white-noise supports are disjoint, so in fact

`r*_{X}(n)=0` for every `n>m`.

Thus zeros of arbitrarily high finite integer order do **not** obstruct interlaced linear mixing. The hard part of Question 8 cannot be merely "the density has a zero" or even "the density has a high-order zero".

The same calculation works for any finite product of polynomial zeros multiplied by a positive continuous factor `g`: finite-order algebraic zeros coming from a finite filter are a source-valid sufficient class.

This exact family is useful diagnostically even though it is almost certainly folklore/a routine corollary of the source machinery. I make no novelty claim.

## 7. Move #7 — TAKE THE LIMIT: the actual missing boundary is infinite/rough zero structure

The finite-filter lemma suggests the correct limiting question. If one approximates a zero-bearing density by

`f_m = |p_m|^2 g_m`

with finite filters `p_m` and positive continuous `g_m`, each approximant can be `r*`-mixing. But Question 8 requires a criterion stable under a limit in which the filter degree, condition number of `g_m`, or geometry of the zero set may degenerate. There is no uniform bound in the preceding lemma unless one also controls the `r*_Y` rates and the filter spans.

This exposes why the obvious approximation argument does not solve the source problem: `r*` takes a supremum over **arbitrarily large interlaced sets**, so weak/uniform convergence of spectral densities does not by itself give uniform control of the corresponding inverse Toeplitz/Gram geometry.

Combining source theorems gives the residual necessary structure:

- `r*(n)->0` implies ordinary `r(n)->0`, hence the Helson--Sarason/VMO factor form of Theorem 6.2;
- the source's interlaced decay also forces continuity through the weaker interlaced criteria in Section 6.5;
- positive continuous densities are already completely characterized by Theorem 6.5;
- finite polynomial zeros times a positive continuous factor are sufficient by the lemma above.

Therefore the unresolved part of D0036 is a **zero-set/outer-factor stability problem inside the continuous VMO/Helson--Sarason class**, not a generic smooth-density problem.

A plausible successful theorem would need a condition that controls the inverses/angles of all separated interlaced trigonometric-polynomial subspaces uniformly as the sets grow. I did not find such a criterion in the bounded current-literature search.

## 8. Why D0036 is still not a lawful CLOSABLE successor

The new screening lemma moves understanding but does not make the source closable. It supplies a broad explicit sufficient subclass, not necessity. The full source quantifier is a necessary-and-sufficient characterization over arbitrary spectral densities, and the hard residual is precisely the possible infinite/rough zero geometry.

The latest coordinator had already labeled D0036 `PENDING / not READY-CLOSABLE` because no bounded deciding route was known. This run sharpens that diagnosis rather than overturning it.

Accordingly:

- D0036 remains open-looking;
- it is **not claimed** by R15;
- it is better suited to a HARD harmonic-analysis/operator lane unless a finite obstruction/complete factorization theorem is found;
- no source-level closure claim is made.

## 9. Beyond Bradley/Virág: quick fresh G-intake screen

To obey the instruction to move beyond the already-screened cluster, I also re-read the 2026 G intake.

- `G0002` looks finite/combinatorial but is already R09-owned and has extensive recovery/handoff history.
- `G0008` (Hammersley--Welsh monotonicity of `n -> P_p(0 <-> (0,n))` on `Z^2`) has no canonical claim in the checked search, but its literal source scope is all `p` and all distances on the lattice and traces back to 1965. Exact small-`n` expansion could test it, but no route was found that would turn finitely many cases into source closure. It is not promoted merely because it is unowned.
- `G0010`--`G0013` are owned/reserved by active tracks.
- `G0014`/`G0015` are continuous-type branching/cascade limit theorems with explicit missing uniform-integrability/tightness inputs; they are HARD, not finite CLOSABLE replacements.

This secondary screen also yields no lawful dispatch.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE OUTSIDE
  active_source: NONE
  retired_preserved:
    I0076:
      source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2"
      metric: "source-matching obligations = 2/4"
      status: "OPEN / PARTIAL / RETIRED-HANDOFF"
      unchanged_count: 6
    I0124:
      source: "Thackeray, cap set problem in AG(7,3)"
      metric: "H_288 = 112"
      status: "PARTIAL / RETIRED-HANDOFF"
      source_interval: "236 <= c_{7,3} <= 285"
      unchanged_count: 6
  admission_gate:
    metric: E_ready
    before: 0
    after: 0
    unchanged_count: UNKNOWN/UNMEASURED
    status: SUCCESSOR_ADMISSION_REQUIRED
  tried_moves: [7, 16, 26]
  screened:
    D0036:
      source: "Bradley (2005), Question 8"
      current_status: "open-looking; bounded fresh search found no source-matching resolution"
      ownership: "no canonical D0036 claim found in checked search"
      finite_filter_lemma: "if f=|p|^2 g with p finite Laurent polynomial and g positive continuous, then r*_f(n)->0"
      disposition: "PENDING/HARD-leaning; NOT CLAIMED"
      remaining_obligation: "necessary-and-sufficient control of zero/outer-factor geometry for arbitrary interlaced supports"
    G0002:
      disposition: "OWNED by R09; excluded"
    G0008:
      disposition: "open-looking but source-wide all-p/all-distance lattice statement; no bounded closure route; NOT CLAIMED"
    G0014_G0015:
      disposition: "HARD continuous-type branching/cascade theorems; NOT CLAIMED"
  evidence:
    repository:
      - "runs/R15/20260917_2008Z_successor_admission_d0039_j39.md"
      - "operations/task_health/runs/2026-09-17T210000Z/status.md"
      - "operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md"
      - "probability_1000_intake_D_20260908/problems.jsonl"
      - "probability_1000_intake_G_20260910/problems.jsonl"
      - "operations/task_health/runs/2026-09-17T080300Z/queue_screening.md"
    literature_queries_date: "2026-09-17"
    literature:
      - "Bradley, Probability Surveys 2 (2005), Question 8 / Theorems 6.2--6.5"
      - "Bradley, A criterion for a continuous spectral density, J. Multivar. Anal. 86 (2003)"
      - "Helson--Sarason spectral characterization as quoted in Bradley Theorem 6.2"
  audit_ids: []
  new_source_claims: 0
  new_finite_claims: 0
  checker: none
  claim_created: false
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 11. Next admission methods

If the gate remains empty on the next invocation, do not repeat the present triple. Suggested fresh moves are:

- **#8 GO THE OTHER WAY AND DISCRETIZE** — prefer sources whose full obstruction can be encoded in a genuinely finite object;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE** — identify finite constants/thresholds that coincide with a solved neighboring classification;
- **#30 ONE SCALE, ONE DIRECTION AT A TIME** — screen for a source whose global quantifier decomposes into finitely many independently certifiable local pieces.

Do not return to I0076, I0124, D0039, D0036, or the already-screened G rows unless a controlling source/current-status/ownership change occurs.

## 12. Model / scheduler status

Still true in this run: the exposed task-management surface provides title, prompt, schedule/relative-start, timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry and no guaranteed-duration field. `GPT-6 / maximum` therefore remains prompt text only and is not claimed as applied.

Changing/verifying it requires an eligible owner/platform-side control or platform support that exposes those fields and runtime telemetry. Historical P26 `You cannot modify this task` errors are authorization boundaries; the lawful workaround is the owning authorized context, a supported ownership/admin change, or platform support, never duplication or permission bypass.

No scheduler or permission mutation is made here.

## 13. Delivery discipline

Only this immutable R15 report is written. No checker is manufactured because there is no finite metric movement and the analytic finite-filter lemma is proved directly above. No shared root, queue, claim, peer-track file, email, Drive item, public post, purchase, permission, workflow or scheduler setting is modified.

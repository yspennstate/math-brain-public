Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION-METRIC MOVEMENT: `E_ready: 0 -> 0`; D0046 status is sharpened to `DIRECT_LATER_PARTIAL / DYNAMICAL-SAO-CANDIDATE-EXPLICIT / OPERATOR-CONVERGENCE-STILL-CONJECTURAL / HARD_NOT_READY`; I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. Methods actually used: B1 CHANGE THE CATEGORY, B2 ATTACK THE NEGATION FIRST, B12 FIND WHAT IS CONSERVED.**

# R08 CLOSABLE OUTSIDE — D0046 dynamic-operator screen and OU-semigroup reduction

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. Its controlling R08 history remains RETIRED/FROZEN after six unchanged runs at the fixed source metric `2/3`; the unproved universal free-convolution obligation remains frozen for a future explicit reassignment. I also did not reopen the retired F0083 expanding-tube route, whose fixed candidate failed and was handed off after six unchanged runs.

Before new research I reread/recovered the required current state: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, the newest own R08 report `runs/R08/20260918T0342Z_d0037_polynomial_zero_closure_6e91c4.md`, current intake material, current claim/ownership hits, the freshest available task-health status, and neighboring successor-admission reports including the existing R20 check of D0046. I therefore do not present D0046 as a never-screened problem.

The freshest coordinator status recovered in this run still certifies **zero** newly free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successors on its bounded front. Several apparently attractive historical queue rows are now resolved, occupied, retired, or pending scope. In particular D0047 / Virag Question 9 has an exclusive canonical owner and is not available to R08.

## 2. Admission metric

R08 has no lawfully admitted successor source, so I do not invent a theorem metric. For this admission/research screen only,

`E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run.`

Before: `E_ready = 0`.  
After: `E_ready = 0`.

The unchanged count for this operational admission metric remains **UNKNOWN**; I do not infer it from prior reports.

## 3. D0046: exact source and the current 2026 boundary

D0046 is B. Virag, *Operator limits of random matrices* (ICM 2014), Question 8 on p.25:

> Are there operator limits of matrix-valued (say Hermitian) Brownian motion?

The intake row still carries the old `source_says_open / current_status unverified` description. That is materially too coarse after later work.

The directly source-matching later paper is Alan Edelman, Sungwoo Jeong and Ron Nissim, *On the Limit of the Tridiagonal Model for beta-Dyson Brownian Motion*, arXiv:2411.01633, currently **v3, revised 19 February 2026**. It studies Householder tridiagonalization of the Gaussian beta matrix process. The current abstract states that the fixed upper-left `k x k` tridiagonal process has an explicit limit as `n -> infinity` with `k` fixed; this is proved for `beta=1`, with numerical evidence for `beta=1,2,4`. The paper then proposes a dynamical beta-stochastic Airy operator.

Crucially, the paper itself says the fixed-`k` theorem does **not** recover eigenvalue or operator-limit information. Its Section 5 explicitly leaves the dynamical-operator statement as a problem/conjecture, and notes that spectral extraction needs control on a growing tridiagonal window, heuristically beyond the `n^{1/3}` edge scale. Thus the later paper is a major direct partial answer, not source closure.

Current repository ownership check: direct fetch of `operations/claims/D0046.md` returned 404 immediately before this report. That establishes absence of the canonical claim file at the checked snapshot, not a global theorem of non-ownership. Existing R20 and P13 screens already classify D0046 as partial/HARD, so I do **not** create a claim.

Honest status after this run:

`D0046 = DIRECT_LATER_PARTIAL / DYNAMICAL-SAO-CANDIDATE-EXPLICIT / FIXED-k-ENTRY-LIMIT-PROVED(beta=1) / SOURCE OPERATOR LIMIT STILL CONJECTURAL / HARD / NOT_READY_CLOSABLE`.

## 4. B1 — CHANGE THE CATEGORY: the candidate noise is an infinite-dimensional OU semigroup

The most useful new way to read the Edelman--Jeong--Nissim candidate is not as “white noise changing in time” but as a **stationary Ornstein--Uhlenbeck process on the spatial white-noise Hilbert scale**.

Their OU space-time white noise `xi(t)` is characterized on test functions by

\[
\mathbb E\langle\xi(t),f\rangle\langle\xi(s),g\rangle
 = \int_0^\infty e^{-|t-s|x}f(x)g(x)\,dx.
\]

Let `H=L^2(0,infinity)` and let `M` be multiplication by the spatial variable,

\[
(Mf)(x)=x f(x).
\]

Then the covariance operator from time `s` to time `t` is exactly

\[
S_{|t-s|}=e^{-|t-s|M}.
\]

So the proposed coefficient field is the generalized stationary solution of the Hilbert-space OU equation

\[
\boxed{d\xi_t=-M\xi_t\,dt+\sqrt{2M}\,dW_t,}
\]

where `W_t` is cylindrical Brownian motion on `H` and the equation is understood after pairing against test functions / on the usual negative Sobolev distribution scale.

### Proposition 4.1 (exact Gaussian transition law)

For every `h>=0`, the candidate field has the Gaussian Markov transition

\[
\boxed{\xi_{t+h}=S_h\xi_t+\eta_{t,h},}
\]

in law, where `eta_{t,h}` is independent of `xi_t`, centered Gaussian, and has covariance operator

\[
\boxed{I-S_h^2.}
\]

In particular its one-time marginal is spatial white noise for every `t`.

### Proof

For a centered Gaussian process, the joint law is determined by the covariance. At one time,

\[
\operatorname{Cov}(\langle\xi_t,f\rangle,\langle\xi_t,g\rangle)
=\langle f,g\rangle_H,
\]

so the marginal covariance is `I`. For `h>=0`,

\[
\operatorname{Cov}(\xi_{t+h},\xi_t)=S_h.
\]

If `eta` is independent of `xi_t` with covariance `I-S_h^2`, then

\[
\operatorname{Cov}(S_h\xi_t+\eta)=S_h^2+(I-S_h^2)=I
\]

and

\[
\operatorname{Cov}(S_h\xi_t+\eta,\xi_t)=S_h.
\]

These are exactly the required same-time and cross-time covariance operators. Gaussianity gives equality of the finite-dimensional laws, and the semigroup identity `S_{h+k}=S_hS_k` gives the Markov composition law. ∎

This is an elementary reformulation of the candidate covariance, not a priority claim. Its value is that it converts the temporal part of the proposed dynamical SAO into a standard infinite-dimensional OU-semigroup problem.

## 5. B2 — ATTACK THE NEGATION: rule out the obvious scalar-OU coupling

A tempting but wrong way to make a dynamical stochastic Airy operator is to take one spatial white-noise field and refresh the **whole field at one scalar OU rate**. Concretely, suppose for some constant `c>=0` one tried a stationary Gaussian field with covariance

\[
\mathbb E\langle\zeta(t),f\rangle\langle\zeta(s),g\rangle
=e^{-c|t-s|}\langle f,g\rangle_H.
\]

This cannot have the covariance required by the directly source-matching tridiagonal limit.

### Proposition 5.1 (non-separability no-go)

There is no constant `c` for which

\[
e^{-c h}\langle f,g\rangle_H
=\int_0^\infty e^{-hx}f(x)g(x)\,dx
\]

for every `h>0` and every compactly supported smooth `f,g`.

### Proof

Fix `h>0`. Equality for all test functions would imply that the multiplication functions `e^{-ch}` and `e^{-hx}` agree almost everywhere on `(0,infinity)`. The left side is constant in `x`, while the right side is strictly decreasing in `x`. Contradiction. ∎

Thus a correct dynamical operator cannot be obtained by a single global OU refresh rate, nor by taking independent static SAOs at each time, nor by freezing one static SAO forever. Different spatial scales decorrelate at different temporal rates. The time-space coupling is intrinsically non-separable.

This is again an immediate structural consequence of the 2026 candidate, not claimed as new literature. It is nevertheless a useful route filter: any proof strategy that attempts to couple the dynamics through one scalar interpolation parameter has the wrong covariance before operator convergence is even considered.

## 6. B12 — FIND WHAT IS CONSERVED: the static SAO law is the invariant marginal

The semigroup formulation identifies the conserved object exactly. Spatial white noise is invariant under the field dynamics:

\[
S_h I S_h+(I-S_h^2)=I.
\]

Therefore for each fixed time `t`, the formal operator

\[
\mathcal H_\beta(t)=-\frac{d^2}{dx^2}+x+\frac{2}{\sqrt\beta}\xi_t
\]

has the usual static stochastic-Airy coefficient law. The dynamic problem is therefore **not** to identify new one-time marginals. The entire source-level content lies in the joint-in-time coupling and in proving that the finite matrix process converges to it in an operator topology strong enough to pass spectral information.

This separates two logically distinct tasks that older intake language blurred:

1. **marginal operator law:** already the static SAO at every time;
2. **dynamical operator limit:** establish joint temporal/spatial form or resolvent convergence from matrix Brownian motion and deduce convergence of the edge spectrum as a process.

The first is built into the candidate; the second remains open in the direct 2026 paper.

## 7. The real residual: mesoscopic spatial control, not a missing candidate

The later paper's fixed-`k` theorem is not close enough to spectral convergence by itself. Static soft-edge operator limits live on the `n^{1/3}` tridiagonal spatial scale. The current paper explicitly notes that fixed `k` (and even very slowly growing `k`) is insufficient for operator/eigenvalue information and that one would need a window growing past this edge scale.

The clean residual route is therefore:

- prove joint process-level convergence of the rescaled tridiagonal coefficient fields on `j` up to at least `n^{1/3+epsilon}` (or another window large enough for edge localization), rather than only every fixed `j`;
- obtain uniform-in-time coercivity/tightness of the associated quadratic forms;
- identify the field limit with the OU-semigroup noise above in a topology such as `C([0,T];H^{-1/2-epsilon}_{loc})` or the weighted form topology actually needed by the SAO;
- then pass to strong-resolvent/Mosco-type convergence and spectral trajectories.

I am **not** claiming these bullets form a completed proof. They isolate the precise scale/topology gap. The direct later paper itself says its fixed-corner theorem cannot extract the spectrum, so calling D0046 CLOSABLE from the current material would be dishonest.

A useful conceptual consequence is that the temporal covariance is no longer the mysterious part: at the candidate level it is the explicit semigroup `e^{-hM}`. The hard step is the **simultaneous mesoscopic spatial limit plus uniform temporal form control**.

## 8. Neighbor / ownership checks

- `D0047` (Virag Question 9, Painleve in the bulk) has canonical exclusive claim `operations/claims/D0047.md`, status `CLAIMED / READY / CLOSABLE OUTSIDE`, owned by another native slot. I did not touch it.
- `D0048` (loop equations from limiting operators) has no canonical claim file at the narrow path checked in neighboring work, but current P13/PROB20 screens classify the surrounding Virag operator questions as broad theorem-scale programs unless and until exact scope is frozen. I did not invent a finite subproblem and did not claim it.
- The latest coordinator screen still supplies no free certified READY+CLOSABLE successor to R08.

Therefore no canonical ownership file is created in this run.

## 9. Current-literature statement and limitation

Fresh searches dated 2026-09-18 checked the exact source wording, `dynamical stochastic Airy operator`, `beta-Dyson Brownian motion tridiagonal limit`, and the current version/history of arXiv:2411.01633. The current arXiv page says v3 was revised **19 February 2026**. It still states: fixed-`k` tridiagonal process limit proved for `beta=1`, numerical evidence for `beta=1,2,4`, and a conjectural dynamical beta-SAO whose low eigenvalues should realize the edge-scaled beta-DBM process.

I also checked nearby 2025--2026 operator/Sine-beta/Airy-beta literature returned by those searches. It contains substantial static operator and eigenvalue-process results, but I did not locate a later primary theorem proving the full matrix-Brownian **operator-valued** scaling limit asked by Virag Question 8. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

## 10. Admission conclusion

No lawful CLOSABLE successor is admitted:

\[
\boxed{E_{\rm ready}:0\to0.}
\]

What moved is the **D0046 status map and mechanism**: the old intake should no longer be read as an untouched 2014 question. A 2026-revised paper gives the direct fixed-corner dynamics, an explicit dynamical-SAO candidate and the correct temporally non-separable OU field. The remaining source endpoint is the genuinely operator-level, mesoscopic-space convergence theorem.

No checker is manufactured because there is no finite claim; Propositions 4.1 and 5.1 are analytic and proved on the page. No priority claim is made for either elementary consequence.

The next R08 admission pass should continue beyond the already heavily screened Bradley/Virag block unless a material ownership/status change occurs. Suggested fresh Section-B methods for the next genuinely new candidate: **B7 TAKE THE LIMIT, B16 COMPUTE EVERY SMALL CASE, B26 HUNT THE SPORADIC CASE**.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R08
  lane: CLOSABLE_OUTSIDE
  active_source: NONE
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  predecessors_preserved:
    I0082:
      status: RETIRED_FROZEN
      metric: 2/3
      retirement_count: 6
      active_research: false
    F0083:
      status: RETIRED_HANDOFF
      metric: 1/2
      active_research: false
  admission_metric:
    name: E_ready
    before: 0
    after: 0
    unchanged_count: UNKNOWN
  methods: [1, 2, 12]
  screened:
    D0046:
      source: "Virag 2014, Question 8 (Dynamics)"
      ownership_canonical_path: "absent at checked snapshot"
      before: "source_says_open / current_status unverified"
      after: "DIRECT_LATER_PARTIAL / DYNAMICAL_SAO_CANDIDATE_EXPLICIT / OPERATOR_CONVERGENCE_STILL_CONJECTURAL / HARD_NOT_READY"
      later_primary: "Edelman--Jeong--Nissim, arXiv:2411.01633v3, revised 2026-02-19"
      proved_later: "fixed-k tridiagonal process limit for beta=1"
      candidate_later: "dynamical beta-stochastic Airy operator driven by OU space-time white noise"
      residual: "mesoscopic spatial coefficient convergence beyond edge scale + uniform temporal form/resolvent convergence + spectral-process passage"
      r08_structural_reduction:
        - "candidate noise is stationary Gaussian OU field with semigroup exp(-h M_x)"
        - "static spatial white noise is invariant marginal"
        - "scalar/separable global OU refresh coupling is impossible"
      priority_claim: false
      disposition: NOT_CLAIMED
    D0047:
      disposition: EXCLUDED_CANONICALLY_CLAIMED_OTHER_SLOT
    D0048:
      disposition: BROAD_HARD_NOT_ADMITTED
  theorem_claims_new_for_source_closure: 0
  finite_claims_new: 0
  checker: none
  claim_created: false
  successor_status: SUCCESSOR_ADMISSION_REQUIRED
  next_methods: [7, 16, 26]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 12. Model / scheduler escalation

The model-control limitation is unchanged in the actually exposed task-management surface. It provides title/prompt, schedule or relative start, timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry and no guaranteed hour-long runtime field. Therefore `GPT-6 / maximum` remains request text only and cannot be honestly reported as applied by this worker.

A task returning `You cannot modify this task` is an authorization-context boundary. The lawful remedies are to operate from the authorized owning context, use a supported ownership/admin transfer, or use platform support / a product surface that exposes the required controls. Duplicating the task, editing GitHub, or bypassing permissions does not enforce the runtime model.

No scheduler, permission, email, Drive, public-posting, purchase or workflow change is attempted here.

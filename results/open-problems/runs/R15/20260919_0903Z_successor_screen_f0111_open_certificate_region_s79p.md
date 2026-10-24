Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations remain `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical positive-route `2/4` is only the frozen handoff value, not a live-candidate score. RETAINED-SCREEN MOVEMENT: the Talagrand F0111 `k=2` exact-contact certificate region is now proved to have nonempty **full-dimensional interior** in base space for every `n>=2`: every sufficiently small two-level interior base `(epsilon^m,log2,log2)` from the preceding theorem has an open neighborhood of completely heterogeneous bases carrying positive quadratic global `C_1` certificates. Methods #1 CHANGE THE CATEGORY, #15 BREAK THE SYMMETRY ON PURPOSE, #19 MAKE IT AN ALGORITHM.**

# R15 retained screen — openness of the heterogeneous `k=2` exact-certificate region

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 from PENDING/NOT READY, establish novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Continuity, source fidelity, exclusions, ownership, and current fleet state

I continued from

`runs/R15/20260919_0759Z_successor_screen_f0111_interior_lift_r78e.md`

rather than restarting. Before new mathematics I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the current I-intake record/history for I0076, the controlling six-run I0076 handoff, the newest R15 report, the neighboring R20 F0111 handoff, and the newest coordinator delta available during the run,

`operations/task_health/runs/2026-09-19T085900Z/root_merge_delta.md`.

That coordinator delta says newly certified **free** READY inventory remains `0`; admitted CLOSABLE targets such as P0219/P0459/I0130/E0017 are already owned. It also says retirement/handoff is not ownership release absent an explicit release. A direct current check of `operations/claims/F0111.md` returned 404, but claim absence is not admission: F0111 remains an active PENDING lead with prior attempt history. I therefore created no successor claim and edited no shared root.

### Exact Burdzy–Scheutzow source rechecked

The primary PDF, arXiv:1302.6958v4, Definition 2.1 and Problem 7.2, still gives exactly:

- FBM: there are random origins `S_n -> -infinity` from which the complete centered future is standard Brownian motion;
- BBM: time reversal is FBM;
- 2BM: there is one random origin `S` at which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2 assumes FBM + BBM and existence of an arbitrary random time `T` at which the two complete centered half-processes are independent.

There is no stopping-time assumption on `T`, and neither seam half at `T` is separately assumed Brownian. Problem 7.5 is different and remains excluded.

The controlling handoff remains valid. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam; the later Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved actually 2BM. Hence there is still no surviving frozen counterexample candidate on which the original four-obligation metric can honestly move.

Fresh public searches dated 2026-09-19 used the exact title/arXiv identifier, `Problem 7.2`, later-author terms, and citation terms. They recovered the original paper, the current Burdzy publication/open-problems pages, and a small citation trail, but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only.

For F0111 I rechecked Talagrand's primary PDF, Definition 10.1 and Problem 10.9. Problem 10.9 asks for one universal `gamma>0` for all cardinality up-classes `{X: |X|>=k}` and all base points `q`. Current searches also recovered Ascoli–He–Park–Talagrand, arXiv:2608.11183 (2026-08-11), which reformulates the broader discrete convexity conjecture via `k`-thresholds and proves substantial classes, and Chen Li, arXiv:2609.08967 (2026-09-08), which resolves a fractional version. Neither retrieved source claims the exact positive-multilinear Problem-10.9 statement or the openness theorem below. Search failure is not a novelty certificate; novelty remains `UNVERIFIED`.

## 2. Carried theorem and the new target

For cardinality two write

`F_n(t)=sum_i t_i - log(1+sum_i(exp(t_i)-1))`.                (2.1)

The preceding R15 theorem `R15-F0111-K2-INTERIOR-LIFT` proved that for every fixed `m>=0`, with `n=m+2` and `b=log 2`, there exists `epsilon_m>0` such that every

`q_e=(epsilon,...,epsilon,b,b)`, `0<epsilon<epsilon_m`,       (2.2)

has a strictly positive quadratic multilinear polynomial `P_e` satisfying

`P_e(t)>=F_n(t)` for all `t>=0`,                              (2.3)

and exact contact

`P_e(q_e)=F_n(q_e)`, `grad P_e(q_e)=grad F_n(q_e)`.          (2.4)

Inspecting the four-region proof gives two extra nondegeneracy facts which were used there explicitly:

`{t>=0:P_e(t)-F_n(t)=0}={0,q_e}`,                            (2.5)

and

`Hess(P_e-F_n)(q_e)` is positive definite.                  (2.6)

The previous report suggested splitting the two large coordinates. This run proves substantially more: all coordinates can be perturbed independently.

## 3. Method #1 — change category: exact contact is a positive edge-mass polytope

Fix an arbitrary fully interior base `q in (0,infinity)^n`. Put

`S(q)=1+sum_i(exp(q_i)-1)`, `r_i(q)=exp(q_i)/S(q)`,           (3.1)

`m_i(q)=q_i(1-r_i(q))`, `D(q)=sum_i m_i(q)`,                (3.2)

and

`W(q)=D(q)-F_n(q)`.                                          (3.3)

Consider a positive quadratic polynomial

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`.              (3.4)

At the base `q`, introduce **contact masses**

`a_i=A_i q_i`, `e_ij=B_ij q_i q_j`.                         (3.5)

Since `partial_i F_n(q)=1-r_i(q)`, exact gradient contact is equivalent to

`a_i + sum_{j!=i} e_ij = m_i(q)` for every `i`.              (3.6)

Summing (3.6) gives

`sum_i a_i + 2 sum_{i<j}e_ij = D(q)`.                       (3.7)

Exact value contact is

`sum_i a_i + sum_{i<j}e_ij = F_n(q)`.                       (3.8)

Subtracting (3.8) from (3.7) yields the single total-mass law

`sum_{i<j}e_ij=W(q)`.                                        (3.9)

Conversely, if nonnegative edge masses satisfy (3.9) and

`sum_{j!=i}e_ij < m_i(q)`                                    (3.10)

for every `i`, then defining

`a_i=m_i(q)-sum_{j!=i}e_ij`                                  (3.11)

produces strictly positive singleton masses and therefore a strictly positive quadratic polynomial with exact value and gradient contact.

Thus the local exact-contact problem is an open face of a weighted fractional-degree polytope. This is the category change of the run: instead of perturbing polynomial coefficients directly, transport a positive edge-mass point inside this polytope.

## 4. Method #19 — an explicit transport algorithm for exact contact

I now prove a general stability lemma.

### Theorem R15-F0111-OPEN — nondegenerate quadratic `C_1` certificates persist on an open set of bases

Let `q_* in (0,infinity)^n`. Suppose there is a quadratic polynomial

`P_*(t)=sum_i A_i^* t_i + sum_{i<j}B_ij^* t_i t_j`           (4.1)

such that:

1. every `A_i^*>0` and every `B_ij^*>0`;
2. `P_*>=F_n` on the whole nonnegative orthant;
3. `P_*(q_*)=F_n(q_*)` and `grad P_*(q_*)=grad F_n(q_*)`;
4. the zero set of `G_*=P_*-F_n` is exactly `{0,q_*}`;
5. `Hess G_*(q_*)` is positive definite.

Then there is an open neighborhood `U` of `q_*` in `(0,infinity)^n` and a continuous map `q -> P_q` such that every `q in U` has a strictly positive quadratic polynomial `P_q` with

`P_q(t)>=F_n(t)` for all `t>=0`,                             (4.2)

`P_q(q)=F_n(q)`, `grad P_q(q)=grad F_n(q)`.                 (4.3)

In particular every `q in U` satisfies the base-point `gamma=1` certificate requirement of Talagrand Definition 10.1 for the cardinality-two class.

#### Proof — exact-contact transport

Let

`a_i^*=A_i^*q_i^*`, `e_ij^*=B_ij^*q_i^*q_j^*`.             (4.4)

By Section 3,

`E_*:=sum_{i<j}e_ij^*=W(q_*)>0`.                             (4.5)

For `q` near `q_*` define

`lambda(q)=W(q)/E_*`,                                        (4.6)

`e_ij(q)=lambda(q)e_ij^*`,                                   (4.7)

`a_i(q)=m_i(q)-lambda(q)sum_{j!=i}e_ij^*`.                  (4.8)

At `q=q_*` these are exactly `e_ij^*,a_i^*`. Since all starred masses are strictly positive and `W,m_i` are continuous, after shrinking to a neighborhood `U_0` we have

`lambda(q)>0`, `e_ij(q)>0`, `a_i(q)>0`.                      (4.9)

Moreover `sum e_ij(q)=W(q)` exactly. Define

`A_i(q)=a_i(q)/q_i`, `B_ij(q)=e_ij(q)/(q_iq_j)`.             (4.10)

Then `P_q` built from these coefficients has exact contact (4.3) for every `q in U_0` by (3.6)--(3.11), and `P_q -> P_*` coefficientwise as `q->q_*`.

#### Proof — uniform noncompact control

Because the coefficient inequalities are strict, shrink `U_0` so there are constants `u,v>0` with

`A_i(q)>=u`, `B_ij(q)>=v`                                    (4.11)

for all `q in U_0` and all indices.

For arbitrary `t>=0`, put

`X=sum_i t_i`, `M=max_i t_i`, `B=X-M`,
`Q=sum_{i<j}t_it_j`.                                         (4.12)

Exactly as in the preceding interior-lift theorem,

`F_n(t)<=B`, `Q>=MB`,                                        (4.13)

and hence

`G_q(t):=P_q(t)-F_n(t)>=uM+B(u-1+vM)`.                      (4.14)

Therefore there is one `R<infinity`, independent of `q in U_0`, such that

`M>=R  => G_q(t)>0`.                                         (4.15)

Near the origin, for `X<=1`, the pair-union estimate gives

`F_n(t)<=X^2`,                                                (4.16)

so

`G_q(t)>=uX-X^2>0`                                           (4.17)

on a fixed punctured neighborhood `0<X<delta`, uniformly in `q`.

#### Proof — the moving contact point

By hypothesis `Hess G_*(q_*)` is positive definite. The Hessian of `G_q(t)` is jointly continuous in `(q,t)`. Hence there are `rho>0`, `lambda_0>0`, and a smaller neighborhood `U_1` of `q_*` such that

`Hess G_q(t) >= lambda_0 I`                                  (4.18)

for every `q in U_1` and every `t` in a fixed ball around `q_*` containing the line segment from `q` to all `t` with `||t-q||<rho`.

Since exact contact gives `G_q(q)=0` and `grad G_q(q)=0`, Taylor's formula along that segment yields

`G_q(t)>= (lambda_0/2)||t-q||^2`                             (4.19)

for `||t-q||<rho`. Thus the moving contact remains the unique zero in this neighborhood.

#### Proof — compact middle region

Remove from the fixed box `{M<=R}` a fixed origin neighborhood and a fixed ball around `q_*` small enough to be covered by (4.19) after `q` moves slightly. The remainder `K` is compact. By the exact zero-set hypothesis,

`eta:=min_{t in K}G_*(t)>0`.                                 (4.20)

Coefficient convergence implies uniform convergence `G_q->G_*` on `K`. Shrinking the base neighborhood once more gives

`G_q(t)>=eta/2>0` on `K`.                                    (4.21)

The infinity region, punctured origin neighborhood, moving-contact neighborhood, and compact middle region exhaust the orthant. Therefore `P_q>=F_n` globally. QED.

The important point is that no implicit-function theorem is being asked to preserve global majorization on a noncompact set. Exact contact is transported algebraically by (4.6)--(4.10), while (4.14) supplies a uniform compactification and (4.17)--(4.21) protect the two zero neighborhoods and middle shell.

## 5. Method #15 — break the symmetry completely

Apply Theorem R15-F0111-OPEN to any one of the interior certificates from the preceding theorem. For every fixed `m>=0` and every sufficiently small `epsilon>0`, choose

`q_*=(epsilon,...,epsilon,b,b)`, `b=log2`.                   (5.1)

The preceding four-region proof supplies all five hypotheses of R15-F0111-OPEN:

- every quadratic coefficient is strictly positive;
- global majorization holds;
- contact is exact;
- every region away from `0` and `q_*` has strict positive slack, so the zero set is `{0,q_*}`;
- the contact Hessian is uniformly positive definite.

Therefore:

### Corollary R15-F0111-OPEN-K2 — full-dimensional heterogeneous base patches

For every `n>=2` there exist fully interior points `q_* in (0,infinity)^n` and open sets

`q_* in U subset (0,infinity)^n`                             (5.2)

such that **every** `q in U` has a strictly positive quadratic multilinear global majorant with exact `gamma=1` contact for the cardinality-two hazard.

More precisely, for every fixed `m=n-2` and every sufficiently small `epsilon>0`, there is a radius `rho(m,epsilon)>0` such that all bases

`q=(q_1,...,q_n)`, `||q-q_*||<rho(m,epsilon)`                (5.3)

are certified. The coordinates may move independently. In particular the previously suggested asymmetric family

`(epsilon,...,epsilon,b-delta,b+delta)`                      (5.4)

is certified for all sufficiently small `|delta|`, but (5.3) is strictly stronger: the `m` small coordinates need not remain equal, and the two large coordinates need not have opposite perturbations.

Thus the certified `k=2` base set is not merely a curve or a collection of symmetric strata. It has nonempty **full-dimensional interior** in hazard space for every dimension.

This is genuine movement, but still only a restricted theorem. Talagrand Problem 10.9 quantifies over **all** base points, all `n`, and all `k`, with one universal `gamma>0`. The present result does not cover arbitrary distant heterogeneous `k=2` bases and says nothing yet about `k>=3`.

## 6. Why this is stronger than the previous run

Before this run the strongest theorem gave a one-parameter family of interior bases

`(epsilon^m,b,b)`.                                           (6.1)

Now, around every sufficiently small point on that family, the valid-certificate region contains a genuine open ball in all `m+2` base coordinates. Equivalently, the set of nondegenerate positive quadratic `C_1` contact bases is open, and the R15 construction proves it is nonempty in every dimension.

The new invariant is therefore geometric: the next useful quantity is the boundary of this open certificate region, not another symmetric ray.

No numerical path sample or floating-point grid is used anywhere, and none would certify a Brownian law or the noncompact polynomial majorization.

## 7. Literature / prior-art log

Public queries run on 2026-09-19 included:

- `"Forward Brownian Motion" Burdzy Scheutzow arXiv 1302.6958 Problem 7.2`;
- `"Problem 7.2" "Forward Brownian motion" Burdzy Scheutzow`;
- later-author / citation terms for forward Brownian motion and two-sided Brownian motion;
- `"Are Many Small Sets Explicitly Small" Talagrand Problem 10.9 C_gamma`;
- `"Talagrand" "positive multilinear polynomial" "C_gamma" cardinality threshold`;
- current `k`-threshold / discrete-convexity literature, including arXiv:2608.11183 and arXiv:2609.08967.

Accessible primary sources checked: Burdzy--Scheutzow arXiv:1302.6958v4, Talagrand's STOC preprint PDF, Ascoli--He--Park--Talagrand arXiv:2608.11183, and Chen Li arXiv:2609.08967. Search access does not supply a complete citation graph, so both Brownian-current-status and F0111-novelty conclusions remain bounded. I found no accessible source explicitly settling exact Burdzy--Scheutzow Problem 7.2, no source claiming exact Talagrand Problem 10.9 is solved, and no source stating the open-base-patch theorem above. None of those negative search outcomes is treated as a proof of openness or novelty.

## 8. Validation / audit status

No new checker was created. The new result is a theorem-sized exact-contact/continuity/coercivity argument. Its only finite transcendental signs and the strict Hessian margins are inherited from already archived exact R15 finite cores; a numerical grid would not certify the global statement.

This report is a **self-check**, not an independent audit. Qualified audits for the new theorem: `0/2`.

## 9. Scheduler/model-control truth

The exposed scheduler surface still provides task identity/title, prompt, recurrence/timing mode, enabled state, and notification controls. It provides **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed-duration field**. Therefore `GPT-6 / maximum` remains requested in prompt text only; this run actually reports `GPT-5.6 Sol / reasoning UNVERIFIED`.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary. Later repository evidence records successful modification from an authorized P/C context. The lawful remedy is an owning/authorized or owner/admin product/backend/API surface that exposes and persists model/reasoning routing; do not clone, duplicate, or bypass a protected task. No scheduler or permission change was attempted here.

## 10. Next route

Do not spend the next run on another symmetric special ray. The theorem above identifies the next obstruction as the **boundary of the open `k=2` certificate region**. A useful next attack is to characterize the first loss of feasibility by one of three events:

1. a singleton contact mass reaches zero;
2. the contact Hessian loses positive definiteness;
3. a new global zero of `P_q-F_n` is born away from `{0,q}`.

That turns arbitrary heterogeneous continuation into a bifurcation problem with a concrete first-failure alternative.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  native_source:
    id: I0076
    citation: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
    metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_handoff_positive_route: "2/4 frozen; not a live-candidate score"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    unchanged_count: "6_FROZEN_AT_HANDOFF"
    remaining_obligation: "requires a genuinely new surviving source-valid candidate or a complete implication proof; retirement remains controlling"
  successor_admission:
    free_ready_before: 0
    free_ready_after: 0
    claim_created: false
    reason: "newest coordinator delta says newly certified free READY inventory remains 0; admitted CLOSABLE targets are already owned"
  retained_screen:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, Definition 10.1 / Problem 10.9"
    status: "PENDING / NOT READY / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
    movement: true
    before: "for fixed m, positive exact-contact k=2 quadratic certificates on the one-parameter interior family (epsilon^m,log2,log2) for all sufficiently small epsilon"
    after: "for every n>=2, the k=2 positive quadratic gamma=1 certificate bases have nonempty full-dimensional interior; every sufficiently small two-level base above has an open neighborhood of arbitrary heterogeneous certified bases"
    theorem_ids:
      - R15-F0111-OPEN
      - R15-F0111-OPEN-K2
    remaining_obligation: "determine or cross the boundary of the heterogeneous k=2 certificate region; then address arbitrary q and k>=3/universal gamma; obtain two qualified independent audits before any closure claim"
  methods_this_run:
    - "#1 CHANGE THE CATEGORY — rewrite exact contact as a positive edge-mass polytope"
    - "#15 BREAK THE SYMMETRY ON PURPOSE — perturb every coordinate independently"
    - "#19 MAKE IT AN ALGORITHM — explicit scaling transport q -> (e(q),a(q),P_q)"
  evidence:
    - "Burdzy--Scheutzow primary PDF Definition 2.1 / Problem 7.2 rechecked 2026-09-19"
    - "Talagrand primary PDF Definition 10.1 / Problem 10.9 rechecked 2026-09-19"
    - "runs/R15/20260919_0759Z_successor_screen_f0111_interior_lift_r78e.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "operations/task_health/runs/2026-09-19T085900Z/root_merge_delta.md"
    - "public exact-title/current-literature searches dated 2026-09-19"
  audit_ids: []
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; there is still no surviving frozen counterexample candidate, so the fixed four-obligation metric remains `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, the preceding rational coordinate-face barrier is upgraded to an exact necessary-and-sufficient face cone for every face size, yielding an exact base-only contact obstruction; an exact `(2,9)` stress point proves that every preceding rational subset-face barrier can pass while the exact face cone still detects failure. Methods used in new roles: #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT, #29 ADD THE POINTS AT INFINITY.**

# R15 retained screen — exact coordinate-face cone for the `k=2` threshold hazard

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below about Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, make F0111 READY, establish novelty, solve Talagrand Problem 10.9, or satisfy the fleet's independent-audit closure rule.

## 1. Continuity, source fidelity, ownership, and exclusions

I continued from

`runs/R15/20260919_1811Z_successor_screen_f0111_subset_face_c88v.md`

at creation commit `c66d162c35d1db1f1e8ca0e4cc1c1a0e3872a4df`, rather than restarting.

Before doing new mathematics I recovered/read the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the controlling I0076 six-run handoff, the newest own R15 report, neighboring successor-gate state, and the latest coordinator status visible on `master`, `operations/task_health/runs/2026-09-19T185900Z/status.md`.

The current coordinator still records five enabled CLOSABLE successor gates with no admitted current target and **zero newly certified free READY CLOSABLE additions**. The current R06 successor gate independently records `E_ready: 0 -> 0`; the newly released P0157 item is HARD and the VDH item has been reassigned. I therefore did not steal another worker's target, relabel a HARD target as CLOSABLE, or promote a PENDING queue item.

### Exact I0076 source rechecked

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. for which every centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is BBM iff the time reversal is FBM;
- `X` is 2BM iff there exists one random time `S` for which the complete centered future and past are independent **standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM plus existence of an arbitrary random time `T` for which

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent as complete half-processes forces 2BM. The source does **not** require `T` to be a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is separate and remains excluded.

The controlling I0076 handoff remains unchanged. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES independent-seam candidate was proved actually 2BM. Hence no frozen counterexample candidate survives and the user's four-obligation metric is not honestly scoreable on a current candidate. The historical positive-route `2/4` is only the retired handoff value.

Fresh dated searches on 2026-09-19 for the exact title, exact `Problem 7.2` language, later author work and citing literature recovered the original paper, the authors' forward-Brownian material, and related Brownian path-splitting papers, but no accessible later primary source explicitly claiming to resolve exact Problem 7.2. This is bounded negative evidence, not a worldwide openness certificate.

### Retained F0111 source/current-literature check

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, Problem 10.9, specialized here to the `k=2` cardinality threshold hazard. Fresh 2026-09-19 searches again recovered Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulating the discrete Convexity Conjecture through `k`-thresholds and proving substantial classes, and Park, arXiv:2609.14681 (2026-09-13), giving a dimension-free comparison explicitly described as progress toward the conjecture. I found no accessible current source stating the exact face-cone theorem below. Because the proof is elementary one-variable convex duality, novelty is **UNVERIFIED** and the mechanism should not be advertised as new without a dedicated prior-art search.

### Section-B methods

The preceding run used #3/#25/#30. Earlier F0111 history has already used all 30 method numbers at least once, so a globally never-before-used triple is impossible without falsifying history. This run therefore uses a different nonconsecutive triple in genuinely new roles:

- **#11 DUALIZE** — replace the rational lower envelope by the exact Legendre/Fenchel face cone;
- **#24 FIND THE EXTREMAL OBJECT** — identify the unique tangent line to `f_m(s)/s` that gives the extremal quadratic for each pair mass `B`;
- **#29 ADD THE POINTS AT INFINITY** — compactify the face parameter `s in (0,infinity)` by its `s=0` and `s=infinity` limits, which exactly produce the boundary points `(B,A)=(N_m,0)` and `(0,m-1)`.

The route was written before validation in

`artifacts/R15/f0111_blockbudget_idea_d89w.md`

at creation commit `06fd2f4791469153a475e1da933cbba2bb7e33a7`. The original plan was to combine the preceding rational face barrier with the null-flow budget. Working that plan exposed the real loss: the rational face barrier itself was not the exact coordinate-face condition. I therefore strengthened that ingredient before returning to the graph-flow elimination.

---

## 2. Setup carried from the preceding run

For the `k=2` threshold,

`F_n(t)=sum_i t_i-log(sum_i exp(t_i)-(n-1))`,                (2.1)

and a nonnegative quadratic candidate is

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,              (2.2)

with `A_i,B_ij>=0`.

For a coordinate subset `J` of size `m>=2`, the equal-coordinate ray `t=s 1_J` gives

`f_m(s):=F_n(s 1_J)=m s-log(m exp(s)-(m-1)).`               (2.3)

Writing

`A_J=sum_{i in J} A_i`,
`B_J=sum_{i<j, i,j in J} B_ij`,                             (2.4)

global majorization implies exactly

`A_J s+B_J s^2 >= f_m(s)` for every `s>=0`.                 (2.5)

The preceding run replaced `f_m` by a strict rational lower envelope. This run solves (2.5) **exactly**.

---

## 3. Methods #11 and #24 — exact face cone

Put

`g_m(s)=f_m(s)/s`, `s>0`,                                   (3.1)

with the continuous extension `g_m(0)=0`. Direct differentiation gives

`f_m''(s)=m(m-1)e^{-s}/(m-(m-1)e^{-s})^2 >0`,               (3.2)

and

`f_m'''(s)`
`=-m(m-1)e^{-s}(m+(m-1)e^{-s})/(m-(m-1)e^{-s})^3 <0`.       (3.3)

Define

`B_m(s)=g_m'(s)=[s f_m'(s)-f_m(s)]/s^2`.                   (3.4)

The derivative of `B_m` has numerator

`H_m(s)=s^2 f_m''(s)-2s f_m'(s)+2f_m(s)`.                  (3.5)

Since

`H_m'(s)=s^2 f_m'''(s)<0`,                                  (3.6)

and `H_m(0)=0` by the Taylor expansion at zero, we have

`H_m(s)<0` for every `s>0`. Hence

`g_m''(s)=B_m'(s)=H_m(s)/s^3<0`.                            (3.7)

Thus `g_m` is strictly concave, with

`g_m'(0+)=N_m:=binom(m,2)`,
`g_m'(infinity)=0`,
`g_m(infinity)=m-1`.                                         (3.8)

### R15-F0111-EXACTFACE1 — exact necessary-and-sufficient face condition

For `A,B>=0`,

`A s+B s^2 >= f_m(s)` for every `s>=0`                      (3.9)

holds **if and only if**

`A >= Phi_m(B)`,                                              (3.10)

where:

- if `B>=N_m`, `Phi_m(B)=0`;
- if `B=0`, `Phi_m(0)=m-1`;
- if `0<B<N_m`, there is a unique `s_B>0` satisfying

`B=B_m(s_B)=[s_B f_m'(s_B)-f_m(s_B)]/s_B^2`,                (3.11)

and

`Phi_m(B)=A_m(s_B)` with

`A_m(s)=[2f_m(s)-s f_m'(s)]/s`.                             (3.12)

Equivalently, the nontrivial boundary of the exact face cone is parametrized by

`(B,A)=(B_m(s),A_m(s)), 0<s<infinity`.                      (3.13)

#### Proof

Divide (3.9) by `s>0`:

`A+B s >= g_m(s)`.                                           (3.14)

Therefore the least admissible intercept at fixed slope `B` is

`Phi_m(B)=sup_{s>0}[g_m(s)-B s]`.                            (3.15)

Strict concavity of `g_m` proves the three cases above. If `0<B<N_m`, the unique maximizer solves `g_m'(s_B)=B`, and substituting (3.4) yields (3.12). If `B>=N_m`, concavity and `g_m(0)=0` give `g_m(s)<=N_m s<=B s`, so zero intercept suffices. If `B=0`, the supremum is `lim_{s->infinity}g_m(s)=m-1`. QED.

The boundary has the useful differential identity

`d Phi_m/dB = -s_B`,                                         (3.16)

so `Phi_m` is strictly convex on `(0,N_m)` because `s_B` decreases strictly with `B`.

---

## 4. Method #29 — the two endpoints at infinity are part of the theorem

The face boundary is not complete unless one includes both missing endpoints:

`lim_{s->0+}(B_m(s),A_m(s))=(N_m,0)`,                       (4.1)

`lim_{s->infinity}(B_m(s),A_m(s))=(0,m-1)`.                 (4.2)

This exactly explains the two extreme quadratic strategies:

- pure pair mass `N_m s^2` at the origin end;
- pure singleton mass `(m-1)s` at the infinite-activity end.

Every optimal equal-face quadratic interpolates uniquely between them.

### Strict improvement over the preceding rational barrier

The preceding report proved the strict lower envelope

`f_m(s) > N_m s^2/(1+c_m s)` for every `s>0`,                (4.3)

where `c_m=(2m-1)/3`. Consequently, for every `0<B<N_m`,

`Phi_m(B)`
`> [3/(2m-1)](sqrt(N_m)-sqrt(B))^2.                          (4.4)

Indeed, evaluate the exact supremum (3.15) at the unique maximizer of the rational surrogate. Thus the previous all-subset theorem was a genuine but strictly lossy relaxation everywhere inside the face cone.

---

## 5. Exact base-only obstruction at an interior contact

Suppose a global certificate is exact at an interior base `q>0`. Put

`r_i=exp(q_i)/(sum_l exp(q_l)-(n-1))`,
`x_J=sum_{i in J}r_i`,
`q_* = min_{i in J}q_i`.                                     (5.1)

Exact gradient contact gives

`A_i+sum_{j!=i}B_ij q_j=1-r_i`.                              (5.2)

Summing over `J` yields

`m-x_J`
`=A_J + sum_{i<j in J}B_ij(q_i+q_j)`
` + sum_{i in J,j notin J}B_ij q_j`
`>=A_J+2q_* B_J`.                                            (5.3)

By the exact face cone,

`m-x_J >= 2q_* B_J+Phi_m(B_J)`.                              (5.4)

Taking the infimum over `B>=0` gives an **exact closed form**. From (3.15), for every `B`,

`2q_*B+Phi_m(B)>=g_m(2q_*)`,                                 (5.5)

and equality is attained at `B=g_m'(2q_*)` when `q_*>0`. Therefore:

### R15-F0111-EXACTFACE2 — exact base-only contact test

For every coordinate subset `J`, `m=|J|>=2`, any global nonnegative quadratic certificate exact at an interior base must satisfy

`boxed:`

`m-x_J >= f_m(2q_*)/(2q_*)`,                                 (5.6)

with the right side interpreted as `0` when `q_*=0`.

Because (4.3) is strict, (5.6) strictly strengthens the preceding rational base-only condition whenever `q_*>0`:

`f_m(2q_*)/(2q_*)`
`> 3m(m-1)q_*/[3+2(2m-1)q_*].                               (5.7)

This is the exact coordinate-face obstruction produced by the current method; no square-root surrogate remains.

---

## 6. Exact stress test — the old entire rational face hierarchy can pass while the exact cone fails

A finite exact example shows that the strengthening is not cosmetic.

Take two active blocks of sizes `2` and `9`, no rest coordinates, and the rational cubic-null parameters

`delta=1/50`, `z=-25/9`.                                     (6.1)

The carried cubic-null formulas give exactly

`x=1191944/909063`,
`y=62046277/14848029`,
`k=-200000000/44544087`,                                     (6.2)

so, since `n-1=10`,

`S=44544087/20000000`,                                       (6.3)

and the block base is

`q=(u,u,v,...,v)`,

`exp(u)=7300657/5000000`,
`exp(v)=62046277/60000000`.                                  (6.4)

Let

`a=1+delta`, `b=1-delta`, `p=delta+z`,                       (6.5)

and define the total pair masses `U,V,W` by the exact Hessian-null aggregate equations plus exact value contact. If

`Omega=log S-u x-v y`,                                       (6.6)

then

`W = [2ab/(bu+av)^2]`
`    *[Omega - x(p-a)u^2/(2a) + y(p+b)v^2/(2b)]`,           (6.7)

`U=[bW+x(p-a)]/(2a)`,
`V=[aW-y(p+b)]/(2b)`.                                        (6.8)

The singleton sums are

`A_J=2-x-2uU-vW`,
`A_K=9-y-2vV-uW`.                                            (6.9)

Using block-symmetric coefficients

`alpha_J=A_J/2`, `alpha_K=A_K/9`,
`beta_JJ=U`, `beta_KK=V/36`, `beta_JK=W/18`,                 (6.10)

we obtain an exact-contact local Hessian-null candidate.

The exact rational-interval checker

`artifacts/R15/f0111_exact_face_cone_stress_d89w.py`

was executed after the analytic theorem was found; archived output is

`artifacts/R15/f0111_exact_face_cone_stress_d89w.out`.

It certifies:

- strict positive quartic factor on the carried cubic-null branch;
- all polynomial coefficient types are positive;
- full contact Hessian PSD, with the prescribed nonzero mixed null vector;
- **every one** of the preceding rational subset-face barriers passes for all subset types `(s,t)` with `0<=s<=2`, `0<=t<=9`, `s+t>=2`; the smallest squared certificate margin is `>1/500`;
- nevertheless, on the **K-only 9-face** at the exact test point

`s=log(4/3)`,                                                 (6.11)

where `9 exp(s)-8=4`, the true face gap satisfies

`boxed: -0.045 < P_K(s)-f_9(s) < -0.044`.                   (6.12)

Thus the candidate passes the complete *old* rational face hierarchy but is decisively not a global certificate. The exact face cone catches a real obstruction that every previous rational coordinate-face test misses.

This is why the next graph-flow elimination should use `Phi_m` itself, not another rational lower envelope.

---

## 7. What moved and what remains

This run does **not** solve Talagrand Problem 10.9, does not prove the full `k=2` statement, and does not eliminate all Hessian-null bifurcations.

It does change the retained-screen geometry in three exact ways:

1. coordinate-face feasibility is now characterized **if and only if**, not merely bounded below;
2. the exact-contact base obstruction has a closed form `f_m(2q_*)/(2q_*)`;
3. an exact local Hessian-null stress point proves the former rational all-subset hierarchy is strictly insufficient even when imposed on every subset type.

The next high-value attack is to combine the exact cone

`A_J>=Phi_|J|(B_J)`                                           (7.1)

with the exact null-flow equations

`2aU-bW=x(p-a)`,
`aW-2bV=y(p+b)`,                                              (7.2)

and exact value contact. In the two-block symmetric quotient, these equations make `(U,V,W)` essentially one-dimensional before value contact and unique after it. The concrete question is now whether the exact pure-block cones already exclude every surviving cubic-null regime, or whether a genuinely nonsymmetric face is necessary. A bounded exploratory scan suggested the exact pure-block cone is dramatically stronger, but **no numerical scan is counted as proof and no such global elimination is claimed here**.

---

## 8. Model / scheduler control truth

The requested GPT-6/maximum setting is still not enforceable or authenticated from the exposed task-control surface. Current repository deployment evidence says the interface exposes task identity/title, prompt, schedule/timing mode and enabled state, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated per-run applied-model/applied-effort telemetry, and no guaranteed-duration field**. GPT-6/maximum is therefore prompt-only in this environment.

The historical P26 `You cannot modify this task` response was authorization-context-specific; `operations/new_methods_2026-09-16/NATIVE_PC_DEPLOYMENT.md` and later P26 reports record a successful update from an authorized context. The lawful workaround for a protected task is the owning/authorized workspace/API/admin context, supported ownership repair/transfer, or platform support — not a permission bypass or duplicate task. Actual GPT-6/maximum enforcement additionally requires a product/backend/API scheduler that persists explicit model and reasoning fields and returns trustworthy applied-runtime attestation.

Per the operational addendum, no scheduler, permission, email, Drive, public-posting, purchase, or access change was attempted here.

---

## ledger_delta

```yaml
worker: R15
lane: CLOSABLE_OUTSIDE
native_target:
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  metric: four_source_matching_obligations_on_one_frozen_counterexample_candidate
  before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  status: OPEN_PARTIAL_RETIRED_HANDOFF
  unchanged_count: "6 frozen at mandatory retirement; not incremented after retirement"
  remaining_obligation: "Either construct a new frozen candidate satisfying FBM, BBM, source seam independence and non-2BM, or prove the complete source implication without a stopping-time strengthening. Operationally await reassignment/admission."
  exclusions:
    - Problem_7_5
    - already_posted_work
retained_screen:
  source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9 / F0111"
  scope: k_equals_2_quadratic_certificate_geometry
  prior_metric: "coordinate-face rational lower barrier only"
  new_metric: "exact iff coordinate-face cone Phi_m for every m, plus exact base-only obstruction"
  before: PARTIAL_RATIONAL_FACE_HIERARCHY
  after: PARTIAL_EXACT_FACE_CONE
  status: SELF_CHECK_ONLY_NOT_CLAIMED
  movement:
    - exact_face_cone_characterization
    - exact_base_only_contact_test
    - exact_2_by_9_stress_point_showing_old_full_rational_face_hierarchy_insufficient
methods_tried: [11, 24, 29]
method_note: "All 30 method numbers had already occurred earlier on F0111; this is a nonconsecutive triple used in new roles."
evidence:
  predecessor_report: "runs/R15/20260919_1811Z_successor_screen_f0111_subset_face_c88v.md @ c66d162c35d1db1f1e8ca0e4cc1c1a0e3872a4df"
  i0076_handoff: "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
  idea_before_code: "artifacts/R15/f0111_blockbudget_idea_d89w.md @ 06fd2f4791469153a475e1da933cbba2bb7e33a7"
  exact_checker: "artifacts/R15/f0111_exact_face_cone_stress_d89w.py @ bdf71f9467ef0ab398929b2ee1c1d385c5ac5af4"
  checker_output: "artifacts/R15/f0111_exact_face_cone_stress_d89w.out @ 72d8b0b5a731b3c644a3a34a127179675720ca1b"
  checker_result: ALL_EXACT_CHECKS_PASS
successor_admission:
  ready_closable_before: 0
  ready_closable_after: 0
  claim_created: false
  latest_coordinator: "operations/task_health/runs/2026-09-19T185900Z/status.md"
audits:
  p26: NONE_FOR_THIS_NEW_RESULT
  distinct_other: NONE_FOR_THIS_NEW_RESULT
closure: false
novelty: UNVERIFIED
```

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations remain `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical positive-route `2/4` is only the frozen handoff value. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, I derive a coefficient-free two-contact Hermite identity and a null-Hessian cubic/quartic filter, rewrite exact contacts as a capacitated weighted-graph/Bregman system, and prove that every subset-constant candidate first-bifurcation direction is impossible unless it generates a whole continuum of additional contacts. In particular the all-coordinate translation direction is neither a second-contact direction nor a Hessian-null direction. Methods #5 ADD A PARAMETER AND DIFFERENTIATE, #18 SAY IT IN ANOTHER LANGUAGE, #30 ONE DIRECTION AT A TIME.**

# R15 retained screen — two-contact Hermite identity and subset-direction bifurcation exclusion

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 from PENDING/NOT READY, establish publication novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Continuity, source, exclusions, ownership, and current fleet state

I continued from

`runs/R15/20260919_1124Z_successor_screen_f0111_closed_boundary_dual_u81h.md`

rather than restarting. Before new mathematics I reread/recovered the current `master` state for:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling R15 I0076 six-run handoff and the newest R15 retained-screen report;
- the current coordinator/successor-gate evidence and nearby admission reports;
- targeted intake/search records for I0076 and F0111.

The newest coordinator evidence available during this run still shows no lawful **free READY+CLOSABLE** successor for this R15 slot. P0169/P0219-type closable admissions remain owned elsewhere; newly released H0008 is a HARD target, not a free closable successor. I therefore created no successor claim, edited no shared root, and took no other worker's target.

### Burdzy--Scheutzow source rechecked exactly

The original `Forward Brownian Motion`, arXiv:1302.6958, Definition 2.1 and Problem 7.2 were rechecked directly from the source PDF (including the page image containing Problem 7.2). The source says:

- FBM: there are random origins `S_n -> -infinity` such that the complete centered future from every `S_n` is standard Brownian motion;
- BBM: the time reversal is FBM;
- 2BM: there is one random origin `S` for which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2: `X` is FBM and BBM and there is an arbitrary random time `T` at which the two complete centered half-processes are independent.

There is **no stopping-time hypothesis on `T`**, no deterministic-time substitute, and neither half at `T` is separately assumed Brownian. Problem 7.5 is a different question and remains excluded.

The controlling I0076 handoff remains valid. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but no source-valid independent seam; the later Brownian-prefix/BES candidate has seam independence but was proved actually 2BM. Hence there is still no surviving frozen candidate on which the original four-obligation metric can honestly move.

Fresh public searches dated 2026-09-19 used the exact paper title/arXiv ID, author names, exact Problem 7.2 language and resolution/citation terms. They recovered the source and related material but no accessible later primary source explicitly claiming a resolution of exact Problem 7.2. This is bounded negative evidence only.

### Current Talagrand literature check

Fresh 2026-09-19 searches recovered:

- Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulating the discrete convexity conjecture via `k`-thresholds and proving substantial graph-property classes;
- Chen Li, arXiv:2609.08967 (2026-09-08), answering the **fractional** version;
- Jinyoung Park, arXiv:2609.14681 (2026-09-13), giving a dimension-free comparison **toward** the conjecture.

None of the retrieved primary statements claims Talagrand's exact Problem 10.9 or the quadratic contact/bifurcation statements below. Absence of a hit is not a novelty certificate; novelty remains `UNVERIFIED`.

The immediately preceding run used #11/#20/#24 and explicitly handed off to #5/#18/#30. The R15 F0111 history has already exhausted the full 30-move inventory at least once, so these are honest **nonconsecutive re-entry methods after inventory exhaustion**, not falsely described as globally untried.

## 2. Carried `k=2` setup and prior bifurcation theorem

For the cardinality-two threshold write

`F(t)=F_n(t)=sum_i t_i - log S(t)`,

`S(t)=1+sum_i(exp(t_i)-1)=sum_i exp(t_i)-(n-1)`,              (2.1)

for `t in R_+^n`, `n>=2`.

At a fully interior base `q`, write

`r_i(q)=exp(q_i)/S(q)`,

`m_i=q_i(1-r_i(q))`.                                         (2.2)

For a quadratic exact value-and-gradient contact

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`, `A_i,B_ij>=0`, (2.3)

use the contact masses

`a_i=A_i q_i`, `e_ij=B_ij q_i q_j`.                          (2.4)

The carried contact equations are

`a_i+sum_{j!=i}e_ij=m_i`,                                    (2.5)

`sum_{i<j}e_ij=W(q)`,                                        (2.6)

where `W(q)=sum_i m_i-F(q)`.

The immediately preceding run proved that the quadratic gamma=1 certificate-base set is relatively closed and that every boundary certificate must exhibit at least one of two first-bifurcation mechanisms:

1. a singular contact Hessian; or
2. an additional global contact point.

The goal here is to attack those two mechanisms directly, not return to coefficient feasibility or another arbitrary local SDP ansatz.

## 3. Method #18 — say it in another language: exact contacts are a graph/Bregman domination problem

Set the dimensionless displacement from `q`

`u_i=(t_i-q_i)/q_i`, so `t_i=q_i(1+u_i)`.                    (3.1)

Define the first-order Taylor remainder

`R_q(t)=F(t)-F(q)-<grad F(q),t-q>`.                            (3.2)

### Lemma R15-F0111-NORMALIZED-GAP

For **every** quadratic exact value-and-gradient contact at `q`, whether or not it is globally valid,

`P(t)-F(t)=sum_{i<j} e_ij u_i u_j - R_q(t)`.                  (3.3)

#### Proof

Expanding (2.3) in normalized coordinates gives

`P(t)=sum_i a_i(1+u_i)+sum_{i<j}e_ij(1+u_i)(1+u_j)`.

The constant term is `P(q)=F(q)`. By (2.5), the coefficient of `u_i` is

`a_i+sum_{j!=i}e_ij=m_i=q_i partial_i F(q)`.

The only remaining term is `sum e_ij u_i u_j`, proving (3.3). QED.

Thus the global certificate problem is exactly:

> choose a nonnegative weighted graph `e_ij` satisfying the contact degree/budget constraints so that its quadratic edge energy dominates the Bregman/Taylor remainder `R_q(t)` for every feasible normalized displacement `u`.

This is the useful category change: coefficient search becomes a capacitated weighted-graph domination problem.

If `t` is an **additional interior contact** of the same `P`, then gradient equality at `t` yields the stronger exact graph system

`sum_{j!=i} e_ij u_j = q_i(r_i(q)-r_i(t))`, for every `i`.    (3.4)

Indeed the derivative of `P` with respect to `u_i` is `m_i+sum_{j!=i}e_ij u_j`, whereas the derivative of `F` with respect to `u_i` is `q_i(1-r_i(t))`.

For the singular-Hessian mechanism, set

`z_i=q_i r_i(q)`                                             (3.5)

and scale the gap Hessian by `diag(q)`. Its entries are

`M_ii=q_i^2 r_i(1-r_i)`,

`M_ij=e_ij-z_i z_j` for `i!=j`.                              (3.6)

If `v` is a null vector and `Z=sum_j z_j v_j`, then `Mv=0` is exactly

`sum_{j!=i}e_ij v_j = z_i(Z-q_i v_i)`, for every `i`.         (3.7)

Equations (3.4) and (3.7) put the two surviving boundary mechanisms into the same weighted-graph language.

## 4. Method #5 — add the segment parameter and differentiate

The next facts are **coefficient-independent necessary conditions** for the two bifurcation mechanisms.

### Theorem R15-F0111-TWO-CONTACT-HERMITE

Let `P>=F` globally and suppose `P` has two distinct interior contacts `q` and `t`. Put

`h=t-q`, `f(s)=F(q+s h)`, `0<=s<=1`.                         (4.1)

Then

`2(F(t)-F(q))=<h,grad F(t)+grad F(q)>`,                       (4.2)

or, equivalently,

`integral_0^1 s(1-s) D_h^3 F(q+s h) ds = 0`.                 (4.3)

#### Proof

Along the segment, `p(s)=P(q+s h)` is a quadratic polynomial in `s`. Since `G=P-F>=0` and both endpoints are interior zeros, `G'(0)=G'(1)=0`. Hence `p` and `f` agree in both value and first derivative at `s=0,1`.

Every quadratic obeys the exact trapezoid identity

`2(p(1)-p(0))=p'(0)+p'(1)`,

which gives (4.2). Applying the standard integral remainder identity for the trapezoid rule to `f'` gives (4.3). QED.

So a second contact requires cancellation of the third directional derivative along the connecting segment. Any direction on which `D_h^3F` has one strict sign is eliminated immediately.

### Lemma R15-F0111-NULL-CUBIC-QUARTIC

Let `P>=F` have an interior contact at `q`, and suppose `h!=0` is a null direction of the contact Hessian:

`h^T Hess(P-F)(q) h=0`.                                      (4.4)

Then necessarily

`D_h^3 F(q)=0`,                                               (4.5)

and

`D_h^4 F(q)<=0`.                                              (4.6)

#### Proof

For `g(s)=(P-F)(q+s h)`, interiority of `q` gives a two-sided neighborhood with `g(s)>=0`. We have `g(0)=g'(0)=g''(0)=0`. A nonzero cubic term would change sign, hence `g'''(0)=0`. Since `P` is quadratic this is (4.5). With the first three derivatives zero, local nonnegativity gives `g''''(0)>=0`; again `P` is quadratic, so `g''''(0)=-D_h^4F(q)`, proving (4.6). QED.

There is also an explicit cubic formula. If

`M_k(h)=sum_i r_i(q) h_i^k`,                                 (4.7)

then direct differentiation of `-log S` gives

`D_h^3F(q)=-( M_3 - 3 M_1 M_2 + 2 M_1^3 )`.                 (4.8)

This converts a singular-Hessian candidate into an exact algebraic moment constraint coupled to the graph equations (3.7).

## 5. Method #30 — one direction at a time: subset-constant directions collapse

Fix a nonempty subset `J subset {1,...,n}` and a nonzero scalar `c`. Consider the direction

`h=c 1_J`.                                                    (5.1)

Write

`A=sum_{i in J} exp(q_i)>0`,

`C=sum_{i notin J} exp(q_i)-(n-1)`,                           (5.2)

and along the segment/ray put

`x(s)=A exp(cs)`.

Then

`S(q+s h)=x(s)+C>0`                                          (5.3)

through every feasible portion of the line. If `f(s)=F(q+s h)`, direct differentiation gives

`f''(s)=-c^2 x(s) C/(x(s)+C)^2`,                             (5.4)

`f'''(s)=c^3 x(s) C(x(s)-C)/(x(s)+C)^3`.                    (5.5)

These two formulas settle the entire subset-constant class.

### Theorem R15-F0111-SUBSET-SECOND-CONTACT

Let `P>=F` be a nonnegative quadratic global certificate with an interior contact at `q`. Suppose a distinct interior point

`t=q+c 1_J`                                                   (5.6)

is also a contact. Then necessarily

`C=0`,                                                        (5.7)

all internal pair coefficients vanish,

`B_ij=0` for every distinct `i,j in J`,                       (5.8)

and in fact **every feasible point on the whole line** `q+s c 1_J` is a contact. In particular, there is no isolated additional contact in any subset-constant direction.

#### Proof

There are three cases.

**Case 1: `C>0`.** By (5.4), `f''(s)<0`. The restriction `p(s)=P(q+s h)` has

`p''(s)=2c^2 sum_{i<j, i,j in J} B_ij >=0`.                  (5.9)

Hence `g=p-f` is **strictly convex** on `[0,1]`. If `g(0)=g(1)=0`, strict convexity gives `g(s)<0` for `0<s<1`, contradicting the global majorant property.

**Case 2: `C<0`.** Since `x(s)>0`, also `x(s)-C>0`. Equation (5.5) therefore has one strict sign throughout the segment. This contradicts the coefficient-free Hermite condition (4.3).

**Case 3: `C=0`.** Then `S(q+s h)=A exp(cs)`, so `f(s)` is affine. The gap restriction `g=p-f` is a convex quadratic with zeros at `s=0,1`. A convex function with zero endpoints is `<=0` in the interval, whereas global majorization gives `g>=0`; hence `g` vanishes identically on `[0,1]`. Its quadratic coefficient is (5.9), so nonnegativity of the `B_ij` forces every internal coefficient to vanish. Both `p` and `f` are then affine in `s`; value and slope contact at `s=0` force equality on the entire feasible line. QED.

Two immediate corollaries are worth recording:

- if `|J|=1`, then because `q` is fully interior,
  `C=sum_{i notin J}exp(q_i)-(n-1)>0`; hence **no one-coordinate translation can be a second contact**;
- for the full translation `J={1,...,n}`, `C=-(n-1)<0`; hence **no all-coordinate translation can be a second contact**.

### Theorem R15-F0111-SUBSET-NULL-COLLAPSE

Under the same hypotheses, suppose `h=c 1_J` is a contact-Hessian null direction. Then the singularity necessarily produces additional global contacts: more precisely,

`C=0`,                                                        (5.10)

all internal `B_ij` vanish, and the whole feasible line `q+s c 1_J` is contact.

Consequently a subset-constant direction can never realize the **singular-only** branch of the previous first-bifurcation theorem.

#### Proof

The cubic filter (4.5) and (5.5) at `s=0` imply

`A C(A-C)=0`.

Since `A>0`, either `C=0` or `C=A`.

If `C=A`, differentiating (5.5) once at `s=0` gives the exact fourth derivative

`D_h^4F(q)=c^4/8>0`,                                         (5.11)

contradicting the necessary quartic inequality (4.6).

Thus `C=0`. In this case `f` is affine along the line. Nullity says `g''(0)=0`; by (5.9) and nonnegative coefficients, every internal `B_ij` is zero. Therefore the restriction of `P-F` to the line is affine. It has zero value and derivative at the contact `q`, so it is identically zero on the whole feasible line. QED.

For the full translation `J={1,...,n}`, `C=-(n-1)`, so this also proves that the all-coordinate direction can **never** be a Hessian null direction.

## 6. What moved, and what remains

The previous run reduced a first boundary certificate to two possible mechanisms: singular Hessian or an additional global contact. This run shows that **neither mechanism can first appear in a subset-constant direction unless the two mechanisms merge into a continuum of global contacts on the exact hypersurface**

`sum_{i notin J} exp(q_i)=n-1`.                               (6.1)

More precisely:

- no isolated second contact can differ from `q` by a constant shift on any subset;
- no singular-only Hessian null vector can be constant on any subset and zero off it;
- the only surviving subset-constant degeneracy is `C=0`, where the relevant internal pair coefficients are forced to zero and an entire feasible line is contact;
- the all-coordinate translation direction is excluded from both mechanisms outright;
- any genuinely new first-bifurcation mechanism must therefore use a **nonconstant direction** (and, for an isolated second contact, cannot be a one-coordinate shift either).

This is real structural movement on the retained `k=2` screen. It is still not a proof that the quadratic certificate region is all of `(0,infinity)^n`, and it says nothing sufficient for `k>=3`. Talagrand Problem 10.9 remains open on the evidence checked here.

## 7. Three attacks tried and what happened

### #5 ADD A PARAMETER AND DIFFERENTIATE

Succeeded. Segment parameterization produces the coefficient-independent Hermite condition (4.2)--(4.3). At a singular contact it gives the exact cubic and quartic necessary conditions (4.5)--(4.6).

### #18 SAY IT IN ANOTHER LANGUAGE

Succeeded. Normalized displacements turn every exact quadratic contact into the weighted-graph/Bregman identity (3.3), with the extra-contact system (3.4) and null-vector graph equation (3.7). The two surviving boundary mechanisms are now comparable in one algebraic language.

### #30 ONE DIRECTION AT A TIME

Succeeded for the whole subset-constant class. Equations (5.4)--(5.5) eliminate isolated second contacts and singular-only null directions there, with the sole exceptional hypersurface `C=0` forcing a continuum of contacts.

## 8. Prior-art and novelty status

Searches dated 2026-09-19 included the exact Talagrand Problem 10.9 terminology, `k`-threshold reformulations, fractional discrete convexity, expectation/fractional-expectation comparisons, exact contact/global-majorant terms and the current 2026 papers listed in section 1. I found no accessible primary source stating the normalized graph identity plus Hermite/null-direction/subset-collapse package above. These are elementary calculations and convexity arguments built from standard machinery, so **novelty remains UNVERIFIED** and no priority claim is made.

## 9. Why no checker was created

No finite arithmetic assertion is load-bearing in this run. The new movement consists of exact symbolic identities and theorem-sized sign/convexity arguments valid for all `n,q,J,c`. A numerical path/grid check would not certify Brownian laws, global majorization, or these parameter-uniform statements and would invert the requested 90/10 research/checking balance.

## 10. Model / scheduler control boundary

The actually running model is GPT-5.6 Sol. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is UNVERIFIED. The exposed scheduler/task-management surface still has task identity/title, prompt, schedule/timing, enabled state and notification controls, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution control. GPT-6/maximum therefore remains prompt-only.

The historical P26 `You cannot modify this task` event is an authorization-context boundary. `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records that exact failure for P26 while separately recording successful updates in authorized contexts; the lawful fix is an eligible owner/admin/product/API surface that actually persists model/reasoning routing fields and attests them per run, or platform support — not task duplication or permission bypass. No scheduler or permission change was made here.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  native_target:
    id: I0076
    source: Burdzy_Scheutzow_Forward_Brownian_Motion_Problem_7_2
    metric_name: source_matching_obligations_for_one_frozen_counterexample
    metric_before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    metric_after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_handoff_value: 2/4
    status: OPEN_PARTIAL_RETIRED_HANDOFF
    unchanged_count: RETIRED_AT_SIX_RUN_RULE
    active_research_this_run: false
  successor_gate:
    free_ready_closable_before: 0
    free_ready_closable_after: 0
    claim_created: false
  methods_actually_tried: [5, 18, 30]
  method_inventory_note: FULL_30_MOVE_INVENTORY_ALREADY_EXHAUSTED_ON_RETAINED_SCREEN_REENTRY_USED
  retained_screen:
    problem_id: F0111
    source: Talagrand_STOC_2010_Problem_10_9
    status: PENDING_NOT_READY_SELF_CHECK_ONLY
    new_results:
      - exact_normalized_graph_Bregman_gap_identity
      - exact_extra_contact_weighted_graph_system
      - coefficient_independent_two_contact_Hermite_identity
      - null_Hessian_cubic_and_quartic_filters
      - subset_constant_second_contacts_only_as_continuum_on_C_zero
      - subset_constant_Hessian_nullity_collapses_to_extra_contact_continuum
      - full_uniform_translation_excluded_from_both_first_bifurcation_mechanisms
    remaining_obligation: >-
      Analyze genuinely nonconstant first-bifurcation directions. A natural next localization
      is two-block piecewise-constant displacement, where S along the segment is a sum of two
      exponentials minus a constant. Either exclude both bifurcation mechanisms there or reduce
      them to an exact finite algebraic/one-dimensional condition, then feed any survivor into
      the finite-support dual alternative. Parent Problem 10.9 still requires one gamma uniform
      over all n,k and heterogeneous q.
  evidence:
    original_brownian_pdf_definition_and_problem_page_checked: true
    talagrand_current_literature_checked_2026_09_19: true
    campaign_index_ranking_posted_results_queue_checked: true
    operations_manifest_checked: true
    current_successor_gate_checked: true
    finite_checker_needed: false
  audit_ids: []
  next_methods: [7, 14, 26]
  closure_claim: false
```

## 12. Next cursor

Do not return to coefficient-feasibility, the old rank-one ansatz, or another unrestricted SDP search. The full 30-method inventory is already exhausted, so the next run should use the nonconsecutive re-entry triple **#7 TAKE THE LIMIT, #14 FIND THE GROUP ACTING, #26 HUNT THE SPORADIC CASE** on the genuinely nonconstant directions left by this run:

1. start with a two-block direction `h=c_1 1_J+c_2 1_{J^c}` and quotient by within-block symmetry;
2. derive the exact one-variable third-derivative sign changes of `S(q+s h)=A exp(c_1 s)+B exp(c_2 s)-(n-1)` and test whether the Hermite zero can occur without forcing another degeneracy;
3. separately impose the null-Hessian graph equation (3.7) and cubic moment equation (4.8) on the two-block quotient;
4. if a sporadic survivor remains, reduce it to an exact scalar/algebraic condition and then use the finite-support dual alternative from the preceding run.

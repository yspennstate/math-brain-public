Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations remain `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical positive-route `2/4` is only the frozen handoff value, not a live-candidate score. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, I prove (i) relative closedness of the gamma=1 certificate-base set, in fact for every fixed up-class; (ii) an exact finite-support alternative for failure of a quadratic certificate with support at most `d=n+binom(n,2)` test points; and (iii) a first-bifurcation theorem showing that a boundary base for the quadratic certificate region must force either a singular contact Hessian or an additional global contact point. Coefficient extinction alone cannot be the obstruction, because the source allows beta_I=0 and the all-base strictly-positive exact-contact theorem lets one strictify any nondegenerate isolated global certificate. Methods #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**

# R15 retained screen — closed certificate regions, finite dual witnesses, and the first-bifurcation alternative

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 from PENDING/NOT READY, establish publication novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Continuity, exact source checks, exclusions, ownership, and current fleet state

I continued from

`runs/R15/20260919_0955Z_successor_screen_f0111_contact_polytope_t80q.md`

rather than restarting. I reread/recovered current `master` state for `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest operations implementation manifest, the newest own report and the current coordinator/successor-gate state. The newest coordinator evidence available during this run still reports **zero newly admitted free READY CLOSABLE successors**; the CLOSABLE targets that have cleared admission are owned. I therefore created no successor claim, edited no shared root, and took no other worker's target.

### Burdzy--Scheutzow source rechecked exactly

The original PDF `Forward Brownian Motion`, arXiv:1302.6958v4, Definition 2.1 and Problem 7.2, was rechecked directly, including page images. It says:

- FBM: there are random origins `S_n -> -infinity` such that every complete centered future from `S_n` is standard Brownian motion;
- BBM: time reversal is FBM;
- 2BM: there is one random origin `S` for which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2: `X` is FBM and BBM and there is an arbitrary random time `T` at which the two complete centered half-processes are independent.

There is **no stopping-time hypothesis on `T`**, no deterministic-time substitute, and neither half at `T` is separately assumed Brownian. Problem 7.5 is a different question and remains excluded.

The controlling I0076 handoff remains valid. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but no source-valid independent seam; the later Brownian-prefix/BES candidate has the seam independence but was proved actually 2BM. Hence there is still no surviving frozen candidate on which the original four-obligation counterexample metric can honestly move.

Fresh public searches dated 2026-09-19 again used the exact title/arXiv identifier, exact Problem 7.2 language, author names and later/citing terms. They recovered the original paper and related splitting-time material but no accessible later primary source explicitly claiming a resolution of exact Problem 7.2. This is bounded negative evidence only.

### Talagrand source point that matters in this run

I rechecked the STOC version / author-hosted PDF of Michel Talagrand, *Are Many Small Sets Explicitly Small?*, Definition 10.1 and exact Problem 10.9. The source defines

`P(t)=sum_{I subset S} beta_I t_I`, with `beta_I >= 0` and `beta_empty=0`.

Thus **zero coefficients are allowed**. For gamma=1, `A in C_1` at base `q` means a nonnegative-coefficient multilinear `P` obeys

`F_A(t):=-log(1-zeta_t(A)) <= P(t)` for all `t>=0`,

and `P(q)<=F_A(q)`. Since the first inequality also holds at `q`, gamma=1 forces exact contact

`P(q)=F_A(q)`.

Problem 10.9 asks for one universal gamma>0 such that every cardinality class `{X subset S: |X|>=k}` belongs to `C_gamma`.

The source's allowance `beta_I=0` is operationally important below: a coefficient reaching zero is **not by itself** a failure of the source condition.

Current-literature searches recovered Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), which reformulates the broader discrete convexity conjecture through k-thresholds and proves substantial graph-property classes, together with the established nearby fractional/expectation-threshold literature. None of the retrieved primary statements claims exact Problem 10.9 or the certificate-topology statements below. Absence of a hit is not a novelty certificate; novelty remains `UNVERIFIED`.

The preceding R15 run used #4/#13/#27. The original I0076 triple #2/#12/#23 was already exhausted. This run therefore uses fresh methods **#11, #20, #24**.

## 2. Carried k=2 setup

For the cardinality-two threshold, write

`F_n(t)=sum_i t_i - log(1+sum_i(exp(t_i)-1))`,  `t in R_+^n`.      (2.1)

The preceding R15 work established two facts that are inputs here:

1. there are explicit full-dimensional open patches of interior bases carrying global quadratic `C_1` certificates;
2. for **every** interior base `q`, there exists a strictly positive quadratic polynomial with exact value-and-gradient contact at `q`, although that contact need not globally majorize `F_n`.

The second fact is the all-base contact-polytope theorem in the preceding immutable report.

Let

`phi(t)=(t_1,...,t_n,(t_i t_j)_{i<j}) in R_+^d`,

`d=n+binom(n,2)`.                                                (2.2)

A quadratic polynomial is `P_beta(t)=<beta,phi(t)>`, `beta>=0`.

Define the quadratic gamma=1 certificate-base set

`C_n^(2)={ q in (0,infinity)^n : exists beta>=0, P_beta>=F_n on R_+^n, P_beta(q)=F_n(q) }`.       (2.3)

No assertion is made here about higher-degree certificates or k>=3 unless explicitly stated.

## 3. Method #20 — find why continuation can fail: the certificate-base set is closed

The first observation is more general than k=2.

### Theorem R15-F0111-CLOSED-BASES

Fix a finite ground set `S` and any up-class `A subset {0,1}^S`. Let

`C_1(A)={q in (0,infinity)^S : A has a source-valid gamma=1 certificate at q}`.

Then `C_1(A)` is relatively closed in `(0,infinity)^S`.

The same statement holds if one restricts the allowed monomials to any fixed finite collection, in particular to singleton-plus-pair (quadratic) polynomials. Hence `C_n^(2)` in (2.3) is relatively closed.

#### Proof

Take `q^(r)->q` in the interior, with source-valid certificates

`P_r(t)=sum_{empty != I subset S} beta_I^(r) t_I`, `beta_I^(r)>=0`.

At gamma=1, global majorization and the budget inequality force

`P_r(q^(r))=F_A(q^(r))`.                                      (3.1)

For each fixed nonempty `I`, positivity gives

`0 <= beta_I^(r) prod_{i in I}q_i^(r) <= F_A(q^(r))`.        (3.2)

Because `q` is fully interior and `F_A` is continuous there, every coefficient sequence is bounded. There are only finitely many monomials. Pass to one subsequence on which all coefficients converge:

`beta_I^(r)->beta_I>=0`.                                     (3.3)

For each fixed `t>=0`, coefficient convergence gives `P_r(t)->P(t)`, so the inequalities `P_r(t)>=F_A(t)` pass to the limit:

`P(t)>=F_A(t)` for every `t>=0`.                              (3.4)

Likewise (3.1) passes to

`P(q)=F_A(q)`.                                                (3.5)

Thus `q in C_1(A)`. QED.

This removes one possible fake obstruction from the continuation picture: a gamma=1 certificate cannot disappear merely by taking an interior limit of certified bases. A first failure along a path must occur **after** a still-certified limiting base.

## 4. Method #11 — exact finite-support dual alternative for quadratic failure

The earlier R15 dual report gave a weak positive-measure obstruction. At gamma=1 and fixed degree two, compactness yields a stronger exact alternative with no semi-infinite-duality gap.

Fix an interior base `q`. Put

`K_q={beta>=0 : <beta,phi(q)>=F_n(q)}`.                       (4.1)

Because every coordinate of `phi(q)` is positive, `K_q` is a compact simplex. A quadratic certificate exists exactly when

`K_q intersect H_t for every t>=0` is nonempty,               (4.2)

where

`H_t={beta : <beta,phi(t)> >= F_n(t)}`.                       (4.3)

### Theorem R15-F0111-FINITE-DUAL-ALT

Exactly one of the following occurs.

**Primal:** there is a nonnegative quadratic global certificate at `q`.

**Dual:** there are `m<=d` points `t^(1),...,t^(m) in R_+^n` and weights `lambda_k>=0`, `sum lambda_k=1`, such that

`F_n(q) * max_I [ sum_k lambda_k phi_I(t^(k))/phi_I(q) ]
 < sum_k lambda_k F_n(t^(k))`,                                (4.4)

where `I` runs over all singleton and pair monomials.

In particular, if the quadratic gamma=1 program ever fails at some base, its failure has a witness using at most

`d=n+binom(n,2)`                                               (4.5)

off-base test points. Numerical grids are not certificates; (4.4), if used, must be proved exactly.

#### Proof

If the primal system is empty, the closed halfspaces `K_q intersect H_t` have empty total intersection. Compactness gives a finite empty subintersection. Working in the affine hull of `K_q`, which has dimension at most `d-1`, Helly's theorem reduces this to at most `d` points `t^(k)`.

For that finite family, set

`ell_k(beta)=<beta,phi(t^(k))>-F_n(t^(k))`.

Because the finite intersection is empty and `K_q` is compact,

`max_{beta in K_q} min_k ell_k(beta) < 0`.                    (4.6)

By the finite-dimensional minimax theorem,

`min_{lambda in Delta_m} max_{beta in K_q} sum_k lambda_k ell_k(beta) <0`.     (4.7)

Choose a minimizing `lambda`. If

`M_I=sum_k lambda_k phi_I(t^(k))/phi_I(q)`,                  (4.8)

then the change of variables

`alpha_I=beta_I phi_I(q)/F_n(q)`                              (4.9)

identifies `K_q` with the standard simplex, so

`max_{beta in K_q} sum_k lambda_k <beta,phi(t^(k))>
 = F_n(q) max_I M_I`.                                        (4.10)

Substitution in (4.7) gives (4.4).

Conversely, if (4.4) holds and `P_beta` were a global certificate, then averaging `P_beta(t^(k))>=F_n(t^(k))` against `lambda` and using (4.10) would give the reverse inequality, contradiction. QED.

This is a genuine strengthening of the old weak-dual screen: **if a quadratic k=2 gamma=1 certificate fails, a finite exact obstruction exists and needs no more than d atoms.**

## 5. Method #24 — extremal boundary object and strictification

Closedness by itself does not prove `C_n^(2)` is all of the connected interior; a closed set can have a nonempty interior and a boundary. The useful question is therefore: **what must a first boundary certificate look like?**

Let `P` be a global quadratic certificate at an interior base `q`, and let

`G=P-F_n >=0`.                                                 (5.1)

Since `q` is interior and `G(q)=0`, automatically

`grad G(q)=0`,                                                 (5.2)

and `H_q=Hess G(q)` is positive semidefinite.

The earlier R15 openness theorem showed that a certificate with strictly positive coefficients, zero set exactly `{0,q}`, and `H_q` positive definite persists under arbitrary sufficiently small perturbations of the base.

The source, however, allows zero coefficients. The new point is that **coefficient extinction alone is not a true boundary mechanism.**

### Lemma R15-F0111-STRICTIFY

Suppose `P` is a global quadratic certificate at `q` such that

1. `G^{-1}(0)={0,q}`; and
2. `H_q` is positive definite.

Then there exists another global quadratic certificate `P_eps` at the same `q` whose singleton and pair coefficients are **all strictly positive**, and which still has zero set `{0,q}` and positive-definite contact Hessian.

#### Proof

By the preceding all-base contact-polytope theorem, choose a strictly positive quadratic polynomial `Q` having exact value-and-gradient contact with `F_n` at `q`. It need not globally majorize `F_n`.

For `0<eps<1`, define

`P_eps=(1-eps)P+eps Q`,

`G_eps=P_eps-F_n=(1-eps)G+eps(Q-F_n)`.                        (5.3)

All coefficients of `P_eps` are strictly positive.

It remains to show that `eps` can be chosen so that `G_eps>=0` globally.

**Near q.** Both `P` and `Q` have exact value and gradient contact at `q`. Since `H_q` is positive definite, continuity of the Hessian gives a ball `B(q,r)` and `c>0` with

`G(t)>=c||t-q||^2` there.                                    (5.4)

The Hessian of `Q-P` is bounded on that ball. For sufficiently small `eps`, `Hess G_eps` remains positive definite throughout a smaller ball, so `G_eps>=0` there with equality only at `q`.

**Near 0.** Let `a>0` be the smallest singleton coefficient of `Q`. If `T=sum_i t_i`, then

`F_n(t) <= T-log(1+T) <= T^2`.                               (5.5)

Also `P_eps(t)>=eps a T`. Hence `G_eps>0` on a fixed punctured neighborhood of `0` once `T<eps a`.

**At infinity.** Let `a>0` and `b>0` be the smallest singleton and pair coefficients of `Q`, let `M=max_i t_i`, and `R=sum_i t_i-M`. Since the denominator in (2.1) is at least `e^M`,

`F_n(t)<=R`.                                                  (5.6)

Moreover

`Q(t)>=a(M+R)+bMR`.                                          (5.7)

Thus

`Q(t)-F_n(t)>=aM+(a-1+bM)R`.                                (5.8)

The right side is nonnegative once `M` is sufficiently large. Therefore the possible negative set of `Q-F_n` is contained in a fixed compact box.

**Compact middle.** Remove small neighborhoods of `0` and `q` from that box. On the remaining compact set, `G` has a strictly positive minimum because its zero set is exactly `{0,q}`. The perturbation `Q-P` is bounded there, so for sufficiently small `eps`, (5.3) remains strictly positive.

These regions exhaust the orthant. Thus `P_eps` is a global certificate, with strict coefficients, isolated zeros and positive-definite contact Hessian. QED.

### Corollary R15-F0111-FIRST-BIFURCATION

Every boundary point `q` of the quadratic certificate region `C_n^(2)` is itself certified (by closedness), but **every** global quadratic certificate `P` at that `q` must satisfy at least one of the following:

1. `Hess(P-F_n)(q)` is singular; or
2. there exists `t_* notin {0,q}` with `P(t_*)=F_n(t_*)`.

In particular, a coefficient reaching zero is not an independent third failure mode.

#### Proof

If one boundary certificate violated both alternatives, the strictification lemma would produce a strict global certificate at `q` with isolated zeros and positive-definite contact Hessian. The previously proved openness theorem would then make `q` an interior point of `C_n^(2)`, contradiction. QED.

This is the clean first-bifurcation description that the preceding continuation program lacked.

## 6. What this changes, and what it does not

The preceding run showed that **zeroth/first-order positive contact feasibility never fails** at an interior k=2 base. This run goes further:

- the actual gamma=1 certificate region is relatively closed;
- if a base lies outside the quadratic region, failure is witnessed by at most `d=n+binom(n,2)` exact test points;
- at a first boundary base, source-permitted coefficient zeros are not the obstruction by themselves;
- the only remaining first-bifurcation mechanisms are an exact **null Hessian direction** at the contact, or the birth of an **additional global contact point**.

This turns the next search into two sharply specified problems instead of another free-form majorant search.

It does **not** prove that `C_n^(2)` is all of `(0,infinity)^n`. It does not rule out either boundary mechanism. It does not establish any statement for `k>=3`, and therefore does not solve Talagrand Problem 10.9.

## 7. Three attacks tried and what happened

### #11 DUALIZE

Succeeded. The weak measure obstruction from the old screening phase upgrades, for quadratic gamma=1, to the exact finite-support alternative (4.4), with support at most `d`. This gives a finite exact certificate of failure if one exists.

### #20 FIND WHY THE ALGORITHM FAILS

Succeeded in reducing the failure modes. Relative closedness shows continuation cannot fail by loss of feasibility at the limiting base. Strictification shows a zero coefficient alone is not the reason continuation stops. The first failure must be second-order singularity or a new global equality point.

### #24 FIND THE EXTREMAL OBJECT

Succeeded in identifying the correct boundary object: a global certificate at a boundary base that is necessarily degenerate in one of the two senses above. I did not yet prove that such an object cannot exist.

## 8. Prior-art/current-literature status

Searches dated 2026-09-19 included the exact Talagrand paper title, `Problem 10.9`, `C_gamma`, cardinality-threshold language, current 2026 `k`-threshold work, and nearby threshold/fractional-threshold papers. The bounded search recovered the original Problem 10.9 and Ascoli--He--Park--Talagrand (2026-08-11), but no accessible source stating the closedness/finite-dual/first-bifurcation package above. These arguments use standard compactness, Helly/minimax and perturbation machinery, so **novelty remains UNVERIFIED** and no priority claim is made.

## 9. Why no checker was created

No finite arithmetic claim is load-bearing in this run. The new results are parameter-uniform finite-dimensional convexity/compactness theorems with complete proofs on the page. A floating-point grid would not certify relative closedness, global majorization on a noncompact orthant, or the Helly/minimax alternative. Creating a numerical receipt would invert the 90/10 rule.

## 10. Model / scheduler control boundary

The actually running model is GPT-5.6 Sol. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is UNVERIFIED. The exposed scheduler/task-management surface still has task identity/title, prompt, schedule/timing, enabled state and notification controls, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution control. GPT-6/maximum therefore remains prompt-only.

The historical P26 `You cannot modify this task` event is an authorization-context boundary. The current operations records also show successful edits from an authorized context. The lawful fix is an eligible owner/admin/product/API surface that actually persists model/reasoning routing fields and attests them per run, or platform support — not task duplication or permission bypass. No scheduler or permission change was made here.

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
  methods_actually_tried: [11, 20, 24]
  retained_screen:
    problem_id: F0111
    source: Talagrand_STOC_2010_Problem_10_9
    status: PENDING_NOT_READY_SELF_CHECK_ONLY
    new_results:
      - gamma1_certificate_base_set_relatively_closed_for_every_fixed_upclass
      - quadratic_failure_exact_finite_dual_support_at_most_d
      - strictification_of_nondegenerate_isolated_k2_global_certificate
      - boundary_first_bifurcation_singular_hessian_or_extra_contact
    source_definition_correction:
      beta_I_nonnegative_zero_allowed: true
    remaining_obligation: >-
      Rule out or construct the two surviving boundary mechanisms for k=2:
      an exact null direction of the contact Hessian, or a second global contact point.
      Parent Problem 10.9 still requires one gamma uniform over all n,k and heterogeneous q.
  evidence:
    original_brownian_pdf_definition_and_problem_page_checked: true
    talagrand_definition_and_problem_10_9_checked: true
    current_literature_checked_2026_09_19: true
    current_queue_and_coordinator_state_checked: true
    finite_checker_needed: false
  audit_ids: []
  next_methods: [5, 18, 30]
  closure_claim: false
```

## 12. Next cursor

Do not return to coefficient-feasibility or another arbitrary local SDP ansatz. Use fresh methods **#5 ADD A PARAMETER AND DIFFERENTIATE, #18 SAY IT IN ANOTHER LANGUAGE, #30 ONE DIRECTION AT A TIME** on the two actual first-bifurcation mechanisms:

1. parameterize a hypothetical second contact `t_*` and differentiate the two exact contact systems to seek a contradiction or a forced lower-dimensional reduction;
2. rewrite a singular contact Hessian as the exact scaled matrix condition
   `diag(q_i^2 r_i(1-r_i)) + (e_ij-z_i z_j)_{i!=j}` having a null vector, and localize one sign pattern/direction at a time;
3. if either mechanism survives, feed it into the finite dual alternative rather than producing another numerical grid.

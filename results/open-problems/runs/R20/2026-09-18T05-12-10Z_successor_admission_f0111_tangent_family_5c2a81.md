Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max=1213`, retirement/unchanged count `6`; methods #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #15 BREAK THE SYMMETRY ON PURPOSE, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# R20 successor admission — F0111 tangent-majorant calculus and multiscale obstruction

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R20, CLOSABLE OUTSIDE.

## 1. Continuity first: I0100 stays retired and frozen

I did **not** reopen Afonso S. Bandeira / Randomstrasse 2025 Conjecture 26 (`I0100`) after its mandatory six-unchanged-run handoff. A fresh 2026-09-18 current-source check still shows the root one-localization problem as **Open**: whether

\[
\vartheta(\overline{G_{p,1}})\sim \sqrt{p/2}
\]

for the source Paley one-localization convention. The degree-four SOS question, the two-localization question and the ETF question remain distinct scopes and were not reassigned.

The frozen exact-certified metric is unchanged:

\[
\boxed{p_{\max}=1213}
\]

with retained exact primal/dual certified set

\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213\}}.
\]

The retirement/unchanged count remains `6`. This run does not increment it, because no Paley research was reopened. The preserved mathematical blocker is the deterministic **joint orientation/sign-compatible Pluecker wall / positive-circuit** problem: arbitrary small minors, marginal Jacobi estimates, Wendel/Cover chamber counts and numerical SDP output do not identify the distinguished positive-orthant wall needed for the asymptotic.

The active R20 successor metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors admitted in this bounded run`.

Before: `0`. After: `0`.

## 2. Required repository recovery and bounded-screen disclosure

Before substantive screening I reread/recovered the required current repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest R20 report, current neighboring admission/coordinator material, and exact ownership evidence for candidates actually screened.

The intake corpus is connector-bounded when rendered wholesale. I used exact-ID/source/ownership searches and exact batch/source reads rather than falsely claiming a byte-for-byte visual reread of every one of the roughly 780 intake rows.

Fresh current coordinator/admission work still shows the same structural gate: newly found CLOSABLE-shaped sources are being claimed elsewhere as soon as they clear admission, while no second source-clean/current-open/ownership-clear CLOSABLE successor was available for R20 at the race snapshot. New terminal handoff prose was not treated as a release of canonical ownership.

## 3. Fresh ownership-clear candidate: F0111, Talagrand Problem 10.9

Source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9, Section 10.

Exact source question: does there exist a universal `gamma>0` such that for every finite set `S` and every `k`, the threshold up-class

\[
A_{S,k}=\{X\subseteq S:|X|\ge k\}
\]

belongs to Talagrand's class `C_gamma`?

For an up-class `A`, write

\[
F_A(t)=-\log(1-\zeta_t(A)),
\]

where under `zeta_t` coordinate `i` is selected with probability `1-e^{-t_i}`. Membership `A in C_gamma` means that for every `q in R_+^S` there is a positive-coefficient multilinear polynomial

\[
P(t)=\sum_{\emptyset\ne I\subseteq S}\beta_I t_I,\qquad \beta_I\ge0,
\]

such that

\[
F_A(t)\le P(t)\quad\forall t\ge0,
\qquad
P(\gamma q)\le \gamma F_A(q).
\]

The source asks for **one gamma uniform in S,k and every heterogeneous q**.

A fresh race check found no canonical `operations/claims/F0111.md`. The immediately preceding R15 screen had already recovered the exact source and current nearby literature and classified F0111 as `OPEN-LOOKING / OWNERSHIP-CLEAR-IN-BOUNDED-SEARCH / HARD-LEANING / NOT CLOSABLE-READY / NOT CLAIMED`. I therefore used F0111 only as a substantive admission probe; I did **not** create a claim.

R15 had proved the exact hazard identity. Let

\[
y_i=e^{t_i}-1,\qquad T=\sum_i t_i,\qquad Z_{k-1}(y)=\sum_{j=0}^{k-1}e_j(y).
\]

Then

\[
\boxed{F_{n,k}(t)=T-\log Z_{k-1}(y).}
\tag{3.1}
\]

It also proved a positive-measure weak-dual counterexample lemma and showed that the most natural symmetric sparse dual family lies on the non-refuting side. Its block-recursion route fails because cardinality-threshold dynamic programs reuse blocks, whereas the source composition lemma requires genuinely disjoint blocks.

The present run asks what the exact differential structure says that these failures were missing.

## 4. Method #5 — exact derivative identity

For every `i`,

\[
\boxed{
\partial_iF_{n,k}(t)=
\frac{e_{k-1}(y_{-i})}{Z_{k-1}(y)}.
}
\tag{4.1}
\]

### Proof

Differentiate (3.1). Since `y_i=e^{t_i}-1`,

\[
\partial_i Z_{k-1}(y)
=(1+y_i) Z^{(-i)}_{k-2}(y),
\]

where `Z^{(-i)}_{k-2}=sum_{j=0}^{k-2}e_j(y_{-i})`. On the other hand, by splitting elementary symmetric terms according to whether they contain `i`,

\[
Z_{k-1}(y)
=(1+y_i)Z^{(-i)}_{k-2}(y)+e_{k-1}(y_{-i}).
\]

Hence

\[
\partial_iF
=1-\frac{(1+y_i)Z^{(-i)}_{k-2}}{Z_{k-1}}
=\frac{e_{k-1}(y_{-i})}{Z_{k-1}},
\]

which proves (4.1).

Along a ray `f_q(s)=F_{n,k}(sq)`,

\[
f_q'(s)=\sum_iq_i
\frac{e_{k-1}(e^{sq_{-i}}-1)}
{Z_{k-1}(e^{sq}-1)}.
\tag{4.2}
\]

For positive `q`, Taylor expansion at zero gives

\[
F_{n,k}(sq)=s^ke_k(q)+O(s^{k+1}),
\tag{4.3}
\]

and therefore the Euler defect satisfies

\[
\boxed{
 s\,q\!\cdot\!\nabla F_{n,k}(sq)-F_{n,k}(sq)
=(k-1)s^ke_k(q)+O(s^{k+1})>0
}
\tag{4.4}
\]

for all sufficiently small `s>0` when `k>=2`.

This immediately kills one overly-simple certificate route, below.

## 5. Exact gradient domination and an explicit global polynomial majorant

Put

\[
p_j=1-e^{-t_j}=\frac{y_j}{1+y_j}.
\]

The derivative in (4.1) obeys the exact bound

\[
\boxed{
0\le \partial_iF_{n,k}(t)
\le e_{k-1}(p_{-i})
\le e_{k-1}(t_{-i}).
}
\tag{5.1}
\]

### Proof of the first nontrivial inequality

Set `r=k-1`. For arbitrary nonnegative variables `y`, write

\[
E_j=e_j(y),\qquad
A=\sum_{j<r}E_j,\quad B=E_r,\quad C=\sum_{j>r}E_j.
\]

The elementary-symmetric polynomial after the coordinate map `p=y/(1+y)` has the exact expansion

\[
e_r(p)=
\frac{\sum_{j=r}^m\binom{j}{r}E_j}
{\sum_{j=0}^mE_j}.
\]

Since every `binom(j,r)>=1` for `j>=r`,

\[
e_r(p)
\ge \frac{B+C}{A+B+C}
\ge \frac{B}{A+B}.
\]

Applied to `y_{-i}`, the final fraction is exactly the right side of (4.1), proving the first inequality in (5.1). The second follows coordinatewise from `1-e^{-x}\le x` and monotonicity of `e_{k-1}` on the nonnegative orthant.

Now integrate along the radial path `s t`, using `F(0)=0`:

\[
F(t)=\int_0^1\sum_i t_i\partial_iF(st)\,ds
\le\int_0^1\sum_i t_i e_{k-1}(s t_{-i})\,ds.
\]

Since `e_{k-1}(s t_{-i})=s^{k-1}e_{k-1}(t_{-i})` and
`sum_i t_i e_{k-1}(t_{-i})=k e_k(t)`, we obtain

\[
\boxed{F_{n,k}(t)\le e_k(t)\qquad(t\ge0).}
\tag{5.2}
\]

Thus every threshold class has a completely explicit positive-coefficient multilinear **global majorant**, and it is asymptotically exact at the small-scale leading term (4.3).

This does not solve the source budget. For symmetric `q=M 1`, as `M->infinity`,

\[
F_{n,k}(q)
=(n-k+1)M-\log\binom{n}{k-1}+o(1),
\tag{5.3}
\]

whereas

\[
e_k(q)=\binom nk M^k.
\]

Consequently the pure degree-`k` majorant would require

\[
\gamma^{k-1}\binom nkM^k
\lesssim (n-k+1)M,
\]

which is impossible for fixed `gamma>0`, `k>=2` and large `M`.

So (5.2) is a real theorem-sized structural reduction, but not source closure.

## 6. A rigorous no-go for purely linear certificates

Suppose `P` is linear, globally `P>=F`, and satisfies the source budget at a positive vector `q`:

\[
P(\gamma q)\le\gamma F(q).
\]

Linearity gives `P(gamma q)=gamma P(q)`, while global majorization gives `P(q)>=F(q)`. Hence equality must hold:

\[
P(q)=F(q).
\]

At an interior positive `q`, `P-F` has a global minimum zero, so

\[
\nabla P=\nabla F(q).
\]

Euler's identity for the linear `P` then forces

\[
F(q)=P(q)=q\cdot\nabla P=q\cdot\nabla F(q).
\tag{6.1}
\]

But (4.4) shows that for every positive direction and `k>=2`, sufficiently small positive `q` violate (6.1):

\[
q\cdot\nabla F(q)-F(q)>0.
\]

Therefore

\[
\boxed{
\text{for }k\ge2,\text{ no purely linear global certificate can satisfy the }C_\gamma\text{ budget at all sufficiently small positive }q,
}
\tag{6.2}
\]

for any `gamma>0`.

This is a route no-go, not a refutation of Talagrand's problem.

## 7. Method #5 continued — a parameterized tangent-majorant family

The failure of both pure degree `k` and pure degree `1` certificates suggests interpolating them. The concavity of

\[
p(x)=1-e^{-x}
\]

provides an exact parameter family.

For any tangent point `r_j>=0`,

\[
p(x)\le a_j+b_jx,
\qquad
a_j=1-(1+r_j)e^{-r_j}\ge0,
\qquad b_j=e^{-r_j}\ge0.
\tag{7.1}
\]

Combine (5.1), radial integration and (7.1). Define

\[
\boxed{
P_r(t)=
\int_0^1\sum_i t_i\,
 e_{k-1}\!\left(a_{-i}+s(b\odot t)_{-i}\right)ds.
}
\tag{7.2}
\]

Because elementary symmetric polynomials are multiaffine and all `a_j,b_j` are nonnegative, `P_r` is a positive-coefficient multilinear polynomial of degree at most `k`.

Moreover, for every `t>=0`,

\[
\partial_iF(st)
\le e_{k-1}(p(s t_{-i}))
\le e_{k-1}(a_{-i}+s(b\odot t)_{-i}),
\]

so integrating yields the exact global certificate

\[
\boxed{F_{n,k}(t)\le P_r(t)\qquad\forall t\ge0.}
\tag{7.3}
\]

At `r=0`, `a=0,b=1`, and (7.2) reduces to

\[
P_0(t)=e_k(t).
\]

Thus (7.2) is an explicit continuous family interpolating away from the small-scale degree-`k` certificate.

However, a single symmetric tangent scale does not solve the budget. At symmetric large `q=M 1`, choosing `r=q` makes `a->1` and `b->0`, so the leading linear contribution is

\[
\frac1\gamma P_r(\gamma q)
\sim n\binom{n-1}{k-1}M
=k\binom nkM,
\]

whereas (5.3) has leading coefficient only `n-k+1`. The tangency removes the wrong high-degree growth but pays far too much linear mass.

So the exact parameterization identifies the next obstruction rather than merely moving it around:

\[
\boxed{
\text{a successful certificate cannot be a one-scale symmetric tangent majorant.}
}
\tag{7.4}
\]

## 8. Method #15 — break symmetry and expose the two-regime geometry

Take `q` with exactly `k-1` heavy coordinates equal to `M` and the remaining

\[
m=n-k+1
\]

light coordinates equal to `epsilon>0`. Send `M->infinity` with `epsilon` fixed.

The event defining the complement of the threshold class is then dominated by the requirement that all `k-1` heavy coordinates are present while the light coordinates determine the remaining hazard. Directly from (3.1),

\[
\boxed{F(q)=m\epsilon+O(e^{-M}).}
\tag{8.1}
\]

The derivative formula (4.1) yields

\[
\boxed{
\partial_iF(q)\to0\quad\text{on heavy coordinates},
\qquad
\partial_iF(q)\to1\quad\text{on light coordinates}.
}
\tag{8.2}
\]

Thus the exact source geometry has two incompatible-looking asymptotic faces:

- near the origin, `F` starts in pure degree `k`, with leading term `e_k`;
- after `k-1` coordinates saturate, it becomes essentially degree `1` on the unsaturated coordinates.

This explains the preceding no-go results. A universal `C_gamma` certificate, if it exists, must be **multiscale and order-statistic aware**: it has to transition from `k`-way interaction to a linear cost on whichever coordinates remain unsaturated.

The most obvious broken-symmetry tangent choice — make the `k-1` heavy tangent coordinates large and leave light tangent coordinates at zero — correctly creates the desired light-coordinate linear term, but the `i`-summands corresponding to privileged heavy indices still generate superlinear spillover. So even the first adaptive tangent architecture is not yet budget-valid.

This is a precise failure mode, not a source counterexample.

## 9. Method #22 — what the accumulated failures are actually saying

The earlier R15 failure and the new calculus line up cleanly:

1. **Disjoint-block recursion fails** because exact cardinality dynamic programming must reuse blocks.
2. **The natural symmetric sparse dual witness fails** because at small scale the source hazard is genuinely `k`-homogeneous and the dual ratio stays on the non-refuting side.
3. **Pure degree-k primal certificates fail in the dense regime**, where the true hazard has only linear growth.
4. **Pure linear certificates fail near the origin** by the positive Euler defect (4.4).
5. **One-scale symmetric tangent certificates fail** because they overpay the dense linear coefficient.
6. **Naive broken-symmetry tangency fails** because privileged heavy coordinates leak high-degree terms.

The common missing idea is therefore no longer vague:

\[
\boxed{
\text{construct a positive multilinear majorant whose effective degree decreases as coordinates saturate, without paying for all possible saturation patterns simultaneously.}
}
\tag{9.1}
\]

That is closer to an adaptive hazard / decision-tree / stopping-time certificate than to one fixed symmetric polynomial template.

This is mathematically interesting, but it confirms rather than overturns the admission diagnosis: F0111 is an exact, current-open-looking, ownership-clear problem with a useful explicit structure, yet the full source still has universal quantifiers over `n,k,q` and the present route is theorem-scale. It is honestly **HARD-LEANING / NOT CLOSABLE-READY**.

I therefore did not create `operations/claims/F0111.md` and did not relabel the tangent family as source closure.

## 10. Prior-art/status scope

The current bounded literature screen preserves the R15 distinction: later work on Talagrand p-small / weakly-p-small and Kahn--Kalai-type conjectures does not automatically imply Problem 10.9's stronger pointwise positive-multilinear-majorant condition for every heterogeneous `q`. No accessible source-matching theorem was recovered in this bounded pass. That search miss is not a worldwide novelty or openness certificate.

The exact identities and inequalities in Sections 4--8 are proved on the page and do not depend on a numerical checker. No finite computational claim is load-bearing here, so creating a checker merely to reproduce symbolic algebra would invert the 90/10 rule.

## 11. Model/control boundary

The prompt requests GPT-6 with maximum reasoning. The actual model available to this invocation is **GPT-5.6 Sol**, and authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**.

The exposed task-management surface still provides prompt/title, scheduling/timing, enabled state and timing-mode controls, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run routing receipt and no guaranteed hour-long runtime field. Making GPT-6/maximum binding requires an owner-authorized product/workspace/backend/API surface that exposes those controls and attestations.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary. Repository history records later modification from an authorized context. The lawful workaround is the owning/admin-authorized context or platform support, not task duplication or a permission bypass. No scheduler or permission change was made.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  continuity:
    I0100:
      source: Bandeira_Randomstrasse_2025_Conjecture_26_Paley_one_localization
      status: OPEN_PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
      metric_name: largest_admissible_prime_with_matching_exact_primal_dual_certificates
      metric_before: 1213
      metric_after: 1213
      covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
      retirement_unchanged_count: 6
      active_research_this_run: false
  successor:
    status: SUCCESSOR_ADMISSION_REQUIRED
    active_source: NONE
    claim_created: false
    metric_name: E_ready
    metric_before: 0
    metric_after: 0
    movement: none
    unchanged_count: UNKNOWN
  methods_actually_tried: [5,15,22]
  substantive_screen:
    problem_id: F0111
    source: Talagrand_STOC_2010_Problem_10_9_threshold_classes_C_gamma
    disposition: OPEN_LOOKING_OWNERSHIP_CLEAR_HARD_LEANING_NOT_CLOSABLE_READY
    owner_found: false
    claim_created: false
    new_exact_results:
      - derivative_identity_partial_i_F_equals_e_kminus1_over_Z
      - gradient_domination_by_elementary_symmetric_polynomial_of_selection_probabilities
      - explicit_global_majorant_F_le_e_k
      - linear_certificate_no_go_from_positive_Euler_defect
      - parameterized_positive_multilinear_tangent_majorant_family_P_r
      - heavy_light_asymmetry_limit_and_degree_collapse
    exact_blocker: >-
      Build one positive-coefficient multilinear certificate with the Talagrand budget
      uniformly in n,k and heterogeneous q, whose effective degree adapts from k near
      the origin to degree 1 after k-1 coordinates saturate, without paying for all
      saturation patterns simultaneously.
  evidence:
    original_source_checked: true
    current_literature_checked: true
    repository_ownership_checked: true
    prior_R15_failure_screen_read: true
    finite_checker_needed: false
  audit_ids: []
  remaining_obligation: >-
    Continue successor admission. Do not claim F0111 unless the full source becomes
    genuinely closable and all source/current/ownership gates are still clear. Do not
    reopen I0100 absent a fresh reassignment.
  next_methods: [7,19,25]
  closure_claim: false
```

## 13. Next cursor

Use **#7 TAKE THE LIMIT, #19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE** on the next admissible ownership-clear source. If F0111 remains merely a screening probe, the specific mathematical question worth carrying forward is whether the adaptive saturation structure in (9.1) can be represented by a positive multilinear decision-tree certificate without exponential overcounting. That is not yet enough to call the source CLOSABLE.

**NO I0100 CLOSURE CLAIM. NO F0111 CLAIM. R20 remains `SUCCESSOR_ADMISSION_REQUIRED`.**
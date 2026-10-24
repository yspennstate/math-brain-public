Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-reasoning telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 constructive random 3-SAT: branching-corrected four-parameter control

Date: 2026-09-20
Repository / branch: private `yspennstate/math-open-problems` / `master`
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`
Current target: **T04 — classical iid random 3-SAT threshold**
Status: **OPEN / PARTIAL**

Source-normalized explicit numerical bracket before / after:

\[
[\alpha_{\rm LB},\alpha_{\rm UB}] = [3.52,4.4898]\;\longrightarrow\;[3.52,4.4898].
\]

Thus the explicit certified-width metric remains

\[
U-L=0.9698\to0.9698.
\]

**No source-level numerical movement this run.** The mathematical progress is mechanism-level: an exact first-order branching-corrected polarity rule for the four-parameter Hajiaghayi–Sorkin degree state is derived below. This directly fills one analytic sub-obligation identified by the original lower-bound paper, but it does not yet certify a lower bound above 3.52.

## 1. Controlling assignment and continuity

The current owner progress-first directive supersedes this track's old residue-shard / admission-only loop. The present assignment is the exact iid random 3-SAT problem: `m=floor(alpha n)` independent uniformly signed clauses on three distinct uniformly selected variables. This run therefore preserves the old NM13-06 admission reports as history but does not continue screening for an unrelated residue-5 source.

The broad F0097 small-fixed-k threshold-existence work is preserved as historical R03 work rather than silently taken over. Its main failed routes included one-variable cavity iteration, fractional solution-count martingales, randomized boosters, generic helper replacement, mesoscopic-to-local Fourier transfer, loose-hypertree cavity, ranked-spreadness black boxes, and positive-temperature/free-energy compactification. The present route is deliberately complementary: a constructive lower-bound algorithm using the four-parameter local degree state explicitly suggested by the Hajiaghayi–Sorkin 3.52 paper.

No exact T04 random-3-SAT result is excluded by the current POSTED registry.

## 2. Source and current-status checkpoint

The source model is the standard random proper 3-CNF model: each clause chooses three distinct variables uniformly and then independent uniform signs.

Hajiaghayi and Sorkin prove the rigorous algorithmic lower bound `alpha>=3.52` and explicitly identify a natural next refinement: instead of recording only total positive/negative occurrence counts, separate each sign by whether it currently appears in a 2-clause or a 3-clause. They state that this four-parameter heuristic remains analyzable in the same differential-equation framework, but leave open both which variable class should be chosen and which truth value should be assigned.

The explicit rigorous numerical upper bound retained here is `alpha<=4.4898` from Diaz--Kirousis--Mitsche--Perez-Gimenez. A 2026 primary status paper on random k-SAT states that the small-fixed-k satisfiability-threshold problem remains open and recalls rigorous interpolation upper bounds matching the one-step-RSB variational prediction. In its degree normalization `d=k alpha`, the displayed physics prediction for `k=3` is about `d_sat=12.801`, i.e. `alpha≈4.267`. I do **not** replace `4.4898` by that decimal in the frozen explicit numerical metric here because this run has not recovered and independently certified the numerical evaluation of the rigorous interpolation functional at that value. The distinction is: a stronger rigorous variational upper bound exists, while `4.4898` remains the explicitly verified project numerical upper endpoint recovered in this run.

Large-k exact-threshold theorems and the 2025 k-wise-independent clause model are not this source problem.

This is a bounded current-status check, not a claim of exhaustive worldwide novelty.

## 3. Four-parameter state

For an unset variable define the degree state

\[
(a,b,c,d),
\]

where

- `a` = positive appearances in current 2-clauses,
- `b` = negative appearances in current 2-clauses,
- `c` = positive appearances in current 3-clauses,
- `d` = negative appearances in current 3-clauses.

Let `x_{a,b,c,d}` be the density of unset variables in this class, measured per original variable. Let `m_2,m_3` be the current densities of 2- and 3-clauses. Then

\[
\sum_{a,b,c,d}(a+b)x_{a,b,c,d}=2m_2,
\qquad
\sum_{a,b,c,d}(c+d)x_{a,b,c,d}=3m_3.
\]

The calculation below is a first-order local calculation under the same conditional-uniform configuration-model / locally tree-like regime used in the standard differential-equation analysis, and while the unit-clause cascade is subcritical.

## 4. Lemma: exact first-order unit-cascade branching factor

A positive unit literal is attached to a variable with size-biased probability

\[
\frac{a\,x_{a,b,c,d}}{2m_2},
\]

and a negative unit literal with probability

\[
\frac{b\,x_{a,b,c,d}}{2m_2}.
\]

If a positive unit sets the variable TRUE, every remaining negative 2-clause containing that variable becomes a new unit, so it creates `b` children. If a negative unit sets the variable FALSE, it creates `a` children. Therefore the mean offspring number of the unit-propagation branching process is

\[
\boxed{
\rho
 = \frac1{2m_2}\sum_{a,b,c,d}x_{a,b,c,d}(ab+ba)
 = \frac1{m_2}\sum_{a,b,c,d}ab\,x_{a,b,c,d}.
}
\tag{1}
\]

This is exact at the first-order local-tree level and notably depends only on the signed 2-clause degrees.

## 5. Expected drift generated by one forced assignment

For a positive forced assignment, the source unit clause has already been removed from the 2-clause count. The remaining `(a-1)+b` incident 2-clauses leave the 2-clause population, while each of the `d` negative 3-clauses shortens to a 2-clause. Hence

\[
\Delta m_2^{(+)}=d-(a+b-1).
\]

For a negative forced assignment,

\[
\Delta m_2^{(-)}=c-(a+b-1).
\]

All incident 3-clauses disappear from the 3-clause population regardless of which sign forced the assignment, so

\[
\Delta m_3=-(c+d).
\]

Averaging over the size-biased forced-literal distribution gives the expected per-forced-assignment drifts

\[
\boxed{
 g_2=
 \frac1{2m_2}\sum x_{a,b,c,d}
 \left[
 a\{d-(a+b-1)\}
 +b\{c-(a+b-1)\}
 \right]
}
\tag{2}
\]

and

\[
\boxed{
 g_3=-\frac1{2m_2}\sum x_{a,b,c,d}(a+b)(c+d).
}
\tag{3}
\]

## 6. Free choice plus its complete expected subcritical avalanche

Now choose a variable in class `(a,b,c,d)` freely.

If it is set TRUE:

- all `a+b` incident 2-clauses leave `m_2`;
- the `d` negative 3-clauses shorten to 2-clauses;
- all `c+d` incident 3-clauses leave `m_3`;
- the `b` negative 2-clauses become seed unit clauses.

Thus before the cascade,

\[
\Delta m_2=d-(a+b),\qquad \Delta m_3=-(c+d).
\]

In a subcritical Galton--Watson cascade with mean offspring `rho`, `b` seeds produce expected total forced assignments `b/(1-rho)`. Consequently

\[
\boxed{
D_T^{(2)}=d-(a+b)+\frac{b g_2}{1-\rho},
\qquad
D_T^{(3)}=-(c+d)+\frac{b g_3}{1-\rho}.
}
\tag{4}
\]

Similarly, if it is set FALSE, the `c` positive 3-clauses shorten to 2-clauses and the `a` positive 2-clauses seed units, giving

\[
\boxed{
D_F^{(2)}=c-(a+b)+\frac{a g_2}{1-\rho},
\qquad
D_F^{(3)}=-(c+d)+\frac{a g_3}{1-\rho}.
}
\tag{5}
\]

These formulas make the tradeoff explicit: a polarity can be locally worse by direct shortening of 3-clauses but better because the resulting unit cascade cleans up clauses.

## 7. Branching-corrected polarity index

For a linear clause-risk potential

\[
V_\eta=m_2+\eta m_3,
\]

define

\[
g_\eta=g_2+\eta g_3.
\]

Subtracting (5) from (4) yields the cancellation

\[
\boxed{
D_T(V_\eta)-D_F(V_\eta)
=(d-c)+(b-a)\frac{g_\eta}{1-\rho}.
}
\tag{6}
\]

Therefore, for this first-order objective, the optimal local polarity is given by a single signed index:

\[
\boxed{
\text{set TRUE iff }
(d-c)+(b-a)\lambda_\eta\le 0,
\qquad
\lambda_\eta:=\frac{g_\eta}{1-\rho};
}
\tag{7}
\]

otherwise set FALSE.

This is the main result of the run. The nominal four-dimensional state does **not** require an arbitrary four-dimensional polarity lookup table for a fixed linear potential. Polarity depends only on the two signed contrasts `d-c` and `b-a`, coupled by one state-dependent global shadow price `lambda_eta` representing the expected value of a unit-propagation cleanup step.

The result does not solve the separate variable-class selection problem, nor does it prove that a linear `V_eta` is the globally optimal control objective. It supplies an explicit analytically justified polarity subroutine that can be embedded in the full four-parameter differential equations or in an HJB/adjoint optimization.

## 8. Forced propagation is potential-decreasing for eta >= 1

There is a useful sign check. For a positive forced assignment, its contribution to `V_eta` is

\[
 d-(a+b-1)-\eta(c+d)
 =-(a+b-1)-\eta c-(\eta-1)d\le0
\]

for `eta>=1`. For a negative forced assignment,

\[
 c-(a+b-1)-\eta(c+d)
 =-(a+b-1)-\eta d-(\eta-1)c\le0.
\]

Hence

\[
\boxed{g_\eta\le0\quad\text{for every }\eta\ge1.}
\tag{8}
\]

So under any such potential, a subcritical unit cascade is not merely a nuisance: in expectation it is a cleanup mechanism. This explains why a degree heuristic that deliberately creates some unit clauses can outperform a myopic rule that minimizes immediate unit creation.

## 9. Poisson-closure sanity calculation — heuristic only

As a diagnostic, suppose temporarily that

\[
a,b\stackrel{\rm iid}{\sim}{\rm Poisson}(m_2),
\qquad
c,d\stackrel{\rm iid}{\sim}{\rm Poisson}(3m_3/2),
\]

independently. This is **not** asserted for the degree-selected process; it is only a sanity closure.

Then

\[
\rho=m_2,
\qquad
 g_2=\frac32m_3-2m_2,
\qquad
 g_3=-3m_3,
\]

and therefore

\[
\boxed{
 g_\eta=\left(\frac32-3\eta\right)m_3-2m_2.
}
\tag{9}
\]

At `eta=0`, the sign changes near `m_3=(4/3)m_2`: in a 3-clause-heavy regime, seeding a forced cascade can increase `m_2`, whereas later in a 2-clause-heavy regime it can decrease `m_2`. At `eta=1`, it is always negative. The qualitative lesson is that a fixed lexicographic polarity rule should not be expected to be optimal across the whole trajectory; the shadow price in (7) should evolve with the state.

## 10. Consequence for a next constructive attack

The source lower-bound route can now be made more concrete:

1. retain the full truncated state `x_{a,b,c,d}` and the Hajiaghayi--Sorkin conditional-degree ODE machinery;
2. use (7) as the exact first-order polarity rule for a chosen adjoint / risk potential instead of an ad hoc sign choice;
3. optimize **which degree class** to expose using an HJB or terminal-shadow-price objective tied to the final residual-2-SAT subcriticality condition;
4. integrate the resulting finite truncation with rigorous interval enclosures and explicit tail/Lipschitz error;
5. certify the first `alpha=3.52+epsilon` at which `rho<1` throughout and the terminal residual 2-SAT lies in a rigorously satisfiable regime.

Only step 5 would move the source-level lower-bound endpoint. This run stops before numerical optimization because the new analytic control law is the actual new idea worth checking first; producing a checker for the unchanged `3.52` endpoint would violate the progress-first policy.

## 11. Before / after ledger

- Exact source: classical iid random 3-SAT with three distinct variables and independent uniform signs.
- Explicit numerical rigorous lower endpoint: `3.52 -> 3.52`.
- Explicit numerical rigorous upper endpoint retained: `4.4898 -> 4.4898`.
- Explicit bracket width: `0.9698 -> 0.9698`.
- Source status: **OPEN**.
- Worker status: **PARTIAL**.
- Mechanism-level result: four-parameter polarity control under the first-order subcritical-cascade model, **absent -> equation (7) derived**.
- Finite certificate: none; no finite claim was made.
- Numerical checker: none; no new numerical threshold claim was made.
- Main remaining obligation: turn the local control law into a globally analyzed degree-selection policy and rigorously certify `alpha>3.52`.

## ledger_delta

```yaml
ledger_delta:
  worker: NM13-06
  current_role: NM06_Constructive_Random_3SAT
  target: T04
  source_model: "iid random proper 3-CNF; m=floor(alpha n); 3 distinct variables; independent uniform signs"
  source_status: OPEN
  worker_status: PARTIAL
  source_metric:
    name: "explicit certified numerical threshold bracket width U-L"
    before: "[3.52, 4.4898], width 0.9698"
    after: "[3.52, 4.4898], width 0.9698"
    movement: NO_SOURCE_NUMERICAL_MOVEMENT
  mechanism_gain:
    name: "branching-corrected four-parameter polarity index"
    before: "four-parameter polarity choice left unspecified in inherited constructive route"
    after: "TRUE iff (d-c)+(b-a)*(g_eta/(1-rho)) <= 0 for linear potential V_eta=m2+eta*m3"
    supporting_identities:
      rho: "sum(ab*x)/m2"
      g2: "(1/(2m2))*sum x*[a(d-a-b+1)+b(c-a-b+1)]"
      g3: "-(1/(2m2))*sum x*(a+b)(c+d)"
      sign_check: "g_eta<=0 for eta>=1"
  literature_status:
    lower_explicit: "Hajiaghayi-Sorkin 3.52"
    upper_explicit_retained: "Diaz-Kirousis-Mitsche-Perez-Gimenez 4.4898"
    stronger_current_upper_note: "rigorous interpolation variational upper exists; displayed 1RSB numerical prediction near alpha 4.267 not independently certified as the project numerical endpoint in this run"
  inherited_failed_routes_not_reopened:
    - one_variable_cavity_iteration
    - fractional_solution_count_martingale
    - randomized_boosters
    - generic_helper_replacement
    - mesoscopic_to_local_fourier_transfer
    - loose_hypertree_cavity
    - ranked_spreadness_black_box
    - positive_temperature_free_energy_boundary
  next_attack: "full four-parameter truncated ODE plus adjoint/HJB class selection and interval-certified test at alpha>3.52"
  substantive_code: none
  reason_no_code: "analytic mechanism derived; no new finite or numerical threshold claim to certify"
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

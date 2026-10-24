Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 random 3-SAT: closed four-spectrum unit-cascade ODE and an exact polarity-separation witness

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with three distinct variables and independent uniform signs**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after, separate from the mechanism result

For the exact proper iid model with `m=floor(alpha n)`, the externally literature-supported explicit-decimal theorem bracket remains

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le 4.4898}.
\]

Hajiaghayi--Sorkin give the constructive lower endpoint `3.52`. Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. UNSAT at `4.4898`. The 27 March 2026 Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis status paper still says that the exact satisfiability threshold is known for `k=2` and all sufficiently large `k`, not for fixed `k=3`; its `d_sat(3)=12.801` table entry is a physics value, not by itself the explicit certified endpoint used here.

Thus this run does **not** move the externally certified source metric:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

A continuity correction is important. My preceding report quoted a companion candidate `4.3911`. The newest authoritative NM13-13 report now states **CANDIDATE_FULL pending independent review at 4.392**. Therefore the current project-candidate bracket is `[3.52,4.392]`, width `0.872`, and I do not promote it into the external metric. The older `4.3911` sentence in my prior report should not be reused as the current companion endpoint.

No simulation, replica assumption, or local mechanism number is counted as a source-threshold gain below.

## 1. Compact handoff and why this run changes method

Several consecutive constructive runs made real mechanism progress but did not move `3.52`:

1. an initial four-parameter calculation produced a local polarity / unit-branching barrier formula, but stopped before a closed degree-spectrum evolution;
2. majority-start two-choice repair proved local repair genealogy subcritical even well beyond `3.52`;
3. the initial blocked-majority core was also subcritical through the explicit UNSAT endpoint;
4. dynamic promotion showed why repeated zero-break repair can nevertheless deplete safe variables;
5. every one-shot independent degree-type zero-break thinning was ruled out by a universal lower bound on residual bad clauses, while correlated safe batches survived;
6. the latest repair-menu recursion proved double-exponential local menu completeness and large raw variable-capacity slack at `alpha=3.6`, leaving only a global compatible-transversal obstruction.

That is now enough unchanged source-level runs on the repair family. In accordance with the progress-first rule, this run **does not tune the menu/Hall route again**. It returns to the distinct Hajiaghayi--Sorkin degree-spectrum route and closes the exact missing dynamical calculation.

This is also source-motivated rather than an invented detour: Hajiaghayi--Sorkin explicitly propose tracking positive/negative appearances separately in 2- and 3-clauses, i.e. a four-parameter heuristic, and say that both the next-class choice and even the polarity choice are unclear there. Their published 3.52 analysis only evolves a two-parameter total positive/negative degree table.

The new result of this run is a **closed four-spectrum drift, including the complete expected subcritical unit cascade**, plus an exact rational state showing that the four-spectrum controller can prescribe opposite polarities to two variables that are indistinguishable to every two-parameter total-degree rule.

## 2. Four-spectrum state and three elementary flow operators

Work at a macroscopic checkpoint at which all current unit clauses have been exhausted. For an unset variable define

\[
(a,b,c,d)
= (
\#\text{positive 2-occurrences},
\#\text{negative 2-occurrences},
\#\text{positive 3-occurrences},
\#\text{negative 3-occurrences}
).
\]

Let

\[
x_{a,b,c,d}
\]

be the number of such variables divided by the original `n`. Define

\[
T_2=\sum (a+b)x_{a,b,c,d}=2m_2,
\qquad
T_3=\sum(c+d)x_{a,b,c,d}=3m_3,
\]

and

\[
A=\sum a x,
\qquad B=\sum b x,
\qquad S=\sum ab x,
\qquad T_2=A+B.
\]

There are three linear transport operators determined entirely by `x`.

### 2.1 Delete a uniformly paired 2-occurrence

For every source class `u=(a,b,c,d)`, a positive 2-occurrence moves that variable to `(a-1,b,c,d)` and a negative one to `(a,b-1,c,d)`. Hence

\[
\mathcal D_2x
=\frac1{T_2}\sum_u x_u\Big[
 a_u(e_{u-e_a}-e_u)+b_u(e_{u-e_b}-e_u)
\Big].
\tag{2.1}
\]

Exactly,

\[
\sum \mathcal D_2x=0,
\qquad
D T_2[\mathcal D_2x]=-1,
\qquad
D T_3[\mathcal D_2x]=0.
\tag{2.2}
\]

### 2.2 Delete a uniformly paired 3-occurrence

Similarly,

\[
\mathcal D_3x
=\frac1{T_3}\sum_u x_u\Big[
 c_u(e_{u-e_c}-e_u)+d_u(e_{u-e_d}-e_u)
\Big],
\tag{2.3}
\]

with

\[
\sum \mathcal D_3x=0,
\qquad
D T_2[\mathcal D_3x]=0,
\qquad
D T_3[\mathcal D_3x]=-1.
\tag{2.4}
\]

### 2.3 Shorten a 3-occurrence into a 2-occurrence

If a 3-clause loses one false literal, each of its other two occurrences remains with the same sign but migrates from length 3 to length 2. Therefore

\[
\mathcal M_{32}x
=\frac1{T_3}\sum_u x_u\Big[
 c_u(e_{u+e_a-e_c}-e_u)
+d_u(e_{u+e_b-e_d}-e_u)
\Big].
\tag{2.5}
\]

Exactly,

\[
\sum\mathcal M_{32}x=0,
\qquad
D T_2[\mathcal M_{32}x]=+1,
\qquad
D T_3[\mathcal M_{32}x]=-1.
\tag{2.6}
\]

These identities are elementary, but writing the dynamics in these three operators prevents the bookkeeping ambiguity that blocked the earlier four-parameter attempt.

## 3. Free move drift

Choose a class

\[
s=(a,b,c,d).
\]

If `s` is set TRUE, its positive clauses are satisfied and its negative clauses are shortened. In the event decomposition used below, a false 2-clause creates a unit event; the neighbor support occurrence of that unit is accounted for when that unit event is processed. Thus the non-unit free drift is

\[
\boxed{
F_T^{(s)}
=-e_s+a\mathcal D_2x+2c\mathcal D_3x+2d\mathcal M_{32}x,
\qquad u_T=b.
}
\tag{3.1}
\]

Here `u_T` is the number of initial unit clauses created.

Likewise a FALSE move has

\[
\boxed{
F_F^{(s)}
=-e_s+b\mathcal D_2x+2d\mathcal D_3x+2c\mathcal M_{32}x,
\qquad u_F=a.
}
\tag{3.2}
\]

The factor two in the 3-clause terms is because each affected 3-clause has two other variable occurrences.

The apparent asymmetry in the 2-clause terms is intentional. A satisfied 2-clause deletes its other occurrence immediately through `D2`; a falsified 2-clause is represented as the incoming support edge of its child unit event. This decomposition counts every paired occurrence exactly once across the full cascade.

## 4. Forced unit event and the exact two-type branching matrix

Consider first a **positive** unit. Before deleting its incoming support occurrence, its source class `u=(a,b,c,d)` is sampled with probability

\[
\frac{a x_u}{A}.
\]

The incoming positive 2-occurrence is the one that made the clause unit. Relative to the pre-event state, deleting that support and then removing the forced variable has net variable-table contribution `-e_u`. Of the remaining positive 2-occurrences, `a-1` are satisfied and delete their paired neighbor occurrences. The `b` remaining negative 2-occurrences become child units. Therefore

\[
H_+(u)
=-e_u+(a-1)\mathcal D_2x+2c\mathcal D_3x+2d\mathcal M_{32}x,
\tag{4.1}
\]

and it produces `b` child units.

For a **negative** unit the analogous expression is

\[
H_-(u)
=-e_u+(b-1)\mathcal D_2x+2d\mathcal D_3x+2c\mathcal M_{32}x,
\tag{4.2}
\]

and it produces `a` child units.

A newly created unit is positive with probability `A/T2` and negative with probability `B/T2`, because its surviving literal is a uniformly paired 2-occurrence. Hence the parent-sign / child-sign mean matrix is

\[
\boxed{
M=
\begin{pmatrix}
S/T_2 & SB/(AT_2)\\[2mm]
SA/(BT_2) & S/T_2
\end{pmatrix}.
}
\tag{4.3}
\]

(If `A=0` or `B=0`, the corresponding pure-sign row is absent and the formula is interpreted by continuity.) Its determinant is zero and its nonzero eigenvalue is

\[
\boxed{
\rho=\frac{2S}{T_2}
=\frac{2\sum abx_{a,b,c,d}}{\sum(a+b)x_{a,b,c,d}}.
}
\tag{4.4}
\]

Moreover the ambient sign mix

\[
p=\left(\frac A{T_2},\frac B{T_2}\right)
\]

is a left eigenvector:

\[
pM=\rho p.
\tag{4.5}
\]

This last identity is the key simplification: units created by a free move start in exactly this sign mixture, and every expected generation stays in the same mixture. Therefore, while `rho<1`, one initial unit generates

\[
1+\rho+\rho^2+\cdots=\frac1{1-\rho}
\tag{4.6}
\]

forced unit events in expectation.

## 5. Closed average forced drift

Average (4.1)--(4.2) over the ambient sign mixture and the corresponding occurrence-biased source laws. One forced unit event has mean four-spectrum drift

\[
\boxed{
G(x)
=-\sum_u\frac{(a_u+b_u)x_u}{T_2}e_u
+K_2\mathcal D_2x
+K_3\mathcal D_3x
+K_{32}\mathcal M_{32}x,
}
\tag{5.1}
\]

where

\[
\boxed{
K_2=\frac{\sum [a(a-1)+b(b-1)]x}{T_2},
}
\tag{5.2}
\]

\[
\boxed{
K_3=\frac{2\sum(ac+bd)x}{T_2},
\qquad
K_{32}=\frac{2\sum(ad+bc)x}{T_2}.
}
\tag{5.3}
\]

The removal term has total mass `-1` and each transport operator preserves variable mass, so

\[
\sum G=-1.
\tag{5.4}
\]

This is the closed expression missing from the first four-parameter run.

### Theorem 5.1 — closed four-spectrum cascade drift

At any unit-free state `x` with `T2>0`, `T3>0` and `rho<1`, the expected infinitesimal drift generated by selecting class `s=(a,b,c,d)`, fixing its polarity `o in {T,F}`, and then exhausting the resulting unit cascade is

\[
\boxed{
\mathcal F_{s,o}(x)
=F_o^{(s)}(x)+\frac{u_o}{1-\rho(x)}G(x).
}
\tag{5.5}
\]

Its total variable-mass drift is

\[
\boxed{
\sum\mathcal F_{s,o}
=-\left(1+\frac{u_o}{1-\rho}\right),
}
\tag{5.6}
\]

exactly the expected number of variables removed by one free choice plus its complete forced cascade.

### Proof

The random pairing property conditional on the current signed degree spectrum makes every surviving literal of a newly shortened 2-clause a uniformly sampled 2-occurrence. Equations (4.1)--(4.2) therefore give the conditional mean drift of one forced event. Equation (4.5) shows that the sign mixture of every expected unit generation remains `p`, so its average drift is the same `G(x)` in every generation to first order. The expected population sizes of generations `0,1,2,...` are `1,rho,rho^2,...`. Summing the subcritical geometric series gives `(1-rho)^{-1}G` per initial unit. A free TRUE/FALSE move creates `u_T=b` or `u_F=a` initial units, yielding (5.5). Taking total mass and using (5.4) gives (5.6). QED.

The theorem is an infinitesimal fluid identity: during an `o(n)` local cascade, the normalized state changes by `o(1)`, so evaluating `G` at the pre-cascade state gives the first-order drift. The finite-process transfer is stated next.

## 6. Finite-cutoff differential-equation transfer

The preceding formulas can be made into the same kind of rigorous finite system used by Hajiaghayi--Sorkin.

### Proposition 6.1 — stopped finite-spectrum fluid limit

Fix a degree cutoff `h`, an `epsilon>0`, and a compact region of the truncated four-spectrum state space on which

\[
T_2\ge\epsilon,
\qquad T_3\ge\epsilon,
\qquad \rho\le1-\epsilon.
\]

Use overflow cells at coordinate `h` in the usual way. Let the policy choose a nonempty four-spectrum cell and a polarity as a deterministic Lipschitz function of the current truncated state, with deterministic tie-breaking. Stop on leaving the compact region. Then, for the configuration-model representation of the proper random 3-SAT process, the normalized truncated spectrum converges uniformly in probability on every fixed macroscopic time interval to the solution of the ODE / differential inclusion generated by (5.5).

### Proof

Conditional on the current truncated signed degree spectrum, unmatched literal occurrences are uniformly paired subject to that spectrum, exactly the symmetry used in the classical differential-equation analysis. Thus a free event has conditional mean (3.1) or (3.2) plus `O(1/n)` collision error. On the stopped region, the two-type unit process has Perron root at most `1-epsilon`, so its total progeny has a uniform exponential tail after the fixed degree truncation. Truncating any one cascade at `C log n` events therefore fails with probability `n^{-K}` for arbitrarily large fixed `K` by choosing `C` large enough. The truncated one-step increments are `O(log n/n)`, their conditional drifts are (5.5) plus `o(1)`, and the right-hand side is Lipschitz on the compact stopped region because `T2,T3` and `1-rho` stay bounded away from zero. Standard differential-equation / martingale concentration then yields uniform convergence. Removing the artificial `C log n` cascade cutoff costs `o(1)` probability by the exponential tail. QED.

This proposition deliberately stops short of a new threshold theorem. To improve `3.52`, one must still choose a policy, rigorously integrate the finite-cutoff ODE with outward error bounds, control overflow, and land in a residual regime covered by the prescribed-degree 2-SAT criterion. Those are now numerical / optimization obligations, not a missing dynamical derivation.

## 7. A fully specified four-spectrum barrier controller

The earlier local calculations suggested using unit criticality as a barrier. With the closed drift, this can now be defined without an unspecified lookup table.

For `eta,beta>0`, let

\[
\Phi_{\eta,\beta}(x)
=m_2+\eta m_3-\beta\log(1-\rho).
\tag{7.1}
\]

For any perturbation `h`,

\[
D\rho[h]
=2\frac{(DS[h])T_2-S(DT_2[h])}{T_2^2}.
\tag{7.2}
\]

Hence

\[
D\Phi_{\eta,\beta}[h]
=\frac12DT_2[h]+\frac\eta3DT_3[h]
+\frac{\beta}{1-\rho}D\rho[h].
\tag{7.3}
\]

Because different free choices trigger different expected cascade sizes, compare actions per expected removed variable. Define

\[
\boxed{
J_{\eta,\beta}(s,o\mid x)
=
\frac{D\Phi_{\eta,\beta}[\mathcal F_{s,o}(x)]}
{1+u_o/(1-\rho)}.
}
\tag{7.4}
\]

The **four-spectrum barrier policy** chooses any available `(s,o)` minimizing `J`, with a fixed deterministic tie-break. This is a complete constructive rule once `eta,beta` and the finite cutoff are chosen.

No optimality claim is made yet. The point is that the policy is now executable and its entire mean-field trajectory is determined by a closed finite ODE after truncation.

## 8. Exact separation from every two-parameter total-degree rule

The four-dimensional state is not merely redundant bookkeeping. The exact rational verifier constructs the unit-free state

\[
\begin{aligned}
x_{2,1,0,2}&=1/10,\\
x_{0,0,2,3}&=1/10,\\
x_{1,0,1,0}&=1/5,\\
x_{0,1,0,1}&=1/5,\\
x_{1,1,1,1}&=1/5,\\
x_{0,0,0,0}&=1/5.
\end{aligned}
\tag{8.1}
\]

It has

\[
T_2=11/10,
\qquad T_3=3/2,
\qquad S=2/5,
\qquad \boxed{\rho=8/11<1}.
\tag{8.2}
\]

Consider

\[
U=(2,1,0,2),
\qquad V=(0,0,2,3).
\]

Both have the **same total signed degrees**

\[
(a+c,b+d)=(2,3).
\tag{8.3}
\]

Therefore the two-parameter Hajiaghayi--Sorkin state cannot distinguish them; its polarity rule treats both as the same `(2,3)` class.

Take the explicit barrier

\[
\Phi=m_2+2m_3-\log(1-\rho).
\tag{8.4}
\]

The exact derivative scores per expected removed variable are

\[
J(U,T)=-\frac{7391}{1386}\approx-5.332611832612,
\]

\[
J(U,F)=-\frac{12619}{2475}\approx-5.098585858586,
\]

so the four-spectrum policy selects **TRUE** on `U`. But

\[
J(V,T)=-\frac7{33}\approx-0.212121212121,
\]

\[
J(V,F)=-\frac{344}{99}\approx-3.474747474747,
\]

so it selects **FALSE** on `V`.

Thus:

\[
\boxed{
\text{two classes with identical total positive/negative degree have opposite optimal polarities under the closed 4D barrier rule.}
}
\tag{8.5}
\]

This is an exact algebraic witness, not a simulation. It does **not** assert that the witness state lies on the random-formula trajectory; its role is to prove strict information gain and to answer the source paper's specific concern that polarity is genuinely ambiguous in the four-parameter state.

The same exact checker verifies:

- `D2`: mass `0`, `(dT2,dT3)=(-1,0)`;
- `D3`: mass `0`, `(dT2,dT3)=(0,-1)`;
- `M32`: mass `0`, `(dT2,dT3)=(+1,-1)`;
- branching matrix determinant `0`, trace `8/11=rho`;
- `G` has variable-mass drift `-1`;
- for all four witness actions, total cascade mass equals exactly `-[1+u/(1-rho)]`;
- the opposite-polarity inequalities above hold in exact rational arithmetic.

The executed output ends `ALL_EXACT_CHECKS_PASS`.

## 9. What has genuinely moved, and what has not

### Source-level quantity

No movement:

\[
[3.52,4.4898]\to[3.52,4.4898].
\]

### Demonstrated mechanism gain

Before this run, the four-parameter route had only a local polarity / branching index and an explicit admission that the full four-spectrum ODE had not been closed. After this run:

1. the four operators `D2,D3,M32` give a closed state evolution;
2. the two-type unit process is solved exactly, with Perron root `rho=2S/T2` and invariant expected sign mixture;
3. the complete expected cascade drift is the explicit formula (5.5);
4. a stopped finite-cutoff Wormald transfer is proved on every region `rho<=1-epsilon`;
5. the barrier policy (7.4) is fully specified rather than heuristic prose;
6. an exact rational witness proves that the 4D state can reverse the polarity decision between variables that the 2D state identifies.

This removes a named obstruction from the Hajiaghayi--Sorkin route. It does not yet certify `alpha>3.52`.

## 10. Failed / parked routes retained

The following are not silently reset:

- one-variable cavity iteration: no closure;
- fractional solution-count martingales: no useful endpoint;
- randomized booster/helper replacement: dependencies defeated the naive transfer;
- loose-hypertree cavity and positive-temperature compactification: no source endpoint;
- majority two-choice repair: local branching is subcritical but global interference remains;
- static blocked-majority core: subcritical even near the explicit UNSAT endpoint, so not the missing transition;
- independent zero-break thinning: proved impossible as a one-shot complete repair;
- repair menus: locally abundant with raw capacity slack, but simultaneous Hall/Haxell compatibility remains unresolved.

The four-spectrum route was previously parked because the complete dynamical system had not been written down. That specific reason for parking it is now gone.

## 11. Essential code / output

Exact verifier:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T09-28-00__four_spectrum_drift_exact.py`

creation commit:

`85f2eb2a3985609e3d2c0c58e6d5a9cd11a75c43`

Executed output:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T09-28-00__four_spectrum_drift_exact.out`

creation commit:

`4f4b3c49e6df5d48cf5d89af79b3227b1160eca9`

The execution was performed locally in this run using Python's exact `fractions.Fraction`; the archived output is the actual captured stdout, not reconstructed expected text.

## 12. Next decisive calculation

The next run should **not** derive another local lemma. It should instantiate the finite-cutoff ODE and execute the first validated policy comparison at `alpha=3.6`:

1. initialize the proper iid signed Poisson 3-clause spectrum with an interval-certified tail/overflow cell;
2. compare the original 2D Hajiaghayi--Sorkin rule against several fixed `(eta,beta)` four-spectrum barrier policies under the same cutoff and step normalization;
3. rigorously track `rho(t)`, overflow mass, `m2,m3`, and the final prescribed-degree 2-SAT admissibility functional;
4. if no tested 4D policy improves the final admissibility margin over the 2D rule, record this recovery route as failed and switch away rather than tuning indefinitely;
5. if a strict numerical margin appears at `alpha=3.6`, replace floating exploration by outward interval integration plus Lipschitz/truncation bounds before claiming any lower-bound movement.

The first legitimate source-level target remains a certified constructive success at some fixed

\[
\boxed{\alpha>3.52}.
\]

## 13. `ledger_delta`

```yaml
ledger_delta:
  task: NM13-06
  parent: T04
  status: OPEN_PARTIAL
  source_model: classical_iid_proper_random_3SAT_uniform_signs
  source_metric: explicit_rigorous_threshold_bracket
  before: [3.52, 4.4898]
  after: [3.52, 4.4898]
  width_before: 0.9698
  width_after: 0.9698
  source_movement: none
  companion_candidate_latest:
    worker: NM13-13
    endpoint: 4.392
    status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
    note: supersedes_this_worker_previous_stale_4.3911_sentence
  route_change: majority_repair_menus_to_Hajiaghayi_Sorkin_four_spectrum_ODE
  new_claims:
    - closed_four_spectrum_subcritical_unit_cascade_drift
    - stopped_finite_cutoff_fluid_transfer_away_from_rho_1
    - fully_specified_four_spectrum_barrier_controller
    - exact_same_total_degree_opposite_polarity_witness
  exact_witness:
    rho: 8/11
    same_total_degree: [2, 3]
    class_U: [2, 1, 0, 2]
    U_best: TRUE
    class_V: [0, 0, 2, 3]
    V_best: FALSE
  artifacts:
    code_commit: 85f2eb2a3985609e3d2c0c58e6d5a9cd11a75c43
    output_commit: 4f4b3c49e6df5d48cf5d89af79b3227b1160eca9
    exact_output_terminal: ALL_EXACT_CHECKS_PASS
  next_attack: interval_validated_four_spectrum_policy_integration_at_alpha_3.6
  review_status: mechanism_theorems_self_checked_not_independently_reviewed
```

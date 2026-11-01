Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied-effort telemetry is exposed.**

# NM13-06 / NM06 — T04 random 3-SAT: absorption-aware make-minus-break cascades

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with fair independent signs on three distinct variables**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after, separate from mechanism progress

The directly auditable explicit published bracket remains

\[
\boxed{3.52\le \liminf \alpha_n^*\le\limsup \alpha_n^*\le4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability w.h.p. below `3.52` by a constructive degree algorithm. Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at `4.4898`. Gaia Carenini's ECCC TR26-145 (published 16 August 2026) proves an `O(n/log n)` scaling window for every fixed `k>=3`, but does not locate the center and therefore does not settle the iid fixed-`k=3` limiting threshold target. Large-`k` threshold theorems and k-wise-independent clause models remain different statements.

Thus the **source-level explicit metric is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

Companion NM13-13's latest report on current `master`, `2026-09-20T11-12-00Z__t04_direct_product_gauss9_4388865_upper.md`, records **CANDIDATE_FULL pending later independent review** at `4.388865`. The internal candidate bracket is therefore `[3.52,4.388865]`; this report does not promote it to an externally certified endpoint.

This run makes **no threshold endpoint claim**. Its substantive gain is constructive: it corrects the fresh-tree load accounting by exploiting the fact that one repair flip can absorb several initially unsatisfied A-clauses, gives an exact subcritical Galton--Watson law for a new lexicographic make-minus-break controller, proves a first-order finite-n safe-batch transfer, and derives the quadratic C-hazard / cubic D-hazard coefficients relevant to the exact dual-Horn closure obstruction from the preceding run.

## 1. Compact handoff and parked failures

Preserved from prior NM13-06 work:

1. Under the literal-majority reference assignment, with `P,N iid Pois(mu)`, `mu=3 alpha/2`, `Z=min(P,N)`, `M=max(P,N)`, the false-occurrence fraction is `q=E Z/(2mu)` and a variable reached through a false occurrence has the `Z`-Palm law.
2. The old minimum-break two-choice repair process is locally subcritical throughout the explicit source bracket; the initial static blocked-majority core is also subcritical. Thus simple local branching is not the obstruction.
3. Independent one-shot zero-break thinning provably leaves a positive linear residual bad-clause density.
4. Repair menus are locally abundant with double-exponentially small no-menu probability, but the former pairwise-resource-disjoint selector surrogate was too restrictive.
5. The preceding run proved the exact A/B/C/D flip normal form relative to a reference assignment. A/B satisfaction is union-closed, and full satisfiability is equivalent to choosing A-seeds and B-orientations, taking deterministic C-closure, and avoiding complete D-triples. Hence overlaps of ordinary A/B repair trees are not intrinsically conflicts.
6. The preceding first-wave make-minus-break calculation showed that choosing a root candidate by `B-A` improves the one-flip unsatisfied-clause drift at `alpha=3.6` from about `-1.22754` for minimum-break to about `-1.48238`.
7. The separate four-spectrum route has exact cascade drift and polarity-refinement lemmas, but no certified terminal prescribed-degree 2-SAT margin above `3.52`; its naive full sparse integration was not usable.

The present run does not retune the obsolete pairwise-disjoint menu surrogate. It develops the exact consequence of A/B union closure that was still missing from the load calculation: **a repair tree frequently repairs other initial A-roots for free, so counting one complete tree per initial bad clause overstates the global variable demand.**

## 2. Exact candidate law with side-root absorption

Work in the local weak limit of the majority-labeled factor graph. Let

\[
P,N\stackrel{\rm iid}{\sim}{\rm Pois}(\mu),\qquad \mu={3\alpha\over2},
\qquad Z=\min(P,N),\quad M=\max(P,N),
\]

and

\[
q={\mathbb E Z\over2\mu}.
\]

A candidate variable reached through a currently false literal has false-Palm law

\[
\Pr_F(Z=z,M=m)={z\Pr(Z=z,M=m)\over\mathbb EZ}.
\tag{2.1}
\]

The occurrence through which the variable is reached belongs to the current unsatisfied clause. For its remaining `Z-1` majority-false occurrences, define `S` to be the number lying in initially unsatisfied type-A clauses. Each such occurrence has two other majority-false literals with probability `q^2`, so

\[
\boxed{S\mid Z\sim\operatorname{Bin}(Z-1,q^2).}
\tag{2.2}
\]

Thus flipping the candidate repairs

\[
A=1+S
\tag{2.3}
\]

currently unsatisfied clauses: the parent obligation plus `S` side A-roots.

For each of the `M` majority-true occurrences, the other two literals have independently false/true statuses with probabilities `q,1-q`. Therefore the numbers `(B,C,D)` of type-B, type-C and type-D clauses incident through a majority-true literal obey

\[
\boxed{
(B,C,D)\mid M
\sim\operatorname{Multinomial}
\left(M;q^2,\,2q(1-q),\,(1-q)^2\right).
}
\tag{2.4}
\]

Conditional on `(Z,M)`, (2.2) and (2.4) are independent in the tree limit. Here `B` is exactly the number of newly broken B-clauses created by flipping the variable. `C,D` do not become violated after one isolated flip, but measure the true-incidence exposure which generates the only non-union-closed obstructions when different repair trees interact.

## 3. New controller: exact drift first, then minimize future exposure at zero primary cost

For a candidate put

\[
d=B-A=B-(1+S).
\tag{3.1}
\]

By the deterministic one-flip identity from the preceding report, `d` is the exact change in the current number of unsatisfied clauses in a collision-free local patch.

The new controller chooses lexicographically by

\[
\boxed{(d,M,B).}
\tag{3.2}
\]

At an A-root there are three candidates; at a broken B-clause there are the two other, initially-false candidates. Ties after all three coordinates are broken uniformly.

The interpretation is deliberate:

- `d` is primary, so the controller is pointwise make-minus-break optimal for immediate unsatisfied-clause drift;
- among candidates with the same optimal `d`, minimize total majority-true degree `M`, which is the entire future B/C/D exposure budget;
- among candidates with the same `d,M`, minimize `B`, reducing repair-tree offspring without changing the primary drift or the total true degree.

The secondary and tertiary objectives are genuinely **zero primary-cost tie refinements**: for every local candidate set, the selected value of `d` is exactly the minimum of the candidates' `d` values, regardless of how the tie is refined.

## 4. Exact fresh-tree cascade theorem

Let `L_k` be the selected candidate law from `k` iid false-Palm candidates under (3.2), with `k=3` at the root and `k=2` at B-descendants. Write

\[
s_k=\mathbb E_{L_k}S,\quad
b_k=\mathbb E_{L_k}B,\quad
c_k=\mathbb E_{L_k}C,\quad
d_k^{(D)}=\mathbb E_{L_k}D,
\]

and similarly `m_k=E_{L_k}M`, `z_k=E_{L_k}Z`.

### Theorem 4.1 — subcritical absorption-aware repair tree

On the collision-free local weak limit, the descendants of a broken B-clause form a Galton--Watson process with offspring law equal to the `B`-marginal of `L_2`. If

\[
\boxed{b_2<1,}
\tag{4.1}
\]

then the repair tree terminates almost surely and has an exponential total-progeny tail. Its expected number of flipped variables is

\[
\boxed{
V=1+{b_3\over1-b_2}.
}
\tag{4.2}
\]

More importantly, the expected number of **initial** A-clauses removed by one root tree is

\[
\boxed{
R=1+s_3+{b_3s_2\over1-b_2}.
}
\tag{4.3}
\]

The expected true-incidence exposures of the same tree are

\[
\boxed{
M_T=m_3+{b_3m_2\over1-b_2},\quad
C_T=c_3+{b_3c_2\over1-b_2},\quad
D_T=d_3^{(D)}+{b_3d_2^{(D)}\over1-b_2}.
}
\tag{4.4}
\]

#### Proof

Every flipped variable creates exactly `B` child obligations, one for each majority-true type-B occurrence that becomes false when the variable flips. In a factor-tree neighborhood, the two available false endpoints of distinct child clauses have independent false-Palm labels, so after applying (3.2) their selected states are iid with law `L_2`. This is exactly a Galton--Watson process. The candidate degree law has exponential moments, hence the selected offspring law does as well; subcriticality (4.1) gives almost-sure extinction and an exponential progeny tail.

The expected number of descendants below one B-obligation is `1/(1-b_2)`, proving (4.2).

For absorption, a descendant B-obligation is **not** itself an initial A-clause. A selected descendant with side count `S` absorbs exactly those `S` initial A-clauses, plus whatever its child subtrees absorb. If `H` is the number of initial A-clauses absorbed below one B-obligation, then

\[
H\stackrel d=S_2+\sum_{i=1}^{B_2}H_i,
\]

so

\[
\mathbb EH={s_2\over1-b_2}.
\]

The root absorbs its own initial A-clause, its `S_3` side A-clauses, and the absorption of its `B_3` descendant subtrees, yielding (4.3). The additive incidence formulas (4.4) are identical branching recursions. QED.

### Corollary 4.2 — telescoping energy identity

Because `A=1+S`, the total expected make-minus-break drift summed over the entire terminating tree is exactly

\[
\boxed{
\mathbb E\sum_{v\in T}(B_v-A_v)=-R.
}
\tag{4.5}
\]

Indeed every genealogical B-clause is created once and repaired once, so all B-obligation contributions telescope. What remains is minus the number of initially unsatisfied A-clauses absorbed by the tree. This is the key correction to the previous one-tree-per-root load estimate.

## 5. Exact absorption PGF and multi-root probability

The tree law gives more than its mean. Let

\[
h(z)=\mathbb E z^H
\]

for the number `H` of side initial-A clauses absorbed below one B-obligation. Then

\[
\boxed{
h(z)=\mathbb E_{L_2}\bigl[z^S h(z)^B\bigr].}
\tag{5.1}
\]

If `p=h(0)`, then `p` is the smallest solution of

\[
\boxed{p=\mathbb E_{L_2}[\mathbf 1_{\{S=0\}}p^B].}
\tag{5.2}
\]

The root tree absorbs exactly one initial A-clause iff its root has no side A-clause and all descendant subtrees absorb zero side A-clauses. Hence

\[
\boxed{
\Pr(R_{\rm tree}=1)=
\mathbb E_{L_3}[\mathbf 1_{\{S=0\}}p^B].
}
\tag{5.3}
\]

Since the map in (5.2) has derivative at most `b_2<1` on `[0,1]`, fixed-point iteration from zero converges geometrically to `p`. This supplies a stable direct calculation of the probability that a single tree absorbs at least two distinct initial bad roots.

## 6. Finite-n transfer: a rigorous safe small-batch theorem

The preceding quantities are not merely fresh-copy heuristics. They compile into a first-order finite-n constructive statement.

### Theorem 6.1 — first-order safe-batch transfer

Fix `alpha` for which `b_2(alpha)<1`, and let `V(alpha),R(alpha)` be (4.2)--(4.3). For every `eta>0` there exists `epsilon_0>0` such that for every fixed `0<epsilon<epsilon_0`, a classical iid proper random 3-SAT formula at density `alpha` has, with probability tending to one, a family of pairwise noninteracting majority-repair patches with

\[
\boxed{
N_{\rm flip}\le (V+\eta)\epsilon n,
\qquad
N_{A,\rm repaired}\ge (R-\eta)\epsilon n.
}
\tag{6.1}
\]

Flipping all variables in these patches simultaneously creates **no newly unsatisfied clause**. Consequently the first-order flip cost per initial A-clause removed is at most

\[
\boxed{{V\over R}.}
\tag{6.2}
\]

#### Proof

Because the Galton--Watson tree is exponentially subcritical, choose fixed `L,H` so that discarding trees of more than `L` selected variables or any explored degree above `H` changes the expectations in (4.2)--(4.4) by at most `eta/10`. For these bounded patches, all controller decisions are determined by a fixed-radius marked factor neighborhood.

Select `epsilon n` A-roots uniformly from the initial majority-unsatisfied A-clauses and expose their bounded repair patches. Standard local weak convergence of the sparse configuration model gives the `L_3/L_2` marked tree law above; fixed-size proper-clause collisions contribute `o(n)`, and de-Poissonization changes the normalized counts by `o(1)`. Thus before cross-patch pruning the total selected variables and absorbed side-A marks obey the laws of large numbers with first-order coefficients `V` and `R` up to the chosen truncation error.

Declare two patches conflicting if their complete incident-clause neighborhoods intersect. Each bounded patch has `O_{L,H}(1)` incidences. Two independently rooted patches therefore conflict with probability `O_{L,H}(1/n)`. Among `epsilon n` sampled roots, the expected number of conflict edges is `O_{L,H}(epsilon^2 n)`, and bounded-neighborhood concentration gives the same order w.h.p. Delete one patch endpoint per conflict edge. The loss in flips and absorbed A-clauses is `O_{L,H}(epsilon^2n)`. Choosing `epsilon_0` sufficiently small absorbs this loss into the remaining `eta epsilon n` margin.

After pruning, complete incident-clause neighborhoods are disjoint. Inside each collision-free patch every genealogical B-clause is repaired and every side A-clause is satisfied. A C-clause would require two of its initially true variables to be flipped before it could fail, and a D-clause would require all three; either event would place two selected variables in one nongenealogical clause, excluded by collision-freeness. Between patches this is excluded by disjoint complete incident neighborhoods. Hence the simultaneous union creates no newly unsatisfied clause. QED.

This is still only a **small-batch** theorem; it does not justify iterating the same coefficients through a finite-density trajectory.

## 7. Second-/third-order compiler for the true obstruction

The dual-Horn reduction from the previous run says that only cross-tree C-promotions and D-triples can obstruct arbitrary A/B unions. The absorption-aware tree law gives their first nonzero density orders explicitly.

Let

\[
L_T=3\alpha(1-q)
\tag{7.1}
\]

be the density of majority-true literal occurrences. If `y n` distinct initial A-clauses have been removed by a dilute random family of fresh repair trees, then to first order the fraction of true stubs lying on flipped variables is

\[
\theta_T(y)= {M_T/R\over L_T}\,y+O(y^2).
\tag{7.2}
\]

The initial type-C and type-D clause densities are

\[
c_C=3\alpha q(1-q)^2,
\qquad
c_D=\alpha(1-q)^3.
\tag{7.3}
\]

Configuration symmetry therefore gives the leading cross-tree hazards

\[
\boxed{
H_C(y)=K_C y^2+O(y^3),
\quad
K_C=c_C\left({M_T/R\over L_T}\right)^2,
}
\tag{7.4}
\]

for C-clauses whose two initially true endpoints have both been flipped, and

\[
\boxed{
H_D(y)=K_D y^3+O(y^4),
\quad
K_D=c_D\left({M_T/R\over L_T}\right)^3,
}
\tag{7.5}
\]

for complete D-triples. The density of two-hit D warning clauses is

\[
3c_D\left({M_T/R\over L_T}\right)^2y^2+O(y^3).
\tag{7.6}
\]

These expansions follow by pairing the selected true stubs into the conditionally uniform clause slots. A C failure needs two selected true slots; a D failure needs all three. Events involving two trees already sharing another bounded patch neighborhood contribute only to the next error order after the conflict pruning used in Theorem 6.1.

Equations (7.4)--(7.6) are precisely the coefficients needed for the next finite-density closure ODE: they quantify, in the correct normalization, the C/D cost of repairing A-demand.

## 8. Executed calculation at alpha = 3.6

The reusable diagnostic is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T15-29-14__absorbing_makebreak.py`

created at commit `96fef4177928d61141e73a19feae589e00ee531c`. Its actual stdout is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T15-29-14__absorbing_makebreak.out`

created at commit `787efe59a757f600d5c9ac2c3f919f1fb8e786f2`.

The script sums the exact finite Poisson formulas through cutoff `K=35`, repeats at `K=30`, and prints a conservative false-Palm omitted-mass bound. It uses ordinary double arithmetic, not directed interval arithmetic; therefore the decimals below are **high-precision mechanism diagnostics, not threshold certificates**. At `alpha=3.6` the `K=30`/`K=35` maximum displayed change is `8.693e-13`, while the crude omitted false-Palm probability bound at `K=35` is `1.74e-17`.

For the new controller (3.2),

\[
q=0.380036729791158,
\qquad
b_2=0.576292627271545<1,
\]

and

\[
\boxed{
V=1.97100997557588,
\qquad
R=2.62271569240726,
\qquad
{V\over R}=0.751514920691531.
}
\tag{8.1}
\]

The absorption PGF gives

\[
\boxed{
\Pr(R_{\rm tree}\ge2)\approx0.689758992713604.
}
\tag{8.2}
\]

Thus almost 69% of fresh local root trees absorb at least one additional initial bad A-clause in the tree-limit diagnostic. The effect is not a rare correction.

The exposure per initial A-clause removed is

\[
\boxed{
{M_T\over R}=4.96103707901088,
\quad
{C_T\over R}=2.52844723614207,
\quad
{D_T\over R}=2.06235910135649.
}
\tag{8.3}
\]

For the old minimum-break controller, recomputed with the **same absorption accounting**,

\[
{V_{\min B}\over R_{\min B}}=0.868235173398149,
\quad
{M_{T,\min B}\over R_{\min B}}=5.82545709099081,
\]

\[
{C_{T,\min B}\over R_{\min B}}=3.02735209804526,
\quad
{D_{T,\min B}\over R_{\min B}}=2.46929699112123.
\]

Hence the new lexicographic make-minus-break cascade improves the fresh safe-batch coefficients at `alpha=3.6` by

\[
\boxed{13.4434\%}
\]

in flips per initial A-clause removed,

\[
\boxed{14.8387\%}
\]

in total true-stub exposure per A removed, and

\[
\boxed{16.4799\%}
\]

in each of the C- and D-incidence exposures per A removed.

The last percentages are demonstrated mechanism gains, not source-threshold gains.

### Hazard coefficients

At `alpha=3.6`,

\[
L_T=6.695603318255494,
\quad
c_C=1.577543155494880,
\quad
c_D=0.857828324570657.
\]

Substitution into (7.4)--(7.5) gives for the old minimum-break controller

\[
K_C^{\min B}\approx1.1941581094,
\qquad
K_D^{\min B}\approx0.5649646274,
\]

while the new absorption-aware make-minus-break controller gives

\[
\boxed{
K_C^{\rm new}\approx0.8660575714,
\qquad
K_D^{\rm new}\approx0.3489383099.
}
\tag{8.4}
\]

Thus the leading quadratic C-conflict coefficient is reduced by about

\[
\boxed{27.48\%},
\]

and the leading cubic D-violation coefficient by about

\[
\boxed{38.24\%}.
\]

This is the most relevant mechanism gain of the run because C/D interactions are exactly the non-union-closed obstruction identified in the preceding theorem.

## 9. Correction to the previous raw-capacity diagnostic

The earlier fresh-copy load `u S_*≈0.318` at `alpha=3.6` assigned one complete minimum-break repair tree to every initial A-root. That was deliberately conservative but should **not** be treated as a genuine capacity barrier: it double-counts side A-roots absorbed by other trees.

With absorption accounted for, even the old minimum-break rule has the fresh-tree full-clear extrapolation

\[
u{V_{\min B}\over R_{\min B}}
\approx0.1715602196,
\]

while the new controller gives

\[
\boxed{
u{V\over R}\approx0.1484967078,}
\qquad
u=\alpha q^3\approx0.1975964864.
\tag{9.1}
\]

Equation (9.1) is **not a proof that all A-roots can be cleared at this cost**: it freezes the initial tree law across a finite-density trajectory and ignores promotion feedback. It is an idealized capacity diagnostic only. Its value is negative information about the obstruction: raw variable supply is even less plausible as the reason the constructive route stalls. The real issue is the finite-density C-promotion / D-avoidance dynamics.

## 10. What is proved, what remains conditional, and next decisive attack

### Proved in this run

- the exact false-Palm side-root / B-C-D multinomial law (2.2)--(2.4);
- the lexicographic controller (3.2), whose secondary exposure minimization has zero pointwise primary drift cost;
- the exact Galton--Watson formulas (4.2)--(4.4) and telescoping absorption identity (4.5);
- the exact absorption PGF (5.1)--(5.3);
- the first-order finite-n safe-batch transfer, Theorem 6.1;
- the quadratic/cubic configuration-model hazard compiler (7.4)--(7.6).

### Demonstrated numerically, not promoted to source threshold progress

At `alpha=3.6`, the new controller is comfortably fresh-tree subcritical (`b_2≈0.5763`), removes about `2.6227` initial A-clauses per root tree while using about `1.9710` flips, reduces flip cost per repaired A-clause by about `13.44%` relative to minimum-break, and reduces the leading C/D interaction coefficients by about `27.5%` and `38.2%` respectively.

### Still missing

A full lower-bound improvement requires a finite-density trajectory theorem. In particular, C-promotions change the false-Palm law and can force variables rather than offer a two-choice repair; D two-hit clauses feed back into which A-seeds and B-orientations are admissible. The coefficients above control the onset but do not by themselves prevent promotion avalanches or complete D-triples after `Theta(n)` A-demand has been removed.

The next decisive attack is therefore no longer another local tree heuristic. It is the **second-order closure ODE at `alpha=3.6`**, using `A`-demand removed as the clock and carrying at minimum:

\[
(\text{remaining A density},\ \text{active true-stub mass},\ \text{C-promotion density},\ \text{D two-hit density}).
\]

The source terms at the origin are now proved: `V/R`, `M_T/R`, `K_C`, and the D two-hit coefficient from (7.6). The next run should derive the forced-C subtree law and determine whether the resulting promotion reproduction remains below one before the A-demand reaches zero. If it crosses one below `alpha=3.6`, that is a concrete obstruction and this majority-closure architecture should be retired; if it stays below one with D slack, it supplies the missing path to a certified lower bound above `3.52`.

## ledger_delta

```yaml
claim_id: NM13-06-T04-ABSORBING-MAKEBREAK-CASCADE-11
status: OPEN_PARTIAL
source_model: classical_iid_proper_signed_random_3sat
source_bracket_before: [3.52, 4.4898]
source_bracket_after: [3.52, 4.4898]
source_endpoint_gain: 0
companion_candidate:
  worker: NM13-13
  upper_endpoint: 4.388865
  status: CANDIDATE_FULL_PENDING_LATER_INDEPENDENT_REVIEW
route: majority_dual_horn_absorption_aware_makebreak
new_theorems:
  - false_Palm_side_A_and_BCD_multinomial_law
  - subcritical_absorption_aware_Galton_Watson_cascade
  - telescoping_initial_A_absorption_identity
  - absorption_probability_PGF
  - first_order_finite_n_safe_batch_transfer
  - quadratic_C_and_cubic_D_hazard_compiler
alpha_3_6_diagnostics:
  q: 0.380036729791158
  offspring_mean_B2_new: 0.576292627271545
  flips_per_tree_new: 1.97100997557588
  initial_A_absorbed_per_tree_new: 2.62271569240726
  flips_per_A_new: 0.751514920691531
  flips_per_A_minbreak: 0.868235173398149
  relative_flip_cost_gain: 0.134433914085502
  true_stubs_per_A_new: 4.96103707901088
  true_stubs_per_A_minbreak: 5.82545709099081
  relative_true_stub_gain: 0.148386641336141
  C_hazard_coefficient_new: 0.8660575714
  C_hazard_coefficient_minbreak: 1.1941581094
  D_hazard_coefficient_new: 0.3489383099
  D_hazard_coefficient_minbreak: 0.5649646274
  probability_tree_absorbs_at_least_two_A: 0.689758992713604
numerics_status: HIGH_PRECISION_DIAGNOSTIC_NOT_DIRECTED_INTERVAL
code_commit: 96fef4177928d61141e73a19feae589e00ee531c
output_commit: 787efe59a757f600d5c9ac2c3f919f1fb8e786f2
failed_or_corrected_routes_preserved:
  - independent_zero_break_thinning_leaves_linear_residual
  - static_blocked_core_subcritical_not_obstruction
  - pairwise_resource_disjoint_menu_surrogate_overrestrictive
  - one_tree_per_A_raw_load_overcounts_side_root_absorption
  - full_four_spectrum_threshold_transfer_not_yet_certified
next_obstruction: finite_density_C_promotion_and_D_avoidance_feedback
next_attack: second_order_closure_ODE_with_forced_C_subtree_law_at_alpha_3_6
threshold_claim: none
```

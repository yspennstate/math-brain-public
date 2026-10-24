# Five-agent open-problem plan

Date: 2026-06-30

## Selection

The best two targets for a five-agent push are:

1. **P1: non-Gaussian bounded-density universality for the extremal
   submatrix/phase-retrieval stability scale.**
2. **P2: the all-apex Poisson/dependency theorem for the exact
   subexponential Gaussian minimum, with fixed-apex Poisson as the first
   intermediate lemma.**

I am not selecting the current Benjamini--Schramm percolation attempt as a
primary target for this five-day push.  The local percolation project has a
compiled draft and many continuation notes, but the latest notes are cycling
through repeated residual transformations and still state that the theorem is
not closed.  A complete proof of the general nonamenable quasi-transitive
conjecture is too high-risk for the requested time box.

I am also not selecting the full deterministic Balan--Wang exponential
conjecture as a primary target.  It is important, but the local notes identify
it as the hardest frontier.  It should remain a background track through
Plucker/MDS-code diagnostics, not the main solvable target.

## Why these two

P1 is the best main target because the local project has already reduced it to
specific random-pair estimates:

- single-submatrix null-normal delocalization is available for the
  bounded-density subgaussian route through the Nguyen--Vu/exchangeability
  reduction;
- the remaining pair problem is the D-stratified estimate
  `E[(1-rho_ST^2)^(-1/2) | D] <= 1 + C/D + eta_m(D)` for `D >= 3`;
- the most concrete current subproblem is the weighted-trace cap-edge bound,
  split into a compact averaged pair local-CLT estimate and a far-tail budget.

P2 is the best secondary target because the first two Poisson factorial moments
are already proved for the fixed-apex proxy and the all-apex first-moment
constant is explicit.  The exact-law scale requires the all-apex count, not
only fixed-apex Poisson.  The next missing step is a dependency ledger that
isolates same-apex, neutral, one-way, swap, and high-overlap pair classes, then
proves the swap cancellation estimate at the all-apex threshold.

Both targets are big enough to matter, but they have precise local reductions,
scripts, and paper-ready notes.  That makes them better suited to five Codex
agents than a broad unsolved percolation theorem.

## Five tracks

Agent 1: P1 integration theorem.

- Own the deterministic reduction from fixed-apex good-family inputs to the
  non-Gaussian upper bound.
- Artifact: a clean theorem statement that assumes the D-stratified pair
  estimate and proves the universal upper bound.
- Starting files:
  - `~\Open problem project\status.md`
  - `~\phase_retrieval_omega\notes\p1_conditional_good_family_second_moment_2026_06_01.md`
  - `~\phase_retrieval_omega\notes\p1_random_subset_reduction_2026_06_01.md`

Agent 2: P1 far-tail bound.

- Own the far-tail half of the weighted-trace estimate:
  `A_L_D(z) <= C log D`.
- Artifact: a proposition turning tilted scalar-density and subgaussian mgf
  bounds into the averaged far-tail estimate, with constants and admissible
  tilt range.
- Starting files:
  - `~\phase_retrieval_omega\notes\p1_weighted_trace_cutoff_bookkeeping_2026_06_01.md`
  - `~\phase_retrieval_omega\notes\p1_tilted_density_tail_budget_2026_06_01.md`
  - `~\phase_retrieval_omega\numerics\p1_weighted_trace_tail_probe.py`

Agent 3: P1 compact averaged local CLT.

- Own the compact-window half:
  `sum_k sup_|y|<=L_D (f_k(0,y)-g_k(y))_+ <= C log D/L_D^3`.
- Artifact: an averaged two-dimensional local-CLT lemma with an explicit
  error ledger in `m`, `D`, and `L_D`.
- Starting files:
  - `~\phase_retrieval_omega\notes\p1_compact_pair_clt_budget_2026_06_01.md`
  - `~\phase_retrieval_omega\notes\p1_pair_local_clt_bounded_density_upgrade_2026_06_01.md`
  - `~\phase_retrieval_omega\notes\p1_quantitative_pair_clt_fourier_budget_2026_06_01.md`

Agent 4: P2 all-apex Poisson approximation.

- Own the all-apex Chen--Stein/factorial moment upgrade, using fixed-apex
  Poisson as an intermediate same-apex lemma.
- Artifact: a dependency-neighborhood or cumulant proof showing that the
  all-apex distance-incidence count converges to Poisson at
  `A_m p(t_m)=lambda`, or a sharp ledger reducing this to one explicit swap
  estimate.
- Starting files:
  - `~\phase_retrieval_omega\notes\fixed_apex_poisson_moments_2026_06_01.md`
  - `~\phase_retrieval_omega\notes\all_apex_dependency_graph_frontier_2026_06_30.md`
  - `~\phase_retrieval_omega\numerics\fixed_apex_poisson_moments.py`
  - `~\phase_retrieval_omega\numerics\all_apex_pair_class_counts.py`
  - `~\phase_retrieval_omega\notes\subexponential_threshold_constants_2026_06_01.md`

Agent 5: verification and guardrails.

- Own reproducibility, counterexample search, and preventing false closure.
- Artifact: a short verification report that runs the P1/P2 scripts at small
  and medium sizes, checks constants, and flags any failed assumptions.
- Starting files:
  - `~\phase_retrieval_omega\numerics`
  - `~\phase_retrieval_omega\paper\main.tex`
  - `~\Open problem project\solved_register.md`

## Verification already run on 2026-06-30

Fixed-apex Poisson moment envelope:

```powershell
python numerics\fixed_apex_poisson_moments.py --min-m 8 --max-m 16
```

The total upper-bound excess dropped from about `2.28` at `m=8` to about
`0.0847` at `m=16`; the exponentially small `D=2` term was already negligible
by `m=16`.  This was the fixed-apex same-apex `D=2` term, not the all-apex
swap `D=2` obstruction identified later in this file.

P1 weighted-trace tail smoke test:

```powershell
python numerics\p1_weighted_trace_tail_probe.py --laws gaussian uniform --m-values 16 --d-values 3 6 --radii 0 1 --tail-cutoffs 2 --far-cutoff 3 --frames 1 --z-directions 2 --row-samples 3000 --bandwidth 0.3
```

The small run gave trace-over-Gaussian ratios close to one for Gaussian and
uniform rows, with far-tail fractions below the Gaussian benchmark in the
tested rows.  This is only a smoke test, but it supports the weighted-trace
reduction as the first concrete P1 subtarget.

## Immediate next actions

1. Write the P1 integration theorem in a new note, explicitly separating
   solved inputs, assumptions, and the remaining weighted-trace pair theorem.
2. Convert the far-tail note into a paper-ready proposition with constants.
3. Start a P2 Chen--Stein note with a precise dependency graph and identify
   whether swap pairs admit a codimension-based `1/(m-c)` cancellation
   estimate.  The new pair counter shows that a raw-overlap `c/m` estimate is
   not enough.
4. Keep the percolation project read-only until it has a non-cycling residual
   invariant or a narrower special-case theorem.

## Continuation update, 2026-06-30

New foreground artifacts created in `~\phase_retrieval_omega`:

- `notes\p1_fixed_apex_pair_integration_theorem_2026_06_30.md`
- `notes\p1_near_zone_tensor_probe_2026_06_30.md`
- `numerics\p1_near_zone_tensor_probe.py`
- `notes\all_apex_pair_class_counts_2026_06_30.md`
- `notes\all_apex_swap_core_lemma_2026_06_30.md`

The P1 tensor probe corrected the first compact-CLT attempt: raw absolute
`T3+T4` tensor bounds are too large for the final `O(log D)` budget, even
though the tensors scale naturally for Haar-like frames.  The compact proof
must therefore use signed Edgeworth/Fourier cancellation after subtracting the
covariance-matched Gaussian term.

The P2 all-apex pair counter now has exact closed forms.  It proves that a
raw-overlap swap estimate of order `(c+1)/m` is too weak because its aggregate
mass tends to `1/8`.  A codimension estimate of order `1/(m-c)` has aggregate
mass `1/(2m)+O(m^-2)` and is the right next analytic target.  The swap-core
lemma reduces that target to a Gaussian quotient problem in dimension
`D=m-c`.

## Continuation update, swap core density, 2026-06-30

New P2 artifacts:

- `notes\all_apex_swap_core_density_formula_2026_06_30.md`
- `notes\all_apex_swap_core_local_regularity_target_2026_06_30.md`
- `numerics\p2_swap_core_density.py`

The Gaussian swap-core origin density is now explicit:

```text
f_{X,Y}(0,0)/phi(0)^2
  = E[sin(theta)^(-2)] / E[sin(theta)^(-1)]^2
  = 1+O(D^-2).
```

This is stronger than the `O(1/D)` codimension envelope required by the
all-apex pair ledger.  The next swap-core task was local regularity: convert
the origin-density formula into a small-square probability estimate uniformly
at the all-apex threshold.  The singular buckets must be separated rather than
grouped together: `D=3` is sparse, while `D=2` needs structural treatment.

## Continuation update, fixed-codimension local regularity, 2026-06-30

New P2 artifact:

- `notes\all_apex_swap_core_small_square_proof_2026_06_30.md`
- `notes\all_apex_swap_core_uniform_d_ge4_2026_06_30.md`
- `notes\all_apex_non_swap_decoupling_2026_06_30.md`
- `notes\all_apex_d2_swap_obstruction_2026_06_30.md`
- `notes\all_apex_d3_swap_log_envelope_2026_06_30.md`
- `notes\all_apex_d2_cluster_structure_2026_06_30.md`
- `notes\all_apex_intercluster_pair_moment_2026_06_30.md`

The swap-core local regularity step is now proved for every fixed
codimension `D>=4`:

```text
P(|X|<=t, |Y|<=t) = p(t)^2(K_D+o_D(1))
```

as `t -> 0`.  The proof uses the conditional representation
`X=r_x Z_1`, `Y=r_y Z_2`, the coordinate density bound
`F_q(s)<=2c_qs`, and dominated convergence against
`E[(r_x r_y)^-1]`, which is finite exactly for `D>=4`.

This moves the all-apex swap obstruction from "derive the joint small-square
law" to the sharper remaining tasks, with one important correction: the raw
all-apex incidence Poisson target appears false unless `D=2` swap clusters are
declustered or otherwise removed.

The dimension-uniform `D>=4` version is now recorded: at the all-apex
threshold,

```text
P_D(|X|<=t_m, |Y|<=t_m)
  = p(t_m)^2 (K_D + o(1)),       4 <= D <= m,
K_D = 1 + O(D^-2).
```

The `D=3` bucket is also now controlled by a logarithmic envelope:

```text
P_D=3(|X|<=t, |Y|<=t) <= C t^2 log(e/t),
```

whose aggregate contribution is `O(lambda^2 m^(7/2)4^-m)`.

The `D=2` obstruction is now structurally identified: incidences are marked
`m`-sets `(B,j)`, and `D=2` swaps are exactly distinct marks inside the same
`B`.  The within-cluster contribution makes

```text
E[(Y_{t_m})_2] >= (2-sqrt(2))lambda(m-1)+o(m),
```

so the raw all-apex incidence count is not Poisson at
`A_m p(t_m)->lambda`.

The cluster-excluded ordered pair moment is salvaged:

```text
E sum_{(B,j)!=(B',k), B!=B'}
  1_{E_(B,j)(t_m)} 1_{E_(B',k)(t_m)}
  -> lambda^2.
```

This proves the only pair-level obstruction is internal to a single square
submatrix `B`.

The pair counter was extended to report `swap_codim_sq_weighted_mass`,
`swap_d2_mass`, and `swap_d3_mass`.  A check at `m=30` gave approximately
`9.72e-4`, `1.63e-17`, and `1.33e-14`, respectively.

The remaining P2 tasks are:

1. prove the cluster-level Poisson theorem for the square-submatrix hard-edge
   process based on `sigma_min(A_B)`;
2. incorporate the exact non-swap decoupling lemma into the final covariance
   ledger so neutral and one-way pairs contribute only product baselines.

## Continuation update, cluster statistic choice, 2026-06-30

New P2 artifacts:

- `notes\all_apex_cluster_statistic_choice_2026_06_30.md`
- `notes\all_apex_square_hard_edge_input_2026_06_30.md`
- `notes\all_apex_square_cluster_pair_counts_2026_06_30.md`
- `notes\all_apex_square_fixed_d_pair_envelope_2026_06_30.md`
- `notes\all_apex_square_typical_pair_reduction_2026_06_30.md`
- `notes\all_apex_square_lc_concentration_probe_2026_06_30.md`
- `notes\all_apex_square_lc_trace_reduction_2026_06_30.md`
- `notes\p1_deterministic_edgeworth_contraction_target_2026_06_30.md`
- `numerics\square_pair_lc_probe.py`
- `numerics\p2_cluster_hard_edge_probe.py`
- `numerics\square_cluster_pair_counts.py`
- updated `numerics\subexponential_thresholds.py`

The cluster-level object should be the square-submatrix hard-edge process

```text
W_s = sum_{|B|=m} 1_{sigma_min(A_B)<=s},
```

not the raw incidence count and not the row-distance cluster indicator at the
raw incidence threshold.

The one-square hard-edge calculation gives

```text
P(sigma_min(G_m)<=s) ~ f_m(0)s,
f_m(0)=sqrt(2) Gamma((m+1)/2)/Gamma(m/2) ~ sqrt(m).
```

This sharp coefficient is an Edelman/Wishart hard-edge input; the current
paper only proves a weaker polynomial upper bound sufficient for the
exponential base.

With `L_m=binom(2m-1,m)`, the refined candidate threshold is

```text
s_m ~ lambda/(L_m f_m(0)) ~ 2 sqrt(pi) lambda 4^-m.
```

The row-distance cluster indicator has an extra singular-vector maximum:

```text
min_j delta_j(G) ~ sigma_min(G)/max_j |u_j|,
P(min_j delta_j<=t) ~ f_m(0)t E max_j |u_j|.
```

Thus its threshold is polynomially different from the `sigma_min` threshold
and is diagnostic rather than final.

Verification:

```powershell
python -m py_compile numerics\p2_cluster_hard_edge_probe.py numerics\p1_signed_edgeworth_probe.py numerics\all_apex_pair_class_counts.py
python numerics\p2_cluster_hard_edge_probe.py --m-values 4 6 --matrices 500 --direction-samples 1000 --levels 0.02 0.05 --seed 20260630
```

The threshold bookkeeping script now also prints the square hard-edge scale
and checks the constant `2 sqrt(pi)`.

The square-cluster pair counter records the overlap ledger for the final
process.  For fixed first square `B`,

```text
N_D = binom(m,D) binom(m-1,D),
D = m-|B cap B'|.
```

Fixed `D` classes are exponentially sparse, while typical pairs have
`D~m/2`.  This is the combinatorial input for the next square hard-edge
pair theorem.

Verification:

```powershell
python -m py_compile numerics\square_cluster_pair_counts.py numerics\subexponential_thresholds.py numerics\p2_cluster_hard_edge_probe.py
python numerics\square_cluster_pair_counts.py --min-m 30 --max-m 30 --summary
```

At `m=30`, the fixed high-overlap masses `D=1,2,3,4` are approximately
`1.47e-14`, `2.99e-12`, `2.51e-10`, and `1.10e-8`.

The fixed-`D` square-pair analysis shows the crude one-matrix tail is too weak:
it gives only a polynomially divergent bound for those classes.  A sufficient
replacement is

```text
D=1:      P(pair event) <= poly(m) s_m^2 log(e/s_m),
D>=2:     P(pair event) <= poly(m) s_m^2.
```

The proposed route conditions on the common `(m-D) x m` block `C`, proves
`q_C(s) <= poly(m) min(1,s/rho)`, and integrates against the rectangular
hard-edge tail of `rho=sigma_min^+(C)`.

For typical square pairs, the conditional hard-edge reduction predicts

```text
q_C(s) = a_D L(C)s + o_C(s),
L(C)=E_Z sqrt(1+Z^T(CC^T)^(-1)Z),
```

so the pair ratio is governed by `E L(C)^2/(E L(C))^2`.  Since typical
`D~m/2`, this should be a smooth inverse-Wishart statistic with fluctuation
small enough for the overlap ledger.

P1 also now has a theorem-level next target: prove the deterministic summed
Edgeworth contraction lemma in
`notes\p1_deterministic_edgeworth_contraction_target_2026_06_30.md`, replacing
the crude compact near-zone Berry budget with `P_3+P_4 <= B log D`.

The typical square-pair coefficient has a trace approximation:

```text
L_typ(D,m)=sqrt((m-1)/(D-1)).
```

The new `square_pair_lc_probe.py` samples the common block and estimates the
concentration of `L(C)` around this value.
The trace reduction note proves the deterministic bound

```text
0 <= sqrt(1+tr((CC^T)^-1)) - L(C) <= tr((CC^T)^-2)/4.
```

So the typical-pair variance problem reduces to concentration of the
inverse-Wishart trace on the mass-carrying overlap range.

Smoke verification:

```powershell
python numerics\square_pair_lc_probe.py --m-values 24 48 --d-values 1/3 1/2 2/3 --common-samples 40 --z-samples 128 --seed 20260630
```

At `m=48`, the mean ratio `L(C)/L_typ` was `0.994`, `0.998`, and `0.998` for
`D/m=1/3,1/2,2/3`; the coefficient of variation dropped from about `0.035` to
`0.016` across those cases.  The mean absolute gap between `L(C)` and
`sqrt(1+tr((CC^T)^-1))` was `2.52e-2`, `1.02e-2`, and `7.14e-3`.

## Continuation update, P1 signed Edgeworth probe, 2026-06-30

New P1 artifacts:

- `numerics\p1_signed_edgeworth_probe.py`
- `notes\p1_signed_edgeworth_probe_2026_06_30.md`

The compact near-zone diagnostic now measures signed Edgeworth/Fourier
cancellation rather than raw absolute `T3+T4` mass.  It reports coefficient
cancellation ratios for `M_{r,j,k}` and signed integrated `I3`, `I4`, `I33`
terms after summing over residual columns.

The smoke run

```powershell
python numerics\p1_signed_edgeworth_probe.py --laws gaussian uniform beta25 --m-values 24 --d-values 6 --radii 0 1 --frames 1 --z-directions 2 --grid-points 41 --fourier-cutoff 5
```

passed.  Gaussian gives zero Edgeworth corrections; `beta25` exercises the
skew-cumulant path; the after-sum positive part is far smaller than the
absolute comparator in the tiny run.  The next P1 task is to run this probe at
larger `m,D` and turn the observed signed cancellation into a deterministic
Fourier lemma.

## Continuation update, P2 inverse-Wishart and P1 profiles, 2026-06-30

Five fresh Codex agents audited disjoint proof gaps.  No background processes,
daemons, or scheduled tasks were created.

New P2 artifacts:

- `notes\all_apex_square_inverse_wishart_trace_target_2026_06_30.md`
- `notes\all_apex_square_conditional_hard_edge_uniformity_2026_06_30.md`

The typical square-pair random-environment step is now a theorem-level
inverse-Wishart target.  For `S=CC^T`, `C` an `(m-D) x m` Gaussian block,
`T=tr(S^-1)`, and `U=tr(S^-2)`,

```text
E T = (m-D)/(D-1),
Var(T) = 2(m-D)(m-1) / (D(D-1)^2(D-3)),
E U = (m-D)(m-1) / (D(D-1)(D-3)).
```

The remaining negative-moment input is

```text
E U^2 <= C_theta m^-2
```

on `theta m <= D <= (1-theta)m`.  Together with

```text
0 <= sqrt(1+T)-L(C) <= U/4,
```

this gives

```text
E[(L(C)/L_typ(D,m)-1)^2] <= C_theta D^-2.
```

The conditional hard-edge note now avoids the false target of a deterministic
`sup_C` expansion.  The right square-pair input is the averaged threshold
linearization

```text
E_C[(q_C(s_m)-a_D L(C)s_m)^2] = o(a_m^2 s_m^2),
s_m(lambda) ~ 2 sqrt(pi) lambda 4^-m.
```

The fixed-small-`D` note was corrected as well.  The safe conditional envelope
is

```text
q_C(s) <= C_D min(1, s(1 + sqrt(D)||C^+||_F)),
```

with only `D=1` needing the logarithmic rectangular hard-edge truncation.

P1 also advanced:

- `notes\p1_signed_multiplier_contraction_route_2026_06_30.md`
- `numerics\p1_signed_edgeworth_probe.py` now reports `P3/P4` profile columns.

The deterministic signed Edgeworth route is now:

```text
Re_+ I_Edgeworth(q,W)
  <= C_{r,law,psi}(1+P_3(q,W)+P_4(q,W)),
```

after proving a signed Fourier multiplier bound without replacing
`widehat{y^2 psi_L}` by its absolute value.  The linear cubic term is removed
by exact parity before any absolute values are taken.

Verification:

```powershell
python -m py_compile numerics\square_pair_lc_probe.py numerics\p1_signed_edgeworth_probe.py
python numerics\square_pair_lc_probe.py --m-values 24 48 --d-values 1/3 1/2 2/3 --common-samples 30 --z-samples 96 --seed 20260630
python numerics\p1_signed_edgeworth_probe.py --laws gaussian uniform beta25 --m-values 24 --d-values 6 --radii 0 1 --frames 1 --z-directions 2 --grid-points 41 --fourier-cutoff 5
```

The square probe now reports `tr(S^-2)`, `m*std(tr(S^-1))`, and
`D^2 Var(L)/E(L)^2` diagnostics.  The P1 smoke output includes
`mean_P3_over_logD`, `mean_P4_over_logD`,
`max_P3plusP4_over_logD`, and
`mean_edgeworth_profile_pos_over_P3plusP4`.

## Continuation update, conditional hard edge and chart profiles, 2026-06-30

Five Codex agents audited the remaining P2 conditional-hard-edge theorem and
the P1 good-frame hypothesis.  No background processes, daemons, or scheduled
tasks were created.

New P2 artifacts:

- `notes\all_apex_square_block_inverse_linearization_2026_06_30.md`
- `notes\all_apex_square_gaussian_hard_edge_package_2026_06_30.md`
- `notes\all_apex_square_conditional_hard_edge_probe_2026_06_30.md`
- `numerics\square_conditional_hard_edge_probe.py`

The block-inverse lemma now gives a deterministic sandwich.  For

```text
A=[0 R; G H],
tau=sigma_min(G),
ell=sqrt(1+||R^{-T}H^T u||^2),
```

and a regularity parameter `Delta`, if `s Delta<1`,

```text
{tau <= s ell/(1+s Delta)}
  subset {sigma_min(A)<=s}
  subset {tau <= s ell/(1-s Delta)}.
```

This turns the conditional expansion into a private-block hard-edge problem
plus exclusions for `sigma_2(G)` and bad common cores.

The required Gaussian hard-edge package is now explicit:

```text
P(tau<=x)=a_D x + O(D^C a_D x^3),
P(tau<=x, sigma_2(G)<=r) <= C D^C x r^3.
```

For independent polynomial-moment weights `W`, this yields

```text
P(tau<=tW)=a_D t E W + negligible error
```

at the exponentially small square threshold.

The new conditional probe estimates `q_C(s)/(a_D L(C)s)` at moderate
normalized levels instead of trying to sample `4^-m` events.  The smoke and
small diagnostic run passed:

```powershell
python -m py_compile numerics\square_conditional_hard_edge_probe.py
python numerics\square_conditional_hard_edge_probe.py --m-values 8 12 --d-values 1/2 --cores 5 --private-samples 2000 --z-samples 256 --levels 0.01 0.03 0.07 --seed 20260630
```

For `m=8,D=4`, `q_hat/level` was `1.00`, `1.03`, `0.999` at levels
`0.01`, `0.03`, `0.07`.  For `m=12,D=6`, it was `0.95`, `1.023`, `1.03`.
The low-tail median of exact `sigma_min([0 R;G H])` divided by the block
prediction was `0.9999+` in both cases.

New P1 artifacts:

- `notes\p1_good_frame_chart_profile_2026_06_30.md`
- `numerics\p1_frame_profile_chart_probe.py`

The good-frame hypothesis was sharpened: `P_3+P_4<=B log D` should be stated
for a Haar/delocalized residual chart, not an arbitrary deterministic
Gram-Schmidt completion.  The profile is basis-dependent in the `W` columns.
The new chart probe compares:

```text
deterministic_completion,
haar_rotated_completion,
direct_haar_frame.
```

Smoke verification:

```powershell
python -m py_compile numerics\p1_frame_profile_chart_probe.py
python numerics\p1_frame_profile_chart_probe.py --laws gaussian beta25 --m-values 24 --d-values 6 12 --radii 0 1 --frames 4 --z-directions 2 --seed 20260630
```

In the smoke output, `(P3+P4)/logD` stayed around `0.8-2.1` across the tested
chart modes and parameters, with deterministic completions consistently
larger than Haar-rotated/direct Haar charts.  This supports the revised
good-chart theorem target.

## Continuation update, square Poisson assembly and P1 cap correction, 2026-06-30

Five Codex agents audited the P2 theorem assembly, the conditional expansion
error budget, the double-hard-edge exponents, and the P1 good-chart target.
No background processes, daemons, or scheduled tasks were created.

New P2 artifacts:

- `notes\all_apex_square_poisson_assembly_2026_06_30.md`
- `notes\all_apex_square_conditional_error_budget_2026_06_30.md`
- `numerics\square_poisson_error_budget.py`
- `numerics\square_pair_error_budget.py`

The square Poisson proof is now organized around the exact pair criterion

```text
sum_D pi_m(D) R_{m,D} -> 1,
R_{m,D}=P_D(s_m)/p_m(s_m)^2,
pi_m(D)=binom(m,D)binom(m-1,D)/binom(2m-1,m).
```

The covered pieces are:

```text
fixed D:     K_m N_D P_D(s_m) -> 0
typical D:   R_{m,D}=1+O(D^-2)+o(1)
```

with the exact ledger

```text
sum_D pi_m(D)D^-2 = 4/m^2 + O(m^-3).
```

The remaining P2 gap is now sharply isolated: the mesoscopic tail

```text
D -> infinity but D < theta m
```

and the symmetric far edge need a product-scale subexponential two-event
bound, e.g.

```text
P_D(s_m) <= exp(o(m)) p_m(s_m)^2.
```

The one-matrix bound is not enough there.  The overlap mass of the tail is
exponentially small,

```text
<= exp(-c_theta m + O(log m)),
```

so any subexponential product-scale pair ratio closes it.

The conditional expansion now has explicit cutoffs:

```text
rho_C >= m^-10,
||H R^-1|| <= m^20,
gamma=m^-B,
s Delta <= m^-2.
```

On these events the block sandwich plus the hard-edge package gives

```text
E_C[(q_C(s_m)-a_D L(C)s_m)^2] = o(a_m^2 s_m^2)
```

in the typical range, modulo the already named uniform hard-edge package and
a crude inverse implication on the `sigma_2(G)`-bad slice.

The Gaussian double-hard-edge exponents were checked from the singular-value
density:

```text
P(sigma_2(G)<=r) <= C D^C r^4,
P(sigma_min(G)<=x, sigma_2(G)<=r) <= C D^C x r^3.
```

New P1 correction:

- `notes\p1_good_frame_chart_profile_2026_06_30.md` was corrected.

The previous full-cap Haar statement was too strong.  In linear aspect,
choosing `z` parallel to a high-leverage row gives

```text
sup_{||z||<=r} d ||q_z||_4^4 >= c_r d^3/m^2,
```

so the right target is polynomial-grid or integrated good-chart control, not
a fixed-radius supremum over all `z`.

Verification:

```powershell
python -m py_compile numerics\square_pair_error_budget.py numerics\square_poisson_error_budget.py numerics\square_conditional_hard_edge_probe.py numerics\p1_frame_profile_chart_probe.py
python numerics\square_poisson_error_budget.py --min-m 20 --max-m 80 --step 20 --theta 0.2 --fixed-cutoff 4
python numerics\square_pair_error_budget.py --m-values 24 48 --theta 0.1 --fixed-d-max 4
```

At `theta=0.2`, the exact tail mass outside the central window dropped from
`1.94e-5` at `m=20` to `1.01e-15` at `m=80`.  The pair-ratio budget script
reported ideal weighted absolute errors `2.64e-2` at `m=24` and `1.17e-2` at
`m=48`; the pure `D^-2` model was `7.78e-3` and `1.83e-3`, respectively.

## Continuation update, mesoscopic product bound and integrated P1 cap, 2026-06-30

Five Codex agents audited the P2 mesoscopic strip, entropy splitting,
nonasymptotic hard-edge upper tails, higher factorial moments, and the P1
integrated good-chart route.  No background processes, daemons, or scheduled
tasks were created.

New P2 artifacts:

- `notes\all_apex_square_mesoscopic_product_bound_2026_06_30.md`
- `notes\all_apex_square_mesoscopic_split_strategy_2026_06_30.md`
- `notes\all_apex_square_higher_factorial_moments_2026_06_30.md`
- `numerics\square_mesoscopic_split_budget.py`

The mesoscopic pair strip now has a direct product-scale route.  For one
completion in block form

```text
A=[R 0; H G],
RR^T=CC^T,
```

the inverse formula gives the implication

```text
{sigma_min(A)<=s}
  subset {rho_C<=2s}
    union {sigma_min(G)<=c s(1+||H R^-1||)}.
```

Using the exact nonasymptotic Gaussian hard-edge upper tail

```text
P(sigma_min(G_D)<=t) <= a_D t <= sqrt(D)t
```

and `E||C^+||_F^2=(m-D)/(D-1)`, this yields for `D>=2`

```text
P_D(s_m) <= C D m s_m^2 + negligible,
R_m(D)=P_D(s_m)/p_m(s_m)^2 <= C D+o(1).
```

That polynomial pair-ratio bound is enough to kill the exponentially small
edge overlap mass, so the previous mesoscopic strip is no longer a structural
obstruction once the two standard inputs are written cleanly:

```text
P(sigma_min(G_D)<=t) <= a_D t,
P(sigma_min^+(C)<=r) <= (C sqrt(m)r)^(D+1).
```

The split strategy remains as a fallback.  It recommends a moving boundary
`D_m=ceil(m^(2/3))`; the count side gives edge mass
`4^-m exp(o(m))`.  A large model loss such as `exp(4D log m)` is asymptotic
only and looks poor at small `m`, but the direct `R_m(D)<=C D` route is much
sharper.

For full Poisson convergence, the new higher-factorial note records that the
second moment closes only the pair obstruction.  The next theorem layer is
fixed factorial moments:

```text
E[(W_m)_k] -> lambda^k
```

for each fixed `k`, via hereditary product bounds for tuples containing a bad
pair and central fixed-`k` joint hard-edge expansions with pair-additive
error.

New P1 artifact:

- `notes\p1_integrated_good_chart_target_2026_06_30.md`

The natural integrated cap measure is the least-squares law from
`p1_least_squares_z_density_formula_2026_06_01.md`; the Gaussian benchmark is
the truncated Cauchy density

```text
dnu^G_{D,r}(z) proportional to
1_{||z||<=r}(1+||z||^2)^(-D/2) dz.
```

`numerics\p1_frame_profile_chart_probe.py` now supports

```text
--z-measures sphere gaussian_cauchy
```

and samples the truncated Gaussian-Cauchy cap law.  The smoke run

```powershell
python numerics\p1_frame_profile_chart_probe.py --laws gaussian beta25 --m-values 24 --d-values 6 12 --radii 1 --z-measures sphere gaussian_cauchy --frames 4 --z-directions 8 --seed 20260630
```

kept `(P3+P4)/logD` in the same controlled range as the sphere diagnostic,
often lower for Haar-rotated charts.

Verification:

```powershell
python -m py_compile numerics\p1_frame_profile_chart_probe.py numerics\square_mesoscopic_split_budget.py numerics\square_pair_error_budget.py numerics\square_poisson_error_budget.py
python numerics\square_mesoscopic_split_budget.py --min-m 40 --max-m 200 --step 40 --d0-mode power --power 0.6666666667 --crude-exponent 4
```

## Continuation update, conditional second moment and least-squares cap sampler, 2026-06-30

Five Codex agents audited the P2 rectangular tail input, the block inverse
implication, fixed-`k` factorial moment packaging, and the P1 least-squares
cap diagnostic.  No background processes, daemons, or scheduled tasks were
created.

Updated P2 artifacts:

- `notes\all_apex_square_poisson_assembly_2026_06_30.md`
- `notes\all_apex_square_standard_gaussian_tail_inputs_2026_06_30.md`
- `notes\all_apex_square_mesoscopic_product_bound_2026_06_30.md`
- `notes\all_apex_square_higher_factorial_moments_2026_06_30.md`

The square second-factorial-moment proof is now packaged as a conditional
theorem.  The earlier mesoscopic pair strip is no longer listed as a
structural gap: the direct block-inverse product bound gives, for `D>=2`,

```text
P_D(s_m) <= C D m s_m^2 + negligible,
R_m(D)=P_D(s_m)/p_m(s_m)^2 <= C D+o(1).
```

The exact edge-overlap mass is exponentially small, so this polynomial
pair-ratio bound kills both edge strips.  The proof is conditional on the
standard Gaussian inputs now stated in
`all_apex_square_standard_gaussian_tail_inputs_2026_06_30.md`:

```text
P(sigma_min(G_D)<=t) <= a_D t <= sqrt(D)t,
P(sigma_min^+(C)<=r) <= (C sqrt(m)r)^(D+1).
```

The rectangular input now has a local Laguerre/Selberg derivation sketch:
freeze `lambda_min=x` for `Wishart_{m-D}(m,I)`, use the normalization ratio
`n Z_{n-1,alpha+1}/Z_{n,alpha}`, and integrate the `x^alpha` density bound.

The resulting theorem statement is:

```text
If K_m a_m s_m -> lambda, then
E W_m(s_m) -> lambda,
E W_m(s_m)(W_m(s_m)-1) -> lambda^2,
```

assuming the one-square hard edge, the private square weighted hard-edge and
double-hard-edge package, the rectangular common-core lower tail, the
inverse-Wishart moment envelope for `L(C)`, the fixed-`D` logarithmic
envelope for `D=1`, and the central pair asymptotic with averaged
`O(D^-2)+o(1)` error.

Full Poisson convergence remains a separate fixed-`k` task.  The updated
higher-factorial note routes it through a Venn-cell entropy ledger,
hereditary product bounds for tuples containing a bad pair, and central
fixed-`k` joint hard-edge expansions with pair-additive error.

Updated P1 artifacts:

- `notes\p1_integrated_good_chart_target_2026_06_30.md`
- `numerics\p1_frame_profile_chart_probe.py`

The chart probe now supports the actual least-squares cap sampler:

```text
--z-measures sphere gaussian_cauchy least_squares
```

In `least_squares` mode it draws fresh private residual rows, solves
`z=-B^{-1}a`, keeps `||z||<=r`, and reports acceptance/conditioning
statistics.  The summary path was hardened so empty least-squares batches
emit `nan` summaries instead of failing on an empty quantile.

Verification:

```powershell
python -m py_compile numerics\p1_frame_profile_chart_probe.py numerics\square_mesoscopic_split_budget.py numerics\square_pair_error_budget.py numerics\square_poisson_error_budget.py
python numerics\p1_frame_profile_chart_probe.py --laws gaussian beta25 --m-values 24 --d-values 6 --radii 1 --z-measures sphere gaussian_cauchy least_squares --frames 2 --z-directions 4 --seed 20260630
```

The least-squares smoke completed every tested frame, accepted `8` cap points
per chart mode with proposal counts `79` to `144`, had no solve failures, and
kept least-squares `(P3+P4)/logD` below `1.23` in the tested cases.

## Continuation update, standard-input proofs and fixed-`k` frontier, 2026-06-30

Five Codex agents audited the next P2 and P1 frontier: rectangular Selberg
constants, inverse-Wishart negative moments, fixed-`k` Venn entropy,
fixed-`k` cluster-product bounds, and the P1 integrated cap theorem.  No
background processes, daemons, or scheduled tasks were created.

New P2 artifacts:

- `notes\all_apex_square_conditional_second_moment_theorem_2026_06_30.md`
- `notes\all_apex_square_fixed_k_venn_entropy_2026_06_30.md`
- `notes\all_apex_square_fixed_k_cluster_intensity_target_2026_06_30.md`

Updated P2 artifacts:

- `notes\all_apex_square_standard_gaussian_tail_inputs_2026_06_30.md`
- `notes\all_apex_square_inverse_wishart_trace_target_2026_06_30.md`
- `notes\all_apex_square_higher_factorial_moments_2026_06_30.md`
- `notes\all_apex_square_poisson_assembly_2026_06_30.md`

The conditional second-factorial-moment theorem is now a standalone proof
artifact.  It states that if

```text
K_m a_m s_m -> lambda,
```

and the one-square hard edge, central pair expansion, fixed-`D` envelope, and
mesoscopic product bound hold, then

```text
E W_m(s_m) -> lambda,
E W_m(s_m)(W_m(s_m)-1) -> lambda^2.
```

The rectangular common-core tail now includes the exact Selberg ratio.  For
`C` an `n x m` Gaussian matrix, `n=m-D`, `alpha=(D-1)/2`, and
`A=(D+1)/2`,

```text
n Z_{n-1,alpha+1}/Z_{n,alpha}
 = n 2^-A Gamma(3/2) Gamma(A+n/2)
   / [Gamma(1+n/2) Gamma(A) Gamma(A+1/2)].
```

This gives

```text
P(sigma_min^+(C)<=r) <= min(1,(C sqrt(m)r)^(D+1)).
```

The inverse-Wishart trace target now has the missing negative-moment proof.
For `S=CC^T` in the proportional range `theta m <= D <= (1-theta)m`,
the split integral

```text
E lambda_min(S)^-4
 <= a^-4 + 4 int_0^a x^-5 P(lambda_min(S)<=x) dx
```

uses the hard-edge CDF near zero and a Gaussian lower-edge tail up to the
Marchenko-Pastur edge, giving

```text
E lambda_min(S)^-4 <= C_theta m^-4,
E tr(S^-2)^2 <= C_theta m^-2.
```

For full Poisson convergence, the old pointwise hereditary-product target was
replaced by the weaker and more plausible counted cluster-intensity theorem.
The fixed-`k` Venn entropy lemma is now essentially combinatorial: after
fixing any central pair, Venn-irregular completions are at most

```text
exp(-c_k m) K_m^(k-2).
```

The remaining analytic fixed-`k` target is:

```text
E[1_{E_1 cap E_2} (Z_C)_r]
 <= exp(o(m)) P(E_1 cap E_2) (|C|p_m)^r.
```

New P1 artifact:

- `notes\p1_integrated_cap_gaussian_benchmark_2026_06_30.md`

The Gaussian integrated cap theorem now has exact radial identities and a
deterministic profile domination:

```text
P_3(q,W)+P_4(q,W)
 <= (2d+1)||q||_4^4
    + 2 sum_k ||w_k||_4^4
    + 2 sum_i q_i^2 ||W_{i,*}||_2^2.
```

For Haar `U=[p|W]` and Gaussian-Cauchy cap law,

```text
E_U E_z [P_3(q_z,W)+P_4(q_z,W)] <= C_r(1+d/m),
```

and the high-probability target is the Haar integrated good-chart lemma

```text
int (P_3+P_4) dnu^G_{D,r} <= C_{r,A} log(eD).
```

The non-Gaussian transfer is now isolated as a determinant-tilted cap
density-ratio lemma with

```text
R_U(z)=h_U(z)/h_G(z),
int F_U dnu_{U,r}
 = E_{nu^G}[F_U R_U] / E_{nu^G}[R_U].
```

Verification:

```powershell
rg -n "hereditary-product|main.*gap|not closed|mesoscopic strip is now the main|still needs the fixed-`k` Venn-cell and hereditary" notes -g "*.md"
rg -n "Conditional theorem|Input ledger|Negative-moment proof|exact ratio|counted pair-conditioned|Density-ratio transfer|Haar Integrated" notes\all_apex_square_conditional_second_moment_theorem_2026_06_30.md notes\all_apex_square_inverse_wishart_trace_target_2026_06_30.md notes\all_apex_square_standard_gaussian_tail_inputs_2026_06_30.md notes\all_apex_square_fixed_k_cluster_intensity_target_2026_06_30.md notes\p1_integrated_cap_gaussian_benchmark_2026_06_30.md
```

The stale-wording scan found no remaining new-P2 references to the old
mesoscopic-main-gap or hereditary-product framing.

## Continuation update, fixed-`k` cluster split and P1 density-ratio probe, 2026-06-30

Five Codex agents attacked the next frontier: fresh-row cluster intensity,
zero-fresh clusters, clean fixed-`k` central expansion, the P1 cap
density-ratio transfer, and a diagnostic for that transfer.  No background
processes, daemons, or scheduled tasks were created.

New P2 artifacts:

- `notes\all_apex_square_clean_fixed_k_expansion_target_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_cluster_target_2026_06_30.md`

Updated P2 artifact:

- `notes\all_apex_square_fixed_k_cluster_intensity_target_2026_06_30.md`

The clean fixed-`k` target now conditions on all rows shared by at least two
of the `k` squares.  The singleton Venn atoms provide independent private
blocks `X_i`, so

```text
P(E_1 cap ... cap E_k | shared environment)
  = prod_i q_i(F).
```

The proof obligation is now explicit:

```text
q_i(F)=a_{r_i}s_m L_i(F)+eps_i(F),
E_F |eps_i(F)/p_m|^(2k)=o_k(1),
```

plus joint decorrelation of the normalized environment coefficients
`Y_i=L_i/E L_i`, with pair-additive error

```text
E prod_i Y_i
 = 1 + sum_{i<j} Gamma_ij + O_k(m^-3),
|Gamma_ij| <= C_k D_ij^-2.
```

The fresh-row cluster lemma is also explicit.  For a completion `B` after a
marked pair, let

```text
f_B = |B \ (B_1 union B_2)|.
```

If `f_B>=1`, then conditioning on the marked pair gives

```text
q_B(s) <= 1_{rho_B<=2s}
  + C p_m(s) [1 + (f_B/sqrt(m)) ||C_B^+||_F].
```

For `f_B>=2`, this reduces the fresh-row sector to a
pair-conditioned, multiplicity-weighted subset-pseudoinverse average.

The zero-fresh sector is not killed by counting alone.  With
`D=m-|B_1 cap B_2|`, the zero-fresh count per marked pair is

```text
M_0(D)=binom(m+D,m).
```

Pair-level counting fails in the central and near-complementary bulk.  The
new target is a pair-Palm planted-vector/Kac-Rice cluster estimate:

```text
E[1_{E_1 cap E_2} (Z_0)_r]
 <= exp(o(m)) P(E_1 cap E_2) (|Z_0|p_m)^r.
```

New P1 artifacts:

- `notes\p1_density_ratio_transfer_target_2026_06_30.md`
- `numerics\p1_cap_density_ratio_probe.py`

The P1 density-ratio transfer now decomposes

```text
R_U(z)=h_U(z)/h_G(z)
```

into three factors:

```text
[J_U(z)/J_G(z)]^d,
det(M_U(z) Sigma_G(z)^-1)^(1/2),
V_U(z).
```

The genuinely hard new sublemma is the whitened determinant-volume
universality bound

```text
V_U(z)=O_r(1)
```

in a cap-averaged `L^p` sense.

The new diagnostic estimates the cap normalizer ratio, radial tilt, and
profile tilt between the least-squares cap law and the Gaussian-Cauchy
benchmark.  Smoke command:

```powershell
python numerics\p1_cap_density_ratio_probe.py --laws gaussian uniform beta25 --m-values 16 --d-values 4 --radii 1 --frames 2 --z-per-frame 16 --radial-bins 4 --seed 20260630
```

Smoke result: Gaussian calibration had `cap_mass_ratio=1.1218` and
`mean_F_ratio=1.0060` with `32` accepted samples; uniform had
`cap_mass_ratio=0.9731`, `mean_F_ratio=1.0183`; beta25 had
`cap_mass_ratio=0.9839`, `mean_F_ratio=1.0292`.

Verification:

```powershell
python -m py_compile numerics\p1_cap_density_ratio_probe.py numerics\p1_frame_profile_chart_probe.py
rg -n "Fresh-row one-step lemma|Small-fresh sector|Required zero-fresh cluster estimate|Planted-vector route|product-remainder|Density-ratio transfer lemma|whitened determinant-volume|cap_mass_ratio" notes numerics -g "*.md" -g "*.py"
```

## Continuation update, small-fresh saddle and Palm refinements, 2026-06-30

Five Codex agents refined the P2 small-fresh cluster obstruction and the P1
determinant-volume transfer.  No background processes, daemons, or scheduled
tasks were created.

New P2 artifacts:

- `notes\all_apex_square_small_fresh_taxonomy_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_sphere_integral_2026_06_30.md`
- `numerics\square_small_fresh_count_budget.py`

Updated P2 artifact:

- `notes\all_apex_square_fixed_k_cluster_intensity_target_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_cluster_target_2026_06_30.md`

The small-fresh count is now explicit.  After a marked pair with
`D=m-|B_1 cap B_2|`, the number of third squares using exactly `f` rows
outside `B_1 union B_2` is

```text
M_f(D)=binom(m-1-D,f) binom(m+D,m-f).
```

Thus

```text
M_0(D)=binom(m+D,m),
M_1(D)=(m-1-D)binom(m+D,m-1),
```

and `f=1` has the same exponential count rate as zero-fresh up to polynomial
factors.

The `f=1` sector now has a re-marking split.  Close neighborhoods are
fixed-`D`/swap cases.  If `c<=D-2` or `b<=D-2`, re-marking creates an
`f>=2` fresh-row case.  The irreducible residual is

```text
b,c >= D-1,
```

and still needs a planted-vector/Palm cluster estimate.

The zero-fresh planted-vector sphere integral was reduced exactly.  With
`rho=<u,v>=cos(phi)`,

```text
I = (m-2)/(4pi) int
    (1-s)^((b+c-4)/2)
    (1-s cos^2 theta)^(-b/2)
    (1-s cos^2(theta-phi))^(-c/2)
    dtheta ds.
```

For `b=beta m`, `c=gamma m`, the exponential rate is

```text
Phi = (beta/2) log((1-s)/(1-s cos^2 theta))
    + (gamma/2) log((1-s)/(1-s cos^2(theta-phi))) <= 0.
```

So the bulk integral has no positive exponential saddle.  The remaining
input is pair-Palm anti-coalescence of planted directions, for example

```text
E_Palm[(1-rho^2)^(-1/2)] <= exp(o(m)).
```

The fresh-row pseudoinverse average was also sharpened.  Under the two-witness
Palm model, the relevant effective excess is

```text
delta_B=1_{b=0}+1_{c=0},
e_B=f_B-delta_B.
```

The target is now a Pair-Palm Subset Pseudoinverse Lemma with
subexponential determinant-weight `L^p` control and inverse-Wishart bounds in
terms of `e_B`.  The critical close sector `f_B=2,b=c=0` must be routed to
close/fixed-`D` machinery or handled by determinant-weight repulsion.

Updated P1 artifact:

- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The P1 determinant-volume transfer is now stated only for an admissible
smooth subgaussian product-law package, or as a conditional log-det
universality input.  Bounded density alone is not enough in linear aspect.
The next hard sublemma is:

```text
Sliced Determinant Universality:
int V_U(z)^p dnu^G_{D,r}(z) <= C_{r,p}.
```

The plausible proof route is regularized log-det universality for

```text
E exp(0.5 Tr log(YY^T + eps I))
```

followed by hard-edge/small-ball removal of `eps`.

Verification:

```powershell
python -m py_compile numerics\square_small_fresh_count_budget.py numerics\p1_cap_density_ratio_probe.py numerics\p1_frame_profile_chart_probe.py
python numerics\square_small_fresh_count_budget.py --min-m 20 --max-m 80 --step 20
rg -n "Fresh-row one-step lemma|effective excess|small-fresh taxonomy|zero-fresh planted-vector sphere|Sliced Determinant Universality|square_small_fresh_count_budget" notes numerics -g "*.md" -g "*.py"
```

The small-fresh smoke reported asymptotic normalized max rate about
`-0.36653` at `D/m ~= 0.61805`, with no nonnegative normalized threshold.
The pair-level comparison crossed at `D/m ~= 0.167967670520` and at the
boundary root `1.0`, matching the zero-fresh obstruction analysis.

## Continuation update, pair-Palm cluster program, 2026-06-30

Five Codex agents attacked the pair-Palm inputs behind the P2 small-fresh
cluster theorem and tightened the P1 determinant-volume transfer target.  No
background processes, daemons, or scheduled tasks were created.

New P2 artifacts:

- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`
- `numerics\square_zero_fresh_sphere_integral_probe.py`

Updated P2 artifacts:

- `notes\all_apex_square_higher_factorial_moments_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_sphere_integral_2026_06_30.md`
- `notes\all_apex_square_small_fresh_taxonomy_2026_06_30.md`
- `notes\all_apex_square_fixed_k_cluster_intensity_target_2026_06_30.md`

The pair-Palm program now has the exact Gaussian two-witness density.  For
planted directions `u,v`, `rho=<u,v>`, and
`r=sqrt(1-rho^2)`, common rows contribute

```text
phi_{u,v}(0)=(2pi)^(-m) r^(-|B_1 cap B_2|).
```

The regular two-witness slab formula is recorded with determinant-volume
weights

```text
J_i=sqrt(det((A_{B_i}|_{u_i^perp})^T(A_{B_i}|_{u_i^perp}))).
```

The leading Gaussian anti-coalescence input is now explicit.  Conditional on
the common core `C`, the planted right directions are independent Haar
vectors in `ker(C)`, whose dimension is `D=m-|B_1 cap B_2|`.  Thus

```text
rho^2 ~ Beta(1/2,(D-1)/2),
E[(1-rho^2)^(-1/2)] <= pi/2       for D>=3.
```

The remaining Palm theorem is no longer vague angular repulsion.  Let `Q_12`
be the sliced Gaussian base law and

```text
R_12=J_1J_2/E_Q[J_1J_2].
```

The required theorem is the two-witness Gaussian Palm weight bound:

```text
E_{Q_12} R_12^p <= exp(o(m)).
```

Then every nonnegative cluster observable satisfies the transfer estimate

```text
E_{Palm_12} Phi <= exp(o(m)) ||Phi||_{L^{p'}(Q_12)}.
```

The one-fresh sector was also sharpened.  In the irreducible residual,
`b,c>=D-1`, so the marked counts satisfy `a+b+c=m-1`.  The same
planted-vector integral gains the nonpositive factor
`(2m)^-1 log(1-s)`, hence one-fresh is no worse than zero-fresh at the
saddle level.  The analytic cost is again a pair-Palm determinant-weight and
subset-pseudoinverse estimate.

The fresh-row pseudoinverse target now uses the corrected effective excess

```text
delta_B=1_{b=0}+1_{c=0},
e_B=f_B-delta_B.
```

For `e_B>=2`, the expected inverse-Wishart scale is
`O(m^C m/(e_B-1))`; for `e_B=1`, it is
`O(m^C log(e/s_m))`.  The critical `f_B=2,b=c=0` sector has `e_B=0` and is
routed to close/fixed-`D` machinery unless determinant-weight repulsion is
proved.

The zero-fresh sphere-integral diagnostic evaluates the exact finite-`m`
two-dimensional integral.  Smoke command:

```powershell
python numerics\square_zero_fresh_sphere_integral_probe.py --m 80 --b 24 --c 30 --rho-values 0 0.5 0.9 --s-nodes 80 --theta-nodes 720
```

It reports integral/poly-scale ratios about `1.03293` for `rho=0`, `0.5`,
and `0.9`, with a nonpositive numerical rate envelope.  This supports the
claim that the endpoint-excluded bulk cost is polynomial and proportional to
`(1-rho^2)^(-1/2)`.

Updated P1 artifact:

- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The P1 density-ratio target now records a sublinear theorem available from
QR one-step control.  If

```text
delta_q(U,z)=sup_H (E dist(Y_z,H)/E chi_q - 1)_+
```

over codimension-`q` subspaces has

```text
||exp(sum_q delta_q(U,z))||_{L^p(nu^G)} <= C,
```

then `||V_U||_{L^p(nu^G)}<=C`.  A one-step Edgeworth estimate of size
`O(L_m^C D/m)` per QR step gives

```text
V_U(z) <= exp(C L_m^C D^2/m+o(D^2/m)),
```

so this closes the determinant-volume transfer only when
`D^2 polylog(m)/m=O(1)`.  The linear-aspect case remains conditional on the
regularized log-det/Sliced Determinant Universality theorem for admissible
smooth subgaussian product laws.

Verification:

```powershell
python -m py_compile numerics\square_zero_fresh_sphere_integral_probe.py numerics\square_small_fresh_count_budget.py numerics\p1_cap_density_ratio_probe.py numerics\p1_frame_profile_chart_probe.py
python numerics\square_zero_fresh_sphere_integral_probe.py --m 80 --b 24 --c 30 --rho-values 0 0.5 0.9 --s-nodes 80 --theta-nodes 720
rg -n "Two-Witness Gaussian Palm Weight|anti-coalescence|Sliced Determinant Universality|square_zero_fresh_sphere_integral_probe|effective excess|one-fresh" notes numerics -g "*.md" -g "*.py"
```

## Continuation update, Palm-weight closure and QR transfer, 2026-06-30

Five Codex agents were assigned to the next pair-Palm and determinant-volume
frontier.  All five returned proof artifacts.  No background processes,
daemons, scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_one_witness_palm_weight_factorization_2026_06_30.md`
- `notes\all_apex_square_two_witness_palm_weight_bound_2026_06_30.md`
- `notes\all_apex_square_finite_threshold_pair_palm_transfer_2026_06_30.md`
- `notes\all_apex_square_palm_weight_moment_reduction_2026_06_30.md`
- `notes\all_apex_square_pair_palm_subset_pseudoinverse_2026_06_30.md`
- `numerics\square_palm_weight_moment_probe.py`

Updated P2 artifact:

- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`

The exact zero-level Gaussian determinant-weight input is now essentially
closed.  Under the sliced base law, after conditioning on planted directions
`u,v` and writing `L=span(u,v)^perp`, one witness has the QR/Wishart
factorization

```text
J^2 = det(S) det(N^T N) (1+h^T S^-1 h),
S ~ Wishart_{m-D}(m-2,I),
N^T N ~ Wishart_{D-1}(D,I).
```

For two witnesses, the private factors are conditionally independent given
`S`.  Standard chi-product moment estimates and the Hotelling
inverse-Wishart quadratic-form moment give, for fixed `p>1`,

```text
sup_rho E_{Q_12}[R_12^p | rho] <= C_p m^{C_p},
```

for every `D>=2`.  Thus

```text
E_{Q_12} R_12^p <= exp(o(m)).
```

The determinant tilt has no `rho` dependence after the subspaces are
identified; the angular beta law remains the only coalescence input.  `D=2`
is determinant-safe but still has the known angular endpoint issue, and
`D=1` remains on the fixed-`D`/close route.

The raw-common-core one-witness factorization is compatible:

```text
J_full = sqrt(det(CC^T)) V_D sqrt(1+Z^T(CC^T)^-1Z).
```

After disintegrating by the raw common core, `sqrt(det(CC^T))` is the common
coarea Jacobian and cancels.  The normalized one-witness factor has
conditional fixed-`p` moments bounded by

```text
C_p D^{p(p-1)/4}.
```

The foreground reduction note isolates the slope tilt and checks the sliced
common-core excess: under the two-witness sliced law,

```text
CC^T ~ Wishart_{m-D}(m-2,I),
E tr((CC^T)^-1) = (m-D)/(D-3).
```

The new probe

```powershell
python numerics\square_palm_weight_moment_probe.py --m-values 32 64 --d-values 8 1/2 --common-samples 20 --z-samples 256 --p 2 --seed 20260630
```

reported common-core moment ratios `1.1567`, `1.0080`, `1.0612`, and
`1.0008` across the tested `(m,D)` cases, with trace ratios close to the
`(m-D)/(D-3)` expectation.

The finite-threshold bridge is now explicit.  At

```text
s_m(lambda) ~ 2 sqrt(pi) lambda 4^-m,
```

`all_apex_square_finite_threshold_pair_palm_transfer_2026_06_30.md` states
regularity events, chart displacement, vector planted-direction transfer,
determinant stability, and perturbation-stable pseudoinverse shells.  It
lets the small-fresh program prove estimates under the exact zero Palm law
and then transfer them to the actual event
`E_{B_1}(s_m) cap E_{B_2}(s_m)`, provided the shell cutoff
`rho_B > s_m exp(o(m))` is included.

The effective-excess subset-pseudoinverse input is also now proved under the
sliced base law.  For a completion with counts `a,b,c,f`,

```text
delta=1_{b=0}+1_{c=0},
e=f-delta,
dim W_B=m-delta.
```

Thus `e` is exactly the active rectangular excess.  Away from fixed-small-`D`
angular endpoints,

```text
e>=2:
E_{Q_12}[(f^2/m)||C_B^+||_F^2] <= m^C f^2/(e-1),

e=1:
E_{Q_12}[(f^2/m)||C_B^+||_F^2 1_{rho_B>tau}]
 <= m^C f^2 log(C/tau).
```

The proof uses an orthogonal-side normal form and a Schur-complement residual
block of size at most `2`.  The only angular loss is `(1-rho^2)^-1` when both
private sides are active, integrable under the beta angular law for `D>3`.
Combining this with the determinant-weight theorem and the finite-threshold
stable cutoff `tau=s_m exp(o(m))` closes Palm input (C) for all noncritical
`e>0` sectors up to `exp(o(m))`.

New P1 artifact:

- `notes\p1_qr_sliced_determinant_universality_2026_06_30.md`

Updated P1 artifact:

- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The P1 QR determinant-volume theorem is now standalone.  It proves

```text
V_U(z) <= exp(sum_q delta_q(U,z)),
```

where `delta_q` is the positive excess in one QR distance over the Gaussian
`chi_q` benchmark.  A one-step Edgeworth/distance bound with error
`O(L_m^C D/m)` gives

```text
V_U(z) <= exp(C_r L_m^C D^2/m + D eps_{m,D}).
```

Therefore the rigorous QR route reaches the sublinear regime
`D^2 polylog(m)/m=O(1)` and gives convergence when that expression tends to
zero.  Linear aspect still needs a cap-averaged `sum_q delta_q=O(1)`,
random-QR-span signed cancellation, or direct regularized log-det
universality.

Verification:

```powershell
python -m py_compile numerics\square_palm_weight_moment_probe.py numerics\square_zero_fresh_sphere_integral_probe.py numerics\square_small_fresh_count_budget.py numerics\p1_cap_density_ratio_probe.py numerics\p1_frame_profile_chart_probe.py
python numerics\square_palm_weight_moment_probe.py --m-values 32 64 --d-values 8 1/2 --common-samples 20 --z-samples 256 --p 2 --seed 20260630
rg -n "Two-Witness Gaussian Palm Weight|two_witness_palm_weight|finite-threshold|one_witness|palm_weight_moment|QR sliced|D\\^2 polylog|square_palm_weight_moment_probe" notes numerics -g "*.md" -g "*.py"
```

The next P2 blocker is now sharply narrowed to assembling the small-fresh
cluster theorem while routing the fixed-small-`D` angular endpoints and the
critical `e=0` sector, especially `f=2,b=c=0`, through close/fixed-`D`
machinery or a separate determinant-repulsion argument.  The
determinant-weight and noncritical subset-pseudoinverse parts of the Gaussian
pair-Palm law should no longer be treated as open exponential obstructions.

## Continuation update, nonzero-fresh assembly and zero-fresh frontier, 2026-06-30

Five Codex agents were assigned to the next P2 assembly frontier and the P1
linear-aspect determinant-volume route.  All five returned proof artifacts.
No background processes, daemons, scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`
- `notes\all_apex_square_nonzero_fresh_reduction_2026_06_30.md`
- `notes\all_apex_square_critical_e0_sector_2026_06_30.md`
- `notes\all_apex_square_fixed_small_d_endpoint_route_2026_06_30.md`
- `notes\all_apex_square_zero_one_fresh_factorial_cluster_2026_06_30.md`

Updated P2 artifacts:

- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`
- `notes\all_apex_square_small_fresh_taxonomy_2026_06_30.md`
- `notes\all_apex_square_fixed_k_cluster_intensity_target_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_cluster_target_2026_06_30.md`
- `numerics\square_small_fresh_count_budget.py`

The nonzero-fresh small-cluster sector is now assembled.  For a completion
after a marked pair, with

```text
e=f-1_{b=0}-1_{c=0},
```

every non-close, non-fixed-small-`D` completion with `f>=1` has `e>0`.
Thus the fresh-row block-inverse lemma, the pair-Palm determinant-weight
bound, the `e>=1` subset-pseudoinverse theorem, and finite-threshold shell
transfer give, for every fixed `r`,

```text
E[1_{E_1 cap E_2} (Z_nonzero)_r]
 <= exp(o(m)) P(E_1 cap E_2) (|Z_nonzero|p_m)^r.
```

The previously scary fresh critical sector is routeable by geometry:

```text
f=2,b=c=0  =>  D<=2,  D(B,B_1)=D(B,B_2)=2.
```

It belongs to the close/fixed-`D` envelope, and no new determinant-repulsion
theorem is needed for that sector.  The optional audit mode

```powershell
python numerics\square_small_fresh_count_budget.py --min-m 20 --max-m 80 --step 20 --audit-nonzero-e --no-entropy
```

reported `surviving_cases=0` for `m=20,40,60,80` with the default
`L=2,D0=2` exclusions.

The fixed-small-`D` endpoint route is also sharper.  For `D=1,2,3`, fixed
zero-fresh and one-fresh endpoint families are count-killed by the fixed-`D`
pair envelope, and the `f=2,b=c=0` corner is count-killed as well.  What
remains is a local fixed-`D=1,2,3` fresh-cluster estimate for non-close
families with at least two fresh rows, with an angular cutoff for `D=2,3`.

The genuine remaining P2 analytic frontier is now zero-fresh fixed factorial
powers.  The `r=1` sphere integral has no positive exponential saddle and
gives the right one-candidate cost, but this does not automatically iterate:
for `r>=2`, candidate-candidate coalescence creates new Gram determinant
endpoints.  The new target is a joint fixed-`r` Kac-Rice/Palm estimate for
endpoint-excluded zero-fresh tuples, or an equivalent sequential multi-Palm
theorem.

New P1 artifact:

- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`

Updated P1 artifact:

- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The P1 linear-aspect route now has two exact formulations:

```text
V_U(z)=prod_q (1+beta_q(U,z))
```

with determinant-tilted random QR spans, and a regularized log-det reduction:

```text
K_{d,tau}=E Phi_tau(G_d)/E|det G_d| <= C,
||E Phi_tau(Y_z^{(d)})/E Phi_tau(G_d)||_{L^p(nu^G)} <= C
  => ||V_U||_{L^p(nu^G)} <= C.
```

The genuinely new linear-aspect work is determinant-tilted hard-edge control,
log-det derivative/resolvent moment bounds at `tau=d^{-B}`, and a
cap-averaged positive-part bound for the signed Edgeworth replacement
increments.

Verification:

```powershell
python -m py_compile numerics\square_small_fresh_count_budget.py numerics\square_palm_weight_moment_probe.py numerics\square_zero_fresh_sphere_integral_probe.py numerics\p1_cap_density_ratio_probe.py numerics\p1_frame_profile_chart_probe.py
python numerics\square_small_fresh_count_budget.py --min-m 20 --max-m 80 --step 20 --audit-nonzero-e --no-entropy
rg -n "nonzero-fresh|zero-fresh fixed|joint fixed|f=2,b=c=0|fixed-small|linear-aspect|Regularized log-det|surviving_cases" notes numerics -g "*.md" -g "*.py"
```

## Continuation update, zero-fresh joint kernel and Gaussian logdet, 2026-06-30

Five Codex agents were assigned to the remaining zero-fresh fixed-factorial
frontier, the fixed-small-`D` fresh endpoint, and the P1 Gaussian logdet
factor.  All five returned artifacts.  No background processes, daemons,
scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_zero_fresh_joint_shearer_reduction_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_joint_gram_inequality_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_candidate_endpoint_route_2026_06_30.md`
- `notes\all_apex_square_fixed_small_d_fresh_cluster_2026_06_30.md`
- `numerics\square_zero_fresh_joint_kernel_probe.py`

Updated P2 artifacts:

- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`
- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`
- `notes\all_apex_square_zero_one_fresh_factorial_cluster_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_cluster_target_2026_06_30.md`
- `notes\all_apex_square_fixed_small_d_endpoint_route_2026_06_30.md`

The fixed-`r` zero-fresh exponential saddle is now removed.  In the joint
planted-vector kernel, the zero-fresh row-pattern weights form a fractional
partition of the candidate set.  Determinantal Shearer gives

```text
log det R_C <= sum_{A,S} lambda_{A,S} log det R_A[S],
```

so there is no positive exponential rate for any fixed `r`.  The remaining
zero-fresh problem is endpoint integrability, not saddle optimization.

The `r=2` Gram note gives the sharper endpoint mechanics.  For orthogonal
marked directions and two zero-fresh candidates at set distance `d=D(B,B')`,
the crude candidate-candidate coalescence factor after angular volume is

```text
(1-tau^2)^((d-5)/2).
```

Thus close candidate-candidate endpoints are exactly the small-`d` cases.
Those are routed by re-marking the candidate pair: the original marked
squares then acquire fresh rows relative to the new pair, and the remaining
cluster is handled by the nonzero-fresh positive-effective-excess theorem or
by the fixed-small-distance route.

The fixed-small-`D` fresh endpoint is also narrowed.  For `D=2,3`, the
regular sector `r=sqrt(1-rho^2)>=r_m` follows from the existing
positive-effective-excess fresh-row/pseudoinverse proof with a truncated
angular loss.  For `D=1`, the two-angle law is the wrong object; the local
model is the degenerate common-kernel model, where a completion with `f`
fresh rows has active excess `f-1`.  The genuine leftover is the capped
common-core finite-threshold transfer lemma.

New P1 artifact:

- `notes\p1_gaussian_regularized_logdet_factor_2026_06_30.md`

Updated P1 artifacts:

- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The Gaussian regularized logdet factor is closed.  For

```text
Phi_tau(M)=det(MM^T+tau^2 I)^(1/2),
K_{d,tau}=E Phi_tau(G_d)/E|det G_d|,
```

the determinant-tilted Wishart identity gives

```text
tau=d^{-B}, B>1/2  =>  K_{d,tau}=1+O_B(d^(1-2B) log d) -> 1.
```

At `B=1/2`, `K_{d,tau}=O(1)`, and for `0<B<1/2` the logarithm is too large.
Thus the P1 linear-aspect route should choose `B>1/2`; the remaining hard
work is non-Gaussian regularized logdet universality at that scale.

Verification:

```powershell
python -m py_compile numerics\square_small_fresh_count_budget.py numerics\square_palm_weight_moment_probe.py numerics\square_zero_fresh_sphere_integral_probe.py numerics\p1_cap_density_ratio_probe.py numerics\p1_frame_profile_chart_probe.py numerics\square_zero_fresh_joint_kernel_probe.py
python numerics\square_small_fresh_count_budget.py --min-m 20 --max-m 80 --step 20 --audit-nonzero-e --no-entropy
python numerics\square_zero_fresh_joint_kernel_probe.py --m 12 --d 6 --c-10 1 --c-01 1 --c-11 3 --p1-10 3 --p1-01 1 --p1-11 2 --p2-10 1 --p2-01 3 --p2-11 2 --samples 256 --seed 20260630
python numerics\square_zero_fresh_joint_kernel_probe.py --m 6 --d 3 --c-10 0 --c-01 0 --c-11 3 --p1-10 3 --p1-01 0 --p1-11 0 --p2-10 0 --p2-01 3 --p2-11 0 --mode grid --grid-s-nodes 2 --grid-theta-nodes 4 --grid-psi-nodes 2 --top-k 3
rg -n 'zero_fresh_joint_shearer|joint_shearer|joint_gram|candidate_endpoint|fixed_small_d_fresh|gaussian_regularized|joint fixed|endpoint integrability|B>1/2|surviving_cases|square_zero_fresh_joint_kernel_probe' notes numerics -g '*.md' -g '*.py'
```

The nonzero-fresh audit again reported `surviving_cases=0` for
`m=20,40,60,80`.  The joint-kernel sample smoke reported
`max_excess_rate=2.428298925156e-01` with `warnings=ok`.  The tiny grid run
correctly flagged candidate coalescence and marked-plane endpoint warnings.

## Continuation update, endpoint reductions and logdet Lindeberg, 2026-06-30

Five Codex agents were assigned to the next P2 endpoint and P1 logdet
frontiers.  All five returned artifacts.  No background processes, daemons,
scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_zero_fresh_r2_conditional_factorization_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_r2_endpoint_atlas_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_fixed_r_endpoint_bootstrap_2026_06_30.md`
- `notes\all_apex_square_d1_capped_common_core_transfer_2026_06_30.md`

Updated P2 artifacts:

- `notes\all_apex_square_zero_fresh_joint_gram_inequality_2026_06_30.md`
- `notes\all_apex_square_zero_one_fresh_factorial_cluster_2026_06_30.md`
- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`
- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`
- `notes\all_apex_square_fixed_small_d_fresh_cluster_2026_06_30.md`

The `r=2` zero-fresh endpoint problem is now smaller than the original Gram
integral.  The conditional factorization proves

```text
K_n(w,z)=K_w(w)K_z(z) prod_A Gamma_A(w,z)^(-n_{A,12}/2),
```

so all marked-plane powers are exactly the one-point zero-fresh weights.  The
endpoint atlas keeps the exact determinants

```text
D_0=|x|^2|y|^2-<x,y>^2,
D_1=|beta y-delta x|^2+D_0,
D_2=|alpha y-gamma x|^2+D_0,
```

and checks the scalar exponents:

```text
u endpoints:              c_1-2, c_2-2,
v endpoints:              b_1-2, b_2-2,
marked-plane normals:     (b_j+c_j-4)/2,
candidate coalescence:    (d-5)/2.
```

Thus `b_1,c_1,b_2,c_2,d>L_m` pays every scalar endpoint.  The exact remaining
`r=2` input is the angular-gap inequality `(AG)`: polynomial uniformity of
the finite-overlap/resolution estimate for `G_0,G_1,G_2`.

For fixed `r`, the bootstrap note proves the sequential determinant identity
and endpoint deficit ledger.  The remaining fixed-`r` endpoint input is the
finite-dimensional arrangement lemma `A(r)`, equivalently joint
Gram-Schmidt inequality `(9)`.  This contains no exponential saddle, no row
set summation, and no random-matrix hard edge.

The `D=1` fixed-small endpoint was narrowed as well.  The capped common-core
weight is

```text
W_s(M)=P(E_{B_1}(s) cap E_{B_2}(s)|M)=q_s(M)^2.
```

The non-close shell estimate is closed using `W_s<=1`, `E W_s>=p_m^2`, and
active excess `f-1`.  The sole remaining `D=1` input is the capped nested
inverse-Wishart deletion moment `(JD)`.

New P1 artifacts:

- `notes\p1_regularized_logdet_derivative_lindeberg_2026_06_30.md`
- `numerics\p1_regularized_logdet_lindeberg_probe.py`
- `notes\p1_regularized_logdet_lindeberg_probe_2026_06_30.md`

Updated P1 artifacts:

- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The P1 derivative note gives the one-row Schur complement formula

```text
Phi_tau(A(B,y))=det(BB^T+tau^2 I)^(1/2)
                (tau^2+y^T R_B y)^(1/2),
R_B=tau^2(B^T B+tau^2 I)^(-1),
```

and the derivative partition formulas.  It proves that Gaussian-paired
signed derivatives are `tau`-uniform before absolute values are taken.  It
also identifies the obstruction: raw absolute order-six and order-eight
derivatives scale like `tau^-4` and `tau^-6`, so the proof must keep signed
Hermite/Edgeworth pairing through the quartic and cubic-square main terms.
The new P1 blockers are the signed contractions, the final unsigned
remainder hard-edge estimate `HE_rem(K)`, and the cap exponential moment for
the positive signed increments.

Verification:

```powershell
python -m py_compile numerics\p1_regularized_logdet_lindeberg_probe.py numerics\square_zero_fresh_joint_kernel_probe.py numerics\square_small_fresh_count_budget.py numerics\p1_cap_density_ratio_probe.py numerics\p1_frame_profile_chart_probe.py
python -B numerics\p1_regularized_logdet_lindeberg_probe.py --laws gaussian uniform beta25 --m-values 8 --d-values 2 --radii 0 0.5 --frames 1 --z-directions 1 --row-samples 300 --matrix-samples 200 --seed 20260630
python numerics\square_small_fresh_count_budget.py --min-m 20 --max-m 80 --step 20 --audit-nonzero-e --no-entropy
rg -n 'r2_conditional|r2_endpoint_atlas|fixed_r_endpoint|angular-gap|\(AG\)|A\(r\)|\(JD\)|capped nested|regularized_logdet_derivative|regularized_logdet_lindeberg|HE_rem|Gaussian-paired|positive signed' notes numerics '..\Open problem project\five_agent_plan_2026_06_30.md' -g '*.md' -g '*.py'
```

The new P1 smoke emitted valid CSV rows for Gaussian, uniform, and beta25 at
`m=8,d=2`; the nonzero-fresh audit again reported `surviving_cases=0` for
`m=20,40,60,80`.

## Continuation update, AG and JD closures, 2026-06-30

Five Codex agents were assigned to the exact blockers `(AG)`, `A(r)/(9)`,
`(JD)`, `(CI-logdet)`, and `HE_rem(K)`.  All five returned artifacts.  No
background processes, daemons, scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_zero_fresh_r2_angular_gap_resolution_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_arrangement_endpoint_lemma_2026_06_30.md`
- `notes\all_apex_square_d1_jd_no_private_reduction_2026_06_30.md`
- `notes\all_apex_square_d1_nested_deletion_moment_2026_06_30.md`

Updated P2 artifacts:

- `notes\all_apex_square_zero_fresh_r2_endpoint_atlas_2026_06_30.md`
- `notes\all_apex_square_d1_capped_common_core_transfer_2026_06_30.md`
- `notes\all_apex_square_fixed_small_d_fresh_cluster_2026_06_30.md`
- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`
- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`

The `r=2` angular-gap blocker `(AG)` is closed in the resolved/factored
sense required by the endpoint atlas.  The key deterministic domination is

```text
G_1 >= kappa_1 G_0,        G_2 >= kappa_2 G_0.
```

After extracting the scalar factors
`kappa_1^(-s_1/2) kappa_2^(-s_2/2)`, the angular integral becomes the
one-dimensional beta integral with exponent `(d-5)/2`, polynomial for
`d>L_m`.  The extracted scalar factors are paid by the already audited
`b_1,c_1,b_2,c_2>L_m` endpoint powers.  Thus the orthogonal `r=2` zero-fresh
endpoint model is closed up to scalar-factor bookkeeping.

For fixed `r>2`, the arrangement note gives a degeneration-aware lattice
form of `A(r)` and reduces the joint endpoint inequality `(9)` to a finite
real-blowup chart statement `LC1-LC7`.  This is now the exact remaining P2
zero-fresh fixed-factorial endpoint input beyond `r=2`.

The `D=1` fixed-small fresh transfer is now closed.  The foreground
no-private note proves the no-private deletion estimate by a two-threshold
argument.  The nested deletion moment note then proves the full `(JD)`,
including one or two selected private projection rows under the normalized
finite-threshold slab tilt, using Holder only in the private variables so the
dangerous cap `T_s(M)` remains in first moment.

New P1 artifacts:

- `notes\p1_logdet_signed_hermite_contractions_2026_06_30.md`
- `notes\p1_logdet_he_rem_hard_edge_2026_06_30.md`
- `numerics\p1_logdet_derivative_hardedge_probe.py`

Updated P1 artifacts:

- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The signed Hermite note gives exact quartic and cubic-square pairings
`H_4` and `H_33`, plus a rank-one hard-edge check showing no raw `tau`
powers in the signed main terms.  It reduces the contraction problem to
`(CI-logdet)`: determinant-tilted residual multipliers must collapse, after
positive part and averaging, to the existing cap profiles `P_4(q_z,W)` and
`P_3(q_z,W)` at one-row scale `d^-1`.

The hard-edge/remainder note defines `HE_rem(K)` as the exact positive
log-remainder theorem after signed main terms are removed.  It explicitly
warns that absolute `|D^6 Phi_tau|` or `|D^8 Phi_tau|` bounds are the wrong
target at `tau=d^{-B}`, `B>1/2`.  The new diagnostic measures the raw
deleted-row leverage envelopes under Gaussian determinant tilt.

Current sharp blockers:

```text
P2: fixed-r>2 arrangement chart inequalities LC1-LC7.
P1: CI-logdet, HE_rem(K), and the cap exponential moment for positive signed
    increments.
```

## Continuation update, LC/r3 and logdet reductions, 2026-06-30

Five Codex agents were assigned to the sharpened P2 zero-fresh endpoint and
P1 logdet frontiers.  All five returned artifacts.  No background processes,
daemons, scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_zero_fresh_lc_chart_proof_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_r3_support_ledger_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_r3_endpoint_2026_06_30.md`

Updated P2 artifacts:

- `notes\all_apex_square_zero_fresh_arrangement_endpoint_lemma_2026_06_30.md`
- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`
- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`

The fixed-`r` chart problem is now reduced as follows:

```text
LC1-LC6: standard real wonderful-model monomialization of the exact
         labelled arrangement E(A,T);

LC7:     reduced to the labelled block-volume theorem LBV(r).
```

Conditional on `LBV(r)`, LC7 is paid by the existing deficits

```text
b_j>L,        c_j>L,        D(B^j,B^l)>L.
```

For `r=3`, the previous-flag obstruction is closed at the endpoint level.
Every incompatible final flat for `w_3` is an exact endpoint of the already
resolved `(w_1,w_2)` pair, through `det R_C[1,2]`, `det R_1[1,2]`,
`det R_2[1,2]`, or a one-point marked endpoint.  The final conditional
integral costs only a fixed power of that pair boundary, so
`D(B^1,B^2)>L` absorbs it.

New P1 artifacts:

- `notes\p1_logdet_ci_multiplier_reduction_2026_06_30.md`
- `notes\p1_logdet_he_rem_decomposition_2026_06_30.md`
- `notes\p1_logdet_positive_increment_cap_moment_2026_06_30.md`
- `numerics\p1_logdet_positive_increment_probe.py`

Updated P1 artifacts:

- `notes\p1_logdet_he_rem_hard_edge_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The deterministic fixed-chart version of `(CI-logdet)` is false: the signed
logdet Hermite multipliers diagonalize in the residual eigenbasis of

```text
C_t=2tR_B(I+2tR_B)^(-1),
```

not in the fixed chart basis.  The replacement target is residual spectral
averaging `(RSA)` under the determinant-tilted deleted-row law; `(RSA)`
implies `(CI-logdet)`.

The hard-edge remainder is now localized.  In the ratio-level decomposition,
the log term is identically zero, the row-norm cutoff budget is closed, and
`HE_rem(K)` is reduced to:

```text
(CT_K)       ordinary Cramer tail for the cutoff test class;
(HE_near(K)) positive near-zone remainder after signed main terms are
             removed.
```

The positive signed increment cap moment is reduced to an exponential
frame-profile theorem:

```text
ExpProfile(lambda) for
d^(-1) sum_i [1+P_4(q_z,W_i)+P_3(q_z,W_i)].
```

The existing integrated profile theorem is not enough for this exponential
budget.  The remaining cap input is a small-Laplace-window quartic cap-chaos
theorem, with the actual `(CI-logdet)` coefficient required to fit inside the
window.

Verification:

```powershell
python -m py_compile numerics\p1_logdet_positive_increment_probe.py numerics\p1_logdet_derivative_hardedge_probe.py numerics\p1_regularized_logdet_lindeberg_probe.py numerics\square_small_fresh_count_budget.py
python numerics\p1_logdet_positive_increment_probe.py --laws gaussian --m-values 16 --d-values 4 --radii 1 --chart-modes direct_haar_frame --z-measures gaussian_cauchy --frames 2 --z-samples 16 --lambdas 0.25 0.5 --seed 20260630
python -B numerics\p1_logdet_derivative_hardedge_probe.py --d-values 2 --tau-powers 0.75 --samples 40 --seed 20260630
python numerics\square_small_fresh_count_budget.py --min-m 20 --max-m 80 --step 20 --audit-nonzero-e --no-entropy
rg -n 'LBV\(r\)|LC1-LC7|r3_support|r3_endpoint|CI-logdet|HE_near|CT_K|positive_increment|cap-chaos|lc_chart|surviving_cases=0|\(RSA\)|ExpProfile' notes numerics '..\Open problem project\five_agent_plan_2026_06_30.md' -g '*.md' -g '*.py'
```

The new positive-increment smoke emitted a finite CSV row at
`m=16,d=4` with `mean_A=2.354074`, `log_mgf_lambda_0.25=0.5894523`, and
`log_mgf_lambda_0.5=1.180794`.  The hard-edge diagnostic emitted valid CSV
rows at `d=2,tau=d^-0.75`.  The nonzero-fresh audit again reported
`surviving_cases=0` for `m=20,40,60,80`.

Current sharp blockers:

```text
P2: prove LBV(r) for general fixed r, then splice the closed r=3 endpoint
    and conditional LC7 proof into the Shearer zero-fresh theorem.

P1: prove (RSA), prove (CT_K)+(HE_near(K)), and prove the small-window
    ExpProfile(lambda)/quartic cap-chaos theorem with the actual CI
    coefficient inside the window.
```

## Continuation update, NQSD, r=3 splice, HE kernels, and cap Laplace, 2026-06-30

Five Codex agents were assigned to the next P2/P1 blockers.  Four returned
completed artifacts so far; the residual spectral averaging `(RSA)` worker
was still running at the time this entry was written.  No background
processes, daemons, scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_zero_fresh_lbv_proof_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_r3_shearer_splice_2026_06_30.md`

Updated P2 artifacts:

- `notes\all_apex_square_zero_fresh_arrangement_endpoint_lemma_2026_06_30.md`
- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`
- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`

The general fixed-`r` endpoint blocker has been reduced again:

```text
NQSD(r) => LBV(r) => LC7.
```

Here `NQSD(r)` is the finite nested quotient support dichotomy: after lower
chart flags are quotiented out, any active support split with no common
primitive witness must expose a current modular defect, giving one extra
`m-O_r(1)` normal block.  Conditional on `NQSD(r)`, the labelled
block-volume theorem and `LC7` are proved.

The `r=3` result has also been spliced into the fixed-factorial route.  The
new splice note proves the endpoint-excluded zero-fresh third falling
factorial estimate by combining:

```text
Shearer no-positive-saddle,
the closed r=3 endpoint integral,
pair-Palm beta anti-coalescence and determinant-weight moments,
finite-threshold transfer.
```

Thus the P2 zero-fresh frontier is:

```text
r=1,2: closed endpoint models;
r=3: endpoint-excluded third factorial bound spliced;
general fixed r: prove NQSD(r).
```

New P1 artifacts:

- `notes\p1_logdet_he_near_cramer_target_2026_06_30.md`
- `notes\p1_quartic_cap_chaos_reduction_2026_06_30.md`
- `notes\p1_quartic_cap_chaos_laplace_2026_06_30.md`
- `numerics\p1_quartic_cap_chaos_probe.py`

Updated P1 artifacts:

- `notes\p1_logdet_he_rem_hard_edge_2026_06_30.md`
- `notes\p1_logdet_positive_increment_cap_moment_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The hard-edge remainder frontier is now:

```text
(OCT_K) => (CT_K),
(NCR_K) or stronger (WNR_K) => HE_near(K).
```

`(OCT_K)` is an ordinary density-level Cramer tail for the sliced row law and
uses only the linear-growth cutoff-test bound.  `(NCR_K)` is the exact
positive physical-space pairing of the cutoff logdet test against the
post-Edgeworth near kernel; `(WNR_K)` is the weighted positive-kernel
sufficient condition.  No raw absolute high-derivative bound is used.

The cap exponential moment has a finite explicit window on the static Haar
good event.  If `d||p||_4^4<=M` and

```text
a_r=192 r^2/(1+r^2),
```

then

```text
E_{nu^G_{D,r}} exp(eta d||q_z||_4^4)
 <= exp(eta(M+9)/(1-a_r eta)),
eta < 1/a_r.
```

Combining this with the profile domination closes homogeneous
`ExpProfile(lambda)` for a finite window, before inserting the actual
`(CI-logdet)` coefficient.  The remaining cap-side work is coefficient
tracking and transfer to step-dependent determinant-tilted residual frames,
not proving existence of a small Laplace window.

Verification:

```powershell
python -m py_compile numerics\p1_quartic_cap_chaos_probe.py numerics\p1_logdet_positive_increment_probe.py numerics\p1_logdet_derivative_hardedge_probe.py numerics\p1_regularized_logdet_lindeberg_probe.py numerics\square_small_fresh_count_budget.py
python -B numerics\p1_quartic_cap_chaos_probe.py --m-values 24 --d-values 6 --radii 1 --frames 1 --z-samples 8 --lambdas 0.001 --seed 20260630
python numerics\p1_logdet_positive_increment_probe.py --laws gaussian --m-values 16 --d-values 4 --radii 1 --chart-modes direct_haar_frame --z-measures gaussian_cauchy --frames 2 --z-samples 16 --lambdas 0.25 0.5 --seed 20260630
python numerics\square_small_fresh_count_budget.py --min-m 20 --max-m 80 --step 20 --audit-nonzero-e --no-entropy
rg -n 'NQSD\(r\)|LBV\(r\)|r3_shearer|OCT_K|NCR_K|WNR_K|quartic cap-chaos|a_r=192|ExpProfile\(lambda\)|p1_quartic_cap_chaos' notes numerics '..\Open problem project\five_agent_plan_2026_06_30.md' -g '*.md' -g '*.py'
```

The quartic cap-chaos smoke row had `mean_T=0.557721`,
`log_mgf_lambda_0.001=5.577228e-04`, and proof log bound
`1.052968e-02`.  The positive-increment smoke again emitted finite rows.
The nonzero-fresh audit again reported `surviving_cases=0` for
`m=20,40,60,80`.

Current sharp blockers after these returns:

```text
P2: prove NQSD(r) for the finite labelled nested quotient building set.

P1: integrate the pending RSA result; prove or reduce the actual residual
    spectral averaging theorem.  Separately, prove (NCR_K)/(WNR_K) for the
    near-zone post-cancellation kernel and track the CI coefficient against
    the cap Laplace window.
```

### RSA return

The fifth agent returned after the entry above.

New P1 artifact:

- `notes\p1_logdet_rsa_gaussian_benchmark_2026_06_30.md`

Updated P1 artifacts:

- `notes\p1_logdet_ci_multiplier_reduction_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The RSA benchmark note proves:

```text
K^B[(Tr C_t)^p] <= C_p
```

for fixed `p`, uniformly in `d`, `tau`, and the deleted-row spectrum.  It
also proves conditional Haar contractions for `Q_2`, `Q_4`, and the mixed
cubic residual words.  Since the Gaussian determinant tilt is spectral, the
residual eigenbasis is Haar conditional on eigenvalues, and the note proves
the Gaussian benchmark

```text
E mathcal R_4 <= C d^-1 P_4,
E mathcal R_3 <= C d^-1(1+P_3).
```

The non-Gaussian `(RSA)` gap is now exactly the determinant-tilted residual
orientation theorem with summable cap errors.

Updated current sharp blockers:

```text
P2: prove NQSD(r).

P1: prove the non-Gaussian determinant-tilted residual orientation theorem;
    prove (NCR_K)/(WNR_K) for the near-zone post-cancellation kernel;
    track the actual CI coefficient and step-dependent frames against the
    finite cap Laplace window.
```

## Continuation update, NQSD closure and P1 finite-test blockers, 2026-06-30

Five Codex agents were assigned to the current blockers, with one foreground
support-family audit added.  All five returned artifacts.  No background
processes, daemons, scheduled tasks, or launchers were created.

New P2 artifacts:

- `notes\all_apex_square_zero_fresh_nqsd_proof_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_nqsd_r4_audit_2026_06_30.md`
- `notes\all_apex_square_zero_fresh_nqsd_support_family_audit_2026_06_30.md`
- `numerics\square_nqsd_support_audit.py`
- `numerics\square_nqsd_support_family_foreground.py`

Updated P2 artifacts:

- `notes\all_apex_square_zero_fresh_arrangement_endpoint_lemma_2026_06_30.md`
- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`
- `notes\all_apex_square_pair_palm_cluster_program_2026_06_30.md`

The saturated-atlas P2 endpoint blocker is now closed.  The proof note shows
that for the saturated exact labelled incidence building set:

```text
no witness -> positive current quotient modular defect
            -> saturated rank-defect center
            -> extra m-O_r(1) normal block.
```

Thus

```text
NQSD(r) closed -> LBV(r) -> LC7.
```

If a smaller non-saturated atlas is used, the residual finite fact is
`SCDE(r)`, the saturated current defect exposure property.  The r=4 audit
found `241` labelled minimal no-witness families, `40` symmetry classes, and
identified `u123|v12|v3` as the first genuinely nested support pattern that
tests the current-vs-ancestor clause.

New P1 artifacts:

- `notes\p1_logdet_orientation_theorem_route_2026_06_30.md`
- `notes\p1_logdet_wnr_edgeworth_remainder_2026_06_30.md`
- `notes\p1_logdet_ci_window_and_step_profile_2026_06_30.md`

Updated P1 artifacts:

- `notes\p1_logdet_ci_multiplier_reduction_2026_06_30.md`
- `notes\p1_logdet_he_rem_hard_edge_2026_06_30.md`
- `notes\p1_logdet_positive_increment_cap_moment_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The non-Gaussian RSA orientation blocker is now the finite `DOT_6` theorem.
The exact tests are:

```text
T_Q2, T_Q4, T_B2, T_C4, T_D6.
```

The orientation note proves `DOT_6 => RSA => CI-logdet` and reduces
admissible product laws to `GC-act`, `GC-H`, and summable cap errors `CAP_6`.

The near-zone remainder route is parity-corrected.  Unprojected `(WNR_K)` is
too strong because an odd cubic kernel has positive part even though it pairs
to zero against the even log-det test.  The useful strong sufficient theorem
is `(WNR_K^ev)`, equivalently a Gaussian-smoothed weighted Edgeworth/Hermite
remainder theorem `(GEW_K)/(HER_K)`; otherwise one should prove `(NCR_K)`
directly with the determinant tilt and even test retained.

The coefficient/window note records that current notes only determine
`a_CI` symbolically.  The homogeneous cap window is

```text
p a_CI < 1/(3a_r),       a_r=192 r^2/(1+r^2),
```

up to profile constants.  Step-dependent profiles are reduced to
`StepStaticAvg` and `StepApexColumnExp`.

Verification:

```powershell
python -m py_compile numerics\square_nqsd_support_family_foreground.py
python numerics\square_nqsd_support_family_foreground.py --r-max 4 --max-family-size 6 --show 6
python numerics\square_nqsd_support_family_foreground.py --r-max 5 --max-family-size 5 --show 0
python -m py_compile numerics\square_nqsd_support_audit.py
python numerics\square_nqsd_support_audit.py --j 4
```

Current sharp blockers:

```text
P2: assemble the saturated-atlas fixed-r endpoint closure into the final
    zero-fresh cluster theorem, or prove SCDE(r) if a smaller atlas is kept.

P1: prove GC-act/GC-H/CAP_6 for the five DOT_6 tests; prove direct NCR_K
    or a strong even-kernel GEW/HER theorem after enough even terms are
    removed; bound a_CI and prove StepStaticAvg/StepApexColumnExp for the
    determinant-tilted row-replacement chain.
```

## Continuation update, fixed-r endpoint assembly and finite P1 blockers, 2026-06-30

Five Codex agents were assigned to the next disjoint blockers, and one
foreground diagnostic was added.  All five returned artifacts.  No
background processes, daemons, scheduled tasks, or launchers were created.

New P2 artifact:

- `notes\all_apex_square_zero_fresh_fixed_r_endpoint_closure_2026_06_30.md`

Updated P2 artifact:

- `notes\all_apex_square_small_fresh_cluster_assembly_2026_06_30.md`

The fixed-`r` zero-fresh endpoint-excluded theorem is now assembled for the
saturated exact labelled incidence atlas `G_r^sat`.  The closed path is:

```text
G_r^sat
  -> NQSD(r)
  -> LBV(r)
  -> LC7
  -> LC1-LC7
  -> endpoint chart estimate (E-r)
  -> exact zero-Palm tuple bound
  -> finite-threshold pair-Palm tuple bound
  -> endpoint-excluded zero-fresh fixed-r theorem (Z0-r).
```

For a smaller non-saturated atlas, the exact residual finite assertion is
still `SCDE(r)`.  No Shearer, pair-Palm, determinant-weight, or threshold
transfer input is reopened by that atlas choice.

New P1 artifacts:

- `notes\p1_logdet_dot6_gc_comparison_program_2026_06_30.md`
- `notes\p1_logdet_direct_ncr_test_class_2026_06_30.md`
- `notes\p1_logdet_ci_coefficient_ledger_2026_06_30.md`
- `notes\p1_logdet_step_frame_avg_program_2026_06_30.md`
- `notes\p1_logdet_step_frame_avg_probe_2026_06_30.md`
- `numerics\p1_step_frame_avg_probe.py`

Updated P1 artifacts:

- `notes\p1_logdet_orientation_theorem_route_2026_06_30.md`
- `notes\p1_logdet_ci_multiplier_reduction_2026_06_30.md`
- `notes\p1_logdet_wnr_edgeworth_remainder_2026_06_30.md`
- `notes\p1_logdet_he_rem_hard_edge_2026_06_30.md`
- `notes\p1_logdet_ci_window_and_step_profile_2026_06_30.md`
- `notes\p1_logdet_positive_increment_cap_moment_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The `DOT_6` orientation blocker is sharpened.  `GC-H` is closed by the
pathwise same-spectrum Haar benchmark and cap profile summability.  The
active comparison is reduced to `FGC_6-act`, a secondary deleted-row exchange
theorem for the centered determinant-tilted observables

```text
Gamma_a,theta(C,x;z)=N_a(B(C,x),z)-theta M(B(C,x)),
a in {Q2,Q4,B2,C4,D6}.
```

The resulting implication chain is:

```text
FGC_6-act -> GC-act + GC-H + CAP_6 -> DOT_6 -> RSA -> CI-logdet.
```

The hard-edge near-zone route is now the direct test-class theorem
`NCR_K^dir`.  Keeping the cutoff log-det test inside the determinant-tilted
average cancels the hard-edge normalizer before the positive part:

```text
E_{Pi_i} [ <Psi_B^c,k> ]_+
 = Z_i^(-1) E_{P_i} F_B [ J_B^c(k) ]_+.
```

Thus:

```text
DTC_K-fin + DTC_K-tail -> NCR_K^dir -> HE_near(K).
```

This bypasses the too-strong global positive-density theorem `(WNR_K^ev)`.
The same-spectrum Haar benchmark for the sixth-cumulant word is only
`O(d^-2)` per row for the direct cutoff log-det pairing.

The coefficient window is now canonical:

```text
a_CI =
  (|kappa_4|/24) M_4^sigma R_4
  + (kappa_3^2/72) M_33^- R_3,

gamma_d = (2d+1)/d = 2 + 1/d,
a_r = 192 r^2/(1+r^2),

gamma_d p h a_CI < 1/a_r.
```

The old `3 p h a_CI < 1/a_r` condition is only the dimension-uniform
rounding `gamma_d<=3`.

The step-frame route is also isolated.  The Gaussian determinant-tilted
tilted-mean version follows from spectral/Haar invariance.  For admissible
non-Gaussian rows, the new comparison target is `SFC_beta`, comparing

```text
sum_k ||w_k||_4^4
and
exp(beta(d||p||_4^4+9))
```

to homogeneous Haar-frame expectations with summable step-averaged errors.
The new probe `p1_step_frame_avg_probe.py` gives the Haar normalization for
`S_av`, `L_av`, `M_i`, `Q_av`, and the Jensen apex-column bound.

Verification:

```powershell
python -m py_compile numerics\p1_step_frame_avg_probe.py numerics\p1_quartic_cap_chaos_probe.py numerics\square_nqsd_support_audit.py numerics\square_nqsd_support_family_foreground.py
python numerics\p1_step_frame_avg_probe.py --m-values 24 --d-values 6 --step-counts 3 5 --radii 1 --collections 2 --z-samples 16 --etas 0.001 --seed 20260630
python -B numerics\p1_quartic_cap_chaos_probe.py --m-values 24 --d-values 6 --radii 1 --frames 1 --z-samples 8 --lambdas 0.001 --seed 20260630
python numerics\square_nqsd_support_audit.py --j 4
rg -n 'fixed-r endpoint|Z0-r|FGC_6-act|NCR_K\^dir|DTC_K-fin|DTC_K-tail|gamma_d|SFC_beta|p1_step_frame_avg_probe|StepApexColumnExp|a_CI|SCDE\(r\)' notes numerics '..\Open problem project\five_agent_plan_2026_06_30.md' -g '*.md' -g '*.py'
```

The step-frame smoke rows were finite; for example at `m=24,D=6,r=1`,
`step_count=3` gave `mean_Q_av=5.660035e-01`,
`log_mgf_eta_0.001=5.660047e-04`, and
`jensen_log_bound_eta_0.001=1.053780e-02`.  The quartic cap-chaos smoke
again gave `log_mgf_lambda_0.001=5.577228e-04` with proof log bound
`1.052968e-02`.  The r=4 NQSD audit again reported `241` labelled minimal
no-witness families and `40` symmetry classes.

Current sharp blockers:

```text
P2: for the saturated atlas, the fixed-r zero-fresh endpoint-excluded input
    is assembled.  If a smaller atlas is required, prove SCDE(r).  Outside
    this endpoint-excluded zero-fresh bulk, continue the already routed
    close-endpoint, fixed-small-D, and fresh-sector work.

P1: prove FGC_6-act for the five DOT_6 tests; generate the exact even
    post-cancellation word list and prove DTC_K-fin/DTC_K-tail for
    NCR_K^dir; bound M_4^sigma, M_33^-, R_4, R_3, and any Holder loss h so
    gamma_d p h a_CI lies inside the cap window; prove SFC_beta for
    non-Gaussian determinant-tilted step frames.
```

## Continuation update, finite P1 subtheorems split, 2026-06-30

Five Codex agents were assigned to disjoint P1 finite blockers, and one
foreground coefficient-window utility was added.  All five returned
artifacts.  No background processes, daemons, scheduled tasks, or launchers
were created.

New P1 artifacts:

- `notes\p1_logdet_fgc6_q2_q4_haar_benchmark_2026_06_30.md`
- `notes\p1_logdet_fgc6_b2_c4_d6_connected_benchmark_2026_06_30.md`
- `notes\p1_logdet_direct_ncr_even_word_list_2026_06_30.md`
- `notes\p1_logdet_direct_ncr_tail_theorem_2026_06_30.md`
- `notes\p1_logdet_sfc_beta_leverage_tail_2026_06_30.md`
- `notes\p1_logdet_ci_window_budget_probe_2026_06_30.md`
- `numerics\p1_edgeworth_word_list.py`
- `numerics\p1_ci_window_budget.py`

Updated P1 artifacts:

- `notes\p1_logdet_dot6_gc_comparison_program_2026_06_30.md`
- `notes\p1_logdet_direct_ncr_test_class_2026_06_30.md`
- `notes\p1_logdet_he_rem_hard_edge_2026_06_30.md`
- `notes\p1_logdet_step_frame_avg_program_2026_06_30.md`
- `notes\p1_logdet_ci_coefficient_ledger_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

The `FGC_6-act` blocker has been split into Haar-benchmark pieces and
actual-minus-Haar leftovers.

For the quartic tests `Q2,Q4`, the same-spectrum Haar side has scale

```text
d^(-2) K4Prof(z,W) A_a(z,W)
  + |theta| d^(-1) K4Prof(z,W)
```

per secondary exchange, and the remaining theorem is the positive
actual-minus-Haar comparison `Q24-FGC4-act`.

For the connected cubic-square tests `B2,C4,D6`, the linear cubic term is
exactly zero by parity for `Gamma_a,theta=N_a-theta M`.  The same-spectrum
Haar side has scale

```text
d^(-2) [1+P_3(q_z,W)]
  + |theta| d^(-1) [1+P_3(q_z,W)].
```

The remaining theorem is the positive leftover

```text
Main33^act - Main33^H.
```

The direct NCR word list is now explicit under the Hermite-degree truncation
convention:

```text
A_6 = {P_6}.

A_8^min = {P_6, P_35, P_44, P_8}.

A_8 with all even words through degree 8 signed-removed:
  empty at degree <=8; the next visible layer starts at degree 10.
```

The reusable enumerator is `numerics\p1_edgeworth_word_list.py`.

The direct NCR tail theorem proves the determinant-tilted cancellation for
absolute tail pairings and reduces `(DTC_K-tail)` to `(SCT_K-tail)`, a
row-law weighted physical tail estimate.  The required scales are:

```text
near Taylor tail:       per-row O(d^-1),
Fourier complement:     per-row O(d^-2).
```

The step-frame comparison is reduced to:

```text
DTS_4 + ITL_beta -> SFC_beta.
```

Here `DTS_4` is the finite determinant-tilted comparison for
`G_S=sum_k||w_k||_4^4`, while `ITL_beta` is the integrated positive leverage
tail comparison for `M_i=d||p_i||_4^4`.  A stronger pointwise theorem
`DTLT_beta(c0,delta)` implies `ITL_beta` by the exact integration-by-tail
identity.

The foreground coefficient utility evaluates

```text
gamma_d p h a_CI < 1/a_r
```

for supplied cumulants and constants.  Unit placeholder constants already
show that the window can fail at radius `r=1` for non-Gaussian laws, so the
constants `M_4^sigma`, `M_33^-`, `R_4`, `R_3`, and `h` must be quantified,
not merely shown finite.

Verification commands for this round:

```powershell
python -m py_compile numerics\p1_ci_window_budget.py numerics\p1_edgeworth_word_list.py
python numerics\p1_ci_window_budget.py --laws gaussian uniform beta25 --d-values 8 --radii 0.5 1 --p 1.05 --holder 1 --m4-plus 1 --m4-minus 1 --m33-minus 1 --r4 1 --r3 1
python numerics\p1_ci_window_budget.py --laws uniform beta25 --d-values 8 --radii 0.5 1 --p 1.05 --holder 1 --m4-plus 0.02 --m4-minus 0.02 --m33-minus 0.02 --r4 1 --r3 1
python numerics\p1_edgeworth_word_list.py --k-values 6 8 --max-part 8 --signed-preset minimal --only all
python numerics\p1_edgeworth_word_list.py --k-values 8 --signed-preset k8-even --only remainder
python numerics\p1_edgeworth_word_list.py --k-values 10 --max-part 8 --signed-preset k8-even --only remainder
rg -n 'Q24-FGC4-act|Main33\\^act|DTS_4|ITL_beta|DTLT_beta|SCT_K-tail|A_6 =|A_8|p1_ci_window_budget|p1_edgeworth_word_list' notes numerics '..\Open problem project\five_agent_plan_2026_06_30.md' -g '*.md' -g '*.py'
```

Current sharp blockers:

```text
P1/F(GC):
  prove Q24-FGC4-act for Q2/Q4;
  prove the Main33 actual-minus-Haar leftover for B2/C4/D6;
  prove the centered post-cancellation remainder comparison for the same
  secondary observables.

P1/NCR:
  choose the K=8 signed convention;
  prove DTC_K-fin for A_K;
  prove SCT_K-tail for the exact analytic remainder.

P1/window:
  quantify M_4^sigma, M_33^-, R_4, R_3, and Holder loss h enough to pass
  gamma_d p h a_CI < 1/a_r.

P1/steps:
  prove DTS_4 and ITL_beta, or the stronger DTLT_beta, for determinant-
  tilted non-Gaussian step frames.

P2:
  saturated-atlas fixed-r zero-fresh endpoint-excluded input remains
  assembled; smaller-atlas work is exactly SCDE(r), and routed fresh/close
  sectors remain outside this endpoint-excluded bulk.
```

## Continuation update, five-agent P1 finite reductions, 2026-06-30

Five Codex agents were assigned to the current P1 finite blockers and all
returned artifacts.  A foreground step-frame diagnostic was added.  No
background processes, daemons, scheduled tasks, or launchers were created.

New artifacts from this round:

- `notes\p1_logdet_q24_fgc4_actual_comparison_2026_06_30.md`
- `notes\p1_logdet_main33_leftover_comparison_2026_06_30.md`
- `notes\p1_logdet_dtc_fin_even_words_2026_06_30.md`
- `notes\p1_logdet_sct_tail_row_law_theorem_2026_06_30.md`
- `notes\p1_logdet_dts4_static_quartic_comparison_2026_06_30.md`
- `notes\p1_logdet_sfc_beta_tail_probe_2026_06_30.md`
- `numerics\p1_sfc_beta_tail_probe.py`
- `notes\p1_logdet_ci_window_thresholds_2026_06_30.md`
- `numerics\p1_ci_window_thresholds.py`

Updated route notes:

- `notes\p1_logdet_dot6_gc_comparison_program_2026_06_30.md`
- `notes\p1_logdet_direct_ncr_test_class_2026_06_30.md`
- `notes\p1_logdet_step_frame_avg_program_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`

Finite reductions now recorded:

```text
Q24-FGC4-act:
  reduced to LC4-N(Q2), LC4-N(Q4), LC4-M, and theta control.

Main33 actual-minus-Haar:
  theta-free after quotient centering; reduced to O_B2, O_C4, O_D6.

DTC_K-fin:
  same-spectrum Haar side closed for P_6, P_35, P_44, P_8 with scales
  O(d^-2), O(d^-2), O(d^-2), O(d^-3);
  actual side is AHC_alpha for the chosen finite list.

DTC_K-tail:
  SCT_K-tail follows from FC_K + HER_tail_K + VT_p.

DTS_4:
  SQ4-FGC-act -> DTS_4 for G_S=sum_k||w_k||_4^4, with Haar benchmark
  E_H G_S=3d/(m+2).

SFC_beta:
  DTS_4 + ITL_beta remains the step-frame route; the new tail probe checks
  non-tilted product-frame and Haar normalizations for M, G_S, and
  exp(beta(M+9)).
```

Current sharp P1 blockers:

```text
1. Prove LC4-N(Q2), LC4-N(Q4), and LC4-M with cap-summable positive
   leftovers and theta control.
2. Prove O_B2, O_C4, and O_D6 for the connected cubic-square leftover.
3. Prove the centered post-cancellation Cramer/hard-edge remainder for the
   same secondary observables.
4. Choose the K=8 signed convention and prove AHC_alpha for A_K.
5. Prove FC_K, audit HER_tail_K, and verify VT_p for SCT_K-tail.
6. Prove SQ4-FGC-act and ITL_beta, or the stronger DTLT_beta, for
   determinant-tilted non-Gaussian step frames.
7. Quantify M_4^sigma, M_33^-, R_4, R_3, and Holder loss h enough to pass
   gamma_d p h a_CI < 1/a_r.
```

Verification commands for this round:

```powershell
python -m py_compile numerics\p1_sfc_beta_tail_probe.py
python numerics\p1_sfc_beta_tail_probe.py --laws gaussian uniform beta25 --m-values 24 --d-values 6 --frames 12 --betas 0.001 0.005 --tail-thresholds 0.5 1 2 --seed 20260630
rg -n 'LC4-N|LC4-M|O_B2|O_C4|O_D6|AHC_alpha|HER_tail_K|SCT_K-tail|SQ4-FGC-act|DTS_4|p1_sfc_beta_tail_probe' notes numerics '..\Open problem project\five_agent_plan_2026_06_30.md' -g '*.md' -g '*.py'
```

## Continuation update, coefficient-threshold inversion, 2026-06-30

The foreground coefficient-window work added an inverse calculator:

```text
numerics\p1_ci_window_thresholds.py
notes\p1_logdet_ci_window_thresholds_2026_06_30.md
```

It rewrites the cap condition in terms of the two unknown products

```text
X4  = M_4^sigma R_4,
X33 = M_33^- R_3,

a_CI = (|kappa_4|/24) X4 + (kappa_3^2/72) X33.
```

The utility reports `max_a_CI`, one-line thresholds for `X4` and `X33`, and
the common-product threshold under `X4=X33`.

Representative output at `d=8`, `p=1.05`, `h=1`, `r=1`:

```text
uniform:
  max_a_CI=4.668534e-03,
  max_X4_if_X33_zero=9.337068e-02.

beta25:
  max_a_CI=4.668534e-03,
  max_X4_if_X33_zero=9.337068e-01,
  max_X33_if_X4_zero=9.452756e-01,
  max_common_X4_eq_X33=4.697103e-01.
```

Thus the coefficient blocker now has explicit proof targets for the signed
multiplier/RSA product sizes.

Verification:

```powershell
python -m py_compile numerics\p1_ci_window_thresholds.py
python numerics\p1_ci_window_thresholds.py --laws gaussian uniform beta25 --d-values 8 --radii 0.5 1 --p 1.05 --holder 1 --target-common-product 1
python numerics\p1_ci_window_thresholds.py --laws uniform beta25 --d-values 8 32 --radii 0.25 0.5 1 --p 1.01 --holder 1 --target-common-product 0.02
```

## Continuation update, next finite P1 blockers, 2026-06-30

Five Codex agents were assigned to the next layer of finite P1 blockers and
all returned new ASCII-only notes.  No background processes, daemons,
scheduled tasks, or launchers were created.

New artifacts:

- `notes\p1_logdet_lc4_numerator_orientation_2026_06_30.md`
- `notes\p1_logdet_lc4_determinant_centering_2026_06_30.md`
- `notes\p1_logdet_o_b2_c4_d6_orientation_defects_2026_06_30.md`
- `notes\p1_logdet_ahc_alpha_finite_comparison_2026_06_30.md`
- `notes\p1_logdet_sct_tail_fc_her_vt_audit_2026_06_30.md`

Updated route notes:

- `notes\p1_logdet_q24_fgc4_actual_comparison_2026_06_30.md`
- `notes\p1_logdet_dot6_gc_comparison_program_2026_06_30.md`
- `notes\p1_logdet_direct_ncr_test_class_2026_06_30.md`
- `notes\p1_linear_aspect_logdet_universality_route_2026_06_30.md`
- `notes\p1_density_ratio_transfer_target_2026_06_30.md`
- `notes\p1_logdet_ci_coefficient_ledger_2026_06_30.md`

New finite names and reductions:

```text
LC4 numerator:
  DeltaN4_a = DeltaN4_a^ani + DeltaN4_a^scal.
  Open inputs:
    ROA4-N-ani(Q2), ROA4-N-scal(Q2),
    ROA4-N-ani(Q4), ROA4-N-scal(Q4).

LC4 determinant centering:
  DeltaM4=F_C D_M(C;K4_z^perp)/24.
  Open input:
    LC4-M-det, the centered squared-leverage estimate at one-row scale
    d^-1, made triangular by theta=O(d^-1).

Main33 connected:
  Open input:
    ROA33(B2,C4,D6), the positive-part cap summability of the three signed
    connected Hermite pairings O_B2,O_C4,O_D6.

Direct finite NCR:
  Open input:
    FAHC-act for the quotient-centered positive numerator
    Gamma_alpha,theta^+.
  Then:
    FAHC-act -> AHC-fin -> DTC_K-fin.

Direct tail:
  Exact Fourier complement symbol C_FC,K,i,z,B is recorded.
  HER_tail_K audit:
    K=6 through degree 8: {3+5,4+4,8}.
    K=8 through degree 10: {3+3+4,3+7,4+6,5+5}, plus {10} if the tenth
    cumulant is included.
  Open input:
    FC_K + HER_tail_K + VT_p.
```

Updated current sharp P1 blockers:

```text
1. Prove ROA4-N-ani/scal for Q2 and Q4.
2. Prove LC4-M-det and the Q2/Q4 theta bootstrap.
3. Prove ROA33(B2,C4,D6).
4. Prove FAHC-act for P_6,P_35,P_44,P_8.
5. Choose the K=8 signed convention and close FC_K/HER_tail_K/VT_p.
6. Prove SQ4-FGC-act and ITL_beta or DTLT_beta for step frames.
7. Prove signed multiplier/RSA constants small enough for the threshold
   utility's X4/X33 cap-window targets.
```

## Continuation update, K=8 direct convention fixed, 2026-06-30

The foreground direct NCR work fixed the main `K=8` signed convention in

```text
notes\p1_logdet_k8_signed_convention_decision_2026_06_30.md
```

The working convention is minimal signed removal:

```text
P_sign=P_4+P_33,
A_8^min={P_6,P_35,P_44,P_8}.
```

Full even signed removal through degree `8` is kept only as an optional
strengthening, because it would require signed quotient comparison for
`P_6,P_35,P_44,P_8`.  Under the main convention, those words remain finite
positive direct tests:

```text
FAHC-act -> AHC-fin -> DTC_8-fin.
```

The first analytic tail audit after `A_8^min` is the degree-ten layer:

```text
{P_334,P_37,P_46,P_55}
```

plus `P_10` if a tenth-cumulant assumption is included.

Enumerator checks:

```powershell
python numerics\p1_edgeworth_word_list.py --k-values 8 --max-part 10 --signed-preset minimal --only remainder --format csv
python numerics\p1_edgeworth_word_list.py --k-values 8 --max-part 10 --signed-preset k8-even --only remainder --format csv
python numerics\p1_edgeworth_word_list.py --k-values 10 --max-part 10 --signed-preset k8-even --only remainder --format csv
python numerics\p1_edgeworth_word_list.py --k-values 10 --max-part 8 --signed-preset k8-even --only remainder --format csv
```

## Continuation update, theta/anisotropy/FAHC/DTLT refinements, 2026-06-30

New artifacts returned or added in this pass:

- `notes\p1_logdet_q24_theta_bootstrap_2026_06_30.md`
- `notes\p1_logdet_roa4_anisotropic_q2_q4_route_2026_06_30.md`
- `notes\p1_logdet_fahc_kink_smoothing_2026_06_30.md`
- `notes\p1_logdet_dtl_beta_leverage_tail_route_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`

Finite reductions:

```text
Q24 theta:
  theta_i,j,Q2=R_i,j-1,Q2 and theta_i,j,Q4=R_i,j-1,Q4 are nonnegative.
  Gaussian start is closed at C d^-1 Pi_4.
  Discrete bootstrap:
    R_j <= (1+B_j)R_j-1 + A_j.
  Open: bound sum B_j, prove admissible exponential theta error, or prove a
  direct partial-law quotient/RSA estimate.

ROA4-N-ani:
  exact residual-basis word forms R_2(beta) and R_4(beta,gamma) are fixed.
  Open: prove the signed positive-part orientation theorem after the
  K4/Gaussian/Laplace pairing.

FAHC:
  positive-part kink reduced to FAHC-act-smooth plus small-ball/sign-gap
  estimates SB_i,j,alpha,q for alpha in {P_6,P_35,P_44,P_8}.

DTLT_beta:
  DTLT_beta(c0,delta) implies ITL_beta with loss
  L_H(c0 beta)-L_H(beta)+Delta_delta(beta).
  Open: prove DTL-FGC-tail_beta and its exponentially weighted defect
  budget.
```

Scalar ROA4 update:

```text
ROA4-N-scal(Q2/Q4) is now ROA4-N-scal-det(Q2/Q4):
  a weighted Schur determinant-kernel theorem with spectral weights
  psi_Q2 and psi_Q4.

It is not implied by current LC4-M-det.  LC4-M-det is the unweighted
denominator square-root kernel after two-row symmetrization; the scalar
numerator pieces keep the single-row Laplace-Schur kernel with psi_Q2 or
psi_Q4 inserted.
```

## Continuation update, five-agent frontier refinements, 2026-06-30

Five Codex agents were assigned to the next P1 frontier layer.  All returned
new ASCII-only theorem notes.  The foreground pass added a DTLT beta window
bookkeeping utility.  No background processes, daemons, scheduled tasks, or
launchers were created.

New artifacts:

- `notes\p1_logdet_q24_theta_multiplier_budget_2026_06_30.md`
- `notes\p1_logdet_roa4_scalar_weighted_kernel_theorem_2026_06_30.md`
- `notes\p1_logdet_fahc_small_ball_layers_2026_06_30.md`
- `notes\p1_logdet_her_tail_degree10_audit_2026_06_30.md`
- `notes\p1_logdet_dtl_fgc_tail_beta_theorem_2026_06_30.md`
- `notes\p1_logdet_dtlt_beta_window_probe_2026_06_30.md`
- `numerics\p1_dtlt_beta_window.py`

Updated navigation:

- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`

Sharper reductions:

```text
Q24 theta:
  one-step recurrence now has exact A_i,j,a and B_i,j envelopes.
  The accumulated multiplier has the form
    sum B <= a_theta Pi_4 + Beta.
  Exponential-profile closure is reduced to the cap check
    gamma_d p h (a_CI+a_theta+rho) < 1/a_r
  plus weighted Alpha/Beta error budgets or a direct partial-law RSA bound.

ROA4-N-scal-det:
  scalar Q2/Q4 pieces are exact signed weighted Schur determinant kernels:
    psi_Q2(Y) = [Tr H_2/d] Tr Y,
    psi_Q4(Y) = [B_4/(d(d+2))][(Tr Y)^2 + 2 Tr(Y^2)].
  Current LC4-M-det still does not imply these single-row weighted kernels.

FAHC-act-smooth:
  kink layers reduce to profile small-ball/sign-gap estimates
    SB_i,j,P6,q, SB_i,j,P35,q, SB_i,j,P44,q, SB_i,j,P8,q,
    q=2,...,L_E.
  Ordinary scalar anti-concentration closes only q=2; q>=3 needs weighted
  density vanishing, sign gaps, or a lower-order smoothing proof.

HER_tail_K:
  post-A_8 degree-ten audit has exact tensors for
    P_334, P_37, P_46, P_55,
  plus optional P_10.  Any word left in the analytic tail needs
    ||T_beta||_HS <= C d^-3/2.
  Generic product-coordinate cumulant sizes are too large, so surviving
  words must be zero, extracted to A_10, moved into an enlarged signed
  polynomial, or proved HS-small by a new cancellation theorem.

DTL-FGC-tail_beta:
  exact smoothed threshold quotient identity is fixed.
  The needed theorem is a signed local Edgeworth comparison for
  Gamma_{u,s,theta}, with exponentially weighted defect budget.
  Gaussian/Haar close at c0=1 and zero defect; bounded product-coordinate
  laws remain open from current inputs.

DTLT beta window:
  numerics\p1_dtlt_beta_window.py reports eta, beta, c0 beta, exact
  a_H,d Haar-window ceilings, optional rounded a_sph=128 theta_plus
  ceilings, and the reference inflation L_H(c0 beta)-L_H(beta).
```

Current next split should prioritize:

```text
1. Q24 Alpha/Beta exponential budgets and the theta cap coefficient
   a_theta.
2. Signed weighted Schur determinant-kernel proof for ROA4-N-scal-det.
3. FAHC smoothing order decision: close L_E=2 or prove q>=3 weighted
   vanishing/sign-gap estimates.
4. Degree-ten extraction decision for HER10-audit.
5. Product-law DTL-FGC-tail_beta signed threshold comparison at the beta
   allowed by the cap/Haar windows.
```

## Continuation update, next-layer route decisions, 2026-06-30

Five Codex agents were assigned to the prioritized next split above.  All
returned new ASCII-only notes.  The foreground pass added a combined
cap/theta/Haar window calculator.  No background processes, daemons,
scheduled tasks, or launchers were created.

New artifacts:

- `notes\p1_logdet_q24_alpha_beta_budget_theorem_2026_06_30.md`
- `notes\p1_logdet_wroa4_kernel_proof_attempt_2026_06_30.md`
- `notes\p1_logdet_fahc_le2_smoothing_decision_2026_06_30.md`
- `notes\p1_logdet_her10_extraction_strategy_2026_06_30.md`
- `notes\p1_logdet_dtl_threshold_edgeworth_budget_2026_06_30.md`
- `notes\p1_logdet_combined_cap_theta_window_2026_06_30.md`
- `numerics\p1_combined_cap_theta_window.py`

Updated navigation:

- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`

Route decisions and sharper blockers:

```text
AB-Q24:
  The sharp current theta coefficient is
    a_theta(i,j)=((j-1)/d)b_theta,
    a_theta(m,d)=((m-1)/d)b_theta,
    a_theta<=theta_-^(-1)b_theta.
  If Beta has a profile split, its coefficient b_B joins the same cap
  ledger:
    gamma_d p h (a_CI+a_theta+b_B+rho) < 1/a_r.
  Alpha remains additive and needs AB-Alpha unless it has polynomial
  domination.  Beta needs AB0/AB-Beta unless profile-dominated.

Combined cap/theta/Haar window:
  numerics\p1_combined_cap_theta_window.py reports the remaining a_CI
  after reserving a_theta+b_B+rho, converts it to X4/X33 thresholds, and
  checks the exact or rounded Haar c0 beta window.

ROA4-N-scal-det:
  The WROA4 proof attempt closes Schur normal form, the fourth-chaos tensor
  representation, fixed-spectrum Haar rotation reduction, and t-derivative
  identities for p=L and p=L^2+2S_2.
  The remaining core is:
    KCB[p]: no-tau-loss Schur chaos coefficient bounds;
    KOT[p]: one-kernel determinant-tilted orientation comparison.

FAHC:
  Main route is L_E=2, conditional on proving the local comparison in
  Hermite-kernel form.  Remaining layer theorem is BD-RL3-C2 bounded
  weighted density for active finite words.  Generic q>=3 small-ball is
  demoted to fallback only if a future proof differentiates the smoothed
  positive part through higher order.

HER10:
  Default route for generic product-coordinate laws is finite direct
  extraction:
    A_10^dir={P_334,P_37,P_46,P_55},
  plus optional P_10 if the tenth cumulant is included and nonzero.
  HS10 and enlarged P_sign^(10) are special/non-default routes.

DTL:
  Pointwise DTLT_beta still needs TLOC_tail_beta, a signed distributional
  shell theorem; ordinary absolute smooth-threshold Edgeworth loses
  s^(1-r) after beta integration.
  A weaker direct apex route Lap-FGC_beta is now isolated: integrate in
  beta before differentiating, replacing s-losses by beta^r exp(beta M),
  yielding a direct Laplace/apex comparison if the top proof accepts it.
```

Current next split should prioritize:

```text
1. KCB[p] fourth-chaos coefficient bounds for p=L and p=L^2+2S_2.
2. KOT[p] determinant-tilted one-kernel orientation comparison.
3. BD-RL3-C2 for the L_E=2 FAHC route, including the selected A_10^dir
   words.
4. A_10^dir direct comparison and FC_K leakage update.
5. Decide whether to alter the top step-frame proof to accept Lap-FGC_beta;
   if not, prove TLOC_tail_beta signed distributional shell estimates.
```

## Continuation update, mixed P1/P2 frontier pass, 2026-06-30

Five Codex agents were assigned to a mixed package: three P1 log-det blockers
and two P2 all-apex square assembly blockers.  All returned new ASCII-only
notes.  The foreground pass verified P2 scripts and patched the singular
`D=2` swap-core density diagnostic.  No background processes, daemons,
scheduled tasks, or launchers were created.

New/updated P1 artifacts:

- `notes\p1_logdet_kcb_schur_coefficient_bounds_2026_06_30.md`
- `notes\p1_logdet_kot_orientation_comparison_2026_06_30.md`
- `notes\p1_logdet_a10_direct_comparison_theorem_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`

New/updated P2 artifacts:

- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`
- `notes\all_apex_square_remaining_sectors_2026_06_30.md`
- `notes\all_apex_square_p2_verification_snapshot_2026_06_30.md`
- `numerics\p2_swap_core_density.py`

P1 updates:

```text
KCB[p]:
  Not closed in full.  Reduced to KCB-Schur-Laguerre[p], a fixed-spectrum
  no-tau Schur-Laguerre coefficient lemma, equivalently Taylor-centered
  tensor estimates TCSL-1/TCSL-2.  The naive derivative proof loses tau
  exactly when separate x-derivative terms are absolutized before the
  Hermite projection.  Zero/isotropic, fixed-positive-tau, and rank-one
  coefficient cases are closed.

KOT[p]:
  Reduced to OKOT_2, the minimal two-kernel conditional orientation theorem
  for p=L and p=L^2+2S_2.  Gaussian/right-invariant, spectral, and
  high-randomness orientation cases are closed.  A rank-one hard-edge model
  rules out deterministic fixed-C Haar-scale comparison.

A_10^dir:
  DTC_8-fin(A_8^min cup A_10^dir) is now stated explicitly with active
  degree-ten tests P_334, P_37, P_46, P_55 and optional P_10.  The new
  pairings have residual degree five, the FAHC/BD-RL3-C2 obligations are
  listed, and the Fourier complement is updated to C_FC,8,A10.
```

P2 updates:

```text
Saturated-atlas route:
  The current P2 DAG is now explicit.  Under the saturated exact labelled
  incidence atlas G_r^sat, the endpoint-excluded zero-fresh fixed-r input is
  closed.  If a smaller atlas is chosen, the exact optional finite assertion
  is SCDE(r).

Remaining sectors:
  The close-endpoint, fixed-small-D, and fresh-sector packages are closed at
  assembly level under the saturated atlas convention.  They still need to
  be cited as route packages in the final cluster assembly, but they are not
  new analytic inputs.

Verification:
  all_apex_pair_class_counts.py, fixed_apex_poisson_moments.py,
  p2_swap_core_density.py, square_nqsd_support_audit.py, and
  square_nqsd_support_family_foreground.py compile.  The P2 verification
  snapshot records current pair-class summaries, NQSD j=4 support counts,
  fixed-apex moment envelope, and swap-core density values.

Diagnostic fix:
  p2_swap_core_density.py now reports D=2 and D=3 singular buckets as
  infinite instead of crashing at D=2.
```

Current next split should prioritize:

```text
P1:
1. Prove KCB-Schur-Laguerre[p] / TCSL-1/TCSL-2 for general spectra.
2. Prove OKOT_2 or a sufficient conditional low-chaos orientation-density
   theorem.
3. Prove BD-RL3-C2 and actual-to-Haar FAHC for A_8^min cup A_10^dir, plus
   FC_8(C_FC,8,A10).

P2:
4. Write the P2-SQ-PairConditioned-CCI(r) assembly note by splicing
   NonzeroFresh-CI, ZeroFresh-Saturated-CI, CloseEndpoint-Route,
   FixedSmallD-ClusterEnvelope, and FreshSector-Closure.
5. Prove or sharply reduce P2-SQ-CleanFixedK-Expansion(k), then assemble
   fixed-k factorial moments.
```

## Continuation update, KCB/OKOT/A10 and P2 fixed-k pass, 2026-06-30

Five Codex agents were assigned to the next frontier package: three P1
log-det blockers and two P2 all-apex square assembly blockers.  The
foreground pass added a KCB coefficient diagnostic.  No background
processes, daemons, scheduled tasks, or launchers were created.

New/updated P1 artifacts:

- `notes\p1_logdet_kcb_schur_laguerre_attempt_2026_06_30.md`
- `notes\p1_logdet_kcb_schur_coeff_probe_2026_06_30.md`
- `notes\p1_logdet_okot2_orientation_density_2026_06_30.md`
- `notes\p1_logdet_bd_rl3_c2_a10_fahc_route_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_kcb_schur_coeff_probe.py`

New/updated P2 artifacts:

- `notes\all_apex_square_pair_conditioned_cci_assembly_2026_06_30.md`
- `notes\all_apex_square_clean_fixed_k_expansion_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`

P1 updates:

```text
KCB-Schur-Laguerre[p]:
  General KCB/TCSL is not closed.  The latest attempt identifies the exact
  logarithmic eigenvalue-loss cancellation
    partial_theta_i F=-(1/2)(1-lambda_i)F,
  removing the apparent tau-loss from the correct Schur derivatives.  The
  remaining proof is reduced to explicit deterministic Schur-Laguerre
  majorization inequalities SLM-2[p] and SLM-4[p].  The trace-component
  centered row-sum estimate SLM-2[p] is the minimal current blocker.

KCB diagnostic:
  numerics\p1_kcb_schur_coeff_probe.py samples the diagonal fixed-spectrum
  coefficient ratios for p=L and p=Q=L^2+2S_2.  It is evidence and debugging
  infrastructure only; it is not used as a proof.

OKOT_2:
  Product-coordinate OKOT_2 remains open.  It is reduced to conditional
  low-chaos orientation-density or moment bounds, recorded as LCOD_2/MOKOT_2.
  Gaussian/right-invariant and independent-Haar/high-randomness orientation
  cases close, but the determinant-tilted SVD orientation local law remains
  the product-law obstacle.

BD-RL3-C2 and A10 FAHC:
  The exact theorem for A_8^min cup A_10^dir is now stated.  The A10
  residual-degree-five tests and profiles S_334,S_37,S_46,S_55,(S_10) are
  fixed.  The mechanical C2/Haar/smoothing extensions are separated from the
  real new work: profile-weighted C2 coarea/sign-gap estimates for every
  surviving A10 scalar numerator, plus the enlarged signed-main/smooth FAHC
  budget.

FC leakage:
  The exact remaining complement is FC_8(C_FC,8,A10), including the
  off-near Delta C_FC,10 leakage and post-degree-ten residual.
```

P2 updates:

```text
PairConditioned-CCI:
  P2-SQ-PairConditioned-CCI(r) is assembled under the saturated atlas
  convention by splicing NonzeroFresh-CI, ZeroFresh-Saturated-CI,
  CloseEndpoint-Route, FixedSmallD-ClusterEnvelope, and FreshSector-Closure.
  The only atlas caveat is SCDE(r) if a smaller exact labelled atlas is used.

Clean fixed-k:
  P2-SQ-CleanFixedK-Expansion(k) is reduced to the conditional hard-edge
  expansion input P2-SQ-CHE-L2k(k), unless the fixed-moment Gaussian
  hard-edge package is imported directly.  Once CHE-L2k(k) is available,
  the trace/Venn concentration ledger gives the clean expansion and the
  remaining work is fixed-k factorial-moment assembly.
```

Current next split should prioritize:

```text
P1:
1. Prove SLM-2[p]/SLM-4[p] for p=L and p=L^2+2S_2, with SLM-2 centered
   row-sum cancellation as the first target.
2. Prove LCOD_2 or MOKOT_2 for determinant-tilted product-coordinate SVD
   orientations.
3. Prove BD-RL3-C2(A_8^min cup A_10^dir) profile-weighted coarea/sign-gap
   estimates and the enlarged signed-main/smooth FAHC budget.
4. Prove FC_8(C_FC,8,A10), the Delta C_FC,10 leakage bound, and the
   post-degree-ten residual/VT_p input.

P2:
5. Prove or import P2-SQ-CHE-L2k(k), then assemble
   P2-SQ-FixedK-FactorialMoment(k) and P2-SQ-HardEdge-Poisson.
```

## Continuation update, SLM/MOKOT/FC and conditional P2 closure pass, 2026-06-30

Five Codex agents were assigned to the corrected frontier: two KCB
Schur-Laguerre subproblems, the OKOT/MOKOT orientation moment theorem, the
A10 Fourier leakage piece, and the P2 CHE/factorial assembly.  The
foreground pass added a direct SLM-2 row-sum diagnostic.  No background
processes, daemons, scheduled tasks, or launchers were created.

New/updated P1 artifacts:

- `notes\p1_logdet_slm2_row_sum_attempt_2026_06_30.md`
- `notes\p1_logdet_slm2_row_sum_probe_2026_06_30.md`
- `notes\p1_logdet_slm4_hs_bound_2026_06_30.md`
- `notes\p1_logdet_mokot2_orientation_moment_attempt_2026_06_30.md`
- `notes\p1_logdet_fc8_a10_leakage_bound_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_kcb_slm2_row_sum_probe.py`

New/updated P2 artifacts:

- `notes\all_apex_square_che_l2k_factorial_assembly_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`

P1 updates:

```text
SLM-2[p]:
  The centered Hermite row algebra is now explicit:
    sum alpha_i row_i = (sum alpha_i H_2,i)(sum H_2,j - 4).
  The Laguerre row primitive splits as Psi_alpha=M F_alpha+G_alpha.
  The remaining trace-component theorem is the row-gradient/rank-transfer
  lemma SLM2-RT[p] for p=L,Q.  The foreground probe
  p1_kcb_slm2_row_sum_probe.py estimates the exact centered row norm and
  supports the spectral-gradient route, but is diagnostic only.

SLM-4[p]:
  The old fixed-time Delta_t SLM-4[p] target is false.  A rank-one
  hard-edge counterexample at t=1/(2 tau^2) leaves a nonzero V4 coefficient
  while the proposed RHS is O(tau).  The viable replacement is ISLM-4[p],
  an integrated harmonic Schur-Laguerre estimate that pairs with P_4 before
  taking absolute values and swaps the t/y integrations before using the
  soft-rank budget.

OKOT/MOKOT:
  Literal OKOT_2 is reformulated as a density-free signed-measure statement.
  A self-normalized eighth-moment theorem SOM8_2[p] implies MOKOT_2[p] for
  p=L,Q.  The product-law SVD coarea calculation exposes the fourth-cumulant
  orientation obstruction and names the next lemma DT-SVD-SOM8_2.

A10 FC leakage:
  Delta C_FC,10 is conditionally closed by a uniform fixed-degree Gaussian
  leakage lemma through degree ten.  The standalone missing item is
  FC-GLeak-10(A10), with exact zero-word and optional P_10 bookkeeping.
```

P2 updates:

```text
P2 conditional closure:
  P2-SQ-FixedK-FactorialMoment(k) is assembled from
  PairConditioned-CCI(k-2), the fixed-k Venn entropy split, and
  CleanFixedK-Expansion(k).  The hard-edge Poisson theorem follows by the
  factorial-moment criterion.

Remaining P2 input:
  Internally, the only remaining analytic input is P2-SQ-CHE-L2k(k).  If
  the fixed-moment Gaussian hard-edge package is imported, then CHE-L2k(k),
  CleanFixedK-Expansion(k), FixedK-FactorialMoment(k), and
  HardEdge-Poisson are closed.
```

Current next split should prioritize:

```text
P1:
1. Prove SLM2-RT[p] for p=L,Q using the Laguerre integration-by-parts
   rank-transfer and centered spectral-gradient estimates.
2. Prove ISLM-4[p] for p=L,Q; do not use the false fixed-time Delta_t
   SLM-4[p] intermediate statement.
3. Prove DT-SVD-SOM8_2 for determinant-tilted product-coordinate SVD
   orientations, or an even sharper one-sided signed moment theorem.
4. Prove FC-GLeak-10(A10), then finish FC_8(C_FC,8,A10) with the
   post-degree-ten residual and VT_p/pointwise substitute.

P2:
5. Prove or explicitly import P2-SQ-CHE-L2k(k).  This is the remaining
   P2 blocker for full square hard-edge Poisson closure.
```

## Continuation update, refined KCB/FC/SVD and CHE-L2k pass, 2026-06-30

Five Codex agents were assigned to the next exact frontier:
`SLM2-RT[p]`, `ISLM-4[p]`, `DT-SVD-SOM8_2`, `FC-GLeak-10(A10)`, and
`P2-SQ-CHE-L2k(k)`.  The foreground pass added an `L^{2k}` conditional
hard-edge diagnostic.  No background processes, daemons, scheduled tasks,
or launchers were created.

New/updated P1 artifacts:

- `notes\p1_logdet_slm2_rt_proof_attempt_2026_06_30.md`
- `notes\p1_logdet_islm4_integrated_attempt_2026_06_30.md`
- `notes\p1_logdet_dt_svd_som8_attempt_2026_06_30.md`
- `notes\p1_logdet_fc_gleak10_proof_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`

New/updated P2 artifacts:

- `notes\all_apex_square_che_l2k_proof_attempt_2026_06_30.md`
- `notes\all_apex_square_che_l2k_moment_probe_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`
- `numerics\p2_che_l2k_moment_probe.py`

P1 updates:

```text
SLM2-RT[p]:
  The Laguerre M-integration-by-parts transfer is written explicitly and
  removes the only unweighted auxiliary-rank factor.  The next lemma is
  SLM2-CGB[p], a centered-gradient bound for the explicit post-transfer
  vector profiles V_L,V_Q.  The hard region is y>t for non-isotropic,
  non-rank-one spectra.

ISLM-4[p]:
  Harmonic pairing before absolute values gives an exact pairwise-difference
  primitive for the fourth-chaos part.  Zero/isotropic/rank-one/y<=t cases
  close.  The next lemma is ISLM4-HG-LY[p], the large-y integrated
  harmonic-gradient Schur-Laguerre estimate.

DT-SVD-SOM8_2:
  The Haar side is closed by KCB[p].  The product-law problem is reduced to
  the two centered same-spectrum SVD finite-test comparisons
  DT-SVD-SOM8-FTC_2 for B_L and B_Q.  The first explicit obstruction is
  the degree-12 Haar coefficient SVD-C4xB8_2 coming from the fourth-cumulant
  coarea bias.

FC-GLeak-10(A10):
  The A10 leakage finite sum is conditionally closed.  The exact remaining
  cutoff lemma is FC8-CutDer-Gauss-10: for the real FC8 cutoff, fixed-degree
  Gaussian-polynomial off-near leakage must beat the worst coefficient
  growth d^3 by d^-5.
```

P2 updates:

```text
CHE-L2k:
  Under the imported fixed-moment Gaussian hard-edge package,
  P2-SQ-CHE-L2k(k) is proved and the saturated-atlas P2 route closes through
  P2-SQ-HardEdge-Poisson.

Internal proof frontier:
  Without that import, the exact remaining two sublemmas are
    P2-SQ-WeightedPrivateHardEdge-L2k(k)
    P2-SQ-BlockLinearization-L2k(k).

Diagnostic:
  numerics\p2_che_l2k_moment_probe.py reports normalized empirical
  L^{2k} conditional errors and a binomial-noise floor at moderate levels.
  The smoke grid showed no visible block approximation error beyond sampling
  noise, but this is diagnostic only.
```

Current next split should prioritize:

```text
P1:
1. Prove SLM2-CGB[p] for the finite post-M-transfer centered profiles.
2. Prove ISLM4-HG-LY[p] for the large-y integrated harmonic-gradient cone.
3. Prove SVD-C4xB8_2, then DT-SVD-SOM8-FTC_2 / LEX_2 for the two SVD tests.
4. Prove FC8-CutDer-Gauss-10 for the exact FC8 cutoff and Holder form.

P2:
5. Either import the fixed-moment Gaussian hard-edge package and mark P2
   closed, or prove the internal pair
   P2-SQ-WeightedPrivateHardEdge-L2k(k) and
   P2-SQ-BlockLinearization-L2k(k).
```

## Continuation update, smallest-lemma reduction pass, 2026-06-30

Five Codex agents were assigned to `SLM2-CGB[p]`, `ISLM4-HG-LY[p]`,
`SVD-C4xB8_2`, `FC8-CutDer-Gauss-10`, and
`P2-SQ-WeightedPrivateHardEdge-L2k(k)`.  The foreground pass handled
`P2-SQ-BlockLinearization-L2k(k)`.  No background processes, daemons,
scheduled tasks, or launchers were created.

New/updated P1 artifacts:

- `notes\p1_logdet_slm2_cgb_attempt_2026_06_30.md`
- `notes\p1_logdet_islm4_hg_ly_attempt_2026_06_30.md`
- `notes\p1_logdet_svd_c4xb8_attempt_2026_06_30.md`
- `notes\p1_logdet_fc8_cutder_gauss10_attempt_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`

New/updated P2 artifacts:

- `notes\all_apex_square_weighted_private_hardedge_l2k_attempt_2026_06_30.md`
- `notes\all_apex_square_block_linearization_l2k_attempt_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`

P1 updates:

```text
SLM2-CGB[p]:
  The eta/rho atom sector is separated as closed by positive Laguerre mass
  estimates.  The pure unweighted large-y sector collapses to one centered
  atom:
    V_L^mu = C_L^mu mu,
    V_Q^mu = C_Q^mu mu.
  The next lemma is SLM2-CMU-LY[p], the determinant-weighted large-y
  centered-mu inequality.

ISLM4-HG-LY[p]:
  The large-y harmonic estimate is reduced to one pairwise
  spectral-difference integral, ISLM4-HG-PDI[p].  The exact p=L pair formula
  and compact exact p=Q pair formula are now written.

SVD-C4xB8_2:
  The first SVD product-law obstruction is reduced to explicit degree-12
  and degree-10 orthogonal Weingarten words.  The next equivalent labels are
  SVD-C4xB8-WG_2 and SVD-C4xB8-LP_2.

FC8-CutDer-Gauss-10:
  The A10 leakage remains conditionally closed, but the written notes still
  lack exact FC8 cutoff geometry, radii, transition width, derivative
  constants, inversion constants, Gaussian shell capture, and Holder form.
  The schedule theorem to add is FC8-CutoffSchedule-GaussShell, proving the
  derivative-tail condition (CDT_N,q).
```

P2 updates:

```text
BlockLinearization-L2k:
  The foreground note reduces the block-linearization fixed-exponent
  envelope to the weighted private hard-edge theorem plus standard
  proportional rectangular Wishart moments and tails.

WeightedPrivateHardEdge-L2k:
  The random-weight and fixed-exponent parts close by conditioning once the
  base private Laguerre estimates are imported.  The random weight creates
  no additional singular-value obstruction.

Current internal P2 frontier:
  P2-SQ-PrivateLaguerreJanossy2-Uniform, the uniform one-point cubic
  hard-edge expansion plus two-smallest-singular-value Janossy bound for the
  real square Gaussian Laguerre ensemble.  With this imported/proved, the
  saturated-atlas P2 route closes through HardEdge-Poisson.
```

Current next split should prioritize:

```text
P1:
1. Prove SLM2-CMU-LY[p] for the centered-mu large-y trace component.
2. Prove ISLM4-HG-PDI[p] for the large-y pairwise harmonic integral.
3. Prove SVD-C4xB8-WG_2 or SVD-C4xB8-LP_2.
4. Prove FC8-CutoffSchedule-GaussShell / (CDT_N,q) for the exact FC8 cutoff.

P2:
5. Prove or cite P2-SQ-PrivateLaguerreJanossy2-Uniform, then mark the P2
   square hard-edge Poisson route closed under the saturated atlas.
```

## Continuation update, hard-edge closure and P1 frontier sharpening, 2026-06-30

Five Codex agents were assigned to `SLM2-CMU-LY[p]`, `ISLM4-HG-PDI[p]`,
`SVD-C4xB8-WG_2 / SVD-C4xB8-LP_2`,
`FC8-CutoffSchedule-GaussShell`, and
`P2-SQ-PrivateLaguerreJanossy2-Uniform`.  The foreground pass added a
direct private Laguerre/Janossy numerical diagnostic.  No background
processes, daemons, scheduled tasks, launchers, or watchers were created.

New/updated P1 artifacts:

- `notes\p1_logdet_slm2_cmu_ly_attempt_2026_06_30.md`
- `notes\p1_logdet_islm4_hg_pdi_attempt_2026_06_30.md`
- `notes\p1_logdet_svd_c4xb8_wg_lp_attempt_2026_06_30.md`
- `notes\p1_logdet_fc8_cutoff_schedule_attempt_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`

New/updated P2 artifacts:

- `notes\all_apex_square_private_laguerre_janossy2_uniform_2026_06_30.md`
- `notes\all_apex_square_private_laguerre_janossy_probe_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`
- `numerics\p2_private_laguerre_janossy_probe.py`

P1 updates:

```text
SLM2-CMU-LY[p]:
  The standalone all-spectrum pure centered-mu atom is false after dividing
  out Delta_t.  The saturated rank-one test has sign-changing coefficients
  and t^(1/2) growth while the divided budget stays O(1).  The replacement
  frontier is SLM2-CMU-TR[p] / SLM2-CMU-Spread[p], after saturated hard-edge
  sectors are returned to the full V_p profile or to a formulation that
  keeps the outside determinant factor.

ISLM4-HG-PDI[p]:
  Exact signed pair kernels for p=L and p=Q are written.  The proof reduces
  to ISLM4-HG-APDI[p], a finite positive pair-atom transport inequality.
  The hard atoms are L_t^a B m^2 and L_t^a |q m|, a=1,2, transported from
  the determinant scale u=t+y back to the t-soft-rank budget.

SVD-C4xB8-WG_2 / SVD-C4xB8-LP_2:
  Reduced to SVD-C4xB8-CGSpecTable[p].  The raw degree-10/12 Weingarten
  obstruction collapses to nine low-projection Clebsch/Gegenbauer rows:
  three degree-10 H_2 rows and six degree-12 H_2/H_4 rows.

FC8-CutoffSchedule-GaussShell:
  The abstract Gaussian-shell schedule closes for an explicit whitened
  radial cutoff with rho_d=(10^6 d log(e d))^(1/2), proving (CDT_N,q) and
  hence FC8-CutDer-Gauss-10 -> FC-GLeak-10(A10) for that cutoff.  The
  remaining exact FC8 input is FC8-GaussShell-Geom, or a direct row-law
  assertion that the actual eta_i,z,B cutoff satisfies (CDT_N,q).
```

P2 updates:

```text
P2-SQ-PrivateLaguerreJanossy2-Uniform:
  The note records a citation-quality standard real Laguerre hard-edge input:
    |P(tau<=x)-a_D x| <= C D^K a_D x^3,
    P(tau<=x, sigma_2<=r) <= C D^K x r^3.
  It reduces the input to finite real Wishart/Laguerre Selberg and Pfaffian
  hard-edge estimates.  This supplies the base theorem needed by
  WeightedPrivateHardEdge-L2k and BlockLinearization-L2k.

P2 route:
  Under the saturated atlas convention G_r^sat, the internal chain now
  closes:
    PrivateLaguerreJanossy2-Uniform
      -> WeightedPrivateHardEdge-L2k
      -> BlockLinearization-L2k
      -> CHE-L2k
      -> CleanFixedK-Expansion
      -> FixedK-FactorialMoment
      -> HardEdge-Poisson.
  The only remaining P2 caveat is optional: if the final proof replaces
  G_r^sat by a smaller exact labelled atlas, prove SCDE(r).

Diagnostic:
  numerics\p2_private_laguerre_janossy_probe.py samples D x D Gaussian
  private blocks and reports the one-point ratio P(tau<=x)/(a_D x), the
  cubic residual scale, and the two-smallest ratio P(tau<=x,sigma_2<=r)/(x r^3).
```

Current next split should prioritize:

```text
P1:
1. Prove SLM2-CMU-TR[p] / SLM2-CMU-Spread[p] for the transition centered-mu
   determinant spread, keeping hard-edge sectors in the full profile.
2. Prove ISLM4-HG-APDI[p], especially the transport of
   L_t^a B m^2 and L_t^a |q m| from u=t+y to the t-soft-rank budget.
3. Compute/prove SVD-C4xB8-CGSpecTable[p] for p=L,Q.
4. Prove FC8-GaussShell-Geom or state direct (CDT_N,q) for the actual FC8
   row-law cutoff eta_i,z,B.
5. Start another independent P1 frontier item, preferably ROA4-N-ani(Q2/Q4)
   or LC4-M-det, unless a P2 editorial pass is desired.

P2:
  Under G_r^sat, no analytic blocker remains in the current DAG.  If a
  smaller atlas is required, the only optional target is SCDE(r); otherwise
  the next P2 task is final proof assembly and citation verification.
```

## Continuation update, P1 reduction pass after P2 closure, 2026-06-30

Five Codex agents were assigned to `SLM2-CMU-TR[p]`,
`ISLM4-HG-APDI[p]`, `SVD-C4xB8-CGSpecTable[p]`,
`FC8-GaussShell-Geom`, and `ROA4-N-ani-min`.  The foreground pass added a
deterministic SVD channel-table helper.  No background processes, daemons,
scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_slm2_cmu_tr_attempt_2026_06_30.md`
- `notes\p1_logdet_islm4_hg_apdi_attempt_2026_06_30.md`
- `notes\p1_logdet_svd_c4xb8_cgspec_table_attempt_2026_06_30.md`
- `notes\p1_logdet_svd_c4xb8_channel_table_probe_2026_06_30.md`
- `notes\p1_logdet_fc8_gaussshell_geom_attempt_2026_06_30.md`
- `notes\p1_logdet_roa4_ani_min_attempt_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_c4xb8_channel_table.py`

P1 reductions:

```text
SLM2-CMU-TR[p]:
  Transition sector is now fixed by eta and x=s eta cutoffs.  The pure
  centered-mu transition problem reduces to DSI-CMU-TR, a dimensionless
  determinant-spread inequality for mu_i=s eta_i/(1+s eta_i).

ISLM4-HG-APDI[p]:
  All h,l,h2,l2,dh,dl descendant atoms reduce pointwise to the primitive
  atoms L_t^a B m^2 and L_t^a |q m|, a=1,2.  The remaining theorem is
  PAT(a) on the far transition cone kappa=t/(t+y)<1/9.  The q nonmonotone
  interval is explicit; bounded-ratio, rank-one, equal-pair, isotropic, and
  derivative-descendant cases are closed.

SVD-C4xB8-CGSpecTable[p]:
  The coarea identity U_T,2=6 L_T/(d+4) collapses the nine formal rows to
  six effective rows: three H_2 rows and three H_4 rows.  The 22 spectral
  contractions are explicit; the 24 and 44 rows reduce to finite
  Laplacian-projection contractions for M_L and M_Q.

FC8-GaussShell-Geom:
  Existing row-law/Cramer notes do not imply the Gaussian-shell geometry and
  do not state (CDT_N,q) for the actual eta_i,z,B cutoff.  The smallest
  row-law insertion is the direct derivative-tail axiom
  (A3-FC8-Gauss-CDT); proving FC8-GaussShell-Geom remains a stronger
  sufficient alternative.

ROA4-N-ani-min:
  The exact centered tensor form is written for Q2/Q4.  Deterministic
  fixed-C algebra does not close because the rank-one hard-edge obstruction
  survives.  After separating the same-spectrum Haar budget, the live
  theorem is ROA4-N-ani-orb, the cap-summed positive excess of the actual
  determinant-tilted anisotropic budget over its same-spectrum Haar budget.
  ROA4-N-ani-orb-pt is a stronger pointwise sufficient route.
```

Foreground SVD helper:

```text
numerics\p1_svd_c4xb8_channel_table.py
```

prints the nine formal channel rows, harmonic dimensions, multiplicities,
coarea vectors, spectral vectors, and prefactor forms.  It is table
bookkeeping only; it does not compute Clebsch constants or Schur spectral
contractions.

Current next split should prioritize:

```text
P1:
1. Prove DSI-CMU-TR for the transition centered-mu determinant spread.
2. Prove PAT(a), a=1,2, on the far cone kappa<1/9.
3. Expand and bound the six-effective-row Reduced-CGSpecTable[p] for
   p=L,Q, especially the 24/44 Laplacian-projection contractions.
4. Add/prove (A3-FC8-Gauss-CDT) for the actual FC8 row-law cutoff eta_i,z,B,
   or change the FC8 split to use a separate Gaussian-word cutoff.
5. Prove ROA4-N-ani-orb or the stronger ROA4-N-ani-orb-pt.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 fifteenth P1 contraction

Five Codex agents were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 blockers, with one foreground CROW probe running in parallel.  All five
worker results were integrated into the P1 DAG.  No background processes,
daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_tcr_rootpack_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_clebsch_generator_spec_2026_07_01.md`
- `notes\p1_logdet_icrow_nsk_kernel_probe_2026_07_01.md`
- `notes\p1_logdet_icrow_nsk_kernel_k2_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_tensor_slots_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_gauge_theorem_packet_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_icrow_nsk_kernel_probe.py`
- `numerics\p1_svd_clebsch_constant_spec.py`
- `numerics\p1_rftc_tensor_slot_schema.py`

P1 reductions:

```text
PAT:
  Tiny-Companion-Reserve_I(a), a=1,2, closes conditionally on bounded
  g=theta H shells under anchored dyadic activation/root packing.  With
  A(H)=tau^2 H/r_p+sum_k log(1+q_k H), D_c=exp(-A/2), and
  L_I^+(theta)=sup_{H in I/theta}L(H), the sufficient condition is
  A(g_0/theta)-A(2)>=log(1/theta)+2a log L_I^+(theta)-K_A.
  Without this condition the exact payment is
  nu_I,a(theta)<=C theta^(3/2)exp(Def_I,a(theta)/2)R_a(theta).  The live
  blocker is bounded deficiency for actual delayed-isolated profiles, or
  downstream payment of the dyadic weights.

SVD:
  The Clebsch/Gegenbauer source-constant generator is specified: six
  channels 22_2,24_2,44_2,22_4,24_4,44_4; normalized-sphere H_2/H_4
  conventions; rational monomial basis; harmonic projection; sphere Gram
  normalization; and rational operator-norm packets for L_T and U_T4.
  The constants N2,L2,U4, chi channels, or direct r,a,b,c,A,B,D remain
  absent, so this is now a build contract rather than a closed proof row.

CROW:
  A deterministic NSk-Kernel probe shows the integrated stress point is
  small.  For k=2,h=1/2,theta=0 the required constants are about
  3.82e-4 for L and 8.84e-4 for Q, and the sampled grid k=2,3,4,
  h=1/4,1/2,3/4, theta=0,1/4,1 stays below 1.2e-3.  The first analytic
  stress point is closed:
  K_L,2,h(0)=-sqrt(pi)(1-sqrt(1-h/2)) and
  K_Q,2,h(0)=-sqrt(pi)(1-(1-h/2)^(3/2)).
  The remaining work is theta>0 at k=2, then uniform k>=3.

RFTC:
  The scalar row adapter now has a tensor-slot contract for K2_z,K4_z,
  M_L_2,M_Q_2, plus the full map containing M_L_4,M_Q_4.  The validator
  checks finite rational packets for symmetry and trace invariants.  The
  exact coefficients, V_Q2/V_Q4 word expansions, beta_l budgets, sharp
  T_b support intervals, and density packet remain missing.

FC8:
  The FC8 cutoff front is split into FC8-CramerGaugeCutoff plus the
  good-frame FC8-etaN-JetTaxedRadiusRowLaw.  It suffices to prove
  ||exp((A_J L_d-rho_J^2)_+/4)1_G||_L^r(P_i)<=exp(C_JX L_d)
  with A_J/4>=C_T+C_JX+C_BK+C_K+2+a, where
  rho_J^2=rho_N^2-4log(1+J_eta).  The separate bad-frame charge
  E_{P_i}[Z_i U_A10 1_{G^c}]<=C d^-2 is not paid by this good-frame
  theorem and remains a separate input.
```

Current next split:

```text
P1:
1. PAT: prove bounded Def_n for actual delayed-isolated root profiles, or
   prove a summable payment for 2^(-3n/2)exp(Def_n/2)R_a(theta_n).
2. SVD: implement the finite Clebsch table and atom-norm certificates, then
   supply N2,L2,U4 and the six chi constants to the row-domination checker.
3. CROW: extend NSk-Kernel[p,h] from theta=0 to theta>0 at k=2, then prove
   the uniform k>=3 signed-kernel inequality.
4. RFTC: supply actual K2_z,K4_z,M_L_2,M_L_4,M_Q_2,M_Q_4 tensors and
   Q2/Q4 word lists; then evaluate B arrays, density arrays, beta_l, and
   T_b intervals.
5. FC8: prove FC8-CramerGaugeCutoff/JTR row-law for the real eta_N cutoff
   and close the separate A10 bad-frame charge.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 P1 frontier contraction

Five Codex agents were assigned to `PAT-QuadTail-min(a)`, the SVD six-row
certificate, `WSDK-scal(Q2/Q4)`, `ANIORB-SOM-FTC`, and the FC8 A3/bridge
choice.  The foreground pass added a deterministic SVD coefficient-array
probe.  No background processes, daemons, scheduled tasks, launchers, or
watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_quadtail_min_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_sixrow_certificate_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_sixrow_probe_2026_07_01.md`
- `notes\p1_logdet_wsdk_scal_attempt_2026_07_01.md`
- `notes\p1_logdet_aniorb_som_ftc_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_a3_bridge_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_sixrow_probe.py`

P1 updates:

```text
PAT-QuadTail-min(a):
  The determinant-derivative piece A_0 m^2 is closed by a positive
  Laplace-kernel lemma, without integration by parts against m^2.  The
  bounded-activation part E_{<=H0} m^2 and the left endpoint quotient
  C_L^0 m^2 also close.  The remaining theorem is strictly smaller:
  PAT-QuadTail-edge(a), a high-activation hard-edge packing estimate for
  E_edge+R_edge when the tested pair has a low t-activation endpoint.

SVD six-row obstruction:
  The six signed rows are bundled into
    Coeff_p=<V_0^p,c^0>_2+<V_xi^p,xi>_2+<V_4^p,z>_4.
  The pointwise certificate is P-SIX: W(S) Z_p <= C A_p(R,z)^2.
  The averaged certificate is A-SIX under the determinant-tilted measure.
  The new foreground probe verifies trace decomposition, harmonic
  constraints, and scalar/quadratic/harmonic zero cases; it is not yet a
  full certificate engine because exact H_4 Gram normalization and Clebsch
  constants still need insertion.

WSDK-scal(Q2/Q4):
  The scalar determinant-kernel theorem is reduced to CROW-scal[p] plus
  POC-scal[p] for p=L,Q.  CROW-scal[p] is the centered row-sum
  fixed-spectrum coefficient lemma for the V_2 trace component.  POC-scal[p]
  is the one-kernel positive-excess orientation comparison.  The harmonic
  V_4 half KCB-scal-H4[p] has a no-tau Laguerre coefficient route once the
  standard Schur denominator moment bound is used.

ANIORB-SOM-FTC:
  The two-test square route now has an exact implication to DLCOD-ANIORB:
  with envelopes u_a>=||psi_a||_2, ANIORB-SOM-FTC[u] gives
  eta=int u_a dmu + eps/2.  The first finite product-law calculation is the
  two-row table C4xB-ANIORB[u; a,T] for a in {Q2,Q4}.

FC8 A3/bridge:
  Direct (A3-FC8-Gauss-CDT)[eta_N] remains the smaller next theorem.  The
  analytic bridge for eta_G-eta_N is equivalent to direct A3 modulo the
  closed eta_G schedule.  A genuinely different fallback would need a new
  cutoff-weighted finite-direct theorem, FC8-A10-Bridge-NG-findir.
```

Foreground verification:

```text
python -m py_compile numerics\p1_svd_sixrow_probe.py
python numerics\p1_svd_sixrow_probe.py --d-values 4 6 --samples 2 --seed 20260701
```

The probe showed reconstruction and harmonic residuals at roundoff,
vanishing scalar-trace rows, and the expected row cancellations for
quadratic-trace and harmonic-only inputs.

Current next split should prioritize:

```text
P1:
1. Prove PAT-QuadTail-edge(a), a=1,2.
2. Turn the SVD six-row probe into a certificate engine by adding the exact
   H_4 Gram normalization and Clebsch constants, then attack P-SIX/A-SIX.
3. Prove CROW-scal[p] for p=L,Q.
4. Prove POC-scal[p] or the two-row C4xB-ANIORB[u; a,T] table with
   cap-summable remainder control.
5. Prove direct (A3-FC8-Gauss-CDT)[eta_N] shell-capture and derivative
   geometry, or explicitly take on FC8-A10-Bridge-NG-findir.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, P1 five-frontier sharpening, 2026-06-30

Five Codex agents were assigned to `PAT-QuadTail(a)`,
the SVD Schur coefficient pipeline, the FC8 two-cutoff architecture,
`P-ROA4-N-ani-orb-lowchaos`, and the scalar `LC4-M-det+` upgrade.  The
foreground pass added a pointwise PAT-QuadTail diagnostic.  No background
processes, daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_quadtail_attempt_2026_06_30.md`
- `notes\p1_logdet_pat_quadtail_probe_2026_06_30.md`
- `notes\p1_logdet_svd_c4xb8_schur_coeff_pipeline_attempt_2026_06_30.md`
- `notes\p1_logdet_fc8_two_cutoff_architecture_2026_06_30.md`
- `notes\p1_logdet_roa4_ani_orb_lowchaos_attempt_2026_06_30.md`
- `notes\p1_logdet_roa4_scal_lc4_m_plus_attempt_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_pat_quadtail_probe.py`

P1 updates:

```text
PAT-QuadTail(a):
  The exact far-cone target is now split into BQT-B(a) and BQT-Tail(a).
  The nonmonotone q interval, large-M separation, left tail away from
  x=0, and right tail with bounded kappa x are pointwise absorbed into
  C B m^2.  The smallest remaining theorem is PAT-QuadTail-min(a): the
  integrated transport of L_t^a B m^2 plus only the left endpoint and hard
  right endpoint monotone-tail quotient degeneracies.  A fixed-t absolute
  estimate is false in the rank-one hard edge, so the proof must use the
  integrated t budget.

Reduced-CGSpecTable[p]:
  The missing linear trace decomposition is closed.  The explicit map is
  C_i^p,C_ij^p -> alpha^p,a_i^p,b_i^p,b_ij^p, followed by the arrays
  u^p,e^p,w^p,X^p,Y^p.  The remaining SVD item is the final signed
  six-row inequality for Coeff_H2^p+Coeff_H4^p, pointwise at scale
  A_p(R,z)^2 or in determinant-tilted averaged form.

FC8/A10 leakage:
  The smaller final edit is the direct insertion (A3-FC8-Gauss-CDT) for
  the actual eta_i,z,B cutoff.  The separate Gaussian-shell cutoff route is
  viable only if the bridge term B_NG^10=-(eta_G-eta_N)phi_gamma P_A10 is
  estimated exactly once, via FC8-A10-Bridge-NG or an enlarged finite direct
  comparison.  Otherwise it drops or double-charges A10 mass.

ROA4-N-ani-orb:
  The low-chaos insertion is exactly the two-function theorem for psi_Q2
  and psi_Q4.  The smallest exact condition is DLCOD-ANIORB, a one-sided
  coarea correlation against the actual minus Haar orientation law.  The
  more checkable replacement is ANIORB-SOM-FTC for the two self-normalized
  square tests B_Q2^orb and B_Q4^orb.

ROA4-N-scal-det(Q2/Q4):
  LC4-M-det+ is LC4-M-det plus two weighted single-row Schur determinant
  kernels.  Current LC4-M-det does not imply them as a black box.  The
  smallest scalar theorem is WSDK-scal(Q2/Q4), equivalently base kernels
  WSDK[L] and WSDK[L^2+2S_2] with bounded soft-rank cost and the actual
  scalar coefficients inserted.
```

Foreground PAT probe:

```text
python -m py_compile numerics\p1_pat_quadtail_probe.py
python numerics\p1_pat_quadtail_probe.py --kappa-values 0.001 0.01 0.05 0.1 --points 48 --x-cap-factor 30
```

The middle-band absorption ratios were moderate in the smoke grid, while
the right monotone-tail quotient grew as expected.  The probe is diagnostic
only and does not prove the integrated transport theorem.

Current next split should prioritize:

```text
P1:
1. Prove PAT-QuadTail-min(a), a=1,2, with the integrated B m^2 transport.
2. Prove the final signed six-row SVD inequality after inserting the explicit
   Schur arrays, or implement a finite symbolic/numeric certificate route.
3. Prove WSDK-scal(Q2/Q4), split into KCB-scal[p] and KOT-scal[p].
4. Prove DLCOD-ANIORB or the ANIORB-SOM-FTC two-test moment replacement.
5. Insert/prove (A3-FC8-Gauss-CDT); if using two cutoffs, prove
   FC8-A10-Bridge-NG.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, DSI closure and far-cone refinements, 2026-06-30

Five Codex agents were assigned to `DSI-CMU-TR`, `PAT(a)`,
`Reduced-CGSpecTable[p]`, `(A3-FC8-Gauss-CDT)`, and
`ROA4-N-ani-orb`.  The foreground pass added a deterministic numerical
stress probe for `DSI-CMU-TR`.  No background processes, daemons, scheduled
tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_dsi_cmu_tr_attempt_2026_06_30.md`
- `notes\p1_logdet_dsi_cmu_tr_probe_2026_06_30.md`
- `notes\p1_logdet_pat_far_cone_attempt_2026_06_30.md`
- `notes\p1_logdet_svd_c4xb8_reduced_cgspec_attempt_2026_06_30.md`
- `notes\p1_logdet_a3_fc8_gauss_cdt_attempt_2026_06_30.md`
- `notes\p1_logdet_roa4_ani_orb_attempt_2026_06_30.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_dsi_cmu_tr_probe.py`

P1 updates:

```text
DSI-CMU-TR:
  Closed.  The proof normalizes by u=sL and theta=lambda/L, proves the two
  normalized integrals I_L and I_Q are O((1+theta)^(1/2)), and therefore
  closes the determinant-spread core of SLM2-CMU-TR[p].  This does not
  revive the false all-spectrum pure atom because the hard-edge sector must
  still be routed outside the transition coefficient envelopes.

PAT(a):
  The explicit q nonmonotone interval on kappa<1/9 is not an independent
  obstruction: q variation inside the interval is absorbed pointwise by
  C B m^2.  The remaining primitive transport is the quadratic far-cone
  inequality PAT-QuadTail(a): transport L_t^a B m^2 plus the monotone-tail
  q derivative quotient.

Reduced-CGSpecTable[p]:
  The 24/44 Laplacian-projection identities are explicit:
    Delta(q_A B)=4E_A B,
    Delta^2(q_A B)=8D_A B,
    Delta^2(B^2)=4U_B,
    Delta^3(B^2)=8T_B.
  The remaining finite symbolic pipeline is to trace-decompose M_L and M_Q
  into diagonal-even arrays (a_i^p,b_i^p,b_ij^p), form
  (u^p,e^p,w^p,X^p,Y^p), and prove the final six-row signed determinant-
  tilted bound.

(A3-FC8-Gauss-CDT):
  Exact insertion text is written.  It is compatible with the existing
  row-law/Cramer package as a direct axiom for the actual eta_i,z,B cutoff.
  If proving it for the single near cutoff conflicts with the Cramer support,
  use the separate Gaussian-word cutoff architecture and record the exact
  decomposition identity.

ROA4-N-ani-orb:
  Orbit disintegration is written.  The right-invariant case closes with
  zero excess, and near-Haar/Lq/low-chaos sufficient conditions are stated.
  The live product-law insertion is P-ROA4-N-ani-orb-lowchaos, a one-sided
  actual-to-Haar correlation bound for the two centered positive orbit
  functions generated by Q2 and Q4.
```

Foreground DSI probe:

```text
numerics\p1_dsi_cmu_tr_probe.py
```

stress-tests the normalized `DSI-CMU-TR` ratios on fixed and random eta
profiles.  The smoke grid showed zero ratios for flat profiles and finite
ratios for sparse transition profiles; largest displayed values were
`ratio_L=0.0885964241892` and `ratio_Q=0.125542888975` on the small grid.

Current next split should prioritize:

```text
P1:
1. Prove PAT-QuadTail(a), a=1,2, on kappa<1/9: the B m^2 transport plus
   monotone-tail q derivative quotient.
2. Trace-decompose M_L and M_Q into diagonal-even arrays and finish the
   six-row Reduced-CGSpecTable[p] signed determinant-tilted bound.
3. Prove or formally insert (A3-FC8-Gauss-CDT), or implement the separate
   Gaussian-word cutoff decomposition identity.
4. Prove P-ROA4-N-ani-orb-lowchaos for the two orbit functions psi_Q2 and
   psi_Q4, or a sufficient near-Haar density/moment theorem.
5. Start another independent frontier item, preferably LC4-M-det or
   ROA4-N-scal-det(Q2/Q4) scalar determinant-kernel upgrades, if agents
   should avoid crowding the four active reduced targets.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Latest active frontier pointer, 2026-07-01

The detailed July 1 contraction passes are recorded earlier in this ledger.
The active bottom-line split after the twelfth July 1 pass is:

```text
P1:
1. Prove PAT-QuadTail-delay-low(a;B_L) via
   DLI-CorePack(a;B_L,B_D,c_D), Eext-CorePack(a;A_E,B_E), and
   Tiny-Companion-Reserve_I(a) or the resulting delayed-isolated companion
   profile for the very-separated high small-`m` branch.
2. Complete SVD AP-CERT-sph / AP-AVG-sph; for the two-block quotient this
   is now the exact `P_diag` / `P_SOS=(r,a,b,c,A,B,D)` / `P_scale=(K)`
   data request, diagonal full-box test `K^2>=R_full`, exact rational
   endpoint signs `S_T(p,q)`, and 8-vertex weighted-square `mu_v`
   witnesses checked by the exact coefficient checker, followed by
   `W_I<=W_crit`.
3. Replace fixed-time all-k CROW with the integrated route:
   `ICROW-scal[p] + POC-scal-int[p]`; N2,N5,N6 are closed, so remaining
   trace-audit checks are N1,N3,N4,N7.
4. Prove the compressed RFTC bundle by `SignedBernstein-PolySandwich`:
   signed minorants/majorants, exact `B_0/B_1/B_2` Weingarten arrays, and
   L2/L4 envelopes; prove `WEc(A)+WH2(A)+Wbar2(A)` for `WSOC2(A;b)`.
5. Prove the actual FC8 raw eta packet
   `BIC5_sum_raw` via `NRJ-ExpMoment`, the exponential moment of
   `log(1+J_eta)+(A_R d log(e d)-rho_N^2)_+/4`, plus the separate
   bad-frame charge.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 second P1 contraction

Five Codex agents were assigned to `PAT-QuadTail-edge(a)`, the SVD
`P-SIX/A-SIX` certificate, `CROW-scal[p]`, the common product-law finite
test comparison, and FC8 `eta_N` geometry.  The foreground pass upgraded
the SVD probe with the exact Gaussian H4 Gram matrix and harmonic
projection diagnostics.  No background processes, daemons, scheduled tasks,
launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_quadtail_edge_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_psix_certificate_attempt_2026_07_01.md`
- `notes\p1_logdet_crow_scal_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_scal_c4xb_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_etaN_geometry_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_sixrow_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_sixrow_probe.py`

P1 reductions:

```text
PAT:
  PAT-QuadTail-edge(a) is reduced to PAT-QuadTail-edge-pack(a).  The right
  q edge is endpoint-carried and not truly inactive; endpoint-carried E
  closes in rich-soft-rank and bounded-companion subcases.  Remaining:
  E_ext, sparse-dominant endpoint E, and active-low R_act packing.

SVD:
  P-SIX is now the exact matrix inequality
    C^2 A_p^4 - W2 Z2_p >= 0.
  The normalized-sphere H4 Gram/projection is fixed symbolically; the
  foreground probe implements the Gaussian homogeneous Gram and projection.
  Remaining: Clebsch substitution/normalization and A_p lower form.

WSDK scalar:
  CROW-scal[p] is closed away from saturated hard-edge spectra.  Remaining:
  HE-CROW-Pair[p,h], the full-profile divided-difference pair-kernel
  inequality for p=L,Q.

Product-law orientation:
  POC-scal[p] and C4xB-ANIORB[u] are both instances of Common-FTC(E).  The
  first-order data are C_l,T=int <F_l,q_T^circ> dmu.  Orthogonality and
  favorable-sign subcases close modulo the common cap-summable remainder.

FC8:
  Existing row-law/Cramer geometry does not imply shell capture for eta_N.
  Remaining choices are direct (A3-FC8-Gauss-CDT)[eta_N], sufficient
  FC8-etaN-ShellGeom, or fallback FC8-A10-Bridge-NG-findir.
```

Current next split remains:

```text
P1:
1. PAT: DLI-CorePack(a;B_L,B_D,c_D), Eext-Pack(a),
   Ract-CorePack(a;B_R).
2. SVD: 8 representative two-block SOS vertices with endpoint W2max(I);
   then global AP-CERT-sph/AP-AVG-sph.
3. CROW: TL-HE-CROW-SGI-bc[p,h] or full boundary cancellation with y<=t;
   pairwise boundary-corrected SP.
4. RFTC: tied rank-one active matrix B_E omega; coordinate Q_s^circ case;
   int A_E rho_2 dmu.
5. FC8: BIC5_act/BIC5_beta/BIC5_sum or ODE10-sum plus random moment packet.

P2:
  Optional SCDE(r) or proof/citation assembly only.
```

## Continuation update, July 1 third P1 contraction

Five Codex agents were assigned to the current P1 bottom split:
`PAT-QuadTail-edge-pack(a)`, the SVD AP lower-form certificate,
`HE-CROW-Pair[p,h]`, the common finite-test comparison tables, and the FC8
route choice.  The foreground pass also updated the SVD six-row probe so the
default `H_4` mode is normalized-sphere, with Gaussian homogeneous
normalization still available by flag.  No background processes, daemons,
scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_edge_pack_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_psix_ap_form_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_pair_attempt_2026_07_01.md`
- `notes\p1_logdet_common_ftc_tables_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_route_choice_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_sixrow_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_sixrow_probe.py`

P1 reductions:

```text
PAT:
  PAT-QuadTail-edge-pack(a) contracted to
  PAT-QuadTail-edge-pack-delay(a).  Sparse endpoint E closes under the
  no-delayed-companion input NDC_p(Lambda,A) by entry-scale coupled
  activation-Hardy.  Remaining: E_ext, R_act, and delayed sparse endpoint
  carriers E_end^delay.

SVD:
  A_p^4 has the AP lower form d^-4 Kprof^4 k_SR^2 E_p^4, while
  Z2_p <= Lambda_p(d,N;rho) E_p^4.  The live certificates are AP-CERT and
  AP-AVG; common-block and two-block quotient cases reduce to finite Schur
  inequalities.  The foreground probe supports sphere/Gaussian H4
  normalizations and defaults to sphere.

WSDK scalar:
  The rank-one saturated HE-CROW-Pair[p,h] subcase is closed.  With one
  saturated packet, the remaining inputs are TL-HE-CROW-Grad[p,h] or the
  stronger sufficient SP-HE-CROW-Grad[p,h].

Product-law orientation:
  Common-FTC(E) now has a two-channel factorization through L_T in H_2 and
  U_T4 in H_4, with U_T2=6L_T/(d+4).  The live target is
  Reduced-Common-FTC(E): positive reduced first-order rows plus the common
  normalized-density remainder rho_2.

FC8:
  The direct route is smaller than the two-cutoff bridge.  The first target
  is FC8-A10-CDT5-word[eta_N], the N=5 degree-ten cutoff tail for each
  surviving A10 word with the actual eta_i,z,B.
```

## Continuation update, July 1 fourth P1 contraction

Five Codex agents were assigned to `PAT-QuadTail-edge-pack-delay(a)`, SVD
`AP-CERT/AP-AVG`, `TL/SP-HE-CROW-Grad[p,h]`, `Reduced-Common-FTC(E)`, and
`FC8-A10-CDT5-word[eta_N]`.  The foreground pass added an AP certificate
diagnostic probe for finite SVD row ratios.  No background processes,
daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_delay_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_ap_cert_constants_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_grad_attempt_2026_07_01.md`
- `notes\p1_logdet_reduced_common_ftc_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_cdt5_word_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_ap_cert_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_ap_cert_probe.py`

P1 reductions:

```text
PAT:
  Delayed endpoint carriers now close in the reverse endpoint subcase and
  in the activated-lower subcase
    h_p^(1/2) <= B_L(1+h_ell)^2(1+L_t)^4.
  The remaining PAT theorem is PAT-QuadTail-delay-low(a;B_L), with inputs
  DLI-EndPack(a;B_L), Eext-Pack(a), and Ract-Pack(a).

SVD:
  The AP scale is corrected in normalized-sphere H4:
    |rho_ch| <= eta_ch Kprof^2.
  Thus Lambda(rho) <= Kprof^4 Lambda(eta), and AP-CERT-sph is the finite
  coarea-size condition
    C^2 d^-4 k_SR,p(d)^2 >= W2(S)Lambda_p(d,N;eta).
  AP-AVG-sph is the determinant-tilted integrability of
    H_AP^sph=d^2[W2 Lambda(eta)]^(1/2)/k_SR,p(d).
  The foreground AP probe emits unit-rho row-ratio diagnostics compatible
  with the six-row trace-decomposition code.

WSDK scalar:
  The lower saturated annulus 1-h<eta_*<=1-h/2 closes by the hard-edge-free
  CROW theorem with parameter h/2.  The live two-level target is the t-free
  scalar inequality DE-TL-HE-CROW-SGI[p,h]; the SP side is the deep-edge
  frozen-background modulus SP-HE-CROW-SGI[p,h].

Product-law orientation:
  Reduced-Common-FTC(E) is replaced by RFTC-RowCert(E).  For
  E_all={L,Q,B_Q2^u,B_Q4^u}, the generic checklist is four signed rows
  J_L,J_Q,J_BQ2,J_BQ4 plus four weighted rho_2 budgets.  In the
  coordinate-isotropic fourth-cumulant subcase, only the four H_4 signed
  rows plus the same rho_2 budgets remain.

FC8:
  FC8-A10-CDT5-word[eta_N] reduces to WCDT5_beta for surviving words
  334,37,46,55 and optional 10, or one eta-only (CDT5,10)[eta_N] check.
  Exact-zero word deletions and the coefficient-growth step to d^-2
  leakage are closed.  Missing data are the actual eta_i,z,B whitened
  radius, transition/outer region, derivative envelopes through ell_d=2d+4,
  weighted inversion constant, and Holder row-law form if random.
```

## Continuation update, July 1 fifth P1 contraction

Five Codex agents were assigned to `PAT-QuadTail-delay-low(a;B_L)`, SVD
`AP-CERT-sph/AP-AVG-sph`, CROW `DE-TL/SP-HE-CROW-SGI`, `RFTC-RowCert`, and
FC8 `WCDT5_beta/(CDT5,10)`.  The foreground pass added a two-block AP
diagnostic probe.  No background processes, daemons, scheduled tasks,
launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_delay_low_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_ap_sos_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_sgi_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_rowcert_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_wcdt5_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_two_block_ap_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_two_block_ap_probe.py`

P1 reductions:

```text
PAT:
  The R_act endpoint-gain region
    h_+^(3/2) Phi(h_-) <= B_R(1+L_t)^4,
    Phi(g)=g/(1+g)^3,
  is closed.  The right quotient is reduced from Ract-Pack(a) to
  Ract-CorePack(a;B_R).  Current PAT inputs:
  DLI-EndPack(a;B_L), Eext-Pack(a), Ract-CorePack(a;B_R).

SVD:
  The two-block AP quotient is explicit.  The spectral factor is the
  univariate trace-normalized W2_2blk(delta;1), with W2_2blk=0 iff
  s_A=s_B.  The Schur side is a three-variable energy matrix M_E and row
  matrix M_Z,2blk(rho).  The eta-profile box reduces to 16 sign-vertex SOS
  checks.  The foreground two-block probe emits matching unit-rho row-ratio
  diagnostics in sphere/Gaussian H4 normalizations.

WSDK scalar:
  The null-soft beta=0 TL and null-soft SP cases reduce to one radial
  scalar inequality.  For p=L the integrand is explicit (`NL0-L[k]`), but
  the literal transferred SGI fails at lambda=0.  The active CROW target is
  therefore positive-lambda transferred SGI with justified boundary limits,
  or a boundary-corrected SGI; p=Q and general SP remain.

Product-law orientation:
  RFTC-RowCert(E_all) is bundled.  First order is one matrix-vector
  `M_E x_lambda` with exact cost `||[M_E x_lambda]_+||_1/[8(N+2)]`; the
  density side is one budget `int A_E rho_2 dmu`.  The coordinate-isotropic
  case is four H4 rows against
  `W_4^coord=sum_b x_b^4-3|x|^4/(d+2)`.

FC8:
  The smallest actual cutoff packet is the four default WCDT5 rows plus
  optional P_10.  The eta-only route is the integrated derivative-tail
  condition `C_inv(d)D_10(eta_N)<=C d^-5`, or equivalent nonradial
  envelopes through ell_d=2d+4, with Holder row-law form if random.
```

## Continuation update, July 1 sixth P1 contraction

Five Codex agents were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 frontiers.  The foreground pass added a numerical diagnostic for the
CROW null-soft `p=L` scalar ratio.  No background processes, daemons,
scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_corepack_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_vertex_sos_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_boundary_sgi_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_bundle_matrix_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_eta_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_nl0_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_he_crow_nl0_probe.py`

P1 reductions:

```text
PAT:
  DLI-EndPack(a;B_L) reduces to DLI-CorePack(a;B_L,B_D,c_D) after closing
  the active-low-gain subcase
    c_D kappa < h_ell,
    h_p^(1/2) Phi(h_ell) <= B_D(1+L_t)^4.
  Current PAT inputs are DLI-CorePack, Eext-Pack, and Ract-CorePack.

SVD:
  The two-block AP eta-box check shrinks from 16 to 8 representative sign
  vertices by the alpha -> -alpha mixed-channel involution.  W2max(I) for
  any trace-normalized interval is the max of the two endpoint values, so
  no univariate critical-point SOS is needed.

WSDK scalar:
  Bare positive-lambda transferred SGI is false in the null-soft subcase.
  The live CROW target is the finite-interval boundary-subtracted theorem
  TL-HE-CROW-SGI-bc[p,h], or a full large/small-cone cancellation of the
  boundary term.  The p=Q null-soft formula is explicit.  The foreground
  probe samples the p=L null-soft ratio.

Product-law orientation:
  Bundle-RFTC first-order rows compress to tied rank-one score columns
  K_u, giving B_E omega.  Coordinate-axis rows are written in terms of
  diagonals of O S O^T, and the equal-coordinate case is the centered
  diagonal-square observable Q_s^circ.  The density input remains
  int A_E rho_2 dmu.

FC8:
  The eta packet is reduced to Bessel-integral certificates
  BIC5_beta/BIC5_act/BIC5_sum or the order-summed derivative-envelope
  class ODE10-sum.  Random-frame requirements reduce to finite L^r eta-tail
  moments plus higher L^b word-seminorm moments.  The actual eta_i,z,B
  estimates are still not proved.
```

## Continuation update, July 1 seventh P1 contraction

Five Codex agents were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 frontiers.  The foreground pass added a two-block `W2_2blk` formula
probe and checked it against the existing coarea arrays.  No background
processes, daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_corepack2_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_sos_constants_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_bc_next_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_qsquare_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_bic5_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_w2_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_2blk_w2_formula_probe.py`

P1 reductions:

```text
PAT:
  Eext-Pack(a) reduces to Eext-CorePack(a;A_E,B_E) after closing the
  aggregate external root-budget subcase
    S_ext(e;t;A_E) <= B_E m_R(1+L_t)^4.
  The remaining PAT inputs are DLI-CorePack, Eext-CorePack, and
  Ract-CorePack.

SVD:
  The explicit W2_2blk(delta;1) formula now matches the coarea-array proxy
  to roundoff in the foreground probe.  The d=3 two-block SOS seed has
  exact eta constants, rank-four outer-product M_Z rows, and one
  six-variable ternary-quartic Gram search per representative vertex.

CROW:
  The standalone integral of the large-y boundary-corrected integrand is
  false at lambda=0 and for sufficiently small positive lambda.  The live
  theorem is therefore FIC-HE-CROW[p,h], a finite-interval cancellation
  between the exact y<=t contribution and the large-y boundary term before
  the pair absolute value is taken, with an analogous SP statement.

RFTC:
  Every tied rank-one first-order row is a covariance row against one active
  score W_omega.  Coordinate-axis rows split into a Q_s column and d-1
  deviation columns.  The equal-coordinate case is four explicit covariance
  rows against Q_s, or exact excursion sign tests.  The density budget
  int A_E rho_2 dmu remains separate.

FC8:
  For the current Delta C_FC,10 leakage consumer, the smallest packet is the
  raw total Bessel scalar BIC5_sum_raw:
    U_A10(i,z,B) <= C d^-2.
  Raw word and raw ODE packets are optional stronger routes.  The
  volume-tilted finite-moment subcase is closed once this raw scalar, or its
  moment version, is supplied for the real eta_i,z,B cutoff.
```

Current next split:

```text
P1:
1. PAT: DLI-CorePack(a;B_L,B_D,c_D), Eext-CorePack(a;A_E,B_E),
   and Ract-CorePack(a;B_R).
2. SVD: insert actual constants into the d=3 two-block seed and run exact
   rational Gram searches for the 8 representative vertices; then global
   AP-CERT-sph/AP-AVG-sph.
3. CROW: derive J_p^<(R), prove the leading cancellation condition, and
   close FIC-HE-CROW[p,h] plus the frozen-background SP analogue.
4. RFTC: evaluate or sign the covariance rows for B_E omega, the
   coordinate-axis matrix, or the equal-coordinate Q_s rows; prove
   int A_E rho_2 dmu.
5. FC8: prove U_A10<=C d^-2, or the raw ODE/moment substitute, for the
   actual eta_i,z,B cutoff.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 eighth P1 contraction

Five Codex agents were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 frontiers.  The foreground pass added an exact rational generator for
the `d=3` two-block SVD Gram seed.  No background processes, daemons,
scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_corepack3_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_gram_search_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_fic_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_covariance_rows_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_raw_uA10_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_d3_gram_seed_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_2blk_d3_gram_seed.py`

P1 reductions:

```text
PAT:
  Ract-CorePack(a;B_R) reduces to Ract-GapCorePack(a;B_R,B_G) after
  closing the exact-gap subcase
    (h_+-h_-)^2 h_+^(-1/2) Phi(h_-) <= B_G(1+L_t)^4.
  The remaining PAT inputs are DLI-CorePack, Eext-CorePack, and
  Ract-GapCorePack.

SVD:
  The d=3 two-block SOS task is split into an interval-independent
  8-vertex Gram threshold computation mu_v and the scalar endpoint
  comparison W_I<=W_crit.  The foreground generator emits exact rational
  row, quartic, and affine Gram-template data.  The full-box seed is still
  undecidable until actual constants N+2, C, k_SR,p, Clebsch norms, L2,
  and U4 are inserted.

CROW:
  The natural all-k finite-interval cancellation theorem FIC-HE-CROW[p,h]
  is false.  The s=1 endpoint cancels, but the full pre-transfer
  coefficient has a nonzero null-soft k=2, lambda=0 leading term for both
  p=L and p=Q.  Only the rank-one finite-interval check FIC-R1-HE-CROW is
  supported.  The live task is a different multi-saturated-packet theorem,
  a missing scalar-reduction term, or a route around this scalar theorem.

RFTC:
  Coordinate-axis rows reduce to conditional profiles on
  y=diag(O S_0 O^T).  Equal-coordinate Q_s rows reduce to a
  one-dimensional diagonal-energy covariance with profile M_l(r;s,z).
  A monotonicity sign subcase is closed, and the remaining exact target is
  finite interval/quadrature certification for the four profiles, plus the
  separate density budget int A_E rho_2 dmu.

FC8:
  U_A10 is exactly rewritten as
    K_B int phi_gamma |A_d^(d+2)[(1-eta_N)P_A10^act]|.
  The pointwise good-frame proof reduces to the pure outer charge R_out
  plus transition charge R_tr.  Volume-tilted moment and bad-frame charges
  are separate.  The actual eta_i,z,B cutoff data are still missing.
```

Current next split:

```text
P1:
1. PAT: DLI-CorePack(a;B_L,B_D,c_D), Eext-CorePack(a;A_E,B_E),
   and Ract-GapCorePack(a;B_R,B_G).
2. SVD: insert actual constants into the d=3 exact generator, compute and
   rationally certify mu_v for the 8 vertices, then compare W_I<=W_crit.
3. CROW: abandon the false natural all-k FIC theorem; find the corrected
   multi-saturated scalar theorem, identify the missing scalar-reduction
   term, or route around CROW-scal[p].
4. RFTC: compute or sign the diagonal conditional profiles M_l(r;s,z) and
   coordinate deviation rows; prove int A_E rho_2 dmu.
5. FC8: prove R_out+R_tr<=C d^-2, or raw ODE/moment substitute, for the
   actual eta_i,z,B cutoff and active polynomial.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 ninth P1 contraction

Five Codex agents were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 frontiers.  The foreground pass added an analytic CROW leading
coefficient probe for the false natural finite-interval theorem.  No
background processes, daemons, scheduled tasks, launchers, or watchers were
created.

New/updated artifacts:

- `notes\p1_logdet_pat_gapcore_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_threshold_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_corrected_route_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_diag_profile_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_rbk_charge_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_fic_leading_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_he_crow_fic_leading_probe.py`

P1 reductions:

```text
PAT:
  Ract-GapCorePack(a;B_R,B_G) reduces to
  Ract-SepCorePack(a;B_R,B_G).  The balanced-pair part is empty when
    M_f(1-theta)^2 theta^(-3/2) <= B_G,
  M_f=25 sqrt(5)/216.  The pure determinant activation-Hardy target is
  false in the separated two-endpoint theta->0 limit.

SVD:
  No actual analytic constant packet is present yet.  The exact inputs are
  reduced to P_diag for diagonal triage and P_Gram for the full certificate.
  The full-box diagonal prefilter is K^2>=R_full.  After an exact Gram
  search, W_crit partitions the d=3 interval by the scalar roots of
  W(delta)=W_crit.

CROW:
  The k=2 null-soft obstruction is a real fixed-time scalar obstruction,
  not a boundary artifact.  The negative label is NS2-NoFixedCROW[p,h].
  The safe fixed-time subcase package is CROW-scal-safe[p,h].  The live
  route is integrated: CROW-TraceAudit[p], then ICROW-scal[p] and
  POC-scal-int[p].

RFTC:
  Equal-coordinate Q_s rows now require only raw conditional positive
  moments given R.  Coordinate-deviation rows reduce to one-dimensional
  profiles given T_b=(y_b-y_d)(y_b+y_d+c_s).  Several monotone, affine,
  constant-profile, orthogonality, and pair-swap sign/zero subcases are
  closed; int A_E rho_2 dmu remains separate.

FC8:
  R_out closes under OUT-rho:
    O_N subset {||t||>=rho_out}, rho_out^2>=A_out d log(e d).
  R_tr reduces to RBK-TR-Jet-sharp, the coarser RBK-TR-Jet, or a shell-jet
  condition.  Pointwise good-frame, volume-tilted moment, and bad-frame
  charges remain separate.
```

Current next split:

```text
P1:
1. PAT: DLI-CorePack(a;B_L,B_D,c_D), Eext-CorePack(a;A_E,B_E),
   and Ract-SepCorePack(a;B_R,B_G).
2. SVD: insert P_diag/P_Gram, test K^2>=R_full, then run the 8-vertex
   exact Gram search and compare W_I<=W_crit.
3. CROW: perform CROW-TraceAudit[p]; if no missing term appears, prove
   ICROW-scal[p] and POC-scal-int[p].
4. RFTC: compute/enclose the raw conditional positive moments given R and
   T_b profiles; prove int A_E rho_2 dmu.
5. FC8: prove OUT-rho and RBK-TR-Jet-sharp, or direct RBK scalars/moment
   substitute, for the actual eta_i,z,B cutoff and active polynomial.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 tenth P1 contraction

Five Codex agents were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 frontiers.  The foreground pass added a scalar threshold partition
helper for the `d=3` two-block SVD packet.  No background processes,
daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_sepcore_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_partition_next_attempt_2026_07_01.md`
- `notes\p1_logdet_he_crow_traceaudit_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_profile_density_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_out_rho_trjet_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_threshold_partition_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_2blk_threshold_partition.py`

P1 reductions:

```text
PAT:
  The exact small-m condition in the separated quotient-scale variable
  s=g/kappa deletes the middle band F_theta(s)>=beta_m.  Therefore
  Ract-SepCorePack(a;B_R,B_G) reduces to
  Ract-SepSMCorePack(a;B_R,B_G,beta_m), with residual support only on the
  two small-m branches determined by s_-(theta),s_+(theta).  The exact
  right-tail quotient has the same order as the crude C_R envelope, so that
  shortcut is false.

SVD:
  The d=3 two-block threshold layer is now exact.  For any rational
  threshold T, W(delta)<=T is certified by the integer endpoint sign
  S_T(p,q), with monotonicity supplied by the negative discriminant in W'.
  The helper emits threshold partitions, diagonal packet classifications,
  and exact interval pass/fail rows.  Actual P_diag/P_Gram constants and
  8-vertex Gram witnesses are still missing.

CROW:
  CROW-TraceAudit[p] found no concrete missing centered term in the current
  row normalization.  It reduces the audit to table identities (A1)-(C5),
  normalization checklist N1-N7, and the mandatory k=2 correction
  w_L(2)=sqrt(pi)/2, w_Q(2)=3sqrt(pi)/2.  With W_p=0 the fixed-time all-k
  obstruction remains, so the live route is ICROW-scal[p] plus
  POC-scal-int[p].

RFTC:
  The positive-part profile packet is replaced by R/T Raw2Mom.  On each
  R or T_b score cell, raw weighted moments int h V_a and int h V_a^2
  enclose the scalar and square rows using the sharp two-moment
  positive-part lemma with constant 1/2.  The density budget is reduced to
  WSOC2(A_E;b), or WSOC2(A_E^red;b) after ANIORB, with factor (1-b)^(-1).

FC8:
  The actual eta_i,z,B cutoff is not closed, but OUT-rho plus the
  transition-jet packet can be replaced for the current active A10 consumer
  by FC8-etaN-OUT/TR-ShellMoment.  This asks for a good-frame moment of
  Tail_{2d+14}(r_out)+E_tr at scale d^(-5) under the default
  A_sum(P)<=C d^3 coefficient growth, with bad-frame charge separate.
```

Current next split:

```text
P1:
1. PAT: DLI-CorePack(a;B_L,B_D,c_D), Eext-CorePack(a;A_E,B_E),
   and Ract-SepSMCorePack(a;B_R,B_G,beta_m), using the exact small-m branch
   support.
2. SVD: insert P_diag/P_Gram, classify by mu_full/mu_left and exact
   S_T(p,q) endpoint signs, then run the 8-vertex rational Gram search and
   compare W_I<=W_crit.
3. CROW: either complete the formal N1-N7 tensor-normalization audit and
   produce a nonzero k=2-cancelling W_p, or proceed directly with
   ICROW-scal[p] and POC-scal-int[p].
4. RFTC: prove the R/T Raw2Mom packet for V_L,V_Q,V_Q2,V_Q4 on the actual
   score cells, insert the row signs/costs, and prove WSOC2(A_E;b).
5. FC8: prove FC8-etaN-OUT/TR-ShellMoment for the actual eta_i,z,B cutoff,
   or return to pointwise OUT-rho plus RBK-TR-Jet-sharp; also close the
   separate bad-frame charge.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 eleventh P1 contraction

Five Codex agents were assigned to the sharpened PAT, SVD, CROW, RFTC, and
FC8 frontiers.  The foreground pass upgraded the `d=3` SVD threshold helper
so interval rows include exact integer endpoint signs and the integer
threshold polynomial coefficients.  No background processes, daemons,
scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_sepsm_branch_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_gram_next_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_poc_int_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_raw2mom_wsco2_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_shellmoment_eta_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_threshold_partition_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_2blk_threshold_partition.py`

P1 reductions:

```text
PAT:
  With 0<beta_m<1, beta_m(1+c_0)<1, and
  B_G>=B_G^branch(c_0,beta_m), the SepSM no-root region and lower branch
  are empty.  The compact theta>=delta high branch is absorbed.  The
  remaining separated blocker is Ract-SepHiTinyCorePack, supported only on
  theta<delta and g/kappa>s_+(theta).  The high-branch kappa-length gain
  alone is false in the theta->0 two-endpoint window.

SVD:
  The d=3 two-block row norm collapses from four rows to three:
  lxi=-3 l0/(7N2).  The SOS search packet is P_SOS=(r,a,b,c,A,B,D) with
  r=N2^(-2); K=Ck is separate and only enters the scalar threshold layer.
  The proof payload can be rational weighted squares checked by 15 exact
  ternary-quartic coefficient equalities per vertex.  The foreground
  threshold helper now emits T_num/T_den, G_T coefficients, and
  sign_lo/sign_hi=S_T(endpoint) for exact interval checking.

CROW:
  Trace-audit subcheck N2 is closed.  The CROW dual/Wick row normalization
  is R_i=c_i+sum_{j!=i}c_ij, so W_p=0 for N2.  The apparent
  6C_i+sum C_ij row is a primal Fischer-coordinate trace row, not a missing
  CROW term.  Fixed-time all-k remains blocked; live route remains
  ICROW-scal[p] plus POC-scal-int[p].

RFTC:
  R/T Raw2Mom reduces to PolySandwich-Raw2Mom: univariate polynomial
  sandwiches for score-cell weights plus exact polynomial-weight
  Haar/Weingarten arrays A_0^Z,A_1,a^Z,A_2,a^Z and L2/L4 envelopes.  Small
  score-mass cells can be closed or paid by explicit L2/L4 constants.
  WSOC2(A;b) reduces to WEc(A)+WH2(A)+Wbar2(A) with exact Young-split
  constants.

FC8:
  FC8-etaN-OUT/TR-ShellMoment reduces to
  FC8-etaN-NearRadiusJetMoment.  With rho_N the whitened Euclidean inradius
  of the real near Cramer zone and J_eta the finite transition-jet
  generator, the good-frame scalar is
  Theta_eta=(1+J_eta)Tail_{2d+14}(rho_N).  Existing notes imply
  r_out,r_tr>=rho_N, but not the needed lower bound on rho_N, width, jets,
  or the L^r moment.  Bad-frame charge remains separate.
```

Current next split:

```text
P1:
1. PAT: DLI-CorePack(a;B_L,B_D,c_D), Eext-CorePack(a;A_E,B_E), and
   Ract-SepHiTinyCorePack(a;B_R,B_G,beta_m,c_0,delta), requiring a genuine
   theta^(1/2) gain, companion activation, or cancellation.
2. SVD: insert P_SOS=(r,a,b,c,A,B,D), find rational weighted-square
   witnesses for the 8 vertices, then insert K and use exact S_T endpoint
   signs for W_I<=W_crit.
3. CROW: close N1,N3,N4,N5,N6,N7, then prove ICROW-scal[p] starting with
   NSk-ICROW[p,h], and prove POC-scal-int[p] via Common-FTC-int({p}).
4. RFTC: build polynomial sandwiches for the chosen R/T cells, compute the
   Weingarten moment arrays, close/pay small-mass cells, and prove
   WEc(A)+WH2(A)+Wbar2(A).
5. FC8: prove FC8-etaN-NearRadiusJetMoment, or pointwise sufficient
   geometry for rho_N, transition width, and jets through order 2d+4; also
   close the separate bad-frame charge.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 twelfth P1 contraction

Five Codex agents were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 frontiers.  The foreground pass added an exact checker for the `d=3`
two-block weighted-square SVD certificates.  No background processes,
daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_hitiny_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_weightedsq_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_next_identity_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_polysandwich_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_nearradiusjet_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_weightedsq_checker_probe_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_2blk_weightedsq_checker.py`

P1 reductions:

```text
PAT:
  On every bounded g=theta H shell, Ract-SepHiTinyCorePack reduces to
  Tiny-Companion-Reserve_I(a), a one-dimensional companion determinant
  reserve supplying exactly the missing theta^(1/2) gain.  Failure of that
  reserve localizes the residue to delayed-isolated companion profiles.
  The signed right-tail quotient shortcut is false because P_kappa>=0 on
  the live monotone right tail and has the same endpoint size as the
  absolute quotient.

SVD:
  The weighted-square route now has explicit rational witness families for
  the rank-one 22 packet and the pure 44 -> H2 degenerate packet.  A
  generic row-domination algorithm produces rational weighted squares by
  finding lambda_i with lambda_i G_E +/- R_i PSD and multiplying rational
  quadratic-factor decompositions.  The foreground checker verifies any
  submitted witness by exact equality of the 15 quartic coefficients.

CROW:
  Trace-audit N5 is closed: the product-rule coefficients are exact with
  derivative signs DM=-K1, D^2M=-DK1, D2M=-T1.  N6 is closed for the ICROW
  profile class H=Lop F_alpha and H=Qop F_alpha, with no M-transfer
  boundary correction.  Remaining audit checks are N1,N3,N4,N7.

RFTC:
  The polynomial score-cell packet is corrected to use signed polynomial
  minorants.  Nonzero global nonnegative lower sandwiches are impossible
  for interior cells.  SignedBernstein-PolySandwich gives a constructive
  degree/error schedule and terminates for every boundary-null R/T score
  cell with a positive interval budget.  The exact arrays are
  B_0^Z[0..2n], B_1,a^Z[0..n], B_2,a^Z[0..n].

FC8:
  FC8-etaN-NearRadiusJetMoment reduces to NRJ-ExpMoment:
    ||exp(log(1+J_eta)+(A_R d log(e d)-rho_N^2)_+/4)1_G||_L^r
      <= exp(C_X d log(e d)).
  A pointwise ball/width/jet schedule, including the radial Gaussian-shell
  schedule when the displayed radius gap holds, implies the required
  d^(-5) cutoff moment.  The actual row-law cutoff is still too
  underspecified to prove rho_N, width, or jets directly.
```

Current next split:

```text
P1:
1. PAT: prove Tiny-Companion-Reserve_I(a) from quantitative companion
   log-determinant/root-packing, or prove failure forces a sparse isolated
   endpoint profile that can be paid separately.
2. SVD: insert actual P_SOS, run the row-domination algorithm and checker;
   if conservative, fall back to the sharper six-variable Gram search and
   recover checker-compatible rational squares.
3. CROW: close N1,N3,N4,N7, then prove ICROW-scal[p] starting with
   NSk-ICROW[p,h], and prove POC-scal-int[p] via Common-FTC-int({p}).
4. RFTC: choose the actual R/T score partition and budgets, generate
   SignedBernstein sandwiches, compute B_0/B_1/B_2 Weingarten arrays, and
   prove WEc(A)+WH2(A)+Wbar2(A).
5. FC8: prove NRJ-ExpMoment or its pointwise ball/width/jet schedule for
   the real eta_i,z,B cutoff; also close the separate bad-frame charge.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 thirteenth P1 contraction

Five Codex agents were assigned to the next PAT, SVD, CROW, RFTC, and FC8
frontiers.  Four branches returned and were integrated into the P1 DAG.
The PAT reserve branch did not produce its assigned note before shutdown,
so it remains an unadvanced blocker for the next pass.  The foreground pass
also added a contract note and a built-in self-test for the SVD
weighted-square checker.  No background processes, daemons, scheduled
tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_thirteenth_split_contracts_2026_07_01.md`
- `notes\p1_logdet_svd_2blk_rowdom_generator_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_traceaudit_remaining_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_signed_bernstein_arrays_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_nrj_expmoment_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_2blk_weightedsq_checker.py`
- `numerics\p1_svd_2blk_rowdom_generator.py`
- `numerics\p1_rftc_signed_bernstein_probe.py`

P1 reductions:

```text
SVD:
  Added an exact rational row-domination generator that emits CSV
  certificates accepted by the 15-coefficient weighted-square checker.
  It supports direct P_SOS rows, packet CSV input, or source constants
  N2,L2,U4,chi22_2,chi24_2,chi44_2,chi22_4,chi24_4,chi44_4.
  Degenerate and diagnostic packets pass the checker.  The checker now has
  a built-in self-test covering all eight zero-eta vertices plus one
  deliberate failing vertex.

CROW:
  The remaining trace-audit checks N1,N3,N4,N7 are closed.  Together with
  the earlier N2,N5,N6 closures, the whole N1-N7 audit finds W_p=0.  The
  fixed-time all-k CROW obstruction remains real, so the live scalar route
  is the integrated package ICROW-scal[p] + POC-scal-int[p] plus the
  determinant-tilted integrated soft-rank average.

RFTC:
  The SignedBernstein packet now has a concrete first-order form: minimal
  R/T support-sign cells, a RowCert budget gate, exact B_0/B_1/B_2 arrays
  defined by orthogonal Weingarten word contractions, and a bounded exact
  probe.  The default R toy arrays are B0=(1,2/5,64/315), B1=(0,0),
  B2=(1/20,8/315); the T toy arrays are B0=(1,0,38/2205), B1=(0,0),
  B2=(1/20,19/2205).

FC8:
  NearRadiusJetMoment is reduced to a weaker jet-taxed radius invariant.
  With rho_J^2=rho_N^2-4 log(1+J_eta), it suffices to prove
    ||exp((A_J d log(e d)-rho_J^2)_+/4)1_G||_L^r
       <= exp(C_JX d log(e d)),
  with A_J/4 >= C_T+C_JX+C_BK+C_K+2+a.  Equivalently, the pointwise
  schedule is rho_N^2 >= A_J d log(e d)+4 log(1+J_eta).  A gauge form
  eta_N=u(g_N) reduces real-cutoff verification to gauge inradius and
  transition derivative scale.
```

Current next split:

```text
P1:
1. PAT: finish Tiny-Companion-Reserve_I(a), or prove its failure forces a
   sparse delayed-isolated endpoint profile with explicit payment.
2. SVD: insert the actual analytic P_SOS constants and P_scale=(K), run the
   row-domination generator/checker on all eight vertices, and compare
   W_crit=K^2/(81 mu_bar) with the scalar endpoint partition.
3. CROW: prove ICROW-scal[p], especially NSk-ICROW[p,h], prove
   POC-scal-int[p], and close the determinant-tilted integrated soft-rank
   average.
4. RFTC: insert the actual V_L,V_Q,V_Q2,V_Q4 cap-row word lists, assign
   row budgets beta_l, certify sharp T_b support intervals if needed, run
   the real degree schedule, and separately prove WEc(A)+WH2(A)+Wbar2(A).
5. FC8: prove the jet-taxed radius moment for the actual eta_i,z,B cutoff,
   or supply a defining Cramer gauge g_N whose inradius and transition
   derivative scale imply it; still close the separate bad-frame A10 charge.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 fourteenth P1 contraction

Five Codex agents were assigned to the live PAT, SVD, CROW, RFTC, and FC8
frontiers.  SVD, CROW, RFTC, and FC8 returned and were integrated into the
P1 DAG.  The PAT worker did not produce its assigned note before shutdown;
the foreground pass advanced PAT by rewriting the tiny reserve as an exact
shell-Carleson condition.  No background processes, daemons, scheduled
tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_tcr_carleson_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_psos_constant_audit_2026_07_01.md`
- `notes\p1_logdet_icrow_nsk_kernel_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_actual_wordlist_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_actual_gauge_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_psos_constant_audit.py`
- `numerics\p1_rftc_wordlist_schema.py`

P1 reductions:

```text
PAT:
  Tiny-Companion-Reserve_I(a) is equivalent to a weighted shell-Carleson
  condition.  With dmu_a=D_c L^a(1+L)^4 H^(-2)dH, the reserve is exactly
  int_{I/theta}(1+L)^(-4)dmu_a <= C_I theta^(3/2)mu_a((0,infty)).
  The pointwise activation certificate requires the aggregate activation
  tau^2 g_0/(r_p theta)+sum_k log(1+q_k g_0/theta) to supply one
  determinant dimension by the shell.  Failure is now a delayed-isolated
  profile with too much reserve mass at H approx 1/theta and subcritical
  aggregate activation.

SVD:
  The P_SOS audit confirms no analytic packet is present.  Missing are
  N2,L2,U4, chi22_2(3), chi24_2(3), chi44_2(3),
  chi22_4(3), chi24_4(3), chi44_4(3), or direct r,a,b,c,A,B,D.
  Current files contain formulas and diagnostic placeholders only, so no
  proof packet CSV can be emitted without inventing constants.

CROW:
  NSk-ICROW[p,h] now has an explicit one-dimensional signed-kernel form.
  The q<=q_0(h)=1/h-1/2 part is closed by the fixed-time safe package, and
  endpoints k=1,l=0,r_*=0 are inherited closures.  The deep sector reduces
  to NSk-Kernel[p,h] for p=L,Q, k>=2, theta>=0, with explicit kernels
  K_L,k,h(theta), K_Q,k,h(theta) and data M_k(theta), D_p,k,h(theta).

RFTC:
  Added a JSON word-list schema and concrete adapters: exact indexed score
  words for R and T_b, plus scalar row adapters
  V_p=<K_2(z),O M_{p,2}>+<K_4(z),O M_{p,4}> for p=L,Q.
  Full B_1/B_2 evaluation is blocked by missing machine-readable K2_z,K4_z,
  M_L_2,M_L_4,M_Q_2,M_Q_4, and finite indexed V_Q2,V_Q4 expansions.
  beta_l budgets and sharp T_b supports are downstream acceptance inputs.

FC8:
  The actual eta_i,z,B notes do not define a usable gauge g_N.  The formal
  Minkowski functional of N_i,z,B is insufficient without star-shapedness,
  smooth/profile cutoff equality, collar, and derivative-scale hypotheses.
  The exact missing input is FC8-etaN-JetTaxedRadiusRowLaw for
  rho_N^2-4log(1+J_eta), or a quantitative FC8-CramerGaugeCutoff plus the
  row-law moment for the gauge-taxed radius.  Bad-frame charge remains
  separate.
```

Current next split:

```text
P1:
1. PAT: prove the shell-Carleson reserve condition from root packing, or
   pay the delayed-isolated reserve-mass profile with theta^(3/2) shell
   cost and subcritical aggregate activation.
2. SVD: produce the actual analytic P_SOS source constants and P_scale=(K);
   then run the row-domination generator/checker and endpoint comparison.
3. CROW: prove NSk-Kernel[p,h], starting with p=L,Q at k=2,theta=0, then
   complete POC-scal-int[p] and the integrated soft-rank average.
4. RFTC: supply K2_z,K4_z,M_L_2,M_L_4,M_Q_2,M_Q_4 and V_Q2/V_Q4 indexed
   word lists; then evaluate B arrays, choose beta_l/T_b supports, and
   prove WEc(A)+WH2(A)+Wbar2(A).
5. FC8: add FC8-CramerGaugeCutoff with row-law moment for rho_g,J, or
   prove FC8-etaN-JetTaxedRadiusRowLaw directly; separately close the A10
   bad-frame charge.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 sixteenth P1 contraction

Five Codex workers were assigned to the current PAT, SVD, CROW, RFTC, and
FC8 blockers, while the foreground pass advanced the complementary CROW
all-`k` endpoint.  All five workers returned and their results were
integrated into the P1 DAG.  No background processes, daemons, scheduled
tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_tcr_deficiency_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_clebsch_generator_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_nsk_kernel_theta0_allk_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_nsk_kernel_k2theta_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_tensor_coefficients_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_badframe_charge_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_clebsch_generator.py`
- `numerics\p1_icrow_nsk_kernel_k2theta_probe.py`
- `numerics\p1_rftc_tensor_coefficient_probe.py`

P1 reductions:

```text
PAT:
  Bounded Def_n is false in the pure two-endpoint delayed profile:
  B_n=0, L_n^+=O_I(1), and Def_n=n log 2+O_I(1).  The high-tail HiTiny
  payment is nevertheless summable.  With
  R_a^hi(theta;H_0)=int_{H_0}^infty D_c L_theta^a(1+L_theta)^4 H^(-2)dH,
  root entropy gives L_n^+<=C_I(1+B_n), R_a^hi is uniformly bounded, and
  Pay_n^hi<=C theta_n.  Remaining step: insert this dyadic payment into
  the HiTiny consumer with the high-tail reserve matching H>=H_0.

SVD:
  The finite d=3 Clebsch generator is implemented.  It emits exact rational
  maps and conservative certified square bounds:
  chi22_2^2<=40/7, chi24_2^2<=15, chi44_2^2<=325440/5929,
  chi22_4^2<=332/49, chi24_4^2<=82680/5929,
  chi44_4^2<=72035406/1002001.  The constants validator and one rowdom
  checker smoke path accept the generated ceilings.  Still missing:
  ledger-certified N2, the actual atom source for L2 and U4, and the
  separate scalar P_scale=(K).

CROW:
  NSk-Kernel[p,h] is now closed on two large boundary pieces.  The
  theta=0 endpoint is closed for p=L,Q and all k>=2 with crude
  C_h=1/h in 0<h<=1.  The full k=2 sector is closed for all theta>=0:
  compact theta follows from continuity and positive denominators, and the
  large-theta boundary gives R_p,h(theta)<=C_p,h theta^(-4).  The remaining
  CROW NSk blocker is only k>=3 with theta>0.

RFTC:
  The tensor-slot blocker is sharpened to a producer packet:
  cap_quartic_source.entries for K4_z^perp, raw Schur sources
  C_i^L,C_ij^L,C_i^Q,C_ij^Q, and q_rows.Q2/Q4 word-list packets with
  degree bounds plus HB/u data.  The extractor now implements
  K4_z^perp -> K2_z,K4_z and C_i^p,C_ij^p -> M_p_2,M_p_4.  No actual
  coefficients were found; the validator is no longer the blocker.

FC8:
  The bad-frame charge has explicit sufficient theorems.  BF-envelope pays
  the charge from U_A10<=M_bad(d) on G^c and
  E[Z_i 1_Gc]<=C d^(-2)/M_bad(d).  HolderMass and three-factor versions
  replace this by volume-tilt, raw-scalar moment, and rare-event bounds;
  the same split applies to R_out/R_tr.  Still missing for the actual
  cutoff: M_bad or an L^s raw-scalar moment, a strong enough bad-event
  mass, or the direct scalar E[Z_i U_A10 1_Gc]<=C d^(-2).  The good-frame
  JTR/Cramer-gauge row law remains separate.
```

Current next split:

```text
P1:
1. PAT: insert the high-tail dyadic payment Pay_n^hi into the HiTiny
   consumer, replacing the per-shell TCR demand without extra loss; if the
   ledger keeps the untruncated R_a, add the low-endpoint normalization.
2. SVD: supply N2 and the actual fourth-cumulant atom list/source for L2
   and U4, then run constants-json through rowdom/checker and P_scale.
3. CROW: prove NSk-Kernel[p,h] for k>=3 and theta>0, using the closed
   theta=0 endpoint and large-theta/compact-theta strategy where possible.
4. RFTC: supply the producer packet fields for K4_z^perp, Schur sources,
   and Q2/Q4 rows; then emit tensor slots and evaluate B/density arrays.
5. FC8: prove the actual good-frame JTR/Cramer row law and the actual
   bad-frame BF-min or direct bad scalar for eta_i,z,B.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 seventeenth P1 contraction

Five Codex workers were assigned to the PAT, SVD, CROW, RFTC, and FC8
frontiers.  The foreground pass proved the complementary large-theta CROW
sector.  All worker results were integrated into the P1 DAG.  No background
processes, daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_hitiny_payment_insertion_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_source_constants_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_nsk_kernel_compacttheta_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_nsk_kernel_largetheta_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_producer_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_actual_rowlaw_badmass_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_source_constant_audit.py`
- `numerics\p1_icrow_nsk_kernel_compacttheta_probe.py`
- `numerics\p1_rftc_producer_packet_audit.py`

P1 reductions:

```text
PAT:
  The high-tail payment cannot be inserted into the current HiTiny consumer
  as written.  On a bounded shell, the positive HiTiny kernel charges
  K_n(I) approx theta_n^(-3/2)nu_n^hi, so the consumer still needs
  theta_n^(-3/2)nu_n^hi<=C R_a^hi.  The summable payment only gives
  theta_n^(3/2)exp(Def_n/2)R_a^hi.  In the pure delayed profile,
  Pay_n^hi approx theta_n but K_n(I) approx theta_n^(-1/2).  The next PAT
  input must be a structural improvement before the positive HiTiny kernel
  or a revised consumer with an actual outer theta_n^(3/2) dyadic weight.

SVD:
  The source audit confirms no complete constants JSON, atom JSON, direct
  checker packet, or ledger-certified SVD N2 exists.  It isolates a
  coordinate-isotropic candidate: for d=3,
  T=kappa sum_b e_b^(tensor 4) gives L2_square_exact=0 and
  U4_square_exact=(16/525)kappa^2.  This remains only a template until
  kappa, source-binding proof, and N2=N+2 are supplied.

CROW:
  NSk-Kernel[p,h] is now closed for p=L,Q, all k>=2, theta>=0, and
  0<h<=1.  Previous notes closed theta=0 all-k and k=2 all-theta.  The new
  compact-theta proof closes k>=3, 0<=theta<=1 with C_h<=C_*/h.  The
  foreground large-theta proof closes k>=2, theta>=1 by a swapped-kernel
  boundary-layer estimate and a short q-interval denominator lower bound.
  Thus NSk-ICROW[p,h] is closed in the standard hard-edge window.

RFTC:
  Added a producer-packet provenance audit.  It emits permissive source
  hooks and a strict failing sample that rejects exactly the absent fields:
  cap_quartic_source.entries, schur_sources.L/Q.C_i, and Q2/Q4
  word_list, degree_bound, HB, and u.  No analytic producer coefficients
  were recoverable.

FC8:
  The actual cutoff-independent subcase P_A10^act=0 is closed: then
  U_A10=R_out=R_tr=0 for every eta_i,z,B, so good-frame and bad-frame A10
  leakage vanish without JTR, gauge, M_bad, or bad-event mass.  For any
  nonempty active A10 list, the exact remaining packet is still actual
  eta_i,z,B JTR/gauge plus BF-min or the direct bad scalar.
```

Current next split:

```text
P1:
1. PAT: bypass the positive HiTiny kernel scale mismatch by proving
   cancellation/structure before line (7), or reformulate the consumer with
   an outer dyadic theta_n^(3/2) payment weight.
2. SVD: certify N2 and bind the coordinate-isotropic atom source, or supply
   another accepted atom/direct L2,U4/P_SOS source packet.
3. CROW: with NSk-ICROW closed, advance POC-scal-int[p] and the
   determinant-tilted integrated soft-rank average.
4. RFTC: supply actual producer data for K4_z^perp, Schur C_i/C_ij arrays,
   and Q2/Q4 row packets; then run tensor slot and B/density array tools.
5. FC8: for nonempty A10, prove the actual eta_i,z,B JTR/gauge row law
   and BF-min/direct bad scalar; otherwise use the closed empty-active-list
   subcase.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 eighteenth P1 contraction

No background processes, daemons, scheduled tasks, launchers, or watchers
were created.

New/updated artifacts:

- `notes\p1_logdet_pat_hitiny_structure_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_parametric_source_attempt_2026_07_01.md`
- `notes\p1_logdet_icrow_soft_rank_average_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_scal_int_rowcert_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_missing_source_manifest_2026_07_01.md`
- `notes\p1_logdet_fc8_active_growth_strata_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_pat_hitiny_structure_probe.py`
- `numerics\p1_svd_parametric_source_scan.py`
- `numerics\p1_poc_scal_int_rowcert_probe.py`
- `numerics\p1_rftc_missing_source_manifest.py`

P1 reductions:

```text
PAT:
  The revised weighted HiTiny consumer is closed:
  sum_n theta_n^(3/2) K_n(I) is payable by the existing high-tail dyadic
  payment.  The current unweighted positive kernel has no remaining
  cancellation source after the m^2, monotone right-tail quotient, and
  positive kappa-kernel reductions.  The pure delayed two-endpoint profile
  is a sharp countermodel: Pay_n^hi approx theta_n but
  K_n(I) approx theta_n^(-1/2).  PAT still needs an upstream consumer that
  exposes the theta_n^(3/2) weight, a genuinely new pre-positive-kernel
  identity, or a structural hypothesis excluding the countermodel.

SVD:
  The coordinate-isotropic source path is now conditional and executable.
  If T=kappa sum_b e_b^(tensor 4) is the active d=3 source and a positive
  rational N2 is supplied, the tool emits constants/P_SOS/checker packets
  with L2=0, U4_q=ceil(q sqrt(16 kappa^2/525))/q, and the explicit
  r,A,B,D formulas.  Smoke values kappa=6/5, N2=5, q=1000 pass the exact
  checker, but no actual kappa, source-binding proof, or ledger-certified
  N2 was recovered.

CROW:
  The determinant-tilted integrated soft-rank average is closed by the
  existing RSA/KCB budgets SR_L^int=m_R K^B[L_t(1+L_t)^4] and
  SR_Q^int=m_R K^B[L_t^2(1+L_t)^4].  Together with the closed N1-N7 audit
  and NSk-ICROW package, this closes ICROW-scal[p].  POC-scal-int[p] is
  reduced to the one-row integrated RFTC certificate [J_p^int]_+ plus the
  density budget int a_p^int rho_2 dmu.  The abstract rowcert reduction and
  several sign/orthogonality subcases are closed; actual integrated tensor
  slots or direct covariance rows, the [B_p^int omega]_+ payment, and the
  weighted density budget remain.

RFTC:
  Added a missing-source manifest checker.  The current provenance packet
  is accepted only as expected_missing_only: permissive validation has no
  errors and strict validation fails only on the manifest fields
  cap_quartic_source.entries, Schur C_i/C_ij sources, and Q2/Q4 word_list,
  degree_bound, HB, and u.  No analytic producer coefficients were found.

FC8:
  Nonempty A10 leakage is stratified by coefficient growth a=0,1,2,3.
  The good-frame request is sharpened to
  Delta_J L_d >= (2+a) log d+O(1), and the factorized bad-frame request is
  d^(-2-a)/M_eta.  The default P_334-deleted nonempty case closes as the
  a=2 coefficient-growth packet, improving the cutoff/BF-min scale from
  d^(-5) to d^(-4).  The actual eta_i,z,B JTR/gauge source and actual
  bad-frame scalar or BFmin_a remain missing.
```

Current next split:

```text
P1:
1. PAT: supply an upstream pair/dyadic consumer with the outer
   theta_n^(3/2) HiTiny weight, or a new pre-positive-kernel identity.
2. SVD: bind the coordinate-isotropic fourth-cumulant source by proving the
   real kappa and ledger N2, or provide an accepted atom/direct P_SOS packet.
3. CROW/POC: finish POC-scal-int[p] by supplying integrated scalar tensor
   slots or direct covariance rows, the [B_p^int omega]_+ sign/payment, and
   the weighted density budget.
4. RFTC: fill the manifest fields with actual K4_z^perp producer data,
   Schur C_i/C_ij arrays, and Q2/Q4 row packets; then rerun the tensor and
   missing-source consumers.
5. FC8: for nonempty A10, prove the real eta_i,z,B JTR/gauge row law and
   the matching stratum-specific BFmin_a or direct bad scalar; empty active
   lists remain closed.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 nineteenth P1 contraction

Five Codex workers were assigned to the current PAT, SVD, CROW/POC, RFTC,
and FC8 frontiers, while the foreground pass reduced the integrated POC
density budget.  No background processes, daemons, scheduled tasks,
launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_weighted_consumer_source_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_n2_kappa_binding_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_int_density_wsco2_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_int_tensor_rows_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_producer_source_search_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_stratum_source_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_svd_n2_kappa_audit.py`
- `numerics\p1_poc_int_tensor_rows_probe.py`
- `numerics\p1_rftc_producer_source_search.py`

P1 reductions:

```text
PAT:
  No legal existing upstream weighted dyadic or pair-ratio consumer was
  found.  The chain remains fixed-pair down to Ract-SepHiTinyCorePack; the
  dyadic indices already present are activation levels, not outer
  pair-ratio shell sums.  The exact missing insertion point is before
  K_n(I)<=C theta_n^(-3/2)nu_n^hi, because after that conversion the
  available theta_n^(3/2) payment cannot be recovered.

SVD:
  A stricter audit reports status=both_missing.  N2=5 cannot be promoted
  from the d=3 two-block normalization: N is the separate orientation-sphere
  dimension in the (N+2)^(-1) source, and no checked note identifies N=3.
  Kappa is also unbound; row-law kappa_4 examples are not active SVD atom
  bindings.

CROW/POC:
  The scalar POC row source is now separated from larger RFTC Q2/Q4 word
  rows.  A direct-row validator checks active, coordinate, and
  equal-coordinate packets and computes [B_p^int omega]_+/[8(N+2)].  The
  current scalar source check has only expected holes:
  cap_quartic_source.entries and Schur L/Q C_i.  The foreground density
  pass reduces int a_p^int rho_2 dmu to POC-WSOC2[p,A;b], i.e.
  WEc(A)+WH2(A)+Wbar2(A) for A_p^row or A_p^KCB.  If rho_2=0, the density
  side closes with D_p^int=0.

RFTC:
  A repo-wide source-search audit found no complete source packet or atom
  packet.  Current candidate hooks are formulas, templates, diagnostics,
  downstream adapters, or closed subcases.  The producer blocker is actual
  analytic data, not a missing schema or search path.

FC8:
  The prioritized nonempty P_334-deleted a=2 source packet is now exact.
  Good frames need actual eta_i,z,B JTR/gauge data with the a=2 gap; bad
  frames need either the direct scalar E[Z_i U_A10 1_Gc]<=C d^(-2) or
  U_A10<=C d^2 M_eta plus BFmin_2 at d^(-4)/M_eta.  The audit table shows
  coefficient growth/interfaces are present, while actual JTR/gauge and
  bad-frame sources are absent.
```

Current next split:

```text
P1:
1. PAT: create a genuinely new upstream weighted HiTiny consumer, or a
   pre-positive-kernel identity before the theta_n^(-3/2) reserve conversion.
2. SVD: certify the orientation dimension N and N2=N+2, and bind kappa to
   the active SVD source; alternatively provide an accepted atom/direct
   P_SOS packet.
3. CROW/POC: supply scalar POC direct rows or scalar producer data
   (K4_z^perp plus Schur C_i/C_ij for L,Q), prove sign/payment for
   [B_p^int omega]_+, and prove POC-WSOC2[p,A;b] unless rho_2=0.
4. RFTC: provide actual K4_z^perp entries or atom producer, evaluated
   integrated Schur arrays, and finite V_Q2/V_Q4 row packets with
   degree_bound, HB, and u.
5. FC8: close the nonempty a=2 packet by proving actual eta_i,z,B
   JTR/gauge plus B-direct-a2 or B-env-a2+BFmin_2; then lift to other
   nonempty growth strata as needed.

P2:
  Still closed under G_r^sat.  Optional only: SCDE(r) for a smaller exact
  labelled atlas, or final proof/citation assembly.
```

## Continuation update, July 1 twentieth integration

Five Codex workers were assigned to the PAT, SVD, CROW/POC, RFTC, and FC8
frontiers, while the foreground pass assembled the P2 final dependency and
citation map.  No background processes, daemons, scheduled tasks, launchers,
or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_upstream_weighted_consumer_design_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_orientation_dimension_contract_2026_07_01.md`
- `notes\p1_logdet_poc_scalar_schur_source_contract_2026_07_01.md`
- `notes\p1_logdet_rftc_q24_row_packet_contract_2026_07_01.md`
- `notes\p1_logdet_fc8_a2_actual_source_contract_2026_07_01.md`
- `notes\all_apex_square_p2_final_dependency_assembly_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`
- `numerics\p1_pat_weighted_consumer_contract.py`
- `numerics\p1_svd_orientation_dimension_contract.py`
- `numerics\p1_poc_scalar_schur_source_contract.py`
- `numerics\p1_fc8_a2_source_contract.py`

P1 reductions:

```text
PAT:
  The legal upstream replacement is now isolated as
  Ract-SepHiTinyWeightedShellCorePack_I(a;...), inserted at the
  SepSM-to-HiTiny handoff before
  K_n(I)<=C theta_n^(-3/2) nu_n^hi.  The new checker accepts only a true
  pair-ratio shell consumer with the outer theta_n^(3/2) payment attached
  before positive-kernel conversion; activation-level and post-conversion
  rewrites are rejected.  This is a precise source theorem request, not a
  proof of the missing upstream pair-summed algebra.

SVD:
  The orientation/source contract is machine-specified as
  p1_svd_orientation_n2_proof.v1.  Existing artifacts still cannot certify
  N2=5: d=3 fixes the two-block column/harmonic quotient, while N is the
  separate orientation row dimension in the (N+2)^(-1) source.  Kappa also
  remains unbound to an active SVD source.  Accepted exits are an
  orientation proof plus atom/source binding, a complete atom packet, or a
  direct checker-style P_SOS packet.

CROW/POC:
  The scalar Schur source contract is separated from RFTC Q2/Q4 row packets
  and now requires K4_z^perp plus C_i/C_ij for L and Q.  Missing C_ij is
  reported explicitly instead of being hidden behind the first missing C_i.
  A real subcase is closed: if the active residual spectrum is scalar, then
  C_i^p=gamma_p and C_ij^p=2 gamma_p emit zero M_p_2/M_p_4 slots, so
  F_p^int=0, B_p^int omega=0, and the row-envelope density cost is zero.
  The live non-scalar case still needs actual source arrays, row sign/payment,
  and POC-WSOC2 unless rho_2=0.

RFTC:
  The Q2/Q4 row-packet blocker is now an explicit contract.  Current tools
  provide schemas, diagnostics, direct-NCR cumulant words, scalar V_L/V_Q
  adapters, and downstream square-row algebra, but not finite indexed
  Schur-word expansions for V_Q2/V_Q4 with degree_bound, HB, and u.
  A future producer must supply those rows directly or give an atom packet
  that lowers to them.

FC8:
  The nonempty P_334-deleted a=2 packet is now validated by
  fc8-a2-source-contract/v1.  Coefficient growth and interfaces are present,
  but the actual good-frame JTR/gauge source and the actual bad-frame
  direct/envelope source are still absent.  The contract requires actual
  eta_N, shared event G, good data through rho_J or rho_g,J, and bad data
  through B-direct-a2 or M_eta plus BFmin_2.
```

P2 assembly:

```text
The final dependency note records the closed route under two explicit
conventions:

1. Use the saturated exact labelled incidence atlas G_r^sat for the fixed-r
   zero-fresh endpoint proof.
2. Import the fixed-k private Laguerre hard-edge package through
   P2-SQ-PrivateLaguerreJanossy2-Uniform, hence P2-SQ-CHE-L2k(k).

Under those conventions, P2-SQ-HardEdge-Poisson is closed by the existing
pair base, PairConditioned-CCI, routed-sector, saturated zero-fresh,
fixed-k Venn, clean fixed-k, and factorial-moment assemblies.

Optional alternatives:
  If a smaller exact labelled atlas replaces G_r^sat, prove SCDE(r).
  If the private Laguerre package is not imported, internalize
  P2-SQ-CHE-L2k(k).
```

Current next split:

```text
P1:
1. PAT: prove Ract-SepHiTinyWeightedShellCorePack_I(a;...) from the
   upstream pair-summed PAT algebra, or produce a pre-positive-kernel
   identity that cancels the sharp delayed two-endpoint profile.
2. SVD: submit a valid p1_svd_orientation_n2_proof.v1 plus active kappa/
   atom binding, or provide an accepted direct P_SOS/atom packet.
3. CROW/POC: for the non-scalar case, supply K4_z^perp and Schur C_i/C_ij
   arrays for L,Q, then prove row sign/payment and POC-WSOC2; scalar
   residual spectrum is already a zero-cost subcase if it is the active one.
4. RFTC: provide actual finite V_Q2/V_Q4 row packets with degree_bound,
   HB, and u, or an atom producer that lowers to those packets.
5. FC8: satisfy fc8-a2-source-contract/v1 by proving actual eta_i,z,B
   JTR/gauge good-frame data and either B-direct-a2 or M_eta+BFmin_2 for
   bad frames.

P2:
  Closed under G_r^sat plus the imported fixed-k private Laguerre package.
  Optional only: SCDE(r) for a smaller atlas, or internal proof of
  P2-SQ-CHE-L2k(k) if the private Laguerre package is not imported.
```

## Continuation update, July 1 twenty-first integration

Five Codex workers were assigned to the sharpened PAT, SVD, CROW/POC, RFTC,
and FC8 contracts, while the foreground pass wrote a paper-facing P2 proof
skeleton.  No background processes, daemons, scheduled tasks, launchers, or
watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_weighted_shell_corepack_proof_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_orientation_n2_proof_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_schur_arrays_derivation_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_q24_row_producer_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_a2_source_proof_attempt_2026_07_01.md`
- `notes\all_apex_square_p2_paper_proof_skeleton_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`
- `numerics\p1_pat_weighted_shell_corepack_probe.py`
- `numerics\p1_svd_orientation_n2_probe.py`
- `numerics\p1_rftc_q24_row_producer.py`
- `numerics\p1_fc8_a2_source_probe.py`

P1 reductions:

```text
PAT:
  The weighted HiTiny core pack is now conditionally proved from the
  explicit new source exposure WeightedSepSMExposure_I(a).  A no-free-weight
  countermodel rules out obtaining the theta_n^(3/2) factor by positive
  dyadic regrouping, finite-overlap shell partitioning, or post-kernel
  reweighting.  The remaining PAT task is therefore to prove the weighted
  exposure itself or find pre-positive-kernel cancellation.

SVD:
  No p1_svd_orientation_n2_proof.v1 or accepted source packet was produced.
  A strict probe shows the existing two-block checker accepts the same
  nonzero degenerate 22-channel d=3 packet with supplied N2=5 and supplied
  N2=6.  Thus the checker layer treats N2 as an external scalar via
  r=N2^(-2) and cannot derive N2=5.  The irreducible missing field is the
  row count after active conditioning, plus active kappa/source binding.

CROW/POC:
  The scalar residual subcase is now derived from R_0(C)=rI
  (equivalently C^T C=sigma I in the active normalization).  Radial Wick
  moments give C_i^p=Gamma_p and C_ij^p=2Gamma_p for p=L,Q; this kills
  M_p_2/M_p_4, the POC active row, and the CROW centered row.  The live
  active residual spectrum is still not proved scalar, and no general
  C_i/C_ij arrays were evaluated.

RFTC:
  A partial d=3 smoke/source-compatible packet now validates the Q2/Q4 row
  schema with nonpositive rows V_Q2=-O_{0,0}^2 and V_Q4=-O_{1,1}^2, so
  HB=0 and u=0.  This proves the validator plumbing can accept complete
  Q2/Q4 fields, but the packet is explicitly nonactual and does not close
  the live ANIORB/RFTC row producer.

FC8:
  The strongest current nonempty P_334-deleted a=2 instance is the P_46
  survivor stratum: the stratum/common interface closes with nonempty
  active list and A_sum(P_A10^act)<=C d^2.  The actual-source contract still
  fails on the good-frame JTR/gauge fields and the bad-frame direct or
  M_eta+BFmin_2 fields.  No nonempty actual-source subcase closes.
```

P2 assembly:

```text
The new proof skeleton states the final square hard-edge Poisson theorem in
paper-facing order under the two explicit conventions:
  G_r^sat for zero-fresh endpoint charts,
  imported fixed-k private Laguerre hard-edge package for CHE-L2k(k).

It gives the factorial-moment proof split into pair-bad, Venn-irregular,
and clean tuples, cites PairConditioned-CCI(k-2) for the non-clean classes,
and uses the clean fixed-k expansion plus the factorial-moment criterion.
```

Current next split:

```text
P1:
1. PAT: prove WeightedSepSMExposure_I(a), or find pre-positive-kernel
   cancellation that supplies the theta_n^(3/2) shell payment.
2. SVD: prove the active conditioned row count rows(C)=3 and active
   kappa/source binding, or bypass N2 by a fully accepted atom/direct P_SOS
   packet.
3. CROW/POC: either prove the active residual spectrum is scalar
   (R_0(C)=rI) or evaluate the live non-scalar K4_z^perp and Schur
   C_i/C_ij arrays, then prove row sign/payment and POC-WSOC2.
4. RFTC: replace the nonactual d=3 smoke Q2/Q4 rows with actual finite
   V_Q2/V_Q4 Schur/Hermite row packets, including degree_bound, HB, and u.
5. FC8: prove actual good-frame JTR/gauge data and actual bad-frame
   B-direct-a2 or M_eta+BFmin_2 for the P_46 survivor a=2 stratum.

P2:
  Paper-facing proof skeleton is written.  Remaining P2 work is optional
  presentation polish unless the proof chooses a smaller atlas or refuses
  the imported private Laguerre hard-edge package.
```

## Continuation update, July 1 twenty-second integration

Five Codex workers were assigned to the next PAT, SVD, CROW/POC, RFTC, and
FC8 source fronts, while the foreground pass added a P2 proof-citation audit.
No background processes, daemons, scheduled tasks, launchers, or watchers
were created.

New/updated artifacts:

- `notes\p1_logdet_pat_weighted_exposure_source_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_active_rowcount_or_bypass_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_active_scalarity_or_arrays_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_actual_q24_rows_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_p46_actual_source_attempt_2026_07_01.md`
- `notes\all_apex_square_p2_proof_audit_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `notes\all_apex_square_current_frontier_dag_2026_06_30.md`
- `numerics\p1_pat_weighted_exposure_probe.py`
- `numerics\p1_svd_active_rowcount_probe.py`
- `numerics\p1_poc_active_scalarity_probe.py`
- `numerics\p1_rftc_actual_q24_rows_probe.py`
- `numerics\p1_fc8_p46_actual_source_probe.py`
- `numerics\p2_paper_proof_audit.py`

P1 reductions:

```text
PAT:
  WeightedSepSMExposure_I(a) remains blocked.  A sharper obstruction,
  NoLocalPrePositiveThetaPayment_I(a), is proved: the exact signed
  monotone-tail quotient gains one theta over the MVT/sup positive kernel
  but not the full theta^(3/2).  In the two-endpoint shell,
  Q_n(I)~theta_n^(1/2), K_n(I)~theta_n^(-1/2), and nu_n^hi~theta_n.
  The next target is RawHiTinyLeadingEndpointCancellation_I(a), before the
  monotone-tail quotient split, cancelling the leading
  S_kappa(H/kappa)~kappa H term.

SVD:
  No orientation proof or bypass packet was accepted.  The exact missing
  field is still row_count_after_conditioning: rows(C)=3 for the active
  determinant-tilted SVD coarea matrix C.  The coordinate-isotropic route
  remains conditional on that row count plus active kappa/source binding;
  direct P_SOS and atom/constants packet scans remain empty.

CROW/POC:
  The scalar-residual subcase is revalidated, but live active scalarity is
  not proved.  In the live regularized normalization,
  R_0(C)=rI iff C^T C=sigma I.  The current source/provenance has no theorem
  forcing C^T C=sigma I, and the non-scalar route still lacks live
  K4_z^perp entries and integrated Schur C_i/C_ij arrays.

RFTC:
  The d=3 smoke packet still validates structurally but remains nonactual.
  The exact missing actual generator is now named:
  FROW-Q2/Q4, the post-Hermite/Laplace finite indexed Schur/Hermite
  O-word expansion for V_Q2 and V_Q4 after the signed fourth-cumulant sum
  and Gaussian/Hermite/Laplace integrations, plus exact positive-part
  HB_Q2/HB_Q4 and u_Q2/u_Q4 certificates.

FC8:
  The P_46 survivor stratum/common interface validates, but the actual
  source does not.  The proof remains blocked on actual good-frame
  rho_J/gauge row-law data and actual bad-frame B-direct-a2 or
  M_eta+BFmin_2 data for the real cutoff.
```

P2 assembly:

```text
The P2 paper proof audit is clean:
  missing_documents = 0,
  missing_citations = 0,
  required convention/theorem labels are present.

This only audits citation and convention hygiene.  It does not reprove the
imported private Laguerre hard-edge package or the saturated endpoint
theorem.
```

Current next split:

```text
P1:
1. PAT: prove RawHiTinyLeadingEndpointCancellation_I(a), or produce a
   replacement parent theorem that consumes exact-quotient dyadic source
   before the current positive monotone-tail quotient split.
2. SVD: prove row_count_after_conditioning rows(C)=3 for the active SVD
   coarea matrix and bind kappa/source, or produce a fully accepted
   atom/constants/direct P_SOS bypass.
3. CROW/POC: prove the live active-source theorem C^T C=sigma I if scalar
   residual is intended; otherwise evaluate live K4_z^perp and integrated
   Schur C_i/C_ij arrays and continue to row sign/payment plus POC-WSOC2.
4. RFTC: implement FROW-Q2/Q4, the actual post-Hermite/Laplace finite
   row generator with HB/u extraction.
5. FC8: prove actual P_46 good-frame rho_J/gauge row law and actual
   bad-frame B-direct-a2 or M_eta+BFmin_2 for the real cutoff.

P2:
  Proof skeleton and citation audit are written.  Remaining P2 work is only
  optional presentation polish unless the proof changes the atlas or refuses
  the private Laguerre import.
```

## Continuation update, July 1 twenty-third integration

Five Codex workers were assigned to the sharpened P1 PAT, SVD, CROW/POC,
RFTC, and FC8 source fronts.  The foreground pass added a P1 source-contract
manifest/gate and integrated the worker outputs.  No background processes,
daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_raw_endpoint_cancellation_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_active_rowcount_derivation_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_active_scalar_or_live_arrays_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_frow_q24_actual_generator_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_p46_source_data_attempt_2026_07_01.md`
- `notes\p1_logdet_source_contract_manifest_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_pat_raw_endpoint_cancellation_probe.py`
- `numerics\p1_poc_live_schur_arrays_probe.py`
- `numerics\p1_rftc_frow_q24_actual_generator.py`
- `numerics\p1_fc8_p46_source_data_probe.py`
- `numerics\p1_frontier_source_contracts.py`

P1 reductions:

```text
PAT:
  RawHiTinyLeadingEndpointCancellation_I(a) is blocked in the natural
  two-endpoint form.  The high endpoint has fixed positive sign and size
  theta_n^(1/2), while the signed low endpoint is only a relative theta_n
  correction.  The leading S_kappa(H/kappa)~kappa H term therefore is not
  cancelled down to reserve scale.  A conditional replacement parent is
  now isolated: ExactQuotientHiTinyDyadicConsumer_I(a), if an upstream
  theorem exposes the exact raw quotient source before |q m|<=C_R m^2.

SVD:
  The row-count derivation remains blocked.  d=3 fixes the right-orientation
  and two-block quotient, but C is still an N x d coarea matrix and the
  (N+2)^(-1) denominator comes from an R^N Stiefel-sphere moment.  No
  accepted p1_svd_orientation_n2_proof.v1, atom/constants JSON, or direct
  checker P_SOS packet is present.

CROW/POC:
  The exact scalarity criterion remains R_0(C)=rI iff C^T C=sigma I.  The
  live Schur arrays are now formula-level explicit and numerically
  probeable for supplied residual spectra.  Scalar spectra recover the
  zero-slot shape up to quadrature error, while a generic non-scalar sample
  has nonzero M2/M4 slots.  This does not certify the live source or row
  sign; the next non-scalar theorem is POC-LiveArrayRowSource[p].

RFTC:
  FROW-Q2/Q4 is now a formal contract with a validator.  The current smoke
  packet passes the old source validator but fails strict actual FROW:
  missing strict_actual_packet=true, actual L_Qa^ani provenance flags,
  post-Hermite/Laplace finite O-word coefficients, actual non-smoke word
  lists for V_Q2/V_Q4, and HB/u certificates for the actual positive parts.

FC8:
  The P_46 source-data audit names the smallest missing packet.  Good
  frames need either FC8-etaN-JetTaxedRadiusRowLaw[P_46-a2] for the real
  eta_i,z,B or FC8-CramerGaugeCutoff[P_46-a2] plus the gauge-taxed row-law
  moment.  Bad frames need either B-direct-a2[P_46] or B-env-a2[P_46] plus
  BFmin_2.  The P_46 word algebra and coefficient growth are already
  present; actual cutoff/row-law and bad-frame source data are not.
```

Verification:

```text
python -m py_compile numerics\p1_frontier_source_contracts.py
python -m py_compile numerics\p1_pat_raw_endpoint_cancellation_probe.py
python -m py_compile numerics\p1_poc_live_schur_arrays_probe.py
python -m py_compile numerics\p1_rftc_frow_q24_actual_generator.py
python -m py_compile numerics\p1_fc8_p46_source_data_probe.py
python -B numerics\p1_frontier_source_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_raw_endpoint_cancellation_probe.py --self-test
python -B numerics\p1_svd_active_rowcount_probe.py --evidence-limit 6
python -B numerics\p1_poc_live_schur_arrays_probe.py --spectrum 0.5,0.5,0.5 --gh-order 7 --laguerre-order 24 --emit summary-md
python -B numerics\p1_poc_live_schur_arrays_probe.py --spectrum 0.2,0.5,0.9 --gh-order 7 --laguerre-order 24 --emit summary-md
python -B numerics\p1_rftc_frow_q24_actual_generator.py --audit-current-smoke
python -B numerics\p1_fc8_p46_source_data_probe.py
python -B numerics\p1_fc8_p46_actual_source_probe.py
```

Current next split:

```text
P1:
1. PAT: prove the upstream identity/source theorem that exposes the exact
   raw quotient shell before |q m|<=C_R m^2, or find a term outside the
   two-endpoint raw quotient with a cancelling theta_n^(1/2) boundary trace.
2. SVD: prove row_count_after_conditioning rows(C)=3 from the active
   deleted-row law, and bind kappa/source; or supply an accepted
   p1_svd_orientation_n2_proof.v1, atom/constants JSON, or direct P_SOS
   bypass.
3. CROW/POC: either prove ActiveGramScalar C^T C=sigma I, or build
   POC-LiveArrayRowSource[p] with exact K4_z^perp, exact Schur arrays, row
   sign/payment, and POC-WSOC2.
4. RFTC: fill the FROW-Q2/Q4 contract with actual post-Hermite/Laplace
   O-word coefficients and HB/u certificates.
5. FC8: prove one good-frame P_46 source packet and one bad-frame P_46
   source packet: JTR/gauge for eta_i,z,B plus B-direct-a2 or
   B-env-a2+BFmin_2.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

## Continuation update, July 1 twenty-ninth integration

Five workers were assigned to the post-28 source split.  The foreground pass
added a post-28 source manifest, reviewed the worker artifacts directly,
reran the new probes and older cross-checks, and integrated the sharper
frontier.  No background processes, daemons, scheduled tasks, launchers, or
watchers were created.

New/updated artifacts:

- `notes\p1_logdet_next_post28_source_manifest_2026_07_01.md`
- `notes\p1_logdet_pat_eext_corepack_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_deleted_row_index_source_construct_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_exact_live_spectral_or_arrays_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_finite_i4_source_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_p46_good_or_bad_route_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_next_post28_source_contracts.py`
- `numerics\p1_pat_eext_corepack_probe.py`
- `numerics\p1_svd_deleted_row_index_source_construct_probe.py`
- `numerics\p1_poc_exact_live_spectral_or_arrays_probe.py`
- `numerics\p1_rftc_finite_i4_source_probe.py`
- `numerics\p1_fc8_p46_good_or_bad_route_probe.py`

P1 reductions:

```text
PAT:
  Eext-CorePack(a;A_E,B_E) is reduced, not closed, to
  Eext-StressTailCarleson(a;A_E,B_E), the aggregate external root-stress
  tail S_ext(e;t;A_E)>B_E m_R(1+L_t)^4 after the legal kappa integration.
  The closed root-budget subcase is the opposite region; carrierwise,
  endpoint-DLI, raw PAT_far handoff, and downstream Ract routes do not close
  the Eext source.  A pre-positive external-carrier cancellation theorem
  would also be acceptable if it implies the same tail payment.

SVD:
  The deleted-row count field is downstream of a missing source definition.
  The sharper first field is active_law.indices.deleted_rows_definition:
  define the finite deleted-row set I_del(i), define the source-local map
  j -> e_j, prove e_j in I_del(i), and bind rows(C) to I_del(i)\{e_j}.
  Current notes name P_i,j^(-j) and the conditioning, but do not define the
  ambient finite row-label set or the map from secondary stage to exchanged
  row.

CROW/POC:
  No exact live spectral route is fillable.  The first exact primitive is
  the determinant-tilted deleted-row spectral pushforward of
  dLambda_i,j,z(C)=Z^(-1)det(C^T C+tau^2 I)^(1/2)dP_i,j^(-j)(C) under
  r(C)=spec(tau^2(C^T C+tau^2 I)^(-1)).  Direct exact arrays for p=L,Q are
  still an acceptable shortcut only if their theorem provenance proves this
  pushforward was already integrated out.

RFTC:
  No active finite I_4 packet exists.  Coordinate-axis lists and rho_1,...
  examples remain templates unless a proof/data artifact binds them to the
  centered whitened RFTC/Q24 sliced row law.  The next field remains
  RFTC-FROW-K4Source.active_atom_source.finite_I4 with strict actual-source
  provenance and active-law binding flags.

FC8:
  The P_46 stratum and common G, eta_N, U_46 interface validate, but no good
  or bad route closes.  The smallest overall field remains
  good_source.direct_jtr.row_law_bound, i.e.
  FC8-etaN-JetTaxedRadiusRowLaw[P_46-a2] for the real eta_i,z,B.  In
  parallel, the bad direct scalar is B-direct-a2[P_46]; on the factorized
  bad route, an actual bad-frame M_eta envelope precedes BFmin_2.
```

Verification:

```text
python -m py_compile numerics\p1_next_post28_source_contracts.py numerics\p1_pat_eext_corepack_probe.py numerics\p1_svd_deleted_row_index_source_construct_probe.py numerics\p1_poc_exact_live_spectral_or_arrays_probe.py numerics\p1_rftc_finite_i4_source_probe.py numerics\p1_fc8_p46_good_or_bad_route_probe.py
python -B numerics\p1_next_post28_source_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_eext_corepack_probe.py --self-test
python -B numerics\p1_pat_eext_corepack_probe.py --emit summary-md
python -B numerics\p1_svd_deleted_row_index_source_construct_probe.py --emit summary-md --limit 24
python -B numerics\p1_svd_deleted_row_index_count_probe.py --self-test
python -B numerics\p1_poc_exact_live_spectral_or_arrays_probe.py --audit-current --limit-per-kind 5 --emit summary-md
python -B numerics\p1_poc_live_spectral_schur_source_probe.py --audit-current --dimension 3 --limit-per-group 3 --emit summary-md
python -B numerics\p1_poc_live_spectral_measure_or_cap_probe.py --audit-current --dimension 3 --limit-per-group 3 --emit summary-md
python -B numerics\p1_rftc_finite_i4_source_probe.py --self-test
python -B numerics\p1_rftc_finite_i4_source_probe.py --audit-current --limit 20
python -B numerics\p1_rftc_active_k4_tensor_atom_construct_probe.py --audit-current --limit 8
python -B numerics\p1_rftc_active_k4_source_packet_probe.py --audit-current --limit-per-group 2
python -B numerics\p1_fc8_p46_good_or_bad_route_probe.py --emit summary-md
python -B numerics\p1_fc8_p46_fill_good_bad_routes_probe.py --emit summary-md
```

Current next split:

```text
P1:
1. PAT: prove Eext-StressTailCarleson(a;A_E,B_E), or a pre-positive
   external-carrier cancellation theorem that implies it.
2. SVD: supply active_law.indices.deleted_rows_definition, including
   I_del(i), the source-local j -> e_j map, e_j in I_del(i), and the row
   binding for I_del(i)\{e_j}; then count it.
3. CROW/POC: supply the exact determinant-tilted deleted-row spectral
   pushforward, or direct exact integrated Schur arrays for p=L,Q with
   theorem provenance; cap_quartic_source.entries remains parallel.
4. RFTC: supply an actual finite_I4 source packet for the centered whitened
   RFTC/Q24 sliced row law, with strict provenance and active-source binding.
5. FC8: prove good_source.direct_jtr.row_law_bound for the real eta_i,z,B;
   in parallel prove B-direct-a2[P_46] or the actual M_eta envelope followed
   by BFmin_2.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

## Continuation update, July 1 twenty-fourth integration

Five Codex workers were assigned to the next PAT, SVD, CROW/POC, RFTC, and
FC8 source-packet fronts.  The foreground pass added a second manifest gate
for this next split and integrated all worker outputs.  No background
processes, daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_pat_exact_quotient_parent_source_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_deleted_row_law_n2_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_live_array_rowsource_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_frow_coefficient_source_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_p46_good_bad_source_attempt_2026_07_01.md`
- `notes\p1_logdet_next_source_packet_manifest_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_next_source_packet_contracts.py`
- `numerics\p1_poc_live_array_rowsource_probe.py`
- `numerics\p1_rftc_frow_coefficient_source_probe.py`
- `numerics\p1_fc8_p46_good_bad_source_probe.py`

P1 reductions:

```text
PAT:
  ExactQuotientHiTinyDyadicConsumer_I(a) is usable only as a replacement
  source at the original PAT_far raw |q m| atom, before the positive
  replacement |q m|<=C_R m^2.  It is not a downstream bound for the already
  positive Ract-SepSMCorePack object; in the two-endpoint shell
  K_n(I)/Q_raw,n,I~theta_n^(-1).  The next theorem is therefore the source
  handoff PAT_far-delay-low-exactQHiTiny_I(a;...), which must expose
  sum_n Q_raw,n,I(a) as the final bounded-shell high-tiny residual.

SVD:
  The active deleted-row law has been located as P_i,j^(-j), the law of all
  deleted rows except the secondary exchanged row, but it does not state the
  cardinality of C.  The exact missing theorem is now
  ActiveDeletedRowLaw-Cardinality[d=3]: for the active secondary law in
  dLambda_i,j(C), C is supported on R^(3 x 3), equivalently
  row_count_after_conditioning rows(C)=3.  Otherwise the source must state
  the actual N and provide an accepted N2=N+2 packet.

CROW/POC:
  The live-array route is reduced to an accepted packet shape.  Either prove
  ActiveGramScalar, which gives zero M_p,2^int/M_p,4^int slots and zero
  first-order/density cost, or provide POC-LiveArrayRowSource[p] with exact
  K4_z^perp entries or atoms, exact residual-spectrum data or a row-
  integrated substitute, exact Schur arrays, a p1-poc-int-tensor-rows/v1
  row packet with sign/payment, and density closure by rho2_zero, A=0, or
  POC-WSOC2[p,A;b].  Current artifacts still have formulas and validators
  only.

RFTC:
  Current symbolic K4_z data cannot be lowered into actual FROW coefficients.
  The next layer is RFTC-FROW-K4Source + FROW-AtomIntegrate-Q24 +
  FROW-HaarPositive-Q24: a filled active K4_z raw tensor or atom packet,
  an exact post-cumulant Gaussian/Hermite/Laplace integration theorem
  emitting finite O-word coefficients for V_Q2/V_Q4, and exact HB/u
  positive-part certificates.

FC8:
  The P_46 good/bad source acceptance table is explicit.  One accepted good
  route is required, either FC8-etaN-JetTaxedRadiusRowLaw[P_46-a2] or
  FC8-CramerGaugeCutoff[P_46-a2] plus the gauge-taxed row-law moment.  One
  accepted bad route is required, either B-direct-a2[P_46] or
  B-env-a2[P_46]+BFmin_2.  The packet already has P_46, active growth power
  2, common cutoff interface, and the expected d^(-2)/d^(-4) exponents; all
  actual route proof fields remain absent.
```

Verification:

```text
python -m py_compile numerics\p1_next_source_packet_contracts.py
python -m py_compile numerics\p1_poc_live_array_rowsource_probe.py
python -m py_compile numerics\p1_rftc_frow_coefficient_source_probe.py
python -m py_compile numerics\p1_fc8_p46_good_bad_source_probe.py
python -B numerics\p1_next_source_packet_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_raw_endpoint_cancellation_probe.py --self-test
python -B numerics\p1_svd_active_rowcount_probe.py --evidence-limit 6
python -B numerics\p1_poc_live_array_rowsource_probe.py --audit-current --dimension 3 --limit-per-group 3 --emit summary-md
python -B numerics\p1_rftc_frow_coefficient_source_probe.py --audit-current --limit-per-group 2
python -B numerics\p1_fc8_p46_good_bad_source_probe.py
```

Current next split:

```text
P1:
1. PAT: prove PAT_far-delay-low-exactQHiTiny_I(a;...), the raw-source
   handoff exposing sum_n Q_raw,n,I(a) before the positive quotient bound.
2. SVD: prove ActiveDeletedRowLaw-Cardinality[d=3], or provide the actual
   N=rows(C) plus accepted N2=N+2 and active kappa/source packet.
3. CROW/POC: fill POC-LiveArrayRowSource[p] or prove ActiveGramScalar.
4. RFTC: provide RFTC-FROW-K4Source, FROW-AtomIntegrate-Q24, and
   FROW-HaarPositive-Q24.
5. FC8: fill one P_46 good route and one P_46 bad route in the
   fc8-a2-source-contract validator.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

## Continuation update, July 1 twenty-fifth integration

Five Codex workers were assigned to the current PAT, SVD, CROW/POC, RFTC,
and FC8 source-closure fronts.  The foreground pass added the current-source
closure manifest and integrated all worker outputs.  No background
processes, daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_current_source_closure_manifest_2026_07_01.md`
- `notes\p1_logdet_pat_far_delay_exactq_handoff_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_active_deleted_row_cardinality_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_fill_live_array_rowsource_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_k4_integrate_positive_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_p46_fill_good_bad_routes_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_current_source_closure_contracts.py`
- `numerics\p1_svd_active_deleted_row_cardinality_probe.py`
- `numerics\p1_poc_fill_live_array_rowsource_probe.py`
- `numerics\p1_rftc_k4_integrate_positive_probe.py`
- `numerics\p1_fc8_p46_fill_good_bad_routes_probe.py`

P1 reductions:

```text
PAT:
  PAT_far-delay-low-exactQHiTiny_I(a;...) is accepted as a raw-source
  replacement at the original PAT_far raw |q m| atom.  The old
  delayed-low/separated/small-m reductions may still pay discarded pieces
  with the old positive estimates, but the final high-tiny shell must remain
  sum_n Q_raw,n,I(a).  The positivity-forcing line is
  |q_tail m| <= C_T(u,kappa;e)m^2 and
  R_act(e;t,u)=sum_n C_R,n(e;t,u)m^2; downstream positive objects such as
  PAT-QuadTail, Ract-Pack, Ract-SepSMCorePack, and
  Ract-SepHiTinyCorePack cannot supply the missing raw quotient.

SVD:
  The validator p1_svd_active_deleted_row_cardinality.v1 finds the active
  law P_i,j^(-j) and the N2=N+2 consumer, but no source currently proves
  that the conditioned active law is supported on C in R^(3 x 3).  The exact
  remaining field is active_law.support.rows.

CROW/POC:
  The conditional scalar-residual subcase is accepted for p=L,Q: under
  R_0(C)=rI, equivalently C^T C=sigma I, the exact K4_z^perp cap, scalar
  Schur shape C_i=Gamma_p and C_ij=2 Gamma_p, zero rows, and exact-zero
  density envelope validate through the live row-source checker.  The global
  source still needs ActiveGramScalar or the non-scalar cap tensor, residual
  spectrum, live Schur arrays, row sign/payment, and nonzero-density fields.

RFTC:
  The next unlock is RFTC-FROW-Q24AtomicPositivePacket, combining the active
  K4_z raw tensor or atom packet, integrated actual V_Q2/V_Q4 O-word rows
  with degree bounds, and HB_Q2/HB_Q4 plus u_Q2/u_Q4 certificates.  A K4
  source alone does not close the Haar-positive layer.

FC8:
  The P_46 stratum and common cutoff interface still validate.  The next
  isolated proof field is good_source.direct_jtr.row_law_bound, the actual
  FC8-etaN-JetTaxedRadiusRowLaw[P_46-a2] for the real eta_i,z,B with the
  a=2 gap.  One bad route remains required afterward.
```

Verification:

```text
python -m py_compile numerics\p1_current_source_closure_contracts.py numerics\p1_svd_active_deleted_row_cardinality_probe.py numerics\p1_poc_fill_live_array_rowsource_probe.py numerics\p1_rftc_k4_integrate_positive_probe.py numerics\p1_fc8_p46_fill_good_bad_routes_probe.py
python -B numerics\p1_current_source_closure_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_raw_endpoint_cancellation_probe.py --self-test
python -B numerics\p1_svd_active_deleted_row_cardinality_probe.py --emit audit-json
python -B numerics\p1_poc_fill_live_array_rowsource_probe.py --check-subcase --dimension 3 --n-plus-2 5 --limit-per-group 3 --emit summary-md
python -B numerics\p1_poc_fill_live_array_rowsource_probe.py --emit-subcase-packet --dimension 3 --n-plus-2 5 | python -B numerics\p1_poc_live_array_rowsource_probe.py --check-packet -
python -B numerics\p1_rftc_k4_integrate_positive_probe.py --audit-current --limit-per-group 2
python -B numerics\p1_fc8_p46_fill_good_bad_routes_probe.py
```

Current next split:

```text
P1:
1. PAT: integrate the top-level replacement using
   PAT_far-delay-low-exactQHiTiny_I(a;...), ensuring consumers use the raw
   exact quotient and DLI/Eext side inputs are unaffected.
2. SVD: supply active_law.support.rows=3, or provide the actual N and an
   accepted N2=N+2 plus active source packet.
3. CROW/POC: prove ActiveGramScalar or fill the non-scalar live row-source
   fields; the conditional scalar subcase is closed.
4. RFTC: produce RFTC-FROW-Q24AtomicPositivePacket.
5. FC8: prove good_source.direct_jtr.row_law_bound, then one bad route.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

## Continuation update, July 1 twenty-sixth integration

Five Codex workers were assigned to the next PAT, SVD, CROW/POC, RFTC, and
FC8 frontier-decision fronts.  The foreground pass added a manifest gate for
this split, reviewed all worker artifacts, and integrated the accepted
reductions and stricter blockers.  No background processes, daemons,
scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_next_frontier_decision_manifest_2026_07_01.md`
- `notes\p1_logdet_pat_top_level_raw_handoff_integration_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_active_support_rows_proof_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_active_gram_scalar_decision_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_q24_atomic_positive_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_p46_direct_jtr_rowlaw_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_next_frontier_decision_contracts.py`
- `numerics\p1_pat_top_level_raw_handoff_probe.py`
- `numerics\p1_svd_active_support_rows_proof_probe.py`
- `numerics\p1_poc_active_gram_scalar_decision_probe.py`
- `numerics\p1_rftc_q24_atomic_positive_packet_probe.py`
- `numerics\p1_fc8_p46_direct_jtr_rowlaw_probe.py`

P1 reductions:

```text
PAT:
  The top-level right-quotient HiTiny branch is now accepted only as a raw
  source replacement inside PAT_far(a): feed sum_n Q_raw,n,I(a) from the
  original raw |q m| atom to ExactQuotientHiTinyDyadicConsumer_I(a), before
  |q_tail m|<=C_T m^2 and R_act=sum C_R,n m^2.  PAT-QuadTail and all Ract-*
  descendants are forbidden parents for this replacement.  DLI-CorePack and
  Eext-CorePack remain unchanged side inputs.  Next analytic PAT field:
  DLI-CorePack(a;B_L,B_D,c_D), with Eext-CorePack in parallel.

SVD:
  The support-row audit is stricter but still blocked.  Current notes keep
  C in R^(N x 3) with symbolic N; d=3 is a right-orientation/consumer
  dimension, and SOS checker rows are not rows of C.  No accepted actual N,
  N2=N+2, active atom/constants packet, or direct P_SOS bypass exists.
  Smallest remaining field remains active_law.support.rows.

CROW/POC:
  ActiveGramScalar is false as a global live-source theorem for d>=2 under
  the current determinant-tilted product support.  The scalar-residual row
  packet remains a conditional subcase only.  The next non-scalar source
  field is residual_spectrum_source.live_spectral_measure, formalized as
  POC-LiveSpectralSchurSource[v1], with exact live spectral cells/evaluator
  or direct integrated Schur arrays for p=L,Q.  cap_quartic_source.entries
  remains an independent parallel source field.

RFTC:
  The strict RFTC-FROW-Q24AtomicPositivePacket checker rejects the current
  constructible candidate as smoke/template data.  The old validator accepts
  toy negative-square row plumbing, but no strict actual packet, active K4
  binding, FROW-AtomIntegrate-Q24 theorem, actual row provenance, or HB/u
  certificates exist.  Smallest next field:
  RFTC-FROW-K4Source.active_raw_tensor_or_atom_packet.

FC8:
  The direct-JTR audit proves the consumer implication only: if
  good_source.direct_jtr.actual_source and the row-law bound are supplied,
  the direct good route validates.  Current eta/radius/jet notes still lack
  the actual row-law theorem for real eta_i,z,B, and even a hypothetical
  direct-JTR fill leaves the separate bad-frame route open.
```

Verification:

```text
python -m py_compile numerics\p1_next_frontier_decision_contracts.py
python -B numerics\p1_next_frontier_decision_contracts.py --self-test
python -B numerics\p1_next_frontier_decision_contracts.py --emit summary-md --require-current
python -m py_compile numerics\p1_pat_top_level_raw_handoff_probe.py numerics\p1_svd_active_support_rows_proof_probe.py numerics\p1_poc_active_gram_scalar_decision_probe.py numerics\p1_rftc_q24_atomic_positive_packet_probe.py numerics\p1_fc8_p46_direct_jtr_rowlaw_probe.py
python -B numerics\p1_next_frontier_decision_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_top_level_raw_handoff_probe.py --self-test
python -B numerics\p1_pat_top_level_raw_handoff_probe.py
python -B numerics\p1_svd_active_support_rows_proof_probe.py --evidence-limit 12 --emit json
python -B numerics\p1_poc_active_gram_scalar_decision_probe.py --dimension 3 --rows 3 --tau 1 --samples 64 --seed 20260701 --emit json
python -B numerics\p1_rftc_q24_atomic_positive_packet_probe.py --audit-current --limit-per-group 2
python -B numerics\p1_fc8_p46_direct_jtr_rowlaw_probe.py --emit json
```

Current next split:

```text
P1:
1. PAT: attack DLI-CorePack(a;B_L,B_D,c_D); keep Eext-CorePack as the
   parallel side source and preserve the raw PAT_far handoff.
2. SVD: prove active_law.support.rows=3 from the active deleted-row law, or
   supply actual N plus accepted N2=N+2 and active source packet.
3. CROW/POC: fill POC-LiveSpectralSchurSource[v1] or the parallel
   cap_quartic_source.entries for K4_z^perp; scalar global route is closed
   only as false.
4. RFTC: fill RFTC-FROW-K4Source.active_raw_tensor_or_atom_packet.
5. FC8: prove good_source.direct_jtr.row_law_bound for eta_i,z,B, then one
   bad-frame route.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

## Continuation update, July 1 twenty-seventh integration

Five Codex workers were assigned to the next PAT, SVD, CROW/POC, RFTC, and
FC8 source-field fronts.  The foreground pass added a source-field manifest,
reviewed all worker outputs, and integrated the sharper source boundaries.
No background processes, daemons, scheduled tasks, launchers, or watchers
were created.

New/updated artifacts:

- `notes\p1_logdet_next_source_field_manifest_2026_07_01.md`
- `notes\p1_logdet_pat_dli_corepack_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_active_support_rows_source_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_live_spectral_schur_source_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_active_k4_source_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_direct_jtr_source_theorem_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_next_source_field_contracts.py`
- `numerics\p1_pat_dli_corepack_probe.py`
- `numerics\p1_svd_active_support_rows_source_packet_probe.py`
- `numerics\p1_poc_live_spectral_schur_source_probe.py`
- `numerics\p1_rftc_active_k4_source_packet_probe.py`

P1 reductions:

```text
PAT:
  DLI-CorePack is reduced, not closed, to
  DLI-DelayedEntryCarleson(a;B_L,B_D,c_D,Lambda,A).  The delayed companion
  model keeps DLI support live while the endpoint/reserve ratio grows like
  delay^(1/2), so current support hypotheses do not imply the source.  The
  accepted raw PAT_far handoff remains separate; Eext remains parallel.

SVD:
  A source-local pass through non-SVD deleted-row and paper hooks found no
  row-count identity for active P_i,j^(-j).  Pi_i/B_i one-row laws, B(C,x)
  reconstruction layers, and Z_i,j normalizers do not count rows(C).  The
  accepted future packet must either prove C in R^(3 x 3), N=3, N2=5, or
  provide actual N plus accepted N2=N+2 and active source packet.

CROW/POC:
  POC-LiveSpectralSchurSource[v1] is strictly specified.  It accepts exact
  finite spectral cells plus evaluator, exact live spectral evaluator, or
  direct integrated exact Schur arrays for p=L,Q; float/quadrature arrays
  are diagnostics only.  First executable field remains
  residual_spectrum_source.live_spectral_measure; cap_quartic_source.entries
  is a parallel downstream source field.

RFTC:
  The focused active-K4 checker rejects symbolic K4_z formulas,
  K4_z^perp consumer identities, coordinate-isotropic templates, and d=3
  smoke rows.  A strict packet needs strict_actual_source=true, active raw
  tensor entries or exact atoms in FROW normalization, active-source binding,
  and scalar-line irrelevance if only K4_z^perp is supplied.

FC8:
  Direct-JTR remains blocked at the actual row-law theorem.  The current
  qualitative cutoff notes lack quantitative N_i,z,B, inradius lower tails,
  transition jets through 2d+4, transition width/gauge derivative scale, and
  the L^r lower-tail estimate for rho_J^2.  The gauge fallback is the full
  FC8-CramerGaugeCutoff[P_46-a2] packet.  A bad-frame route can proceed
  independently if it freezes the same G, eta_N, and U_46.
```

Verification:

```text
python -m py_compile numerics\p1_next_source_field_contracts.py
python -B numerics\p1_next_source_field_contracts.py --self-test
python -B numerics\p1_next_source_field_contracts.py --emit summary-md --require-current
python -m py_compile numerics\p1_pat_dli_corepack_probe.py numerics\p1_svd_active_support_rows_source_packet_probe.py numerics\p1_poc_live_spectral_schur_source_probe.py numerics\p1_rftc_active_k4_source_packet_probe.py
python -B numerics\p1_next_source_field_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_dli_corepack_probe.py --self-test
python -B numerics\p1_svd_active_support_rows_source_packet_probe.py --emit summary-md --limit 12
python -B numerics\p1_poc_live_spectral_schur_source_probe.py --audit-current --dimension 3 --limit-per-group 3 --emit summary-md
python -B numerics\p1_rftc_active_k4_source_packet_probe.py --audit-current --limit-per-group 2
python -B numerics\p1_fc8_p46_direct_jtr_rowlaw_probe.py --emit summary-md
```

Current next split:

```text
P1:
1. PAT: prove DLI-DelayedEntryCarleson(a;B_L,B_D,c_D,Lambda,A) or find an
   endpoint-level cancellation before the positive endpoint kernel.
2. SVD: prove active_law.support.rows=3, or supply actual N plus accepted
   N2=N+2 and active source packet in the new source-packet shape.
3. CROW/POC: fill residual_spectrum_source.live_spectral_measure or direct
   exact integrated Schur arrays; cap_quartic_source.entries remains
   parallel.
4. RFTC: fill active K4_z raw tensor/atom source with FROW normalization and
   active-source binding.
5. FC8: prove the direct JTR row-law theorem or the full Cramer gauge packet;
   a bad-frame worker can proceed independently on B-direct-a2 or M_eta+BFmin_2.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

## Continuation update, July 1 twenty-eighth integration

Five workers were assigned to the next primitive-source split after the
twenty-seventh integration.  The foreground pass added a primitive-contract
manifest, reviewed the worker artifacts directly, reran the focused probes,
and integrated the resulting frontier update.  No background processes,
daemons, scheduled tasks, launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_next_primitive_manifest_2026_07_01.md`
- `notes\p1_logdet_pat_dli_delayed_entry_carleson_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_deleted_row_index_count_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_live_spectral_measure_or_cap_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_active_k4_tensor_atom_construct_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_p46_badframe_route_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_next_primitive_contracts.py`
- `numerics\p1_pat_dli_delayed_entry_carleson_probe.py`
- `numerics\p1_svd_deleted_row_index_count_probe.py`
- `numerics\p1_poc_live_spectral_measure_or_cap_probe.py`
- `numerics\p1_rftc_active_k4_tensor_atom_construct_probe.py`
- `numerics\p1_fc8_p46_badframe_route_probe.py`

P1 reductions:

```text
PAT:
  DLI-DelayedEntryCarleson(a;B_L,B_D,c_D,Lambda,A) is closed for a=1,2.
  The proof uses bounded post-kappa endpoint kernel, carrier baseline
  L(h)>=c_0, monotone D(h), and sparse support h>=c(1+L)^8; the monotone
  Hardy comparison turns the delayed local density issue into a global
  reserve estimate.  Therefore DLI-CorePack closes by the previous
  reduction.  The next PAT-side source visible from this branch is the
  parallel Eext-CorePack(a;A_E,B_E).

SVD:
  No source-local deleted-row index count was found for active P_i,j^(-j).
  The smaller next field is active_law.indices.deleted_rows_count, with an
  explicit I_del(i), secondary exchanged index e_j, membership e_j in
  I_del(i), and the counting identity for I_del(i)\{e_j}.  If the count is
  four, this yields rows(C)=3, N=3, N2=5; otherwise the actual N and matching
  accepted N2=N+2 packet must be supplied.

CROW/POC:
  Current non-scalar Schur data remain formula/quadrature diagnostics only.
  The accepted live spectral route still needs
  residual_spectrum_source.live_spectral_measure, an exact live evaluator,
  or direct exact integrated Schur arrays for p=L,Q.  In parallel,
  cap_quartic_source.entries cannot be filled until the active K4_z source
  is supplied.

RFTC:
  The active K4 tensor/atom route is narrowed to the first primitive
  RFTC-FROW-K4Source.active_atom_source.finite_I4.  Current symbolic formulas
  name K4_z=sum c_rho T_rho but do not enumerate a nonempty active finite
  I_4.  Exact coefficients, atom coordinates, FROW normalization,
  scalar-line irrelevance, and active-source binding remain downstream.

FC8:
  The P_46 bad-frame route is isolated.  The direct accepting theorem is
  B-direct-a2[P_46]: E_{P_i}[Z_i U_46 1_{G^c}] <= C d^(-2).  The factorized
  alternative is B-env-a2[P_46]+BFmin_2: U_46 <= C d^2 M_eta(d) on G^c and
  E_{P_i}[Z_i 1_{G^c}] <= C d^(-4)/M_eta(d).  Current notes provide neither
  the actual bad envelope nor the matching tilted bad mass.  The separate
  good route still needs direct JTR row-law or the full Cramer gauge packet.
```

Verification:

```text
python -m py_compile numerics\p1_next_primitive_contracts.py numerics\p1_pat_dli_delayed_entry_carleson_probe.py numerics\p1_svd_deleted_row_index_count_probe.py numerics\p1_poc_live_spectral_measure_or_cap_probe.py numerics\p1_rftc_active_k4_tensor_atom_construct_probe.py numerics\p1_fc8_p46_badframe_route_probe.py
python -B numerics\p1_next_primitive_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_dli_delayed_entry_carleson_probe.py --self-test
python -B numerics\p1_pat_dli_delayed_entry_carleson_probe.py --a 1 --delays 1,4,16,64,256
python -B numerics\p1_pat_dli_delayed_entry_carleson_probe.py --a 2 --delays 1,4,16,64,256
python -B numerics\p1_svd_deleted_row_index_count_probe.py --self-test
python -B numerics\p1_svd_deleted_row_index_count_probe.py --emit summary-md --limit 24
python -B numerics\p1_poc_live_spectral_measure_or_cap_probe.py --audit-current --dimension 3 --limit-per-group 3 --emit summary-md
python -B numerics\p1_rftc_active_k4_tensor_atom_construct_probe.py --audit-current --limit 8
python -B numerics\p1_fc8_p46_badframe_route_probe.py --emit summary-md
python -B numerics\p1_pat_dli_corepack_probe.py --self-test
python -B numerics\p1_svd_active_support_rows_source_packet_probe.py --emit summary-md --limit 16
python -B numerics\p1_svd_active_deleted_row_cardinality_probe.py --emit audit-json
python -B numerics\p1_rftc_active_k4_source_packet_probe.py --audit-current --limit-per-group 2
python -B numerics\p1_fc8_p46_good_bad_source_probe.py
```

Current next split:

```text
P1:
1. PAT: attack Eext-CorePack(a;A_E,B_E), preserving the accepted raw
   PAT_far handoff and the now-closed DLI branch.
2. SVD: supply active_law.indices.deleted_rows_count and the counting
   identity for I_del(i)\{e_j}, or give actual N plus accepted N2=N+2 and
   the active source packet.
3. CROW/POC: fill residual_spectrum_source.live_spectral_measure or direct
   exact integrated Schur arrays for p=L,Q; cap_quartic_source.entries
   remains parallel and depends on active K4_z source data.
4. RFTC: supply RFTC-FROW-K4Source.active_atom_source.finite_I4, then exact
   c_rho, atom coordinates, FROW normalization, scalar-line irrelevance if
   needed, and active-source binding.
5. FC8: prove one good route, direct JTR row-law or the full Cramer gauge
   packet, and one bad route, B-direct-a2[P_46] or
   B-env-a2[P_46]+BFmin_2.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

## Continuation update, July 1 thirtieth integration

Five workers were assigned to the sharper post-29 source split recorded in
the frontier DAG and in the earlier twenty-ninth integration block in this
ledger.  The foreground pass added a post-29 source manifest, reviewed the
worker artifacts directly, reran the new probes, and integrated the resulting
frontier update.  No background processes, daemons, scheduled tasks,
launchers, or watchers were created.

New/updated artifacts:

- `notes\p1_logdet_next_post29_source_manifest_2026_07_01.md`
- `notes\p1_logdet_pat_eext_stress_tail_carleson_attempt_2026_07_01.md`
- `notes\p1_logdet_svd_deleted_rows_definition_attempt_2026_07_01.md`
- `notes\p1_logdet_poc_spectral_pushforward_source_attempt_2026_07_01.md`
- `notes\p1_logdet_rftc_active_finite_i4_packet_attempt_2026_07_01.md`
- `notes\p1_logdet_fc8_jtr_bad_route_source_attempt_2026_07_01.md`
- `notes\p1_logdet_current_frontier_dag_2026_06_30.md`
- `numerics\p1_next_post29_source_contracts.py`
- `numerics\p1_pat_eext_stress_tail_carleson_probe.py`
- `numerics\p1_svd_deleted_rows_definition_probe.py`
- `numerics\p1_poc_spectral_pushforward_source_probe.py`
- `numerics\p1_rftc_active_finite_i4_packet_probe.py`
- `numerics\p1_fc8_jtr_bad_route_source_probe.py`

P1 reductions:

```text
PAT:
  Eext-StressTailCarleson(a;A_E,B_E) remains open.  The new audit rejects
  root-budget replay, pointwise soft-rank domination, carrierwise payment,
  endpoint-DLI transfer, raw PAT_far, downstream Ract parents, and
  post-positive cancellation.  Accepted future routes are direct ESTC, an
  aggregate high-moment tail theorem implying ESTC, or a true pre-positive
  external-carrier cancellation.

SVD:
  active_law.indices.deleted_rows_definition is still missing.  Existing
  P_i,j^(-j), conditioning, and B(C,x) reconstruction notation do not define
  RowLabels(i), I_del(i), the source-local e_j=e(i,j), membership
  e_j in I_del(i), or the row binding rows(C)=I_del(i)\{e_j}.  The count and
  rows(C)=3 remain downstream.

CROW/POC:
  No exact spectral packet is present.  Current sources contain symbolic
  pushforward references, formula layers, quadrature diagnostics, and
  conditional scalar packets, but no exact determinant-tilted deleted-row
  spectral pushforward and no direct exact L,Q arrays with provenance proving
  that pushforward was integrated out.  The next theorem is
  POC-DeletedRowSpectralPushforward; cap_quartic_source.entries remains
  parallel.

RFTC:
  No actual finite_I4 packet exists.  Symbolic K4_z sums, coordinate-axis
  templates, placeholder rho lists, and smoke rows remain rejected unless a
  proof/data artifact enumerates active_atom_source.finite_I4 for the
  centered whitened RFTC/Q24 sliced row law with strict provenance and
  active-source binding.

FC8:
  The P_46 stratum and common G, eta_N, U_46 interface still validate, but
  no route closes.  Direct JTR still lacks actual_source and
  good_source.direct_jtr.row_law_bound.  The direct bad route still lacks
  bad_source.direct_a2.actual_source.  The factorized bad route first needs
  bad_source.envelope_bfmin2.M_eta.definition proving
  U_46 <= C d^2 M_eta(d) on G^c, then BFmin_2.
```

Verification:

```text
python -m py_compile numerics\p1_next_post29_source_contracts.py
python -B numerics\p1_next_post29_source_contracts.py --self-test
python -B numerics\p1_next_post29_source_contracts.py --emit summary-md --require-current
python -m py_compile numerics\p1_next_post29_source_contracts.py numerics\p1_pat_eext_stress_tail_carleson_probe.py numerics\p1_svd_deleted_rows_definition_probe.py numerics\p1_poc_spectral_pushforward_source_probe.py numerics\p1_rftc_active_finite_i4_packet_probe.py numerics\p1_fc8_jtr_bad_route_source_probe.py
python -B numerics\p1_next_post29_source_contracts.py --require-current --require-next-notes
python -B numerics\p1_pat_eext_stress_tail_carleson_probe.py --self-test
python -B numerics\p1_pat_eext_stress_tail_carleson_probe.py --emit summary-md
python -B numerics\p1_svd_deleted_rows_definition_probe.py --self-test
python -B numerics\p1_svd_deleted_rows_definition_probe.py --emit summary-md --limit 24
python -B numerics\p1_poc_spectral_pushforward_source_probe.py --self-test --dimension 3
python -B numerics\p1_poc_spectral_pushforward_source_probe.py --audit-current --limit-per-kind 4 --emit summary-md
python -B numerics\p1_rftc_active_finite_i4_packet_probe.py --self-test
python -B numerics\p1_rftc_active_finite_i4_packet_probe.py --audit-current --limit 8
python -B numerics\p1_fc8_jtr_bad_route_source_probe.py --emit summary-md
```

Current next split:

```text
P1:
1. PAT: prove Eext-StressTailCarleson(a;A_E,B_E), or prove an aggregate
   high-moment tail theorem or pre-positive cancellation that implies it.
2. SVD: supply active_law.indices.deleted_rows_definition with RowLabels(i),
   I_del(i), e_j=e(i,j), e_j in I_del(i), row binding to I_del(i)\{e_j},
   and then the count.
3. CROW/POC: prove POC-DeletedRowSpectralPushforward, or direct exact L,Q
   Schur arrays with provenance that the pushforward was integrated out;
   cap_quartic_source.entries remains parallel.
4. RFTC: supply an actual active finite_I4 packet for the centered whitened
   RFTC/Q24 sliced row law, then coefficients, atom coordinates, and
   integration/Haar-positive rows.
5. FC8: prove good_source.direct_jtr.actual_source plus
   good_source.direct_jtr.row_law_bound; in parallel prove B-direct-a2[P_46]
   or actual M_eta.definition followed by BFmin_2.

P2:
  Proof skeleton and citation audit remain clean.  No P2 blocker is active
  unless the proof leaves the saturated atlas or rejects the imported
  private Laguerre hard-edge package.
```

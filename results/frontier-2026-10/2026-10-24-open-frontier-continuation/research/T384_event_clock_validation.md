# T384 exact-gate scalar-flow numerical check

2026-10-23. This checks the **finite-width** one-input gradient-flow identities and the sign-selected approximation in `T384_scalar_dynamics.md`, using the independent standard symmetric-stable initialization in `T384_joint_limit.md`. It is numerical evidence, not a proof of either asymptotic theorem. In the simulation filenames containing `seed`, the eight-digit suffix identifies the pseudorandom seed, not the run date. The audit file stores its own seed (`388104`) inside the JSON.

Code: `../code/t384_event_clock.py` (experiment) and `../code/t384_validate_solver.py` (independent per-neuron/tolerance audit). Raw per-replicate values, settings, summaries, and software versions are in `../code/t384_event_clock_t3_seed20261026.json`; the audit is `../code/t384_solver_audit_20261023.json`. An additional fixed-`t=0.25,1` run is in `../code/t384_event_clock_20261023.json`, with larger-width separate-seed runs in `../code/t384_event_clock_alpha1_large_seed20261025.json` and `../code/t384_event_clock_alpha15_large_seed20261024.json`.

## Numerical method and its checks

For each draw, define `r₀=y−F_m`, `σ=sign(r₀)`, `V_i=σ W_i(0)`, and the exact clock `s=β_m∫|r|dt`, `β_m=(log m/m)^(1/α)`. Every initially active opposing neuron with `V_i<−U_i` has an **analytic hit clock** `h_i=atanh(U_i/|V_i|)`. Sort these clocks. Between hits, the survivor kernel is exactly

```
K(s)=m^(−2/α)[q cosh(2s)+c sinh(2s)],
q=Σ_survivors (U_i²+V_i²), c=2Σ_survivors U_i V_i.
```

At segment start `s_j`, put `ξ=s−s_j`, `K_j=K(s_j)` and `J_j=m^(−2/α)[q sinh(2s_j)+c cosh(2s_j)]`. The scalar equation passed to `solve_ivp(DOP853)` is the exact residual-clock identity

```
ξ' = β_m |r_j| − (K_j/2)sinh(2ξ) − J_j sinh²ξ.
```

The solver terminates at the **next known hit clock**, drops that neuron, and restarts. This avoids both subtraction of `y−f(s)` when the residual is small and Euler steps that skip gates. It uses relative/absolute tolerances `2e−10/2e−12`. The symmetric-stable CMS sampler was checked at characteristic argument one: empirical cosine means `0.36728` (`α=1`) and `0.36764` (`α=1.5`) on 400,000 draws, versus `e^(−1)=0.36788`.

The independent audit drew 8 paths at each of `α∈{1,1.5}`, `m∈{512,8192,131072}` and six observation times (48 paths). Directly rebuilding every surviving neuron at each saved clock gave maximum aggregate-vs-direct discrepancies `1.14e−13` for `K` and `3.55e−15` for `y−f−r`. Rerunning with tighter tolerances `5e−12/5e−14` changed clocks by at most `2.86e−12`, kernels by `1.45e−13`, and residuals by at most `2.51e−7` absolute (`1.30e−7` after division by `1+|r₀|`). In the 120-replicate primary run, the largest `|y−f(s(t))−r(t)|` was `3.45e−12`. These numerical errors are far below the empirical approximation errors below.

## Fixed-time comparison

Parameters: `y=0.7`, times `0,1,3`; 120 iid **replicate streams per α**. Within a replicate the widths use prefixes of a common sample, with width-specific normalization. The table gives medians over replicates; the last column gives the 90th percentile. `Q_m=C_m+A_m` for positive initial residual and `C_m+B_m` for negative, exactly as in the scalar note. The first numerical column is the unselected initial-kernel gap; the next two compare the **trained** kernel with `Q_m`.

| α | m | med `K(0)−Q_m` | med `|K(1)−Q_m|` | med `|K(3)−Q_m|` | med `|r(3)−r₀e^(−3Q_m)|` | p90 residual error |
|---:|---:|---:|---:|---:|---:|---:|
| 1.0 | 8,192 | .091 | .034 | .028 | .006 | .106 |
| 1.0 | 32,768 | .082 | .036 | .025 | .008 | .141 |
| 1.0 | 131,072 | .087 | .030 | .024 | .009 | .106 |
| 1.0 | 524,288 | .080 | .027 | .018 | .006 | .060 |
| 1.5 | 8,192 | .246 | .170 | .148 | .019 | .102 |
| 1.5 | 32,768 | .253 | .172 | .158 | .016 | .101 |
| 1.5 | 131,072 | .277 | .186 | .144 | .014 | .085 |
| 1.5 | 524,288 | .258 | .185 | .152 | .011 | .077 |

For `α=1`, the median positive-time kernel error at `t=3` falls from `.028` to `.018` across this range while the initial gap stays near `.08–.09`. The residual 90th percentile falls from `.106` to `.060`, though intermediate widths fluctuate. For `α=1.5`, the residual median falls from `.019` to `.011`, but the kernel median remains around `.15`; the widths studied do **not** resolve its predicted convergence. At `t=3` the observed kernel error was below the initial gap on 86–94% of the `α=1` paths and 95–99% of the `α=1.5` paths, depending on width. The larger positive-time kernel errors and their slow width trend are compatible with a heavy-tailed initial layer whose opposing contribution vanishes slowly, but this simulation alone cannot establish its rate or the limit.

Reproduction (from workspace root):

```bash
python continuation_2026_10_24/code/t384_event_clock.py \
  --widths 8192 32768 131072 524288 --alphas 1 1.5 --reps 120 \
  --seed 20261026 --label 0.7 --times 0 1 3 \
  --output continuation_2026_10_24/code/t384_event_clock_t3_seed20261026.json
python continuation_2026_10_24/code/t384_validate_solver.py \
  --output continuation_2026_10_24/code/t384_solver_audit_20261023.json
```

The fixed-time finite-width data are consistent with fast sign selection and a slower, especially `α=1.5`, approach to `Q_m`; they do not replace the pathwise estimates or prove convergence in probability.

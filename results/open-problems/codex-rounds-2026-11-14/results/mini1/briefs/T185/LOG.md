# T185 work log

Task received: 14 November 2026, approximately 22:06 Asia/Tbilisi (18:06 UTC tool clock). The transcript does not expose the exact receipt timestamp.

## 1. Orientation and literature check (started 18:06 UTC)

The task-specific instruction to write only in this folder takes precedence over the global instructions to update the shared brain, checklist, and mesh. Those shared systems were not mutated. No git or subagents are used.

Read `~/.claude/brain_startup.md` and the compute state. The governor reports `warn`, `owner_away_open`, saturated CPU. This task will use web searches and short, single-thread checks only.

Initial command: `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /bin/cat ~/.claude/brain_startup.md ~/.claude/compute/compute_state.json`.

Output: `nice: setpriority: Operation not permitted`; the read completed. The sandbox prevents setting priority, so no computationally heavy program will be attempted. All further program invocations will still request nice 15 and one thread.

Initial web searches: `"bandwidth sharing" "general" "stability" "alpha" 2021 2022 2023 2024 2025 2026` and `"Fu" "Williams" "Stability of a subcritical fluid model" stochastic positive recurrence`.

Promising results to open: Fu–Williams (2020), Fu–Williams (2022), and Vlasiou–Zhang–Zwart (2026), *Insensitivity of proportional fairness in critically loaded bandwidth sharing networks*. A search result alone is not evidence that stochastic stability has been proved.

## 2. Literature outcome and choice (18:08 UTC)

The literature check took about three minutes, below the ten-minute cap. Further queries included `"A sufficient condition for stochastic stability" "Lee"`, `"alpha-fair" "general file" "positive" stability 2023 2024 2025 2026`, and `"bandwidth" "stability" "general file" after:2022-01-01`.

Opened primary sources:

- Yingjia Fu and Ruth J. Williams, *Asymptotic behavior of a critical fluid model for bandwidth sharing with general file size distributions*, Ann. Appl. Probab. 32 (2022), 1862–1901, DOI 10.1214/21-AAP1723: <https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf>. Its introduction, p. 1863, says their subcritical result combined with Lee yields positive recurrence under suitable distributional assumptions. Its new theorems concern critical fluid behavior, not the unrestricted stochastic claim of T185.
- Nam H. Lee, *A sufficient condition for stochastic stability of an Internet congestion control model in terms of fluid model stability*, UC San Diego dissertation (2008): <https://escholarship.org/content/qt1986s3zq/qt1986s3zq.pdf>. The abstract describes positive Harris recurrence for an age-based state conditional on fluid stability and assumptions. This is earlier work, not a new unrestricted solution.
- Yingjia Fu and Ruth J. Williams, *Stability of a Subcritical Fluid Model for Fair Bandwidth Sharing with General File Size Distributions*, Stochastic Systems 10 (2020), 251–273: <https://pubsonline.informs.org/doi/10.1287/stsy.2019.0058>. The author PDF fetch twice timed out, but the publisher page opened. Indexed text identifies light-tail and spread-out restrictions in the proposed use of Lee. These restrictions are not assumed to cover arbitrary finite-mean files.
- Maria Vlasiou, Jiheng Zhang and Bert Zwart, *Insensitivity of proportional fairness in critically loaded bandwidth sharing networks*, Queueing Systems 110, article 18 (2026): <https://link.springer.com/article/10.1007/s11134-026-09978-1>; arXiv:1411.4841, also opened at <https://arxiv.org/abs/1411.4841>. Its abstract restricts file sizes to phase-type and studies heavy traffic. It does not settle T185.
- Maury Bramson, *Network stability under max--min fair bandwidth sharing*, arXiv:1010.3142: <https://arxiv.org/abs/1010.3142>. The abstract matches the supplied max–min result.

No later solution of the unrestricted stochastic problem was found. This is a search outcome, not a proof of absence. The supplied status omits an existing conditional fluid-to-stochastic theorem, but the post-2020 papers opened do not remove its distributional restrictions. Therefore the stop condition for a later solution or substantial advance on the unrestricted stability question was not met.

**Chosen piece, before proof:** characterize exactly the load region detectable by a single positive linear functional of route residual workloads, and prove stochastic positive Harris recurrence in that region for Poisson arrivals and arbitrary finite-mean file sizes. Let `b_i` be a route's service rate when it is alone. The candidate sharp region is `sum_i rho_i/b_i < 1`. Prove both sufficiency and impossibility of a uniform negative linear-workload drift outside this region; exhibit a strictly subcritical two-link example excluded by every such certificate.

Why this piece: it needs no fluid-to-stochastic theorem or file-size smoothness, provides an explicit emptying-time bound, and identifies an exact obstruction to the simplest proposed proof of T185. The sufficient region is elementary and no novelty is claimed. The result deliberately covers Poisson arrivals only; renewal arrivals need an augmented state and a different regeneration argument.

## 3. Proof saved

Wrote `PROOF.md`. It proves the exact minimum weighted aggregate service, the if-and-only-if characterization of uniform negative drift for positive linear residual-workload functions, and positive Harris recurrence for `beta<1`. The recurrence argument uses compensated compound Poisson input and an explicit regenerative invariant probability. The two-link obstruction has link loads `7/10,7/10`, but `beta=6/5`.

## 4. Exact finite checks

Wrote `check_certificate.py`, using only Python's standard library and exact rational arithmetic. The computation enumerates feasible vertices for every active route support in two small networks and checks the minimum weighted service. It also verifies the two-link example by independent load formulas and checks 512 coefficient vectors. These checks supplement the symbolic proof; they do not establish stability outside the proved region.

Exact command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_certificate.py
```

The command completed in under one second, exit code 0. It printed `nice: setpriority: Operation not permitted`; the sandbox cannot apply the requested priority. This tiny standard-library run does not launch numerical workers or allocate large arrays. No simulation or heavy computation was run. Full data/output are in `certificate_checks.json`:

```json
{
  "two_link_obstruction": {
    "loads_by_matrix_and_route_sums": ["7/10", "7/10"],
    "beta_by_load_sum_and_arrival_marks": "6/5",
    "positive_integer_weight_vectors_checked": 512,
    "positive_drift_lower_bound": "min(weights)/5"
  },
  "equal_capacity_vertices": {
    "active_supports": 7,
    "pareto_vertices_counted_by_support": 10,
    "b": ["1", "1", "1"],
    "minimum_weighted_service": "2",
    "predicted_minimum": "2"
  },
  "unequal_capacity_vertices": {
    "active_supports": 15,
    "pareto_vertices_counted_by_support": 24,
    "b": ["2", "2", "3", "5"],
    "minimum_weighted_service": "4/3",
    "predicted_minimum": "4/3"
  },
  "status": "all exact checks passed"
}
```

## 5. Independent audit and report

Saved `AUDIT.md`. Re-derived the emptying-time bound by coupling with a scalar workload queue and summing expected busy-period generations, independently of optional stopping. Re-derived the service lower bound by showing that normalized service below one makes every link slack. Checked the proof against bounded-support files (necessity uses more files, not unbounded residuals), atoms, infinite variance, near-zero residuals, absence of a common bottleneck, and the positive drift at the empty state.

Saved `REPORT.md` with a PARTIAL verdict. The full linkwise-subcritical stochastic problem is not solved. The contribution is a checkable exact characterization of this restricted certificate, a self-contained recurrence proof in its sufficient region, and a small explicit obstruction explaining where the certificate fails. All writes stayed inside this folder.

Final read-back command: `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /bin/cat REPORT.md certificate_checks.json`. Exit code 0; the report starts with the required verdict and the saved rational data match the logged output. The same sandbox priority warning appeared. No further numerical runs were needed.

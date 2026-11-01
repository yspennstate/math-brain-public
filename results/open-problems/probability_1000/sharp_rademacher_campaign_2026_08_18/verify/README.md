# Verification scripts for the 2026-08-20 results

Every number in `problem/the_fibre_is_an_ising_partition_function.md`,
`problem/rc_on_the_ising_reformulation.md`, `problem/the_cut_inflation_conjecture.md` and
`problem/cut_inflation_PROVED.md` comes from one of these. They are here so the writeups can
reproduce themselves rather than cite runs nobody can repeat.

All are read-only, plain Python 3, no third-party packages. They were run on <box> under
`nice -n 15`.

## Self-contained (run anywhere)

| script | what it establishes |
|---|---|
| `cycle_formula_check.py` | the m-cycle fibre `|A| = 3^m + (-1)^m`, brute force, m = 3..10 |
| `c_structure.py` | correlation excess `c` against cycle rank and sharing excess |
| `c_additivity.py` | `c` additive over independent cycles; trees contribute 0 |
| `cyclespace_law.py` | the cycle-SPACE law vs a basis sum; K4, theta graphs, chorded cycles |
| `ising_law_general.py` | extension to triangles with three shared coordinates |
| `ising_mass_verify.py` | 400 random systems per seed, exact rationals, all four triangle types |
| `kbipartite_rc.py` | `K_{n,n}` closed form vs brute force; the tightness table |
| `bipartite_tightness.py` | the unsigned-incidence rank formula, 9 graphs |
| `rc_graph_inequality.py` | the inequality on every connected graph to V = 7 (1,893,730) |
| `targeted_ineq.py` | odd cycles, complete, complete bipartite, wheels, dense random |
| `deletion_contraction.py` | `F(G) = 2F(G-e) - F(G/e)`, 27,474 graphs |
| `two_sided.py` | the failed lower-bound routes (Jensen, max-cut) |
| `one_case_left.py` | the 470,797 critical-edge failures of the naive induction |
| `proof_steps_check.py` | S0/S2/S3/S4/S5/S6 of the proof, individually |
| `multigraph_check.py` | the theorem, recursion, S2 and S3 on multigraphs |
| `positive_c_hunt.py` | hunts systems with `c > 0` |

## NOT self-contained - they load the campaign's own solver

These `exec` the definitions from `/srv/aiwork/rc_deep_box.py` on <box> (`full_dual`,
`valid_R`, `rank_of`, `fib`), deliberately, so that `d_cb` and admissibility are the CAMPAIGN's
notions and not my re-implementation of them. **They will not run without that file**, which is not
in this repo and is not mine to vendor. Copy it beside them, or point `SRC` at your own copy.

| script | what it establishes |
|---|---|
| `pairsum_validR.py` | the pair-sum space is admissible on 9 structured systems |
| `validR_mass.py` | 240 random systems; finds the one selection-rule failure |
| `failing_system.py` | all 729 pair-choices for that system; 725 admissible, min dim 5 |
| `validR_chosen.py` | 180 systems with the pair chosen rather than fixed |
| `D_size_predicts.py` | `|D| = r+k` against admissibility; the refuting cell is empty |
| `mechanism_check.py` | M2/M3 directly, confirming the reason and not just the outcome |
| `outside_regime.py` | `c` outside the `|D| = r+k` regime, 596 systems |

## Reading order

`cycle_formula_check` -> `c_additivity` -> `cyclespace_law` -> `ising_law_general` ->
`ising_mass_verify` gives the Ising theorem. Then `rc_graph_inequality` and `targeted_ineq` for the
inequality, `deletion_contraction` and `two_sided` and `one_case_left` for the routes that failed,
and `proof_steps_check` plus `multigraph_check` for the proof as it finally stands.

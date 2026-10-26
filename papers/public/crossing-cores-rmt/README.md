# crossing-cores-rmt

Verification package for "Crossing cores, Gorenstein moment polytopes, and
sharp volume gaps for random Toeplitz and Hankel laws" and for the new
material in `paper/crossing_cores_merged_sections.tex`.

Everything is exact rational arithmetic; no floating-point value enters any
conclusion. Python 3, standard library only (NumPy is used in one optional
simulation script and in Gauss quadrature for diagnostics, never for a
stated result).

## Layout

- `engine/` - the exact rational polytope volume engine: incremental double
  description for vertex enumeration, combinatorial face triangulation, and
  exact determinants, with an integer fast path (Bareiss) that is entered
  whenever the vertices are integral.
- `data/` - per-orbit exact volumes for both ensembles through order
  fourteen, with a `SHA256SUMS` manifest.
- `verify/` - the checkers, each standalone, each printing its own verdict.
- `paper/` - the manuscript, the new sections in both merged and standalone
  form, and the end-matter statements.

## Reproducing the original results

| script | what it certifies |
| --- | --- |
| `check_identities.py` | every closed-form identity: the primitive-mass table and its inversion, reduced-core counts by formula and by direct enumeration, the peeling law's normalisation, Poisson coefficients, sharp total-variation constants, free cumulants, the order-sixteen Schur threshold, refined moment bounds |
| `verify_order8.py` | all 105 order-eight polytopes and the core-sorted histogram giving 908/15 |
| `check_volumes_spot.py` | named extremal volumes, termwise Hankel-Toeplitz equality, the five- and six-pair Hankel layers, both appendix slab tables |
| `check_appendixA_completeness.py` | that the printed 9/19/26 case lists are complete, re-derived from the coefficient-sum condition |
| `check_ehrhart.py` | the Gorenstein layer by direct lattice counting: palindromic h*, the mod-2 identity, codegree two, interior-point uniqueness, ear-deletion factorisation |
| `check_peeling.py` | deletion confluence and the exact cascade law at k = 4, 5, 6 |
| `rebuild_four_slab_certificate.py` | the rank-four certificate from scratch: both frames, the full multiplicity enumeration, the 69 + 48 minimal orbits |
| `verify_archived_data.py` | hashes plus reconstruction of every moment and pairing count from `data/` |
| `rerun_moments_full.py` | every moment through order fourteen in two independent lanes (direct sweeps, and reduced-core sweeps through the Catalan transform) |
| `check_extension.py` | the order-22 extension: aggregate Ehrhart reconstruction, conditional-positivity minors re-derived, growth-ratio checks |

## Reproducing the new results

| script | what it certifies |
| --- | --- |
| `verify_new_results.py` | every claim in the new sections, tested against the statements rather than the derivations, with negative controls |
| `three_slab_scan.py` | the three-slab maximum, exhaustively at d = 4, 5, 6 |
| `anderson_reduction.py` | that deleting a coordinate private to one form never increases the slab probability |
| `five_slab_search.py` | the star system's value 2/7 and a search for any five-slab system exceeding it |
| `dfinite_exclusion.py` | the size-explicit exclusion of algebraic and holonomic equations, by guess-and-verify with held-out moments |
| `order24_threshold.py` | the exact threshold on m_24 that decides the next free conditional-positivity test |
| `localized_perword.py` | the per-word section-profile sums and their Stieltjes minors at x = 0, 1/4, 1/2 |
| `density_falsification.py` | the mixture conjecture's density prediction against eigenvalues of simulated random Toeplitz matrices |
| `three_triangle_complete.py` | the complete enumeration of three-triangle slab systems (463 configurations), proving the 2/5 bound where its extremum lives |
| `star_local_search.py` | the star is an exact local maximum: every single-form replacement, computed exactly |
| `grammar_max.py`, `grammar_max_hankel.py` | maxima over the grammar class, far past exhaustive reach |
| `calculus_closure.py` | that the three profile rules close: closed evaluation against the engine on random words of the grammar |
| `grammar_coverage.py`, `outside_grammar.py` | how thin the class is, and which cores lie outside it |
| `normalized_volume_check.py` | 628 grammar volumes against Corollary 5.2/5.3 integrality and parity |
| `cactus_vs_volume.py`, `dyck_invariant.py`, `crossing_invariant.py`, `crossing_graph_invariant.py` | which combinatorial statistics determine the volume: block data no, Dyck path no, nesting number no, crossing number nearly, crossing graph pure at orders 6 and 8 but not at 10 |
| `crossing_graph_order10.py`, `cg_failure_witness.py` | the order-ten falsification and its two witnesses: `aabcbcdede` and `ababcdedec` share an interlacement graph and give 9/20 and 4/9 |
| `crossing_graph_connected.py` | whether connectivity of the crossing graph is what the failure needs |
| `two_point_kernel.py` | the kernel a gluing rule would need, for the square |
| `identification_attacks.md` | the running record of what has been excluded, what survives, and with what evidence |

## The long computation

`compute_kappa8.py` sweeps the reduced eight-pair cores. The Hankel side is
complete (198 orbits, giving kappa_8^H = 88999/168 and
m_16(gamma_H) = 9179819/840). The Toeplitz side is 21,994 orbits and runs
for hours; it is checkpointed, so it can be stopped and resumed freely.

- `partial_bracket.py` gives a certified interval for kappa_8^T from a
  partial sweep, using the proved bound 9/20 on the remaining cores.
- `verdict.py` produces the final comparison once the sweep completes, and
  refuses to report anything on partial data.

## Running everything

`run_all.py` re-runs the whole battery and prints one line per checker.
All nine checkers pass on the current engine.

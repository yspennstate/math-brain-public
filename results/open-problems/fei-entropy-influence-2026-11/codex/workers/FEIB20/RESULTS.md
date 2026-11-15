# FEIB20 results

Alternative (a) is proved on the balanced tree family. A leaf and an explicit order give a bounded nested witness. This does not solve the general FEI conjecture.

## Proven statement

For integers D≥2 and L=w−1≥2 with D² L 2^-L≤2, choose a terminal leaf i. Reveal every variable outside its terminal clause first, then the other L−1 private leaves of that clause. With δ=Inf_i, this gives

    2(1−2^{−(L−1)}) ≤ E_i/δ ≤ L_i^π/δ
      ≤ 2 + 2^{−(L−1)}(2L−2+4 log2 e) < 6.

The chosen witness and the optimal leaf witness both tend to 2 as L grows in this regime. Therefore min_{i,π} L_i^π/Inf_i≤2+o(1) along the balanced family, even with D→∞. The tree model cannot give a positive-c log D lower bound for every coordinate and every order. Its terminal leaves have degree one. The proof does not extend to a D-regular hypergraph.

The full argument is in [PROOF.md](PROOF.md). It first proves a private-clause lemma, then derives the leaf influence exactly and bounds it below. The general resampling identities are in [MOMENTS.md](MOMENTS.md).

## Dimensions and influences

| w | D | n | D² L 2^-L | Inf root | Inf mate | Inf leaf |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 8 | 4609 | 1.125000 | 0.00893227696 | 0.00943140934 | 0.00117973092 |
| 12 | 16 | 29217 | 1.375000 | 0.00392880203 | 0.00408059623 | 0.000254734377 |
| 14 | 30 | 147421 | 1.428223 | 0.00179237087 | 0.00183274462 | 6.10297357e-05 |
| 16 | 55 | 669076 | 1.384735 | 0.000839618844 | 0.000849875472 | 1.54430029e-05 |

Source: `python3 proof_checks.py`, `proof_checks.json`. Influences are probabilities, and every witness/erasure ratio below is bits per unit influence. The brief's proposed second truth table w=4,D=2 has n=25, not n=22. The model's count is n=1+DL+D(D−1)L². We validated the actual 25-variable function and used n=13 and n=17 for searches restricted to n≤22.

## All requested orders

| w | coordinate | leaves first | mates first | clause | block | random | private last |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | root | 6.572499 | 5.539180 | 4.222135 | 6.893568 | 6.294987 | — |
| 10 | mate | 5.195000 | 4.995974 | 4.998449 | 5.235524 | 3.956898 | — |
| 10 | leaf | 6.576444 | 6.078477 | 6.153042 | 7.042606 | 4.989702 | 2.052020 |
| 12 | root | 7.651641 | 6.492412 | 4.815896 | 8.075301 | 7.451328 | — |
| 12 | mate | 6.156679 | 6.035916 | 6.046962 | 6.182258 | 4.884791 | — |
| 12 | leaf | 8.368498 | 7.913504 | 7.955357 | 9.036374 | 6.932423 | 2.016072 |
| 14 | root | 8.615957 | 7.115107 | 5.178346 | 9.096157 | 8.411775 | — |
| 14 | mate | 6.828531 | 6.749208 | 6.758001 | 6.844152 | 4.884490 | — |
| 14 | leaf | 9.699206 | 9.200126 | 9.222521 | 10.515845 | 6.249148 | 2.004337 |
| 16 | root | 9.555559 | 7.559241 | 5.418939 | 10.066587 | 9.306725 | — |
| 16 | mate | 7.314688 | 7.261589 | 7.267159 | 7.324017 | 5.007159 | — |
| 16 | leaf | 10.738428 | 10.110539 | 10.122288 | 11.671510 | 9.414857 | 2.001379 |

Source: `python3 nested.py rows` and the Decimal audits, combined by `python3 build_report.py` into `rows_verified.json`. Values displayed to six decimal places. Every listed witness includes all variables and their actual last-element labels.

The orders are defined as follows, with the target i deleted from each full list. Except for random, the root is first when it is not the target. Mates and blocks use increasing indices.

- Leaves first: all leaves in mate/clause/leaf index order, then all mates.
- Mates first: all mates, then all leaves in that index order.
- Clause: each mate is immediately followed by its Q clauses, each clause's leaves consecutive.
- Block: each block's leaves, followed by that block's mates, then the next block.
- Random: NumPy permutation with seed 20261110, same full permutation for the three target types.
- Private last: the clause order with the target leaf's other L−1 private clause leaves moved to the end.

The existing `tree_dnf.py` mates-only witness merges all cells with no spectral mate into one cell. Our full-order leaves-first witness resolves their leaf labels, so it can be slightly smaller. The exact truth-table comparisons use the full statistic.

| w | D | best tested root | best tested mate | leaf private order |
| --- | --- | --- | --- | --- |
| 10 | 8 | 4.222135 | 3.956898 | 2.052020 |
| 12 | 16 | 4.815896 | 4.884791 | 2.016072 |
| 14 | 30 | 5.178346 | 4.884490 | 2.004337 |
| 16 | 55 | 5.418939 | 5.007159 | 2.001379 |

These are best among the tested orders, not all-order minima. Root winners use clause order and mate winners use the one seeded random order. The proof bounds the all-order optimum by the explicit leaf construction.

## Erasure entropy

| w | root E/Inf (MC ± SE) | mate E/Inf (MC ± SE) | leaf E/Inf (proven bounds) |
| --- | --- | --- | --- |
| 10 | 2.2668 ± 0.0031 | 2.1798 ± 0.0063 | [1.992187, 2.067071] |
| 12 | 2.1239 ± 0.0031 | 2.0804 ± 0.0069 | [1.998046, 2.020881] |
| 14 | 2.0477 ± 0.0031 | 2.0314 ± 0.0072 | [1.999511, 2.006212] |
| 16 | 2.0315 ± 0.0031 | 2.0209 ± 0.0073 | [1.999877, 2.001796] |

Source: `python3 erasure.py`, `erasure.json`; leaf bounds use the proved private-clause inequality and exact influences in `proof_checks.json`. The leaf bounds are rounded outward. Root and mate entries are importance-sampling estimates, with one standard error, 400000 samples per entry and seed 20261110. They are measurements, not proofs of a root/mate limit. The derivative normalization and total spectral mass checks are saved with every estimate.

The mate sampler sums six separable tensor terms plus the constant atom. It collapses nonempty Q Fourier supports into their normalized centered-Q factor; homogeneity of Phi makes this collapse exact. It is checked against exact mate E/Inf at w=3,D=2 and w=4,D=2 (`erasure.json`, `sampler_validation.json`). The latter discrepancy is -1.429 standard errors.

## Mates-first prediction

| w | c=P[no leaf in U | root in U] | (1-c) log2(1/Inf) | mates-first L/Inf | difference |
| --- | --- | --- | --- | --- |
| 10 | 0.577273 | 2.877402 | 5.539180 | 2.661777 |
| 12 | 0.505847 | 3.949121 | 6.492412 | 2.543291 |
| 14 | 0.490883 | 4.645143 | 7.115107 | 2.469964 |
| 16 | 0.500917 | 5.099616 | 7.559241 | 2.459625 |

Source: `proof_checks.json`, `rows_verified.json`. Here c is computed exactly from root resampling moments after resampling every leaf. The difference remains about 2.5 bits per unit influence in these rows. This is compatible with the proposed leading logarithmic term plus a bounded additive term, but four finite rows do not prove that asymptotic statement. The leading term alone substantially underestimates the observed witness.

## Small-instance search

| n | min_i E/Inf | best hill min L/Inf | exact min L/Inf | winning type |
| --- | --- | --- | --- | --- |
| 13 | 2.2359895471 | 2.3602347205 | 2.3602347205 | mate |
| 17 | 2.6581403554 | 2.7172191407 | not computed | root |

| n | type | coordinates searched | E/Inf | best hill L/Inf | exact min L/Inf |
| --- | --- | --- | --- | --- | --- |
| 13 | root | 1 | 2.7966895805 | 3.1213262866 | 3.1213262866 |
| 13 | mate | 4 | 2.2359895471 | 2.3602347205 | 2.3602347205 |
| 13 | leaf | 8 | 2.7277324186 | 2.8227570453 | 2.8227570453 |
| 17 | root | 1 | 2.6581403554 | 2.7172191407 | not computed |
| 17 | mate | 4 | 2.8709953869 | 2.8809110890 | not computed |
| 17 | leaf | 12 | 3.1425451570 | 3.2381533265 | not computed |

Source: `python3 hill.py`, `hill.json`. Every coordinate was searched. Each hill run uses six preset starts (including one seeded random order) and ten additional random starts, exhaustive pair swaps per sweep, at most twenty sweeps per start, with fixed seed 20261110. The objective is evaluated from exact-spectrum subset zeta sums. At n=13 a separate shortest-path dynamic program checks every order implicitly for every coordinate. Hill climbing reaches the global exact minimum, but can miss a particular coordinate's optimum: the largest gap is 0.000166107920486. At n=17 the hill result is only an upper bound; the true global minimum lies between the displayed min E and best hill values.

## Checks and resources

`tree_dnf.py selftest` passed (`baseline_selftest.txt`). `python3 nested.py validate` compared arbitrary-mask correlations and all six full orders for root/mate/leaf representatives with exact truth tables at n=13 and n=25 (`validation.jsonl`). Maximum correlation errors were zero at the printed precision; maximum witness ratio errors were 3.11e−15 and 8.88e−16 respectively.

All 64 large-row witnesses were reevaluated using 70-digit Decimal moments, with ordinary double precision only for the final stable Phi logarithms and summation. Sources: `decimal_audit.json`, `decimal_small.json`, `decimal_large.json`. Every resampling cell difference was nonnegative to a tolerance of 1e−55. The largest change from the first floating run was 2.9281887e-05 bits per unit influence. The largest leaf private-order value changed from 2.001408230692 to 2.001378948805. The proof is independent of these numerical differences. `proof_checks.json` independently compares the conditioning formulas for all three influences against Decimal correlation differences, agreeing within 1.8e−69.

`resources.json` records inherited nice 10. The sandbox refused the redundant nice wrapper's setpriority call; direct priority inspection confirms the requested inherited value. Commands set one BLAS/OMP thread and used at most two compute processes concurrently. The n=25 independent sampler validation measured 1638383616 bytes (1.526 GiB) peak RSS. No truth tables or large arrays were saved. The folder-byte count at the resource check was 457628 bytes, far below 200 MB; final size is recorded in `final_audit.json`.

Brain recall supplied orientation and older FEI pointers; the mathematical result came from FLOW, the supplied code, and the derivations here. No external files, mesh messages, memory entries, or fleet board entries were written, as required by RULES.md.

## Still open

The general FEI conjecture and universality of the window-one witness remain open here. We have not found exact all-order root/mate minima at large size, proved a logarithmic bound on regular hypergraphs, or proved a uniform witness bound for every unbalanced choice of D,w. The proved regime is D² L 2^-L≤2, which covers the requested balanced rows. There is no remaining blocker to the assigned alternative (a).

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 22:20 ask; FEIB20 nested-witness brief.

# FEIB22 results

Task: percolation coordinate erasure entropy and witnesses, the author's 9 Nov 2026 22:20 request to solve the Fourier Entropy-Influence conjecture.

No numerical conclusions yet. Inputs: ../../RULES.md, BRIEF.md, ~/fei_solve_agent/FLOW.md and code/mc_chain.py. Relevant brain recall found a provisional percolation entropy argument; it is not evidence for the coordinate bound and will not be assumed. The math recall command reported that its store was not found.

All entropies use bits. Witness/Inf ratios have units bits per unit influence. Exact enumeration has sampling standard error zero; rounding error is separately checked. Sampled block plug-in values are downward biased and are not upper bounds.

## Exact small boards and validation

Commands: `clang++ -O3 -std=c++17 -dynamiclib engine.cpp -o engine.dylib`; `python3 study.py validate`; `python3 study.py exact 3`; `python3 study.py exact 4`. Compute children inherit nice 10; the attempted additional `nice -n 10` printed a setpriority denial, so subsequent launches retain the already verified inherited nice 10. All numerical kernels are single threaded.

The articulation-based all-pivotal evaluator agreed with explicit site flips on every checked configuration in validation.json. The spectra on boards L=2,3,4 agreed entrywise with mc_chain.py (maximum absolute difference 0). The exact L=3 restriction mixture identity also had maximum difference 0. The L=4 shell-window Monte Carlo value was 2.75224 ± 0.02538 against exact 2.74902 (32,768 paired configurations; these figures are from validation.json).

| L | coordinate | Inf | exact E/Inf | best nested/Inf | best last-two/Inf | sampling SE |
|---|---|---|---|---|---|---|
| 3 | 4 | 0.320312500 | 1.48829004 | 1.96313225 | 1.64067330 | 0 |
| 4 | 10 | 0.185974121 | 2.10845167 | 2.84088737 | 2.42395029 | 0 |

Every coordinate is saved in exact_L3.json and exact_L4.json. Both optimisations use subset shortest paths; reconstructed orders were checked by independently regrouping the full spectrum. The L=2 optima were also checked against every permutation.

## Larger block measurements

Command: `python3 run_suite.py blocks`. Each row averages exact restricted transforms over 16,384 independent outside configurations, split into 16 independent batches. Values below are the independent pilot-tangent upper targets at fixed alpha=0.001; ± means one standard error conditional on the pilot. The first half trains the tangent and the second half (8,192 configurations) estimates it. The target is an upper bound; its numerical estimate still has sampling uncertainty.

| L | r=1 tangent/Inf | r=2 tangent/Inf | r=2 pooled plug-in | r=2 jackknife plug-in |
|---|---|---|---|---|
| 8 | 3.95859 ± 0.00622 | 3.67919 ± 0.00504 | 3.67213 | 3.67223 ± 0.00394 |
| 12 | 4.22335 ± 0.01337 | 3.91116 ± 0.00396 | 3.91013 | 3.91031 ± 0.00278 |
| 16 | 4.39229 ± 0.00918 | 4.02324 ± 0.00446 | 4.02136 | 4.02160 ± 0.00364 |
| 24 | 4.58012 ± 0.01615 | 4.14733 ± 0.00445 | 4.14108 | 4.14150 ± 0.00408 |

The plug-in column shares the SE of the jackknife estimate to the displayed precision; it is not an upper bound. Split estimates and smoothing sensitivity checks are saved in the corresponding block_L*_r*_s*.json files.

## Analytic result

ARGUMENT.md derives W(B_r minus i) ≤ C Inf_i α_4(r) and V(B_r minus i) ≤ C Inf_i / α_4(r) for a bulk site. Their product is uniformly bounded in units of Inf_i², including a final jump from an interior macroscopic ball to the whole board. The two-sequence lemma, or a separate summability argument, therefore gives E_i ≤ nested ≤ C Inf_i uniformly in board size. This is a new derivation here, not a theorem attributed to GPS, and requires referee review. A separate finite-block argument proves that every fixed local block witness eventually grows like log(1/Inf_i), despite that boundedness.

## Exact 5×5 board

`python3 study.py exact 5 noopt` enumerated the full 25-site spectrum and saved E_i/Inf_i for every site in exact_L5.json. At the centre, Inf=0.171384453773, E_i/Inf_i=2.0008300789, with sampling SE zero. `python3 optimal5.py` gives the centre optimum nested=3.0427732132 and last-two=2.5556775617, also SE zero. Other sites are saved as their symmetry classes finish; transpose and half-turn invariance are checked entrywise on the full spectrum before using them.

## First larger window result

`python3 run_suite.py windows`, L=12, 2,097,152 independent resampling pairs: Inf=0.0589256 ± 0.0001624; nested=4.08502 ± 0.00744; two-hit shell plug-in=3.73821 ± 0.01139; jackknife-corrected=3.74647. The independent tangent with smoothing 0.1 targets an upper bound and is 3.75988 ± 0.00824. Negative empirical masses and split-sample drift are explicitly retained in the JSON. This is the shell coarsening of the vertex-resolved last-two statistic, as defined in METHODS.md.

## L=16 window and completed audits

`python3 run_suite.py windows`, L=16, 2,097,152 pairs: nested=4.24829 ± 0.00868; two-hit shell raw=3.89768 ± 0.01054; jackknife=3.91340; tangent alpha=0.1 upper target=3.92820 ± 0.00956.

`python3 audit.py --no-windows` passed: all 33,554,432 L=5 spectral weights and every direct-flip influence agree exactly with the independent supplied evaluator. Stable log1p calculations change the site erasure ratios by at most 1.6431300764452317e-14 (sampling SE zero). The peak resident memory of this audit process was 1,902,559,232 bytes. `python3 audit_estimators.py` checks tangent bounds on exact small-board distributions and the finite-block lower bound in every saved block batch; it passed. The provided mc_chain.py self-test and final local validation also passed.

## Final estimator refinement

The final window summaries set the same-shell two-hit atom to exactly zero when that shell contains one site. This is a structural identity, so estimating it from noisy correlation differences is unnecessary. The corresponding tangent reference also omits those impossible cells. Earlier window figures in this running results log used the preliminary summary; their full outputs remain in windows_suite.log and window_L8.log. Raw batch counts are unchanged. The final REPORT.md and regenerated window JSON files use this refinement. The final small-board validation and exact-distribution tangent audits both pass.

## Completed final table

All window summaries now use the structural-zero refinement. Commands: `python3 finalise_windows.py` and `python3 make_report.py`. The exact-site and block tables are unchanged. All ± values below are one sampling standard error; ratio units are bits per unit influence.

| L | Inf_i | nested/Inf | corrected two-hit shell/Inf | independent tangent upper target, alpha=0.1 |
|---|---|---|---|---|
| 8 | 0.0931158 ± 0.0002613 | 3.76379 ± 0.01212 | 3.41625 ± 0.01205 | 3.44750 ± 0.01955 |
| 12 | 0.0589256 ± 0.0001624 | 4.08502 ± 0.00744 | 3.73683 ± 0.01090 | 3.75898 ± 0.01352 |
| 16 | 0.0425010 ± 0.0001337 | 4.24829 ± 0.00868 | 3.89678 ± 0.01057 | 3.91311 ± 0.01855 |
| 24 | 0.0261617 ± 0.0001190 | 4.45901 ± 0.00973 | 4.11506 ± 0.01695 | 4.13058 ± 0.02392 |

REPORT.md contains the complete comparison, block bias checks, exact optima for every small-board site, the literature discussion, the boundedness derivation and its limitations. General FEI is not solved by this work.

Task: “solve the Fourier Entropy-Influence conjecture” — owner’s 9 Nov 2026, 22:20 ask; FEIB22 percolation brief.

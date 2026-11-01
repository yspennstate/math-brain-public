# Fourier chapter provenance and verification

## Deliverable and scope

`fourier.tex` is an anonymous mathematical chapter. It contains complete proofs of the stated analytic consequences, with explicitly cited classical input theorems. It does not claim that the unrestricted three-eigenvalue conjecture is solved.

Repository snapshot: `yspennstate/math-open-problems@36d0dc0c4ac0910e8d84ae64d443136df86242d5`.

The chapter is reconstructed from the sources below and re-derived algebraically. Source prose and administrative records are not included in the mathematical chapter.

## Classical dependencies

- Geometric rank-one Brascamp–Lieb: `BL1976`, with normalized formulation in `LPP2016`.
- Gaussian exhaustion for general rank-one Brascamp–Lieb data: `Lieb1990`.
- Sharp Hausdorff–Young and sharp Young convolution: `Beckner1975`.
- Sharp product projection density `2^{k/2}`: `LPP2016`, Theorem 1.1. A complete geometric-BL proof of the weaker `e^{k/2}` bound is included; the explicit constant is not incorrectly attributed to `RV2015`.
- Two-part tight-frame partition: `MSS2015`, Corollary 1.5.
- Compact convex minimax: `Sion1958`; the chapter separately proves the multiplier-limit argument including empty feasible sets and boundary optima.

## Main statements and additions

1. `four:projection`: projection density ≤ `e^{k/2}` by a direct fiber integral proof; classical `2^{k/2}` refinement; general full-row-rank linear maps with Jacobian.
2. `four:lp`: exact modulated-transform bound `2π p^{-1/2}(p/(p−1))^{(p−1)/2} ≤ 2π√e/√p < 4π/√p`, for every real `p≥2` and measurable modulus-at-most-one modulation.
3. `four:fresnel`, `four:diffuse`: Gaussian regularization, absolute domination, complex product marginal, and separable-phase theorem with density constant `r B(U)^{2/r}/(r−2)` times determinant scale.
4. `four:volume`, `four:volume-density`: general `k,q` theorem, including original D/D′/D5 constants and improved coefficient `ke/((k−2q)√q)`. The determinant polynomial is valid for zero Gaussian coordinate parameters at saturated column marginals.
5. `four:exact-marginal`: exact general-`k,q` row/column scalar factors; sharp weighted `q=1,k=3` formula from fresh B04 r14. The general `k,q` version is a direct re-derivation, not a claim copied from the source.
6. `four:gibbs`: row-law entropy compression, exact Gibbs dual with boundary/infeasibility proof, bounded-row deletion bound `|H|<k/h` and residual `e_k≤G_h`; one-row information projection; balanced six-by-six example. The source states the Gibbs and deletion theorem for `k=3`; the proof here explicitly establishes general `k`.
7. `four:graph`, `four:regularized`, `four:ridge`: exact free-regularizer graph calculation, full determinant bound, gamma-integral and simple density constants, and fixed-scale ridge leverage.
8. `four:ridge-stability`, `four:full-range`, `four:window`: operator perturbation proof, MSS partition consequences, scaled spectral-window bound `288√(3e)/(13s)` with arbitrary additional spectral directions.
9. `four:volume-operator`, `four:volume-stability`, `four:near-diffuse`, `four:tail`: exact spectral marginal identity including repeated singular values, general-k tail operator bound, three-volume perturbation constant `24√3 e/(5a)`, and distributed-tail consequence without a smallest-tail-eigenvalue penalty.
10. `four:quarter`, `four:log-potential`: arbitrary-rank nonzero quadratic concentration `min(1,5(ρ/||S||)^{1/4})`, original-coordinate cut proof and Gaussian constant calculation, logarithmic and fractional negative potentials.

## Source pins

Each URL below fixes the repository snapshot and each listed blob is the Git blob in that snapshot. All mathematical content is independent of the administrative status labels in those sources.

| Source | Snapshot blob | Local byte verification |
|---|---|---|
| [interactive/20260922T120815Z-separable-perturbations/REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md) | `d08d2488c072386e2b8ad818e30b1a6dec79e63a` | Exact after removing one appended final newline |
| [interactive/20260922T131746Z-regularized-determinant/REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md) | `080253f929411bfa9c7aa3254a2bdaf37be72ebb` | Exact after removing one appended final newline |
| [interactive/20260922T151048Z-ridge-window/REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md) | `1241fa7ba9a36a91bc75f047677f2daac764c2bf` | Exact after removing one appended final newline |
| [interactive/20260922T161801Z-rank-two-fusion/REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md) | `00681629acaba8f2e04edda6c9f6b5c4f0fdafa4` | Exact after removing one appended final newline |
| [interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md) | `d690b4e1e9f29a458c5ee7d8f2f107b98da64360` | Exact after removing one appended final newline |
| [interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md) | `9da148eed6cd43b1046a6f91d0f9329e12921cb4` | Exact after removing one appended final newline |
| [interactive/20260922T220600Z-claude-review/REVIEW.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md) | `44ee51368aad3796beda43e15534087cd0b298fd` | Exact after removing one appended final newline |
| [interactive/20260923T002323Z-volume-stability/REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md) | `f9efb2a4c89b81707d720b88db35ebdea2013f74` | Exact after removing one appended final newline |
| [interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md) | `d728798f2a5656bd6e34ee5da0f3d080e41a6315` | Exact after removing one appended final newline |
| [fleet/fleet01/B04/20260923T144427Z-fleet01-B04-QFORM-auto11-r13/REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T144427Z-fleet01-B04-QFORM-auto11-r13/REPORT.md) | `fe94d8ac06cc25527a259d291887b6112bf6cf28` | Exact bytes |
| [fleet/fleet01/B04/20260923T154425Z-fleet01-B04-QFORM-auto11-r14/REPORT.md](https://github.com/yspennstate/math-open-problems/blob/36d0dc0c4ac0910e8d84ae64d443136df86242d5/proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T154425Z-fleet01-B04-QFORM-auto11-r14/REPORT.md) | `1333b52ede708fd86a5bd68158e540ba72e5ad1f` | Exact bytes |

The nine interactive local copies each contain one extra final newline compared with their source blobs. Removing that one byte in memory reproduces the expected Git blob hash in every case. The two fresh B04 fleet reports match their Git blobs byte-for-byte. No shared snapshot file was modified. Detailed local checks are saved in `fleet_work/fourier_source_checks.json`.

## Verification

- Algebra was re-derived for the sharp scalar norms, entropy factors, Fresnel constants, free regularization multiplier, determinant exponents, ridge spectral scaling, marginal-stability inequalities, and quarter-power Gaussian conversion.
- An independent reviewer (`/root/claude_core/adapted_attack`) reported a passing proof review through the original weighted-volume remark: modulated Lp constant, difference/Fourier-power norms, Fresnel signs and normalization, diffuse phase estimate, decoupling, saturated-marginal determinant proof, entropy factors, and inversion constants. That review found no corrections necessary.
- The same independent reviewer completed a full second-half re-derivation and reported a pass: general-k Gibbs boundary minimax and infeasible case; strict-cardinality bounded-row deletion; graph constants; ridge/window constants; general volume-tail operator and perturbation bounds; quarter-power Gaussian coefficient. One requested clarification was applied: the Gibbs theorem now explicitly states `Z_k>0`. No substantive mathematical error was identified.
- Isolated LaTeX compilation uses `fleet_work/fourier_check/check.tex` with the manuscript preamble and chapter source, leaving the master compiled files untouched. BibTeX and two subsequent pdfLaTeX passes succeeded: 20 pages including references, zero warnings, zero unresolved citations/references, and zero overfull boxes. A source scan found 98 unique labels, no duplicate labels, and no undefined internal references. All requested cross-chapter labels resolve.
- Numeric experiments are not used as proof. No numerical tests were added to mirror these symbolic arguments.

## Boundaries retained

The chapter never substitutes arbitrary bounded joint density for the product source in an indefinite coarea estimate. It does not assume independence after orthogonal rotation, law-uniform pointwise scalar stationary-phase decay, or independence of a retained component from an arbitrary spectral tail. All cut, leverage, rank, and marginal hypotheses appear explicitly. The strict Fourier condition `k>2q` or `theta>2q` is required wherever inversion is used.

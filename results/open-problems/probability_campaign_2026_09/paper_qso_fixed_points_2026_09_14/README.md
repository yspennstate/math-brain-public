# Fixed points of strictly non-Volterra quadratic stochastic operators in four or more types

## Source attribution correction, 15 September 2026

The archived five-type operator W and its original two fixed points are due to U. U. Jamilov, *Dynamics of a strictly non-Volterra quadratic stochastic operator on S^4* (Uzbek Mathematical Journal,2017,no.2,pp.66–75), equation(7) and Theorem3. The [complete primary-source audit091](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/agents/091.md) verifies the exact tensor and spectrum against the original issue.

The preserved manuscript's earlier novelty discussion and its specific description of the2016 symmetry are superseded by that audit. The exact2016 coefficient hypotheses remain unverified. The [positive-mixture classification](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/QSO_FIVE_TYPE_PERTURBATION.md) is a separate extension beyond the2017 paper; worldwide priority remains unverified. The original manuscript and prior formal artifacts are preserved.

The [current completion and audit collection](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/README.md) contains the complete four-type proof, guaranteed exact solver, further dynamics results, source corrections and actual execution record. The new uniqueness theorem has not been formally verified in this run.

Companion material for the paper of the same title (Y. Shmalo, September 2026), which answers Problem 11
of Ganikhodzhaev and Rozikov, *Quadratic stochastic operators: results and open problems* (2009): Theorem 6
(unique, non-attractive fixed point of a strictly non-Volterra operator on three types) does not extend to
four or more types. Non-attractiveness fails from four types (the equiprobable family of Jamilov, Ladra
and Mukhitdinov, 2017); uniqueness fails from five types, by a rational operator with two fixed points
studied by Jamilov (Uzbek Math. J., 2017), which the paper shows to be one member of a family in which
the count is always exactly two, and a six-type operator has a whole segment of fixed points. Uniqueness
at four types is proved in the paper (an elementary transfer argument, formalised in Lean).
The four-type uniqueness theorem of that completion was re-derived, formalised in Lean (QSOFourTypeUnique.lean, build_four_type.log) and is now Theorem 6.1 of the paper.

Contents

- `paper/` the LaTeX source and the compiled PDF.
- `numerics/qso_fixed_points.py` the numerical companion: exact verification of the five-type operator, all
  its fixed points (Newton and an exact Groebner solve), its dynamics, the equiprobable family, six-type
  operators with two invariant triples, and fixed-point counts for random operators on four to six types;
  `numerics/results.md` is its output.
- `figures/` the figure produced by the script.
- `lean/QSOFixedPoints.lean` the Lean 4 verification (operator and Jacobian for any number of types; Euler's
  identity, zero trace, the invariant-face lemma, the four-type face observation; the five-type operator's
  conditions, fixed points, Jacobians and complete spectra; the equiprobable four-type Jacobian at the
  barycentre; the six-type segment of fixed points), with the build log and axiom report. It compiles
  against Mathlib with Lean 4.33.1 (`lean/lean-toolchain`, `lean/lake-manifest.json`).
- `lean/QSOFourTypeUnique.lean` the Lean 4 proof of the four-type uniqueness theorem (`QSO4.unique_fixed_point`):
  for any coefficient table on four types that is symmetric, nonnegative, stochastic and strictly non-Volterra,
  two fixed points in the simplex coincide. `lean/build_four_type.log` is its build and axiom report.

To reproduce the numerics: `python numerics/qso_fixed_points.py` (numpy, sympy, matplotlib). To check the
Lean file: put it in a Lake project depending on Mathlib at the pinned commit and run `lake env lean QSOFixedPoints.lean`.

# account03/B13 Lean verification r28

Run: `20260925T143512Z-account03-B13-lean-r28`

Target: `yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa`, repaired paper blob `98e45d53d106db9a205051a4dd4917fc39dc2e3a`, SHA-256 `90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb`.

Fresh controls and the current repaired Lean coverage were read. The 25 Sep 2026 12:29 owner override remains in force: Lean verification only. Current `LEAN_COVERAGE.md` blob is `80491f1e5a8e43a8890034a0bfbd3168f0040ec7`; Lemma 5.2 is still partial, with only `QformFiveB.ellipse_jacobian` and `QformFiveB.definite_const` compiled for this lemma. No newer matching full-Lemma-5.2 compile was found.

## New formalization advance

At the exact project Mathlib pin `5e932f97`, the missing B13 infrastructure is already library-proved:

- `Real.polarCoord`: an open partial homeomorphism from the slit plane to `(0,∞) × (-π,π)`.
- `Real.polarCoord_source_ae_eq_univ`: the deleted seam is volume-null.
- `Real.hasFDerivAt_polarCoord_symm` and `Real.det_fderivPolarCoordSymm`.
- `Real.lintegral_comp_polarCoord_symm`: the full nonnegative polar change-of-variables formula with radial Jacobian.
- `MeasureTheory.lintegral_image_eq_lintegral_deriv_mul_of_monotoneOn` from `JacobianOneDim.lean`: a direct compiled route for the radial substitution `δ=r²`.
- `Measure.addHaar_image_linearMap` / `addHaar_preimage_linearMap`: exact determinant scaling for the anisotropic diagonal map.
- `OrthonormalBasis.measurePreserving_repr`, `measurePreserving_repr_symm`, and `LinearIsometryEquiv.measurePreserving`: orthonormal eigenbasis transport without any rotated-coordinate independence claim.

This removes the need to formalize the paper's custom open polar chart from first principles. Mathlib's chart deletes the nonpositive x-axis and uses angles `(-π,π)` rather than the paper's positive-ray / `(0,2π)` convention; this is equivalent for the lemma because both seams are null and both angular intervals have length `2π`.

## Recommended paper-specific theorem shape

The shortest robust Lean assembly is Borel-set domination rather than first constructing a pointwise density. For every Borel `E ⊂ ℝ`, prove

[
\Pr(q(W)\in E) \le \frac{\pi L}{\sqrt{\det B}}\,\operatorname{vol}(E).
]

Use the joint two-dimensional input density `p_W≤L`; transport through the orthonormal eigenbasis measure-preservingly; use determinant scaling for `diag(1/√μ₁,1/√μ₂)`; use `Real.lintegral_comp_polarCoord_symm`; then use the one-dimensional monotone Jacobian theorem for `r↦r²`, which produces the exact `1/2` factor. The angular integral contributes `2π`, giving the existing compiled `definite_const`. Translation by `w₀` is Haar-measure preserving. The resulting measure domination interfaces directly with the paper's conditioning lemma and Radon–Nikodym, while preserving the full arbitrary joint bounded-density scope.

## Formal-credit status

No new paper theorem is counted as verified in this run. There is no `lean` or `lake` executable exposed in this runtime, installation is prohibited, and remote workflow execution is prohibited. Therefore no matching new compile, no new axiom log, and no full-Lemma-5.2 verification is claimed.

Current B13 status: **PARTIAL_LEAN_VERIFICATION**. The remaining obligation is to compile the paper-specific composition/density-domination wrapper and then run `#print axioms` with no `sorry`, `admit`, new `axiom`, or `sorryAx`.

Brain status: `WITHOUT_VERIFIED_BRAIN`. Unexposed model/effort settings remain `UNKNOWN`.

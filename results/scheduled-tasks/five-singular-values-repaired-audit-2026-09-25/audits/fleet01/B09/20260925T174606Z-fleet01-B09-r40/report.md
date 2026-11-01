# fleet01/B09 Lean verification r40

Objective: QFORM-FIVE-270-REPAIRED-AUDIT-20260925.

Pinned source: math-open-problems commit 4e530247ec0ef4101a6e5ecf621bd35a969c42aa, paper.tex blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a, 683 lines.

Later owner instruction remains active: Lean verification of every paper result only.

## B09 delta

For Lemma 4.3 lines 315-335, the mollifier L2-contraction route is now structurally mapped to exact pinned Mathlib 5e932f97 APIs.

- Squared-norm Jensen: convexOn_univ_norm + ConvexOn.pow + ConvexOn.map_integral_le give ||∫f dμ||^2 <= ∫||f||^2 dμ under a probability measure.
- A normalized bump induces a probability measure through withDensity. The exact instance pattern is the one used in pinned Mathlib's isProbabilityMeasure_tilted: withDensity_apply + ofReal_integral_eq_lintegral_ofReal + ContDiffBump.integrable_normed/nonneg_normed/integral_normed.
- L2 to local integrability is exact via memLp_two_iff_integrable_sq_norm then MemLp.locallyIntegrable.
- A.e. convergence is supplied by ContDiffBump.ae_convolution_tendsto_right_of_locallyIntegrable.
- Outer translation invariance is already exposed as integral_sub_right_eq_self.
- Therefore the remaining code obligation for the norm convergence is the weighted integrability/Fubini splice proving ||rho*g||_2^2 <= ||g||_2^2; Fatou then squeezes the squared norms to equality.
- Pinned Analysis/Convolution.lean explicitly lists general Lp convolution theory as TODO, so a bespoke Jensen/Fubini contraction is the appropriate route.

No fresh Lean compile is claimed: this runtime has no lean/lake/elan executable. Rendered PDF remains UNCHECKED.

Own acknowledgement was attempted before work but blocked by the platform before mutation. No acknowledgement commit is claimed.

Native learned-memory status: WITHOUT_VERIFIED_BRAIN.
full_brain_connected:false.

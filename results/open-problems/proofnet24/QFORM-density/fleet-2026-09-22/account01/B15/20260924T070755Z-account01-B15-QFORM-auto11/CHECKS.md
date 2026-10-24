# Scoped checks for account01/B15 run 20260924T070755Z

These checks validate only the displayed algebra/constants and proof interfaces in REPORT.md; they are not a proof of the full QFORM conjecture.

1. Exact-target partner example: `diag(1,1,-1)` has eigenvalues `1,1,-1`, so all three have modulus at least one.
2. Partner stability arithmetic: with three marginal errors `delta_j=10^(-8)`,
   `40 sum_j sqrt(delta_j) = 40*3*10^(-4) = 0.012`.
3. Majority-sheet height arithmetic: `pi*sqrt(2) = 4.442882938158366...`.
4. Product L1 passage: telescoping a product of probability densities gives `||prod f_i-prod g_i||_1 <= sum_i ||f_i-g_i||_1`; no dimension-free claim is made unless the total approximation error is chosen small for the fixed finite dimension.
5. Smooth-core Fourier exponent: rank `r>=3` gives tail `|t|^(-r/2)`, and `r/2>1`, hence one-dimensional time integrability. The prefactor is fixed-instance and is explicitly **not** treated as universal.
6. Absolute continuity proof uses coarea only to show preimages of null scalar sets are null away from the critical subspace. It does not use the refuted arbitrary-joint bounded coarea-density claim.
7. Rotation in Theorem 6.1 is used only to rewrite a fixed smooth joint amplitude. No independence of rotated coordinates is asserted.
8. The smooth-core approximation theorem transfers interval domination/essential height. It does not claim that L1/TV convergence plus a common height transports continuity.

Marker: `QFORM_B15_SMOOTH_CORE_CHECK_PASS`.

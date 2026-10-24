# account01/B04 Lean r04

Source: yspennstate/math-open-problems commit 4e530247ec0ef4101a6e5ecf621bd35a969c42aa, paper.tex blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

Target: Theorem 3.1, source lines 177-205.

Fresh LEAN_COVERAGE.md reports 570 theorem declarations in repaired-source Lean files. Theorem 3.1 remains partial: frame_trace, frame_quadratic, bl_pointwise, bl_heat_algebra and gaussian_normalization are compiled; monotonicity, limiting operations and Fatou are not.

This run isolated the line-195 analytic interfaces against pinned Mathlib 5e932f97. A candidate wrapper uses hasDerivAt_integral_of_dominated_loc_of_deriv_le for differentiation under the integral. A second candidate proves the whole-line bridge integral f' = 0 from HasDerivAt f f', integrability of f', and f -> 0 at both infinities, using integral_Iic_of_hasDerivAt_of_tendsto', integral_Ioi_of_hasDerivAt_of_tendsto', and intervalIntegral.integral_Iic_add_Ioi.

Paper-specific remaining obligations: formalize F and its first/second derivatives, the polynomial-times-Gaussian majorant, slice boundary decay and Fubini; then the large-time DCT, small-time approximate identity/null-preimage/Fatou step, and monotone truncation.

New candidate Lean is UNCOMPILED WIP: current runtime has no lean/lake and owner controls prohibit installation or remote workflow workarounds. No kernel-verification credit is claimed.

Native brain status: WITHOUT_VERIFIED_BRAIN; full_brain_connected:false.

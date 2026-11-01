# Independent review of the final hub supplement

Reviewer: `/root/claude_core/adapted_attack`.
Date: 23 September 2026.
Reviewed source: `paper_work/hubs.tex`.
SHA-256 of the corrected source:
`c3c650c9b62be8952a0e558f05f357570b1812e78ca08b7596378613452ff897`.

## Verdict

**Pass.** The reviewer independently read and rederived the supplement from
“Collisions on shells and a logarithmic support dependence” through the end
of the chapter, including the preceding results invoked in its proofs.
The reviewer did not author these sections.

The sole necessary correction identified was the domain of the centers in
the definition of `alpha_1`: the supremum must range over all real centers
and positive radii. Root applied this correction, and the corrected formula
was checked in the source with the hash recorded above.

## Verification scope

- Shell collision projection geometry, the constant `8/|lambda|`, bounded-
  support tail estimate, parameter optimization, and concave profile.
- Weighted collision criterion, its nonlinear integral hypothesis, and the
  distinction between the pointwise projection cap and the additional
  integrated collision bound.
- Parabola extension constant `4*pi^3/sqrt(3)`, both Fresnel factors, the
  frame-integral interpolation, Holder exponents, parameter Jacobian, `B_0`,
  and the density conversion.
- Uniformity through zero partner curvature: the three-event window bound,
  dyadic Fourier smoothing, and cancellation of the singular curvature
  factor. The normalized density expression is approximately
  `17.98006547`, consistent with the stated bound below 18.
- Joint square-root hypothesis, scalar discriminant constant `2^(7/4)`,
  random-center composition, conditional density use, logarithmic critical-
  value estimate, and independent-square corollary.

All sufficient conditional hypotheses remain explicit. The supplement does
not assert that its weighted collision or joint square-root assumptions hold
automatically for arbitrary product laws. No additional mathematical
correction was required. The review was read-only; no manuscript build or
further expansion was performed by this reviewer.

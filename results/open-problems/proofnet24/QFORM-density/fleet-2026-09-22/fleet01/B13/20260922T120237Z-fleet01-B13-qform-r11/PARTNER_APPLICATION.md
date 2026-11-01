# Partner application — fleet02/B13 bang-bang theorem

Exact consumed source:

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`

The partner independently proves the exact fixed-kernel bang-bang reduction and finite-union localization, and gives a decisive quadratic-fiber falsifier to the stronger shortcut “one interval / centered uniform per coordinate is extremal.” For

\[
h(x)=1_{\{R^2\le x^2\le R^2+\varepsilon\}},\qquad R>1,
\]

write

\[
\ell=\sqrt{R^2+\varepsilon}-R,
\]

with `2 ell < 1`. The two slab branches have total length `2 ell`; a unit-measure disconnected set can contain both branches and achieve integral `2 ell`, while every unit interval meets at most one branch and achieves at most `ell`. Thus the factor-two separation is exact at this fiber.

## Application to the present run

The new theorem in `REPORT.md` proves that the full admissible density class is the `L1` closed convex hull of unit-measure indicators, and hence transfers every convex TV-lower-semicontinuous output functional—including the nonlinear integrated Fourier norm—to product indicators and then to bounded finite unions of intervals.

The partner's explicit quadratic-fiber example shows that this endpoint cannot be simplified to the convex hull generated only by **single** unit intervals if one wants an extremal statement adapted to quadratic shells: already a single physical quadratic fiber has a factor-two gain from disconnected support. Therefore the source-coherent reduced class for both the geometric shell route and the nonlinear Fourier route must retain arbitrary finite fragmentation (or an equivalent class capable of representing it); centered-uniform/single-interval rearrangement is not a valid universal next step.

This narrows the unpaid implication to a genuinely fragmentation-uniform estimate:

\[
\boxed{
\text{prove the shell or integrated-Fourier bound uniformly over finite unions, with no bound on component count/separation.}
}
\]

The partner result is used here to rule out a materially stronger but false reduction, not merely cited for agreement with the bathtub theorem. Full QFORM remains open.

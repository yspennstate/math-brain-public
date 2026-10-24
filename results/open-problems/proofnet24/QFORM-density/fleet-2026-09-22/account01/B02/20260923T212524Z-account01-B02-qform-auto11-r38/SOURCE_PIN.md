# r38 source-pin clarification

The quantitative marginal-free physical-`E3` theorem used in r38, including the explicit unweighted Fourier integral bound, is pinned most directly at:

- repository: `yspennstate/math-open-problems`
- full commit: `3fccd9b82b456e198758e5839be364b4b0ec5024`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T170839Z-account02-B02-qform-auto11/REPORT.md`
- theorem: `QFORM-CROSS-E3-MARGINALFREE-SHARP-rational-v1`

It states, for every literal original-coordinate cross block `B` with `Z=E3(B)>0`,

`||p_Q||_infinity <= 10.345084 Z^(-1/6)`,

`integral_R |phi_Q(t)|dt <= 2 pi * 10.345084 Z^(-1/6)`,

with a continuous representative vanishing at infinity. The later account02/B02 report pinned in the main r38 report (`aeaba9e3351623ead11450857c2d014b43664aef`) restates the marginal-free density theorem and `phi_Q in L1`; this file supplies the exact source for the quantitative integral constant used in r38.

The r38 theorem itself is unchanged.
